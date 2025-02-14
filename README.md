# Mementum: AI-Powered Trading & Content Creation on Solana

## Overview

Mementum is an AI-driven platform that combines trading automation, content generation, and decentralized governance using the Solana blockchain. The ecosystem revolves around **$MEME**, an ERC-20 (or equivalent) token, enabling AI-assisted trading, NFT minting, and governance mechanisms.

Mementum's SDK provides seamless integration with AI services and blockchain functionalities, allowing developers to:

- Generate AI-powered multimedia content (text, images, videos).
- Interact with smart contracts (trading, staking, governance).
- Utilize a secure and modular framework for decentralized AI applications.

## Features

- **$MEME Token**: A secure ERC-20 (or equivalent) token with minting, burning, and transfer functionalities.
- **AI Content Generation**: Multi-modal AI for text, images, and video generation.
- **Governance Mechanism**: DAO-powered voting for protocol upgrades and decisions.
- **SDK for Developers**: Easy-to-use Python SDK to interact with Mementum's AI and blockchain features.
- **Scripts for Deployment and Management**: Pre-built scripts for deploying contracts, minting tokens, creating governance proposals, and executing airdrops.
- **Examples for Quick Integration**: Ready-to-run example scripts demonstrating basic and advanced usage of the SDK.
- **Smart Contracts**: Secure and modular smart contracts for token management, governance, and additional features like NFT minting and staking.
- **Security First**: Utilizes OpenZeppelin libraries, rigorous validation, and best practices.

## Installation

To get started with Mementum, install the SDK:

```bash
pip install mementum-sdk
```

Alternatively, clone the repository and install dependencies:

```bash
git clone https://github.com/mementum-ai/mementum-sdk.git
cd mementum-sdk
pip install -r requirements.txt
```

### Prerequisites

