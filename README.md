<p align="center">
  <img src="assets/banner.svg" alt="KtzchenWeb3 Banner" width="100%">
</p>

<p align="center">
  <a href="https://ktzchenweb3.io"><img src="https://img.shields.io/badge/Website-ktzchenweb3.io-6366f1?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNy45M2MtMy45NS0uNDktNy0zLjg1LTctNy45MyAwLS42Mi4wOC0xLjIxLjIxLTEuNzlMOSAxNXYxYzAgMS4xLjkgMiAyIDJ2MS45M3ptNi45LTIuNTRjLS4yNi0uODEtMS0xLjM5LTEuOS0xLjM5aC0xdi0zYzAtLjU1LS40NS0xLTEtMUg4di0yaDJjLjU1IDAgMS0uNDUgMS0xVjdoMmMxLjEgMCAyLS45IDItMnYtLjQxYzIuOTMgMS4xOSA1IDQuMDYgNSA3LjQxIDAgMi4wOC0uOCAzLjk3LTIuMSA1LjM5eiIvPjwvc3ZnPg==" alt="Website"></a>
  <a href="#"><img src="https://img.shields.io/badge/API%20Status-Operational-22c55e?style=for-the-badge" alt="API Status"></a>
  <a href="#"><img src="https://img.shields.io/badge/Version-3.0-a855f7?style=for-the-badge" alt="Version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-22d3ee?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <b>Enterprise-grade Multi-Chain Blockchain API for Web3 Developers</b>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-features">Features</a> •
  <a href="#-supported-networks">Networks</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-examples">Examples</a> •
  <a href="#-sdk">SDK</a> •
  <a href="#-pricing">Pricing</a>
</p>

---

## What is KtzchenWeb3?

**KtzchenWeb3** is a comprehensive blockchain infrastructure platform that provides developers with reliable, fast, and unified access to multiple blockchain networks through a single API. Build decentralized applications without worrying about node management, network reliability, or complex integrations.

### Why Choose KtzchenWeb3?

- **Multi-Chain Support**: Access 50+ blockchain networks through one unified API
- **Real-Time Data**: Get gas prices, block data, and transaction info in milliseconds
- **Smart Contract Auditing**: Professional security audits for your smart contracts
- **99.9% Uptime**: Enterprise-grade infrastructure with automatic failover
- **Developer-First**: Clean RESTful API with comprehensive documentation

---

## Quick Start

### 1. Get Your API Key

