/**
 * KtzchenWeb3 API - JavaScript Examples
 * Basic usage examples for the KtzchenWeb3 blockchain API
 */

const API_KEY = 'your_api_key_here';
const BASE_URL = 'https://ktzchenweb3.io/api';

// ============================================
// Helper function for API calls
// ============================================

async function apiCall(endpoint, options = {}) {
  const url = `${BASE_URL}${endpoint}`;
  const config = {
    headers: {
      'X-API-Key': API_KEY,
      'Content-Type': 'application/json',
      ...options.headers
    },
    ...options
  };

  const response = await fetch(url, config);
  
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.error || `HTTP ${response.status}`);
  }
  
  return response.json();
}

// ============================================
// Gas Fees Examples
// ============================================

/**
 * Get current gas prices for a network
 */
async function getGasFees(network = 'ethereum_mainnet') {
  try {
    const result = await apiCall(`/v3/${network}/gas-fees/`);
    
    if (result.success) {
      const { gas_prices, base_fee, unit } = result.data;
      console.log(`\n📊 Gas Fees for ${network}:`);
      console.log(`   Slow:     ${gas_prices.slow} ${unit}`);
      console.log(`   Standard: ${gas_prices.standard} ${unit}`);
      console.log(`   Fast:     ${gas_prices.fast} ${unit}`);
      console.log(`   Instant:  ${gas_prices.instant} ${unit}`);
      console.log(`   Base Fee: ${base_fee} ${unit}`);
    }
    
    return result;
  } catch (error) {
    console.error('Error fetching gas fees:', error.message);
    throw error;
  }
}

/**
 * Compare gas fees across multiple networks
 */
async function compareGasFees(networks = ['ethereum_mainnet', 'polygon', 'arbitrum', 'bsc']) {
  console.log('\n🔄 Comparing gas fees across networks...\n');
  
  const results = await Promise.all(
    networks.map(async (network) => {
      try {
        const result = await apiCall(`/v3/${network}/gas-fees/`);
        return { network, ...result.data };
      } catch (error) {
        return { network, error: error.message };
      }
    })
  );
  
  console.log('Network'.padEnd(20) + 'Standard'.padEnd(15) + 'Fast');
  console.log('-'.repeat(50));
  
  results.forEach(({ network, gas_prices, error }) => {
    if (error) {
      console.log(`${network.padEnd(20)}Error: ${error}`);
    } else {
      console.log(
        `${network.padEnd(20)}${gas_prices.standard.padEnd(15)}${gas_prices.fast}`
      );
    }
  });
  
  return results;
}

// ============================================
// Blockchain Explorer Examples
// ============================================

/**
 * Get address information
 */
async function getAddressInfo(network, address) {
  try {
    const result = await apiCall(`/v3/${network}/address/${address}/`);
    
    if (result.success) {
      const { balance, transaction_count, is_contract } = result.data;
      console.log(`\n📍 Address Info:`);
      console.log(`   Address: ${address}`);
      console.log(`   Balance: ${balance} ETH`);
      console.log(`   Transactions: ${transaction_count}`);
      console.log(`   Is Contract: ${is_contract}`);
    }
    
    return result;
  } catch (error) {
    console.error('Error fetching address info:', error.message);
    throw error;
  }
}

/**
 * Get transaction details
 */
async function getTransaction(network, txHash) {
  try {
    const result = await apiCall(`/v3/${network}/tx/${txHash}/`);
    
    if (result.success) {
      const { from, to, value, status, gas_used, confirmations } = result.data;
      console.log(`\n📝 Transaction Details:`);
      console.log(`   Hash: ${txHash}`);
      console.log(`   From: ${from}`);
      console.log(`   To: ${to}`);
      console.log(`   Value: ${value} ETH`);
      console.log(`   Status: ${status}`);
      console.log(`   Gas Used: ${gas_used}`);
      console.log(`   Confirmations: ${confirmations}`);
    }
    
    return result;
  } catch (error) {
    console.error('Error fetching transaction:', error.message);
    throw error;
  }
}

/**
 * Get latest block information
 */
async function getLatestBlock(network = 'ethereum_mainnet') {
  try {
    const result = await apiCall(`/v3/${network}/block/latest/`);
    
    if (result.success) {
      const { number, hash, transaction_count, gas_used, timestamp } = result.data;
      console.log(`\n🧱 Latest Block on ${network}:`);
      console.log(`   Number: ${number}`);
      console.log(`   Hash: ${hash.slice(0, 20)}...`);
      console.log(`   Transactions: ${transaction_count}`);
      console.log(`   Gas Used: ${gas_used}`);
      console.log(`   Time: ${timestamp}`);
    }
    
    return result;
  } catch (error) {
    console.error('Error fetching block:', error.message);
    throw error;
  }
}

/**
 * Get token information
 */
