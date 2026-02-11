# KtzchenWeb3 API Reference

Complete API documentation for the KtzchenWeb3 blockchain infrastructure platform.

## Base URL

```
Production: https://ktzchenweb3.io/api
```

## Authentication

All authenticated endpoints require one of the following:

### API Key (Recommended)

```bash
curl -H "X-API-Key: your_api_key" https://ktzchenweb3.io/api/...
```

### JWT Token

```bash
curl -H "Authorization: Bearer your_jwt_token" https://ktzchenweb3.io/api/...
```

---

## Gas Fees API

### Get Gas Prices

Returns current gas prices for a specific network.

**Endpoint:** `GET /api/v3/{network}/gas-fees/`

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| network | string | Yes | Network identifier (e.g., `ethereum_mainnet`) |

**Example Request:**

```bash
curl -X GET "https://ktzchenweb3.io/api/v3/ethereum_mainnet/gas-fees/" \
  -H "X-API-Key: your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "network": "ethereum_mainnet",
    "gas_prices": {
      "slow": "12.5",
      "standard": "15.8",
      "fast": "22.3",
      "instant": "35.0"
    },
    "base_fee": "12.1",
    "priority_fee": "1.5",
    "estimated_time": {
      "slow": "10 min",
      "standard": "3 min",
      "fast": "30 sec",
      "instant": "15 sec"
    },
    "unit": "gwei",
    "last_block": 19234567,
    "timestamp": "2026-02-11T12:00:00Z"
  }
}
```

---

## Blockchain Explorer API

### Get Address Information

Returns balance, transaction count, and recent transactions for an address.

**Endpoint:** `GET /api/v3/{network}/address/{address}/`

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| network | string | Yes | Network identifier |
| address | string | Yes | Wallet or contract address |

**Example Request:**

```bash
curl -X GET "https://ktzchenweb3.io/api/v3/ethereum_mainnet/address/0x742d35Cc6634C0532925a3b844Bc9e7595f8dB21/" \
  -H "X-API-Key: your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "address": "0x742d35Cc6634C0532925a3b844Bc9e7595f8dB21",
    "balance": "1.234567890123456789",
    "balance_wei": "1234567890123456789",
    "transaction_count": 42,
    "is_contract": false,
    "first_seen": "2024-01-15T10:30:00Z",
    "last_activity": "2026-02-10T18:45:00Z",
    "recent_transactions": [
      {
        "hash": "0x...",
        "from": "0x...",
        "to": "0x...",
        "value": "0.5",
        "timestamp": "2026-02-10T18:45:00Z"
      }
    ]
  }
}
```

### Get Transaction Details

Returns detailed information about a specific transaction.

**Endpoint:** `GET /api/v3/{network}/tx/{hash}/`

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| network | string | Yes | Network identifier |
| hash | string | Yes | Transaction hash |

**Example Request:**

```bash
curl -X GET "https://ktzchenweb3.io/api/v3/ethereum_mainnet/tx/0x123abc.../" \
  -H "X-API-Key: your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "hash": "0x123abc...",
    "block_number": 19234567,
    "block_hash": "0x...",
    "from": "0x...",
    "to": "0x...",
    "value": "1.5",
    "value_wei": "1500000000000000000",
    "gas_used": 21000,
    "gas_price": "15.5",
    "gas_price_wei": "15500000000",
    "nonce": 42,
    "status": "success",
    "timestamp": "2026-02-10T15:30:00Z",
    "confirmations": 125
  }
}
```

### Get Block Information

Returns detailed information about a specific block.

**Endpoint:** `GET /api/v3/{network}/block/{identifier}/`

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| network | string | Yes | Network identifier |
| identifier | string/int | Yes | Block number or `latest` |

**Example Request:**

```bash
curl -X GET "https://ktzchenweb3.io/api/v3/ethereum_mainnet/block/19234567/" \
  -H "X-API-Key: your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "number": 19234567,
    "hash": "0x...",
    "parent_hash": "0x...",
    "timestamp": "2026-02-10T15:30:00Z",
    "miner": "0x...",
    "gas_used": 12500000,
    "gas_limit": 30000000,
    "base_fee_per_gas": "12.5",
    "transaction_count": 185,
    "size": 125000
  }
}
```

### Get Token Information

Returns information about an ERC-20/BEP-20 token.

**Endpoint:** `GET /api/v3/{network}/token/{address}/`

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| network | string | Yes | Network identifier |
| address | string | Yes | Token contract address |

**Example Request:**

```bash
curl -X GET "https://ktzchenweb3.io/api/v3/ethereum_mainnet/token/0xdAC17F958D2ee523a2206206994597C13D831ec7/" \
  -H "X-API-Key: your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
    "name": "Tether USD",
    "symbol": "USDT",
    "decimals": 6,
    "total_supply": "50000000000000000",
    "holders": 5234567,
    "transfers_24h": 125000
  }
}
```

---

## Node Status API

### Get Node Status

Returns current status and health of network nodes.

**Endpoint:** `GET /api/v3/{network}/node/status/`

**Example Request:**