- Python 3.8 or higher.
- Install dependencies using `pip install -r requirements.txt`.
- Set up environment variables in a `.env` file (see [Configuration](#configuration)).

## Smart Contracts

The smart contracts are the backbone of the Mementum ecosystem, providing secure and modular functionality for token management, governance, and additional features like NFT minting and staking.

### Available Contracts

- **`MementumToken.sol`**: The ERC-20 token contract for `$MEME`, with secure implementations of minting, burning, and transfer functionalities.
- **`MemeGovernance.sol`**: The governance contract for voting, DAO features, or on-chain decision-making.
- **`MemeNFT.sol`**: An ERC-721 contract for minting NFTs, which can represent memes or other digital content.
- **`ContentOwnership.sol`**: A contract for registering and verifying ownership of content tied to NFTs.
- **`MemeStakingRewards.sol`**: A staking rewards contract that allows users to stake `$MEME` tokens and earn rewards.

#### Key Features

- **Secure Implementation**: Leverages OpenZeppelin libraries for secure and audited implementations.
- **Modular Design**: Each contract is designed to be modular, allowing for easy upgrades and extensions.
- **Best Practices**: Implements thorough checks (e.g., `require` statements, modifiers) to prevent common exploits like reentrancy and overflow/underflow.

#### Deployment

To deploy the smart contracts, use the provided deployment script:

```bash
node scripts/deploy_contracts.js --network <network_name>
```

Replace `<network_name>` with `testnet` or `mainnet`.

#### Interacting with Contracts

Once deployed, you can interact with the contracts using the SDK or directly via Web3 tools like MetaMask or Hardhat.

Example: Querying the balance of a wallet:

```python
from sdk import BlockchainInteractions

blockchain = BlockchainInteractions()
balance = blockchain.get_balance("your_wallet_address")
print(f"Token Balance: {balance} $MEME")
```

## Examples for Quick Integration

The `examples/` directory contains ready-to-run scripts to help developers quickly understand how to integrate and use the Mementum SDK.

### Available Examples

- **`basic_integration.py`**: Demonstrates a minimal workflow for initializing the SDK, generating AI content, and handling token transactions.
- **`local_sdk_usage.py`**: Shows how to use AI modules locally (offline inference) and interact with test networks.

#### Running Examples

Each example script is self-contained and includes detailed comments for clarity. To run an example, navigate to the `examples/` directory and execute the script:

1. **Basic Integration**

   ```bash
   python examples/basic_integration.py
   ```

   This script demonstrates:

   - Generating AI-powered text and images.
   - Querying token balances.
   - Transferring tokens on the blockchain.
2. **Local SDK Usage**

   ```bash
   python examples/local_sdk_usage.py
   ```

   This script demonstrates:

   - Generating AI content locally without requiring an internet connection.
   - Interacting with a testnet to query balances and simulate token transfers.

#### Key Notes

- Ensure all required environment variables (e.g., `AI_API_KEY`, `BLOCKCHAIN_PROVIDER_URL`) are set in your `.env` file.
- Use these examples as templates for building your own integrations.

## Scripts for Deployment and Management

The `scripts/` directory contains pre-built scripts to simplify common tasks like deploying contracts, minting tokens, creating governance proposals, and executing airdrops.

### Available Scripts

- **`deploy_contracts.js`**: Deploys or upgrades Mementum smart contracts to testnet or mainnet.
- **`mint_tokens.js`**: Mints `$MEME` tokens or distributes them for community events.
- **`create_proposal.js`**: Creates governance proposals for voting.
- **`airdrop_tokens.js`**: Executes token airdrops to multiple recipients.

#### Usage Instructions

Each script includes detailed usage instructions in its header. Below are examples of how to run these scripts:

1. **Deploy Contracts**

   ```bash
   node scripts/deploy_contracts.js --network <network_name>
   ```

   Replace `<network_name>` with `testnet` or `mainnet`.
2. **Mint Tokens**

   ```bash
   node scripts/mint_tokens.js --network <network_name> <recipient_address> <amount>
   ```

   Example:

   ```bash
   node scripts/mint_tokens.js --network testnet 0xRecipientAddress 1000
   ```
3. **Create Governance Proposal**

   ```bash
   node scripts/create_proposal.js --network <network_name> "Proposal Description" <duration_in_seconds>
   ```

   Example:

   ```bash
   node scripts/create_proposal.js --network testnet "Increase staking rewards" 86400
   ```
4. **Execute Airdrop**

   ```bash
   node scripts/airdrop_tokens.js --network <network_name> "0xAddr1,0xAddr2" "100,200"
   ```

   Example:

   ```bash
   node scripts/airdrop_tokens.js --network testnet "0xAddr1,0xAddr2" "100,200"
   ```

#### Key Notes

- Ensure all required environment variables (e.g., `CONTRACT_ADDRESS`, `PRIVATE_KEY`) are set in your `.env` file.
- Use strong logging and error handling to avoid misdeployments or failures.

## SDK Structure

The SDK is organized into modular components for ease of use and maintainability:

- **`__init__.py`**: Marks the directory as a Python package and exposes key classes/functions.
- **`mementum_ai.py`**: Houses AI logic for generating multi-modal content (text, images, videos).
- **`mementum_api.py`**: Manages REST or GraphQL endpoints for interacting with the platform's backend.
- **`blockchain_interactions.py`**: Provides utility functions for blockchain interactions (e.g., transferring tokens, querying balances).
- **`config.py`**: Centralizes configuration loading (e.g., API keys, contract addresses).
- **`errors.py`**: Defines custom exceptions for better error handling.
- **`logging_config.py`**: Standardizes logging setup for consistent outputs.
- **`utils.py`**: Contains reusable helper functions (e.g., data validation, text formatting).

## Configuration

The SDK uses environment variables for configuration. Create a `.env` file in the root directory with the following variables:

```env
# AI Service Configuration
AI_API_KEY=your_ai_service_api_key

# Blockchain Configuration
BLOCKCHAIN_PROVIDER_URL=https://solana-rpc-url
CONTRACT_ADDRESS=your_contract_address
WALLET_ADDRESS=your_wallet_address
PRIVATE_KEY=your_private_key
RECIPIENT_ADDRESS=recipient_wallet_address

# Testnet Configuration
TESTNET_PROVIDER_URL=https://testnet-rpc-url
TESTNET_CONTRACT_ADDRESS=testnet_contract_address
TEST_WALLET_ADDRESS=test_wallet_address
TEST_PRIVATE_KEY=test_private_key
TEST_RECIPIENT_ADDRESS=test_recipient_address
CONTRACT_ABI=[...]  # JSON array of ABI
```

## Error Handling

The SDK includes custom exception classes for better error reporting:

- **`BlockchainError`**: Raised for blockchain-related issues (e.g., failed transactions).
- **`AIServiceError`**: Raised for AI service-related issues (e.g., failed content generation).

Example:

```python
from sdk.errors import BlockchainError, AIServiceError

try:
    tx_hash = blockchain.transfer_tokens(sender_private_key, recipient, amount)
except BlockchainError as e:
    print(f"Blockchain Error: {e}")
```

## Logging

The SDK standardizes logging for debugging and monitoring. Logs are formatted as:

```
[timestamp] - [module] - [log level] - [message]
```

Example:

```python
from sdk.logging_config import logger

logger.info("This is an informational message.")
logger.error("This is an error message.")
```

## License

Mementum is licensed under the MIT License.
