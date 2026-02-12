<p align="center">
  <img src="assets/logo.png" alt="KtzchenWeb3 Logo" width="150">
</p>

<h1 align="center">KtzchenWeb3</h1>

<p align="center">
  <b>Multi-Chain Blockchain API Platform</b>
</p>

<p align="center">
  <a href="https://ktzchenweb3.io"><img src="https://img.shields.io/badge/Website-ktzchenweb3.io-ffd700?style=for-the-badge" alt="Website"></a>
  <a href="#"><img src="https://img.shields.io/badge/API%20Status-Operational-22c55e?style=for-the-badge" alt="API Status"></a>
  <a href="#"><img src="https://img.shields.io/badge/Version-3.0-6366f1?style=for-the-badge" alt="Version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-22d3ee?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-features">Features</a> •
  <a href="#-supported-networks">Networks</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-examples">Examples</a> •
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

### Trace API Tools

Debug and trace transactions with detailed execution logs.

```bash
# Trace a transaction
curl -X POST "https://ktzchenweb3.io/api/trace/transaction/" \
  -H "Content-Type: application/json" \
  -d '{"tx_hash": "0x..."}'
```

---

## Supported Networks

| Network | API ID | Status |
|---------|--------|--------|
| Ethereum Mainnet | `ethereum_mainnet` | 🟢 Active |
| Polygon | `polygon` | 🟢 Active |
| BNB Smart Chain | `bsc` | 🟢 Active |
| Arbitrum One | `arbitrum` | 🟢 Active |
| Optimism | `optimism` | 🟢 Active |
| Avalanche C-Chain | `avalanche` | 🟢 Active |
| Fantom | `fantom` | 🟢 Active |
| Gnosis Chain | `gnosis` | 🟢 Active |
| Base | `base` | 🟢 Active |
| zkSync Era | `zksync` | 🟢 Active |
| Linea | `linea` | 🟢 Active |

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

## Pricing

| Plan | API Keys | Calls/Day | Rate Limit | Price |
|------|----------|-----------|------------|-------|
| **Core** | 5 | 120,000 | 10 req/sec | **Free** |
| **Developer** | 10 | 250,000 | 15 req/sec | **$24/mo** |
| **Team** | 50 | 750,000 | 30 req/sec | **$110/mo** |
| **Enterprise** | Custom | Custom | Custom | **Contact Us** |

### Plan Features

| Feature | Core | Developer | Team | Enterprise |
|---------|:----:|:---------:|:----:|:----------:|
| Ethereum Mainnet | ✅ | ✅ | ✅ | ✅ |
| All 50+ Networks | ✅ | ✅ | ✅ | ✅ |
| Blockchain Explorer | ✅ | ✅ | ✅ | ✅ |
| Gas Monitor | ✅ | ✅ | ✅ | ✅ |
| Trace API Tools | ✅ | ✅ | ✅ | ✅ |
| Full Archive Data | ✅ | ✅ | ✅ | ✅ |
| Community Forums | ✅ | ✅ | ✅ | ✅ |
| Priority Support | - | ✅ | ✅ | ✅ |
| Advanced Analytics | - | - | ✅ | ✅ |
| Dedicated Support | - | - | - | ✅ |
| SLA Guarantee | - | - | - | ✅ |

Rate limit headers are included in every response:

```
X-RateLimit-Limit: 120000
X-RateLimit-Remaining: 119999
X-RateLimit-Reset: 1707656400
```

[Get Started Free](https://ktzchenweb3.io/register) | [Compare Plans](https://ktzchenweb3.io/pricing)

---

## Support

- **Documentation**: [ktzchenweb3.io/docs](https://ktzchenweb3.io/docs)
- **Discord**: [Join our community](https://discord.gg/gxVJdV4D)
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
  <img src="assets/logo.png" alt="KtzchenWeb3" width="80">
  <br><br>
  <b>Built by Ktzchen Labs</b>
  <br>
  <a href="https://ktzchenweb3.io">ktzchenweb3.io</a>
</p>
