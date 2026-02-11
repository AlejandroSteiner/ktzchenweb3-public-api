"""
KtzchenWeb3 SDK - Python
Official SDK for the KtzchenWeb3 blockchain API platform

Version: 1.0.0
License: MIT
"""

import requests
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass


class KtzchenWeb3Error(Exception):
    """Custom exception for KtzchenWeb3 API errors"""
    
    def __init__(self, message: str, status: int = 0, details: Dict = None):
        super().__init__(message)
        self.message = message
        self.status = status
        self.details = details or {}


@dataclass
class RateLimit:
    """Rate limit information from API response"""
    limit: Optional[int]
    remaining: Optional[int]
    reset: Optional[int]


class GasModule:
    """Gas fees operations"""
    
    def __init__(self, client: 'KtzchenWeb3'):
        self._client = client
    
    def get_fees(self, network: str) -> Dict[str, Any]:
        """
        Get gas fees for a network
        
        Args:
            network: Network identifier (e.g., 'ethereum_mainnet')
            
        Returns:
            Gas fees data
        """
        return self._client._request('GET', f'/v3/{network}/gas-fees/')
    
    def get_fees_multiple(self, networks: List[str]) -> List[Dict[str, Any]]:
        """
        Get gas fees for multiple networks
        
        Args:
            networks: List of network identifiers
            
        Returns:
            List of gas fees data
        """
        return [self.get_fees(n) for n in networks]


class ExplorerModule:
    """Blockchain explorer operations"""
    
    def __init__(self, client: 'KtzchenWeb3'):
        self._client = client
    
    def get_address(self, network: str, address: str) -> Dict[str, Any]:
        """
        Get address information
        
        Args:
            network: Network identifier
            address: Wallet or contract address
            
        Returns:
            Address data
        """
        return self._client._request('GET', f'/v3/{network}/address/{address}/')
    
    def get_transaction(self, network: str, tx_hash: str) -> Dict[str, Any]:
        """
        Get transaction details
        
        Args:
            network: Network identifier
            tx_hash: Transaction hash
            
        Returns:
            Transaction data
        """
        return self._client._request('GET', f'/v3/{network}/tx/{tx_hash}/')
    
    def get_block(self, network: str, block_number: Union[int, str]) -> Dict[str, Any]:
        """
        Get block information
        
        Args:
            network: Network identifier
            block_number: Block number or 'latest'
            
        Returns:
            Block data
        """
        return self._client._request('GET', f'/v3/{network}/block/{block_number}/')
    
    def get_token(self, network: str, token_address: str) -> Dict[str, Any]:
        """
        Get token information
        
        Args:
            network: Network identifier
            token_address: Token contract address
            
        Returns:
            Token data
        """
        return self._client._request('GET', f'/v3/{network}/token/{token_address}/')


class NodeModule:
    """Node status operations"""
    
    SUPPORTED_NETWORKS = [
        'ethereum_mainnet', 'polygon', 'bsc', 'arbitrum',
        'optimism', 'avalanche', 'fantom', 'gnosis'
    ]
    
    def __init__(self, client: 'KtzchenWeb3'):
        self._client = client
    
    def get_status(self, network: str) -> Dict[str, Any]:
        """
        Get node status for a network
        
        Args:
            network: Network identifier
            
        Returns:
            Node status data
        """
        return self._client._request('GET', f'/v3/{network}/node/status/')
    
    def check_all(self) -> List[Dict[str, Any]]:
        """
        Check status of all supported networks
        
        Returns:
            List of node status data
        """
        results = []
        for network in self.SUPPORTED_NETWORKS:
            try:
                results.append(self.get_status(network))
            except KtzchenWeb3Error as e:
                results.append({'network': network, 'error': str(e)})
        return results


class AuditModule:
    """Contract audit operations"""
    
    def __init__(self, client: 'KtzchenWeb3'):
        self._client = client
    
    def request(
        self,
        contract_address: str,
        network: str,
        email: Optional[str] = None,
        source_code: Optional[str] = None,
        priority: str = 'standard'
    ) -> Dict[str, Any]:
        """
        Request a contract audit
        
        Args:
            contract_address: Contract address to audit
            network: Network identifier
            email: Contact email (optional)
            source_code: Contract source code (optional)
            priority: Audit priority ('standard' or 'urgent')
            
        Returns:
            Audit request data
        """
        data = {
            'contract_address': contract_address,
            'network': network,
            'priority': priority
        }
        if email:
            data['contact_email'] = email
        if source_code:
            data['source_code'] = source_code
            
        return self._client._request('POST', '/contract-audit/request/', data)
    
    def get_status(self, audit_id: str) -> Dict[str, Any]:
        """
        Get audit status
        
        Args:
            audit_id: Audit request ID
            
        Returns:
            Audit status data
        """
        return self._client._request('GET', f'/contract-audit/status/{audit_id}/')
    
    def get_plans(self) -> List[Dict[str, Any]]:
        """
        Get available audit plans
        
        Returns:
            List of audit plans
        """
        return self._client._request('GET', '/contract-audit/plans/')