Sign up at [ktzchenweb3.io](https://ktzchenweb3.io) to get your free API key.

### 2. Make Your First Request

```bash
# Get current gas prices on Ethereum
curl -X GET "https://ktzchenweb3.io/api/v3/ethereum_mainnet/gas-fees/" \
  -H "X-API-Key: your_api_key_here"
```

### 3. Explore the Response

```json
{
  "success": true,
  "data": {
    "network": "ethereum_mainnet",
    "gas_prices": {
      "slow": "15.2",
      "standard": "18.5",
      "fast": "25.1",
      "instant": "35.0"
    },
    "base_fee": "14.8",
    "priority_fee": "1.5",
    "unit": "gwei",
    "timestamp": "2026-02-11T12:00:00Z"
  }
}
```

---

## Features

### Blockchain Explorer API

Query any address, transaction, block, or token across supported networks.

```bash
# Get address balance and transactions
curl "https://ktzchenweb3.io/api/v3/ethereum_mainnet/address/0x742d35Cc6634C0532925a3b844Bc9e7595f8dB21/"
```

### Gas Fees API

Real-time gas price recommendations for optimal transaction costs.

```bash
# Get gas fees for Polygon
curl "https://ktzchenweb3.io/api/v3/polygon/gas-fees/"
```

### Smart Contract Audit

Professional security audits with vulnerability detection and recommendations.

```bash
# Request an audit
curl -X POST "https://ktzchenweb3.io/api/contract-audit/request/" \
  -H "Content-Type: application/json" \
  -d '{
    "contract_address": "0x...",
    "network": "ethereum_mainnet"
  }'
```

### Node Status & Health

Monitor network health and node status in real-time.

```bash
# Check node status
curl "https://ktzchenweb3.io/api/v3/ethereum_mainnet/node/status/"
```

### Transaction Tracing

Debug and trace transactions with detailed execution logs.

```bash
# Trace a transaction
curl -X POST "https://ktzchenweb3.io/api/trace/transaction/" \
  -H "Content-Type: application/json" \
  -d '{"tx_hash": "0x..."}'
```

---

## Supported Networks

<table>
  <tr>
    <th>Network</th>
    <th>ID</th>
    <th>Status</th>
  </tr>
  <tr>
    <td><img src="https://cryptologos.cc/logos/ethereum-eth-logo.svg?v=026" width="20"> Ethereum Mainnet</td>
    <td><code>ethereum_mainnet</code></td>
    <td>🟢 Active</td>
  </tr>
  <tr>
    <td><img src="https://cryptologos.cc/logos/polygon-matic-logo.svg?v=026" width="20"> Polygon</td>
    <td><code>polygon</code></td>
    <td>🟢 Active</td>
  </tr>
  <tr>
    <td><img src="https://cryptologos.cc/logos/bnb-bnb-logo.svg?v=026" width="20"> BNB Smart Chain</td>
    <td><code>bsc</code></td>
    <td>🟢 Active</td>
  </tr>
  <tr>
    <td><img src="https://cryptologos.cc/logos/arbitrum-arb-logo.svg?v=026" width="20"> Arbitrum One</td>
    <td><code>arbitrum</code></td>
    <td>🟢 Active</td>
  </tr>
  <tr>
    <td><img src="https://cryptologos.cc/logos/optimism-ethereum-op-logo.svg?v=026" width="20"> Optimism</td>
    <td><code>optimism</code></td>
    <td>🟢 Active</td>
  </tr>
  <tr>
    <td><img src="https://cryptologos.cc/logos/avalanche-avax-logo.svg?v=026" width="20"> Avalanche C-Chain</td>
    <td><code>avalanche</code></td>
    <td>🟢 Active</td>
  </tr>
  <tr>
    <td><img src="https://cryptologos.cc/logos/fantom-ftm-logo.svg?v=026" width="20"> Fantom</td>
    <td><code>fantom</code></td>
    <td>🟢 Active</td>
  </tr>
  <tr>
    <td><img src="https://cryptologos.cc/logos/gnosis-gno-gno-logo.svg?v=026" width="20"> Gnosis Chain</td>
    <td><code>gnosis</code></td>
    <td>🟢 Active</td>
  </tr>
</table>

**+ 40 more networks available!** See [full network list](docs/NETWORKS.md).

---

## API Reference

### Base URL

```
https://ktzchenweb3.io/api
```

### Authentication

All API requests require authentication via API key:

```bash
# Header authentication (recommended)
curl -H "X-API-Key: your_api_key" https://ktzchenweb3.io/api/...

# Or via Bearer token (JWT)
curl -H "Authorization: Bearer your_jwt_token" https://ktzchenweb3.io/api/...
```

### Response Format

All responses follow a consistent format:

```json
{
  "success": true,
  "data": { ... },
  "message": "Operation successful"
}
```

Error responses:

```json
{
  "success": false,
  "error": "Error description",
  "details": { ... }
}
```

### Core Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v3/{network}/gas-fees/` | GET | Get current gas prices |
| `/api/v3/{network}/node/status/` | GET | Get node status |
| `/api/v3/{network}/address/{address}/` | GET | Get address info |
| `/api/v3/{network}/tx/{hash}/` | GET | Get transaction details |
| `/api/v3/{network}/block/{number}/` | GET | Get block data |
| `/api/v3/{network}/token/{address}/` | GET | Get token info |
| `/api/contract-audit/request/` | POST | Request contract audit |
| `/api/health/` | GET | API health check |

See [full API documentation](docs/API.md) for complete endpoint reference.

---

## Examples

### JavaScript / Node.js

```javascript
// Using fetch
const API_KEY = 'your_api_key';
const BASE_URL = 'https://ktzchenweb3.io/api';

async function getGasFees(network) {
  const response = await fetch(`${BASE_URL}/v3/${network}/gas-fees/`, {
    headers: { 'X-API-Key': API_KEY }
  });
  return response.json();
}

// Get Ethereum gas fees
const gasFees = await getGasFees('ethereum_mainnet');
console.log('Current gas:', gasFees.data.gas_prices.standard, 'gwei');
```

### Python

```python
import requests

API_KEY = 'your_api_key'
BASE_URL = 'https://ktzchenweb3.io/api'

def get_gas_fees(network):
    response = requests.get(
        f'{BASE_URL}/v3/{network}/gas-fees/',
        headers={'X-API-Key': API_KEY}
    )
    return response.json()

# Get Polygon gas fees
gas_fees = get_gas_fees('polygon')
print(f"Current gas: {gas_fees['data']['gas_prices']['standard']} gwei")
```

### cURL

```bash
# Get address balance
curl -X GET "https://ktzchenweb3.io/api/v3/ethereum_mainnet/address/0x742d35Cc6634C0532925a3b844Bc9e7595f8dB21/" \
  -H "X-API-Key: your_api_key"

# Get transaction details
curl -X GET "https://ktzchenweb3.io/api/v3/ethereum_mainnet/tx/0x123.../" \
  -H "X-API-Key: your_api_key"
```

More examples in the [examples directory](examples/).

---

## SDK

### Installation

```bash
# JavaScript/TypeScript
npm install @ktzchenweb3/sdk

# Python
pip install ktzchenweb3
```

### Quick Usage

**JavaScript:**

```javascript
import { KtzchenWeb3 } from '@ktzchenweb3/sdk';

const client = new KtzchenWeb3({ apiKey: 'your_api_key' });

// Get gas fees
const gas = await client.gas.getFees('ethereum_mainnet');

// Get address info
const address = await client.explorer.getAddress('ethereum_mainnet', '0x...');

// Request contract audit
const audit = await client.audit.request({
  contractAddress: '0x...',
  network: 'ethereum_mainnet'
});
```

**Python:**

```python
from ktzchenweb3 import KtzchenWeb3

client = KtzchenWeb3(api_key='your_api_key')

# Get gas fees
gas = client.gas.get_fees('ethereum_mainnet')

# Get address info
address = client.explorer.get_address('ethereum_mainnet', '0x...')
```

See [SDK documentation](sdk/README.md) for complete reference.

---

## Rate Limits

| Plan | Requests/Day | Rate Limit | Networks |
|------|-------------|------------|----------|
| **Free** | 1,000 | 10 req/min | All |
| **Starter** | 50,000 | 100 req/min | All |
| **Pro** | 500,000 | 1,000 req/min | All + Priority |
| **Enterprise** | Unlimited | Custom | All + Dedicated |

Rate limit headers are included in every response:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1707656400
```

---

## Pricing

| Feature | Free | Starter | Pro | Enterprise |
|---------|------|---------|-----|------------|
| API Calls/Day | 1,000 | 50,000 | 500,000 | Unlimited |
| Networks | All | All | All | All + Private |
| Support | Community | Email | Priority | Dedicated |
| SLA | - | 99% | 99.9% | 99.99% |
| Contract Audits | 1/month | 5/month | 20/month | Unlimited |
| Price | $0 | $29/mo | $99/mo | Custom |

[Get Started Free](https://ktzchenweb3.io/register) | [Compare Plans](https://ktzchenweb3.io/pricing)

---

## Support

- **Documentation**: [docs.ktzchenweb3.io](https://docs.ktzchenweb3.io)
- **Discord**: [Join our community](https://discord.gg/ktzchenweb3)
- **Twitter**: [@ktzchenweb3](https://twitter.com/ktzchenweb3)
- **Email**: support@ktzchenweb3.io

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <img src="assets/logo.svg" alt="KtzchenWeb3" width="60">
  <br>
  <b>Built with ❤️ by the KtzchenWeb3 Team</b>
  <br>
  <a href="https://ktzchenweb3.io">ktzchenweb3.io</a>
</p>
