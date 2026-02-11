# KtzchenWeb3 SDK

Official SDKs for the KtzchenWeb3 blockchain API platform.

## Available SDKs

- **JavaScript/TypeScript** - `@ktzchenweb3/sdk`
- **Python** - `ktzchenweb3`

## JavaScript/TypeScript SDK

### Installation

```bash
npm install @ktzchenweb3/sdk
# or
yarn add @ktzchenweb3/sdk
# or
pnpm add @ktzchenweb3/sdk
```

### Quick Start

```typescript
import { KtzchenWeb3 } from '@ktzchenweb3/sdk';

// Initialize the client
const client = new KtzchenWeb3({
  apiKey: 'your_api_key_here'
});

// Get gas fees
const gasFees = await client.gas.getFees('ethereum_mainnet');
console.log('Standard gas:', gasFees.gas_prices.standard, 'gwei');

// Get address info
const addressInfo = await client.explorer.getAddress(
  'ethereum_mainnet',
  '0x742d35Cc6634C0532925a3b844Bc9e7595f8dB21'
);
console.log('Balance:', addressInfo.balance, 'ETH');

// Check node status
const nodeStatus = await client.node.getStatus('polygon');
console.log('Node status:', nodeStatus.status);

// Request contract audit
const audit = await client.audit.request({
  contractAddress: '0x...',
  network: 'ethereum_mainnet',
  email: 'dev@example.com'
});
console.log('Audit ID:', audit.audit_id);
```

### API Reference

#### Constructor

```typescript
new KtzchenWeb3(options: KtzchenWeb3Options)
```

**Options:**

| Option | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| apiKey | string | Yes | - | Your API key |
| baseUrl | string | No | `https://ktzchenweb3.io/api` | Base URL |
| timeout | number | No | 30000 | Request timeout (ms) |

#### Gas Module

```typescript
// Get gas fees for a network
client.gas.getFees(network: string): Promise<GasFeesResponse>

// Get gas fees for multiple networks
client.gas.getFeesMultiple(networks: string[]): Promise<GasFeesResponse[]>
```

#### Explorer Module

```typescript
// Get address information
client.explorer.getAddress(network: string, address: string): Promise<AddressResponse>

// Get transaction details
client.explorer.getTransaction(network: string, txHash: string): Promise<TransactionResponse>

// Get block information
client.explorer.getBlock(network: string, blockNumber: number | 'latest'): Promise<BlockResponse>

// Get token information
client.explorer.getToken(network: string, tokenAddress: string): Promise<TokenResponse>
```

#### Node Module

```typescript
// Get node status
client.node.getStatus(network: string): Promise<NodeStatusResponse>

// Check multiple networks
client.node.checkAll(): Promise<NodeStatusResponse[]>
```

#### Audit Module

```typescript
// Request a contract audit
client.audit.request(options: AuditRequestOptions): Promise<AuditResponse>

// Get audit status
client.audit.getStatus(auditId: string): Promise<AuditStatusResponse>

// Get available plans
client.audit.getPlans(): Promise<AuditPlan[]>
```

---

## Python SDK

### Installation

```bash
pip install ktzchenweb3
```

### Quick Start

```python
from ktzchenweb3 import KtzchenWeb3

# Initialize the client
client = KtzchenWeb3(api_key='your_api_key_here')

# Get gas fees
gas_fees = client.gas.get_fees('ethereum_mainnet')
print(f"Standard gas: {gas_fees['gas_prices']['standard']} gwei")

# Get address info
address_info = client.explorer.get_address(
    'ethereum_mainnet',
    '0x742d35Cc6634C0532925a3b844Bc9e7595f8dB21'
)
print(f"Balance: {address_info['balance']} ETH")

# Check node status
node_status = client.node.get_status('polygon')
print(f"Node status: {node_status['status']}")

# Request contract audit
audit = client.audit.request(
    contract_address='0x...',
    network='ethereum_mainnet',
    email='dev@example.com'
)
print(f"Audit ID: {audit['audit_id']}")
```

### API Reference

#### Constructor

```python
KtzchenWeb3(api_key: str, base_url: str = None, timeout: int = 30)
```

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| api_key | str | Yes | - | Your API key |
| base_url | str | No | `https://ktzchenweb3.io/api` | Base URL |
| timeout | int | No | 30 | Request timeout (seconds) |

#### Gas Module

```python
# Get gas fees for a network
client.gas.get_fees(network: str) -> dict

# Get gas fees for multiple networks
client.gas.get_fees_multiple(networks: list[str]) -> list[dict]
```

#### Explorer Module

```python
# Get address information
client.explorer.get_address(network: str, address: str) -> dict

# Get transaction details
client.explorer.get_transaction(network: str, tx_hash: str) -> dict

# Get block information
client.explorer.get_block(network: str, block_number: int | str) -> dict

# Get token information
client.explorer.get_token(network: str, token_address: str) -> dict
```

#### Node Module

```python
# Get node status
client.node.get_status(network: str) -> dict

# Check multiple networks
client.node.check_all() -> list[dict]
```

#### Audit Module

```python
# Request a contract audit
client.audit.request(
    contract_address: str,
    network: str,
    email: str = None
) -> dict

# Get audit status
client.audit.get_status(audit_id: str) -> dict

# Get available plans
client.audit.get_plans() -> list[dict]
```

---

## Error Handling

Both SDKs throw/raise errors for API errors. Handle them appropriately:

**JavaScript:**

```typescript
try {
  const gas = await client.gas.getFees('invalid_network');
} catch (error) {
  if (error instanceof KtzchenWeb3Error) {
    console.error('API Error:', error.message);
    console.error('Status:', error.status);
  }
}
```

**Python:**

```python
from ktzchenweb3.exceptions import KtzchenWeb3Error

try:
    gas = client.gas.get_fees('invalid_network')
except KtzchenWeb3Error as e:
    print(f"API Error: {e.message}")
    print(f"Status: {e.status}")
```

---

## Rate Limiting

Both SDKs include built-in rate limit handling:

- Automatic retry with exponential backoff
- Rate limit headers exposed in responses
- Configurable retry behavior

---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## Support

- Documentation: [docs.ktzchenweb3.io](https://docs.ktzchenweb3.io)
- Discord: [Join Community](https://discord.gg/ktzchenweb3)
- Email: sdk-support@ktzchenweb3.io
