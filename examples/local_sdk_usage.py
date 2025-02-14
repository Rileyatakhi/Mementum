# examples/local_sdk_usage.py

from sdk import MementumAI, BlockchainInteractions
from sdk.config import Config
from sdk.errors import BlockchainError, AIServiceError
from sdk.logging_config import logger
from sdk.utils import validate_data

def generate_local_content(ai):
    """Generate AI content locally."""
    try:
        prompt = "Explain the concept of decentralized finance."
        logger.info(f"Generating local content for prompt: {prompt}")
        content = ai.generate_text(prompt)
        logger.info(f"Generated Content: {content}")
    except AIServiceError as e:
        logger.error(f"Failed to generate content: {e}")

def interact_with_testnet(blockchain):
    """Interact with a test network."""
    try:
        # Validate testnet configuration
        required_keys = ["TESTNET_PROVIDER_URL", "TESTNET_CONTRACT_ADDRESS"]
        if not validate_data(Config.__dict__, required_keys):
            raise ValueError("Missing required testnet configuration.")

        # Query testnet balance
        test_wallet = Config.get("TEST_WALLET_ADDRESS")
        balance = blockchain.get_balance(test_wallet)
        logger.info(f"Testnet Balance for {test_wallet}: {balance} $MEME")

        # Simulate a token transfer
        recipient = Config.get("TEST_RECIPIENT_ADDRESS")
        amount = 5  # Example amount
        logger.info(f"Simulating transfer of {amount} $MEME to {recipient}...")
        tx_hash = blockchain.transfer_tokens(Config.get("TEST_PRIVATE_KEY"), recipient, amount)
        logger.info(f"Simulated Transaction Hash: {tx_hash}")

    except BlockchainError as e:
        logger.error(f"Blockchain interaction failed: {e}")

def main():
    try:
        # Initialize AI module
        ai = MementumAI()

        # Local AI content generation
        generate_local_content(ai)

        # Initialize blockchain module for testnet
        blockchain = BlockchainInteractions(
            provider_url=Config.get("TESTNET_PROVIDER_URL"),
            contract_address=Config.get("TESTNET_CONTRACT_ADDRESS"),
            abi=Config.get("CONTRACT_ABI")  # ABI should be loaded dynamically
        )

        # Testnet interactions
        interact_with_testnet(blockchain)

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()