async function getTokenInfo(network, tokenAddress) {
  try {
    const result = await apiCall(`/v3/${network}/token/${tokenAddress}/`);
    
    if (result.success) {
      const { name, symbol, decimals, total_supply, holders } = result.data;
      console.log(`\n🪙 Token Info:`);
      console.log(`   Name: ${name}`);
      console.log(`   Symbol: ${symbol}`);
      console.log(`   Decimals: ${decimals}`);
      console.log(`   Total Supply: ${total_supply}`);
      console.log(`   Holders: ${holders}`);
    }
    
    return result;
  } catch (error) {
    console.error('Error fetching token info:', error.message);
    throw error;
  }
}

// ============================================
// Node Status Examples
// ============================================

/**
 * Check node status for a network
 */
async function checkNodeStatus(network = 'ethereum_mainnet') {
  try {
    const result = await apiCall(`/v3/${network}/node/status/`);
    
    if (result.success) {
      const { status, latest_block, syncing, response_time_ms, uptime_percent } = result.data;
      console.log(`\n🖥️ Node Status for ${network}:`);
      console.log(`   Status: ${status}`);
      console.log(`   Latest Block: ${latest_block}`);
      console.log(`   Syncing: ${syncing}`);
      console.log(`   Response Time: ${response_time_ms}ms`);
      console.log(`   Uptime: ${uptime_percent}%`);
    }
    
    return result;
  } catch (error) {
    console.error('Error checking node status:', error.message);
    throw error;
  }
}

/**
 * Check health of all supported networks
 */
async function checkAllNetworks() {
  const networks = [
    'ethereum_mainnet', 'polygon', 'bsc', 'arbitrum', 
    'optimism', 'avalanche', 'fantom', 'gnosis'
  ];
  
  console.log('\n🌐 Checking all network statuses...\n');
  console.log('Network'.padEnd(20) + 'Status'.padEnd(12) + 'Block'.padEnd(12) + 'Response');
  console.log('-'.repeat(60));
  
  for (const network of networks) {
    try {
      const result = await apiCall(`/v3/${network}/node/status/`);
      const { status, latest_block, response_time_ms } = result.data;
      const statusEmoji = status === 'healthy' ? '🟢' : '🔴';
      console.log(
        `${network.padEnd(20)}${statusEmoji} ${status.padEnd(9)}${String(latest_block).padEnd(12)}${response_time_ms}ms`
      );
    } catch (error) {
      console.log(`${network.padEnd(20)}🔴 Error`);
    }
  }
}

// ============================================
// Contract Audit Examples
// ============================================

/**
 * Request a contract audit
 */
async function requestContractAudit(contractAddress, network = 'ethereum_mainnet', email) {
  try {
    const result = await apiCall('/contract-audit/request/', {
      method: 'POST',
      body: JSON.stringify({
        contract_address: contractAddress,
        network: network,
        contact_email: email
      })
    });
    
    if (result.success) {
      const { audit_id, status, estimated_completion } = result.data;
      console.log(`\n🔍 Audit Request Submitted:`);
      console.log(`   Audit ID: ${audit_id}`);
      console.log(`   Status: ${status}`);
      console.log(`   Est. Completion: ${estimated_completion}`);
    }
    
    return result;
  } catch (error) {
    console.error('Error requesting audit:', error.message);
    throw error;
  }
}

/**
 * Get audit plans
 */
async function getAuditPlans() {
  try {
    const result = await apiCall('/contract-audit/plans/');
    
    if (result.success) {
      console.log('\n📋 Available Audit Plans:\n');
      result.data.forEach(plan => {
        console.log(`   ${plan.name} - $${plan.price_usd}`);
        plan.features.forEach(feature => {
          console.log(`      ✓ ${feature}`);
        });
        console.log('');
      });
    }
    
    return result;
  } catch (error) {
    console.error('Error fetching audit plans:', error.message);
    throw error;
  }
}

// ============================================
// Run Examples
// ============================================

async function runExamples() {
  console.log('═'.repeat(60));
  console.log('   KtzchenWeb3 API - JavaScript Examples');
  console.log('═'.repeat(60));
  
  // Gas fees
  await getGasFees('ethereum_mainnet');
  await getGasFees('polygon');
  
  // Compare networks
  await compareGasFees();
  
  // Node status
  await checkNodeStatus('ethereum_mainnet');
  
  // Check all networks
  await checkAllNetworks();
  
  // Audit plans
  await getAuditPlans();
  
  console.log('\n✅ All examples completed!');
}

// Export functions for module use
export {
  getGasFees,
  compareGasFees,
  getAddressInfo,
  getTransaction,
  getLatestBlock,
  getTokenInfo,
  checkNodeStatus,
  checkAllNetworks,
  requestContractAudit,
  getAuditPlans
};

// Run if executed directly
if (typeof window === 'undefined') {
  runExamples().catch(console.error);
}