class TraceModule:
    """Transaction tracing operations"""
    
    def __init__(self, client: 'KtzchenWeb3'):
        self._client = client
    
    def trace_transaction(
        self, 
        tx_hash: str, 
        network: str = 'ethereum_mainnet'
    ) -> Dict[str, Any]:
        """
        Trace a transaction
        
        Args:
            tx_hash: Transaction hash
            network: Network identifier
            
        Returns:
            Transaction trace data
        """
        return self._client._request('POST', '/trace/transaction/', {
            'tx_hash': tx_hash,
            'network': network
        })
    
    def trace_block(
        self, 
        block_number: int, 
        network: str = 'ethereum_mainnet'
    ) -> Dict[str, Any]:
        """
        Trace a block
        
        Args:
            block_number: Block number
            network: Network identifier
            
        Returns:
            Block trace data
        """
        return self._client._request('POST', '/trace/block/', {
            'block_number': block_number,
            'network': network
        })


class KtzchenWeb3:
    """
    KtzchenWeb3 API Client
    
    Official Python SDK for the KtzchenWeb3 blockchain API platform.
    
    Example:
        >>> client = KtzchenWeb3(api_key='your_api_key')
        >>> gas = client.gas.get_fees('ethereum_mainnet')
        >>> print(gas['gas_prices']['standard'])
    """
    
    DEFAULT_BASE_URL = 'https://ktzchenweb3.io/api'
    DEFAULT_TIMEOUT = 30
    
    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        timeout: int = DEFAULT_TIMEOUT
    ):
        """
        Initialize the KtzchenWeb3 client
        
        Args:
            api_key: Your API key
            base_url: Base URL (default: https://ktzchenweb3.io/api)
            timeout: Request timeout in seconds (default: 30)
        """
        if not api_key:
            raise ValueError('API key is required')
        
        self.api_key = api_key
        self.base_url = base_url or self.DEFAULT_BASE_URL
        self.timeout = timeout
        
        # Initialize session
        self._session = requests.Session()
        self._session.headers.update({
            'X-API-Key': api_key,
            'Content-Type': 'application/json',
            'User-Agent': 'KtzchenWeb3-Python/1.0.0'
        })
        
        # Initialize modules
        self.gas = GasModule(self)
        self.explorer = ExplorerModule(self)
        self.node = NodeModule(self)
        self.audit = AuditModule(self)
        self.trace = TraceModule(self)
        
        # Rate limit info from last request
        self.last_rate_limit: Optional[RateLimit] = None
    
    def _request(
        self, 
        method: str, 
        endpoint: str, 
        data: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Make an API request
        
        Args:
            method: HTTP method
            endpoint: API endpoint
            data: Request body data (optional)
            
        Returns:
            Response data
            
        Raises:
            KtzchenWeb3Error: On API error
        """
        url = f'{self.base_url}{endpoint}'
        
        try:
            if method.upper() == 'GET':
                response = self._session.get(url, timeout=self.timeout)
            else:
                response = self._session.request(
                    method, url, json=data, timeout=self.timeout
                )
            
            # Parse rate limit headers
            self.last_rate_limit = RateLimit(
                limit=int(response.headers.get('X-RateLimit-Limit', 0)) or None,
                remaining=int(response.headers.get('X-RateLimit-Remaining', 0)) or None,
                reset=int(response.headers.get('X-RateLimit-Reset', 0)) or None
            )
            
            # Parse response
            result = response.json()
            
            if not response.ok:
                raise KtzchenWeb3Error(
                    message=result.get('error', f'HTTP {response.status_code}'),
                    status=response.status_code,
                    details=result.get('details')
                )
            
            return result.get('data', result)
            
        except requests.exceptions.Timeout:
            raise KtzchenWeb3Error('Request timeout', status=408)
        except requests.exceptions.RequestException as e:
            raise KtzchenWeb3Error(str(e), status=0)
    
    def health(self) -> Dict[str, Any]:
        """
        Check API health
        
        Returns:
            Health status data
        """
        return self._request('GET', '/health/')
    
    def __repr__(self) -> str:
        return f'KtzchenWeb3(base_url="{self.base_url}")'


# Convenience function for quick initialization
def create_client(api_key: str, **kwargs) -> KtzchenWeb3:
    """
    Create a KtzchenWeb3 client instance
    
    Args:
        api_key: Your API key
        **kwargs: Additional arguments for KtzchenWeb3
        
    Returns:
        KtzchenWeb3 client instance
    """
    return KtzchenWeb3(api_key=api_key, **kwargs)


__all__ = ['KtzchenWeb3', 'KtzchenWeb3Error', 'RateLimit', 'create_client']
