#!/usr/bin/env python3
"""
KtzchenWeb3 API - Python Examples
Basic usage examples for the KtzchenWeb3 blockchain API
"""

import requests
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from datetime import datetime

# Configuration
API_KEY = "your_api_key_here"
BASE_URL = "https://ktzchenweb3.io/api"


# ============================================
# Client Class
# ============================================

class KtzchenWeb3Client:
    """Simple client for KtzchenWeb3 API"""
    
    def __init__(self, api_key: str, base_url: str = BASE_URL):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "X-API-Key": api_key,
            "Content-Type": "application/json"
        })
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make an API request"""
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()
    
    def get(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """GET request"""
        return self._request("GET", endpoint, **kwargs)
    
    def post(self, endpoint: str, data: Dict = None, **kwargs) -> Dict[str, Any]:
        """POST request"""
        return self._request("POST", endpoint, json=data, **kwargs)


# ============================================
# Gas Fees Functions
# ============================================

def get_gas_fees(client: KtzchenWeb3Client, network: str = "ethereum_mainnet") -> Dict:
    """
    Get current gas prices for a network
    
    Args:
        client: KtzchenWeb3Client instance
        network: Network identifier
        
    Returns:
        Gas fees data
    """
    result = client.get(f"/v3/{network}/gas-fees/")
    
    if result.get("success"):
        data = result["data"]
        gas_prices = data["gas_prices"]
        unit = data["unit"]
        
        print(f"\n📊 Gas Fees for {network}:")
        print(f"   Slow:     {gas_prices['slow']} {unit}")
        print(f"   Standard: {gas_prices['standard']} {unit}")
        print(f"   Fast:     {gas_prices['fast']} {unit}")
        print(f"   Instant:  {gas_prices['instant']} {unit}")
        print(f"   Base Fee: {data['base_fee']} {unit}")
    
    return result


def compare_gas_fees(client: KtzchenWeb3Client, 
                     networks: List[str] = None) -> List[Dict]:
    """
    Compare gas fees across multiple networks
    
    Args:
        client: KtzchenWeb3Client instance
        networks: List of network identifiers
        
    Returns:
        List of gas fee data for each network
    """
    if networks is None:
        networks = ["ethereum_mainnet", "polygon", "arbitrum", "bsc"]
    
    print("\n🔄 Comparing gas fees across networks...\n")
    print(f"{'Network':<20}{'Standard':<15}{'Fast'}")
    print("-" * 50)
    
    results = []
    for network in networks:
        try:
            result = client.get(f"/v3/{network}/gas-fees/")
            if result.get("success"):
                gas_prices = result["data"]["gas_prices"]
                print(f"{network:<20}{gas_prices['standard']:<15}{gas_prices['fast']}")
                results.append({"network": network, **result["data"]})
            else:
                print(f"{network:<20}Error")
                results.append({"network": network, "error": "Failed"})
        except Exception as e:
            print(f"{network:<20}Error: {e}")
            results.append({"network": network, "error": str(e)})
    
    return results


# ============================================
# Blockchain Explorer Functions
# ============================================

def get_address_info(client: KtzchenWeb3Client, 
                     network: str, 
                     address: str) -> Dict:
    """
    Get address information including balance and transactions
    
    Args:
        client: KtzchenWeb3Client instance
        network: Network identifier
        address: Wallet or contract address
        
    Returns:
        Address data
    """
    result = client.get(f"/v3/{network}/address/{address}/")
    
    if result.get("success"):
        data = result["data"]
        print(f"\n📍 Address Info:")
        print(f"   Address: {address}")
        print(f"   Balance: {data['balance']} ETH")
        print(f"   Transactions: {data['transaction_count']}")
        print(f"   Is Contract: {data['is_contract']}")
    
    return result


def get_transaction(client: KtzchenWeb3Client, 
                   network: str, 
                   tx_hash: str) -> Dict:
    """
    Get transaction details
    
    Args:
        client: KtzchenWeb3Client instance
        network: Network identifier
        tx_hash: Transaction hash
        
    Returns:
        Transaction data
    """
    result = client.get(f"/v3/{network}/tx/{tx_hash}/")
    
    if result.get("success"):
        data = result["data"]
        print(f"\n📝 Transaction Details:")
        print(f"   Hash: {tx_hash}")
        print(f"   From: {data['from']}")
        print(f"   To: {data['to']}")
        print(f"   Value: {data['value']} ETH")
        print(f"   Status: {data['status']}")
        print(f"   Gas Used: {data['gas_used']}")
        print(f"   Confirmations: {data['confirmations']}")
    
    return result


def get_latest_block(client: KtzchenWeb3Client, 
                    network: str = "ethereum_mainnet") -> Dict:
    """
    Get latest block information
    
    Args:
        client: KtzchenWeb3Client instance
        network: Network identifier
        
    Returns:
        Block data
    """
    result = client.get(f"/v3/{network}/block/latest/")
    
    if result.get("success"):
        data = result["data"]
        print(f"\n🧱 Latest Block on {network}:")
        print(f"   Number: {data['number']}")
        print(f"   Hash: {data['hash'][:20]}...")
        print(f"   Transactions: {data['transaction_count']}")
        print(f"   Gas Used: {data['gas_used']}")
        print(f"   Time: {data['timestamp']}")
    
    return result


def get_token_info(client: KtzchenWeb3Client, 
                  network: str, 
                  token_address: str) -> Dict:
    """
    Get ERC-20 token information
    
    Args:
        client: KtzchenWeb3Client instance
        network: Network identifier
        token_address: Token contract address
        
    Returns:
        Token data
    """
    result = client.get(f"/v3/{network}/token/{token_address}/")
    
    if result.get("success"):
        data = result["data"]
        print(f"\n🪙 Token Info:")
        print(f"   Name: {data['name']}")
        print(f"   Symbol: {data['symbol']}")
        print(f"   Decimals: {data['decimals']}")
        print(f"   Total Supply: {data['total_supply']}")
        print(f"   Holders: {data['holders']}")
    
    return result


# ============================================
# Node Status Functions
# ============================================

def check_node_status(client: KtzchenWeb3Client, 
                     network: str = "ethereum_mainnet") -> Dict:
    """
    Check node status for a network
    
    Args:
        client: KtzchenWeb3Client instance
        network: Network identifier
        
    Returns:
        Node status data
    """
    result = client.get(f"/v3/{network}/node/status/")
    
    if result.get("success"):
        data = result["data"]
        print(f"\n🖥️ Node Status for {network}:")
        print(f"   Status: {data['status']}")
        print(f"   Latest Block: {data['latest_block']}")
        print(f"   Syncing: {data['syncing']}")
        print(f"   Response Time: {data['response_time_ms']}ms")
        print(f"   Uptime: {data['uptime_percent']}%")
    
    return result


def check_all_networks(client: KtzchenWeb3Client) -> List[Dict]:
    """
    Check health of all supported networks
    
    Args:
        client: KtzchenWeb3Client instance
        
    Returns:
        List of network status data
    """
    networks = [
        "ethereum_mainnet", "polygon", "bsc", "arbitrum",
        "optimism", "avalanche", "fantom", "gnosis"
    ]
    
    print("\n🌐 Checking all network statuses...\n")
    print(f"{'Network':<20}{'Status':<12}{'Block':<12}Response")
    print("-" * 60)
    
    results = []
    for network in networks:
        try:
            result = client.get(f"/v3/{network}/node/status/")
            if result.get("success"):
                data = result["data"]
                status_emoji = "🟢" if data["status"] == "healthy" else "🔴"
                print(f"{network:<20}{status_emoji} {data['status']:<9}{data['latest_block']:<12}{data['response_time_ms']}ms")
                results.append({"network": network, **data})
            else:
                print(f"{network:<20}🔴 Error")
        except Exception as e:
            print(f"{network:<20}🔴 Error")
            results.append({"network": network, "error": str(e)})
    
    return results


# ============================================
# Contract Audit Functions
# ============================================

def request_contract_audit(client: KtzchenWeb3Client,
                          contract_address: str,
                          network: str = "ethereum_mainnet",
                          email: Optional[str] = None) -> Dict:
    """
    Request a contract audit
    
    Args:
        client: KtzchenWeb3Client instance
        contract_address: Contract address to audit
        network: Network identifier
        email: Contact email (optional)
        
    Returns:
        Audit request data
    """
    data = {
        "contract_address": contract_address,
        "network": network
    }
    if email:
        data["contact_email"] = email
    
    result = client.post("/contract-audit/request/", data)
    
    if result.get("success"):
        audit_data = result["data"]
        print(f"\n🔍 Audit Request Submitted:")
        print(f"   Audit ID: {audit_data['audit_id']}")
        print(f"   Status: {audit_data['status']}")
        print(f"   Est. Completion: {audit_data['estimated_completion']}")
    
    return result


def get_audit_plans(client: KtzchenWeb3Client) -> Dict:
    """
    Get available audit plans
    
    Args:
        client: KtzchenWeb3Client instance
        
    Returns:
        List of audit plans
    """
    result = client.get("/contract-audit/plans/")
    
    if result.get("success"):
        print("\n📋 Available Audit Plans:\n")
        for plan in result["data"]:
            print(f"   {plan['name']} - ${plan['price_usd']}")
            for feature in plan["features"]:
                print(f"      ✓ {feature}")
            print()
    
    return result


# ============================================
# Main Example Runner
# ============================================

def run_examples():
    """Run all example functions"""
    print("=" * 60)
    print("   KtzchenWeb3 API - Python Examples")
    print("=" * 60)
    
    # Initialize client
    client = KtzchenWeb3Client(API_KEY)
    
    # Gas fees
    get_gas_fees(client, "ethereum_mainnet")
    get_gas_fees(client, "polygon")
    
    # Compare networks
    compare_gas_fees(client)
    
    # Node status
    check_node_status(client, "ethereum_mainnet")
    
    # Check all networks
    check_all_networks(client)
    
    # Audit plans
    get_audit_plans(client)
    
    print("\n✅ All examples completed!")


if __name__ == "__main__":
    run_examples()
