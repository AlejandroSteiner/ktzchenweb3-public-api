# Supported Networks

KtzchenWeb3 provides unified API access to 50+ blockchain networks.

## Mainnet Networks

### Layer 1 Networks

| Network | API ID | Chain ID | Native Token | Status |
|---------|--------|----------|--------------|--------|
| Ethereum | `ethereum_mainnet` | 1 | ETH | 🟢 Active |
| BNB Smart Chain | `bsc` | 56 | BNB | 🟢 Active |
| Avalanche C-Chain | `avalanche` | 43114 | AVAX | 🟢 Active |
| Fantom Opera | `fantom` | 250 | FTM | 🟢 Active |
| Gnosis Chain | `gnosis` | 100 | xDAI | 🟢 Active |
| Cronos | `cronos` | 25 | CRO | 🟢 Active |
| Moonbeam | `moonbeam` | 1284 | GLMR | 🟢 Active |
| Moonriver | `moonriver` | 1285 | MOVR | 🟢 Active |
| Harmony | `harmony` | 1666600000 | ONE | 🟢 Active |
| Celo | `celo` | 42220 | CELO | 🟢 Active |
| Aurora | `aurora` | 1313161554 | ETH | 🟢 Active |
| Klaytn | `klaytn` | 8217 | KLAY | 🟢 Active |
| Metis | `metis` | 1088 | METIS | 🟢 Active |
| Boba Network | `boba` | 288 | ETH | 🟢 Active |

### Layer 2 Networks

| Network | API ID | Chain ID | Native Token | Status |
|---------|--------|----------|--------------|--------|
| Polygon (Matic) | `polygon` | 137 | MATIC | 🟢 Active |
| Arbitrum One | `arbitrum` | 42161 | ETH | 🟢 Active |
| Optimism | `optimism` | 10 | ETH | 🟢 Active |
| Base | `base` | 8453 | ETH | 🟢 Active |
| zkSync Era | `zksync` | 324 | ETH | 🟢 Active |
| Polygon zkEVM | `polygon_zkevm` | 1101 | ETH | 🟢 Active |
| Linea | `linea` | 59144 | ETH | 🟢 Active |
| Scroll | `scroll` | 534352 | ETH | 🟢 Active |
| Mantle | `mantle` | 5000 | MNT | 🟢 Active |
| Mode | `mode` | 34443 | ETH | 🟢 Active |
| Blast | `blast` | 81457 | ETH | 🟢 Active |

## Testnet Networks

| Network | API ID | Chain ID | Status |
|---------|--------|----------|--------|
| Ethereum Sepolia | `ethereum_sepolia` | 11155111 | 🟢 Active |
| Ethereum Goerli | `ethereum_goerli` | 5 | 🟡 Deprecated |
| Polygon Mumbai | `polygon_mumbai` | 80001 | 🟢 Active |
| BSC Testnet | `bsc_testnet` | 97 | 🟢 Active |
| Arbitrum Sepolia | `arbitrum_sepolia` | 421614 | 🟢 Active |
| Optimism Sepolia | `optimism_sepolia` | 11155420 | 🟢 Active |
| Base Sepolia | `base_sepolia` | 84532 | 🟢 Active |
| Avalanche Fuji | `avalanche_fuji` | 43113 | 🟢 Active |

## Network Features Matrix

| Feature | L1 Networks | L2 Networks | Testnets |
|---------|------------|-------------|----------|
| Gas Fees API | ✅ | ✅ | ✅ |
| Block Explorer | ✅ | ✅ | ✅ |
| Transaction Tracing | ✅ | ✅ | ✅ |
| Contract Verification | ✅ | ✅ | ✅ |
| Token Transfers | ✅ | ✅ | ✅ |
| NFT Support | ✅ | ✅ | ✅ |
| Contract Audit | ✅ | ✅ | ⚠️ Limited |
| Websocket Support | ✅ | ✅ | ✅ |

## Usage Examples

### Ethereum Mainnet

```bash
curl "https://ktzchenweb3.io/api/v3/ethereum_mainnet/gas-fees/"
```

### Polygon

```bash
curl "https://ktzchenweb3.io/api/v3/polygon/gas-fees/"
```

### Arbitrum

```bash
curl "https://ktzchenweb3.io/api/v3/arbitrum/gas-fees/"
```

### BSC

```bash
curl "https://ktzchenweb3.io/api/v3/bsc/gas-fees/"
```

## Network Status

Check real-time network status at: [status.ktzchenweb3.io](https://status.ktzchenweb3.io)

Or via API:

```bash
curl "https://ktzchenweb3.io/api/v3/{network}/node/status/"
```

## Adding New Networks

We're constantly adding support for new networks. To request a new network:

1. Open an issue on GitHub
2. Email: networks@ktzchenweb3.io
3. Join our Discord and use #network-requests

## RPC Endpoints

For direct RPC access (Enterprise plans only):

```
https://rpc.ktzchenweb3.io/v1/{network}/{api_key}
```

Supports standard JSON-RPC methods:
- `eth_blockNumber`
- `eth_getBalance`
- `eth_getTransactionByHash`
- `eth_call`
- And 50+ more methods

---

**Note:** Network availability and features may vary. Check our status page for real-time updates.