```bash
curl -X GET "https://ktzchenweb3.io/api/v3/ethereum_mainnet/node/status/" \
  -H "X-API-Key: your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "network": "ethereum_mainnet",
    "status": "healthy",
    "latest_block": 19234567,
    "syncing": false,
    "peer_count": 125,
    "response_time_ms": 45,
    "uptime_percent": 99.99,
    "last_check": "2026-02-11T12:00:00Z"
  }
}
```

---

## Contract Audit API

### Request Audit

Submit a smart contract for security audit.

**Endpoint:** `POST /api/contract-audit/request/`

**Request Body:**

```json
{
  "contract_address": "0x...",
  "network": "ethereum_mainnet",
  "source_code": "// optional: paste source code",
  "contact_email": "dev@example.com",
  "priority": "standard"
}
```

**Example Request:**

```bash
curl -X POST "https://ktzchenweb3.io/api/contract-audit/request/" \
  -H "X-API-Key: your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "contract_address": "0x742d35Cc6634C0532925a3b844Bc9e7595f8dB21",
    "network": "ethereum_mainnet",
    "contact_email": "dev@example.com"
  }'
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "audit_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "status": "pending",
    "estimated_completion": "2026-02-14T12:00:00Z",
    "contract_address": "0x...",
    "network": "ethereum_mainnet"
  },
  "message": "Audit request submitted successfully"
}
```

### Get Audit Status

Check the status of an audit request.

**Endpoint:** `GET /api/contract-audit/status/{audit_id}/`

**Example Response:**

```json
{
  "success": true,
  "data": {
    "audit_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "status": "in_progress",
    "progress_percent": 65,
    "started_at": "2026-02-11T10:00:00Z",
    "estimated_completion": "2026-02-14T12:00:00Z",
    "findings_preview": {
      "critical": 0,
      "high": 1,
      "medium": 3,
      "low": 5,
      "informational": 8
    }
  }
}
```

### Get Audit Plans

List available audit plans and pricing.

**Endpoint:** `GET /api/contract-audit/plans/`

**Example Response:**

```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Basic",
      "price_usd": 499,
      "features": [
        "Automated vulnerability scan",
        "Gas optimization report",
        "48-hour delivery"
      ]
    },
    {
      "id": 2,
      "name": "Standard",
      "price_usd": 1499,
      "features": [
        "Manual code review",
        "Vulnerability assessment",
        "Remediation guidance",
        "7-day delivery"
      ]
    },
    {
      "id": 3,
      "name": "Premium",
      "price_usd": 4999,
      "features": [
        "Comprehensive manual audit",
        "Economic attack analysis",
        "Re-audit after fixes",
        "Certification badge"
      ]
    }
  ]
}
```

---

## Transaction Tracing API

### Trace Transaction

Get detailed execution trace of a transaction.

**Endpoint:** `POST /api/trace/transaction/`

**Request Body:**

```json
{
  "tx_hash": "0x...",
  "network": "ethereum_mainnet"
}
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "tx_hash": "0x...",
    "trace": [
      {
        "type": "call",
        "from": "0x...",
        "to": "0x...",
        "value": "1000000000000000000",
        "gas": 21000,
        "input": "0x...",
        "output": "0x"
      }
    ],
    "logs": [...],
    "internal_transactions": [...]
  }
}
```

---

## Health & Status

### API Health Check

**Endpoint:** `GET /api/health/`

No authentication required.

**Example Response:**

```json
{
  "success": true,
  "data": {
    "status": "healthy",
    "version": "3.0.0",
    "uptime": "99.99%",
    "timestamp": "2026-02-11T12:00:00Z"
  }
}
```

### Public System Metrics

**Endpoint:** `GET /api/public/system/metrics/`

No authentication required.

**Example Response:**

```json
{
  "success": true,
  "data": {
    "requests_today": 15234567,
    "active_users": 12500,
    "networks_online": 50,
    "avg_response_time_ms": 45
  }
}
```

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Invalid or missing API key |
| 403 | Forbidden - Access denied |
| 404 | Not Found - Resource doesn't exist |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error |
| 503 | Service Unavailable - Network temporarily down |

---

## Rate Limiting

Rate limits are applied per API key:

| Plan | API Keys | Requests/Day | Rate Limit |
|------|----------|-------------|------------|
| Core (Free) | 5 | 120,000 | 10 req/sec |
| Developer ($24/mo) | 10 | 250,000 | 15 req/sec |
| Team ($110/mo) | 50 | 750,000 | 30 req/sec |
| Enterprise | Custom | Custom | Custom |

Rate limit headers:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1707656400
```

---

## Webhooks (Coming Soon)

Subscribe to real-time events:

- New transactions to/from address
- Contract events
- Gas price alerts
- Block confirmations

---

## SDKs

- [JavaScript/TypeScript SDK](../sdk/javascript/)
- [Python SDK](../sdk/python/)

---

## Support

- Email: api-support@ktzchenweb3.io
- Discord: [Join Community](https://discord.gg/ktzchenweb3)
- Documentation: [docs.ktzchenweb3.io](https://docs.ktzchenweb3.io)
