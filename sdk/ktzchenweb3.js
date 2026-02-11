/**
 * KtzchenWeb3 SDK - JavaScript/TypeScript
 * Official SDK for the KtzchenWeb3 blockchain API platform
 * 
 * @version 1.0.0
 * @license MIT
 */

class KtzchenWeb3Error extends Error {
  constructor(message, status, details = null) {
    super(message);
    this.name = 'KtzchenWeb3Error';
    this.status = status;
    this.details = details;
  }
}

class GasModule {
  constructor(client) {
    this.client = client;
  }

  async getFees(network) {
    return this.client._request('GET', `/v3/${network}/gas-fees/`);
  }

  async getFeesMultiple(networks) {
    return Promise.all(networks.map(n => this.getFees(n)));
  }
}

class ExplorerModule {
  constructor(client) {
    this.client = client;
  }

  async getAddress(network, address) {
    return this.client._request('GET', `/v3/${network}/address/${address}/`);
  }

  async getTransaction(network, txHash) {
    return this.client._request('GET', `/v3/${network}/tx/${txHash}/`);
  }

  async getBlock(network, blockNumber) {
    return this.client._request('GET', `/v3/${network}/block/${blockNumber}/`);
  }

  async getToken(network, tokenAddress) {
    return this.client._request('GET', `/v3/${network}/token/${tokenAddress}/`);
  }
}

class NodeModule {
  constructor(client) {
    this.client = client;
  }

  async getStatus(network) {
    return this.client._request('GET', `/v3/${network}/node/status/`);
  }

  async checkAll() {
    const networks = [
      'ethereum_mainnet', 'polygon', 'bsc', 'arbitrum',
      'optimism', 'avalanche', 'fantom', 'gnosis'
    ];
    return Promise.all(networks.map(n => this.getStatus(n).catch(e => ({ network: n, error: e.message }))));
  }
}

class AuditModule {
  constructor(client) {
    this.client = client;
  }

  async request({ contractAddress, network, email, sourceCode, priority }) {
    return this.client._request('POST', '/contract-audit/request/', {
      contract_address: contractAddress,
      network,
      contact_email: email,
      source_code: sourceCode,
      priority
    });
  }

  async getStatus(auditId) {
    return this.client._request('GET', `/contract-audit/status/${auditId}/`);
  }

  async getPlans() {
    return this.client._request('GET', '/contract-audit/plans/');
  }
}

class TraceModule {
  constructor(client) {
    this.client = client;
  }

  async traceTransaction(txHash, network = 'ethereum_mainnet') {
    return this.client._request('POST', '/trace/transaction/', {
      tx_hash: txHash,
      network
    });
  }

  async traceBlock(blockNumber, network = 'ethereum_mainnet') {
    return this.client._request('POST', '/trace/block/', {
      block_number: blockNumber,
      network
    });
  }

  async traceCall(params) {
    return this.client._request('POST', '/trace/call/', params);
  }
}

class KtzchenWeb3 {
  /**
   * Create a new KtzchenWeb3 client
   * @param {Object} options - Configuration options
   * @param {string} options.apiKey - Your API key
   * @param {string} [options.baseUrl] - Base URL (default: https://ktzchenweb3.io/api)
   * @param {number} [options.timeout] - Request timeout in ms (default: 30000)
   */
  constructor(options = {}) {
    if (!options.apiKey) {
      throw new Error('API key is required');
    }

    this.apiKey = options.apiKey;
    this.baseUrl = options.baseUrl || 'https://ktzchenweb3.io/api';
    this.timeout = options.timeout || 30000;

    // Initialize modules
    this.gas = new GasModule(this);
    this.explorer = new ExplorerModule(this);
    this.node = new NodeModule(this);
    this.audit = new AuditModule(this);
    this.trace = new TraceModule(this);
  }

  /**
   * Make an API request
   * @private
   */
  async _request(method, endpoint, body = null) {
    const url = `${this.baseUrl}${endpoint}`;
    
    const options = {
      method,
      headers: {
        'X-API-Key': this.apiKey,
        'Content-Type': 'application/json'
      }
    };

    if (body && method !== 'GET') {
      options.body = JSON.stringify(body);
    }

    // Create abort controller for timeout
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), this.timeout);
    options.signal = controller.signal;

    try {
      const response = await fetch(url, options);
      clearTimeout(timeoutId);

      const data = await response.json();

      if (!response.ok) {
        throw new KtzchenWeb3Error(
          data.error || `HTTP ${response.status}`,
          response.status,
          data.details
        );
      }

      // Extract rate limit info
      const rateLimit = {
        limit: response.headers.get('X-RateLimit-Limit'),
        remaining: response.headers.get('X-RateLimit-Remaining'),
        reset: response.headers.get('X-RateLimit-Reset')
      };

      return {
        ...data.data,
        _rateLimit: rateLimit
      };
    } catch (error) {
      clearTimeout(timeoutId);
      
      if (error.name === 'AbortError') {
        throw new KtzchenWeb3Error('Request timeout', 408);
      }
      
      if (error instanceof KtzchenWeb3Error) {
        throw error;
      }
      
      throw new KtzchenWeb3Error(error.message, 0);
    }
  }

  /**
   * Check API health
   */
  async health() {
    return this._request('GET', '/health/');
  }
}

// Export for different module systems
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { KtzchenWeb3, KtzchenWeb3Error };
}

if (typeof window !== 'undefined') {
  window.KtzchenWeb3 = KtzchenWeb3;
  window.KtzchenWeb3Error = KtzchenWeb3Error;
}

export { KtzchenWeb3, KtzchenWeb3Error };
export default KtzchenWeb3;
