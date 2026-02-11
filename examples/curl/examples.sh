#!/bin/bash
# ============================================
# KtzchenWeb3 API - cURL Examples
# ============================================

# Configuration - Replace with your actual API key
API_KEY="your_api_key_here"
BASE_URL="https://ktzchenweb3.io/api"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}   KtzchenWeb3 API - cURL Examples${NC}"
echo -e "${BLUE}============================================${NC}"

# ============================================
# Gas Fees Examples
# ============================================

echo -e "\n${YELLOW}📊 Gas Fees - Ethereum Mainnet${NC}"
curl -s -X GET "${BASE_URL}/v3/ethereum_mainnet/gas-fees/" \
  -H "X-API-Key: ${API_KEY}" | jq .

echo -e "\n${YELLOW}📊 Gas Fees - Polygon${NC}"
curl -s -X GET "${BASE_URL}/v3/polygon/gas-fees/" \
  -H "X-API-Key: ${API_KEY}" | jq .

echo -e "\n${YELLOW}📊 Gas Fees - Arbitrum${NC}"
curl -s -X GET "${BASE_URL}/v3/arbitrum/gas-fees/" \
  -H "X-API-Key: ${API_KEY}" | jq .

echo -e "\n${YELLOW}📊 Gas Fees - BSC${NC}"
curl -s -X GET "${BASE_URL}/v3/bsc/gas-fees/" \
  -H "X-API-Key: ${API_KEY}" | jq .

# ============================================
# Blockchain Explorer Examples
# ============================================

echo -e "\n${YELLOW}📍 Address Info - Vitalik's Address${NC}"
curl -s -X GET "${BASE_URL}/v3/ethereum_mainnet/address/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045/" \
  -H "X-API-Key: ${API_KEY}" | jq .

echo -e "\n${YELLOW}📝 Transaction Details${NC}"
# Replace with a real transaction hash
curl -s -X GET "${BASE_URL}/v3/ethereum_mainnet/tx/0x123abc.../" \
  -H "X-API-Key: ${API_KEY}" | jq .

echo -e "\n${YELLOW}🧱 Latest Block${NC}"
curl -s -X GET "${BASE_URL}/v3/ethereum_mainnet/block/latest/" \
  -H "X-API-Key: ${API_KEY}" | jq .

echo -e "\n${YELLOW}🪙 Token Info - USDT${NC}"
curl -s -X GET "${BASE_URL}/v3/ethereum_mainnet/token/0xdAC17F958D2ee523a2206206994597C13D831ec7/" \
  -H "X-API-Key: ${API_KEY}" | jq .

# ============================================
# Node Status Examples
# ============================================

echo -e "\n${YELLOW}🖥️ Node Status - Ethereum${NC}"
curl -s -X GET "${BASE_URL}/v3/ethereum_mainnet/node/status/" \
  -H "X-API-Key: ${API_KEY}" | jq .

echo -e "\n${YELLOW}🖥️ Node Status - Polygon${NC}"
curl -s -X GET "${BASE_URL}/v3/polygon/node/status/" \
  -H "X-API-Key: ${API_KEY}" | jq .

# ============================================
# Contract Audit Examples
# ============================================

echo -e "\n${YELLOW}📋 Audit Plans${NC}"
curl -s -X GET "${BASE_URL}/contract-audit/plans/" \
  -H "X-API-Key: ${API_KEY}" | jq .

echo -e "\n${YELLOW}🔍 Request Audit${NC}"
curl -s -X POST "${BASE_URL}/contract-audit/request/" \
  -H "X-API-Key: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "contract_address": "0x742d35Cc6634C0532925a3b844Bc9e7595f8dB21",
    "network": "ethereum_mainnet",
    "contact_email": "developer@example.com"
  }' | jq .

# ============================================
# Health Check Examples
# ============================================

echo -e "\n${YELLOW}❤️ Health Check (No Auth Required)${NC}"
curl -s -X GET "${BASE_URL}/health/" | jq .

echo -e "\n${YELLOW}📈 Public System Metrics (No Auth Required)${NC}"
curl -s -X GET "${BASE_URL}/public/system/metrics/" | jq .

# ============================================
# Transaction Tracing Examples
# ============================================

echo -e "\n${YELLOW}🔬 Trace Transaction${NC}"
curl -s -X POST "${BASE_URL}/trace/transaction/" \
  -H "X-API-Key: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "tx_hash": "0x123abc...",
    "network": "ethereum_mainnet"
  }' | jq .

echo -e "\n${GREEN}✅ All cURL examples completed!${NC}"
