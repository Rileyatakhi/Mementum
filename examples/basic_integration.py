# examples/basic_integration.py

from sdk import MementumAI, BlockchainInteractions
from sdk.config import Config
from sdk.errors import BlockchainError, AIServiceError
from sdk.logging_config import logger

def main():
    try:
        # Initialize AI module
        ai = MementumAI()

        # Generate AI-powered content
        logger.info("Generating AI content...")
        text_content = ai.generate_text("Create a market analysis report.")
        image_url = ai.generate_image("A futuristic cityscape at sunset.")

        logger.info(f"Generated Text: {text_content}")
        logger.info(f"Generated Image URL: {image_url}")

        # Initialize blockchain module
        blockchain = BlockchainInteractions()

        # Get token balance
        wallet_address = Config.get("WALLET_ADDRESS")
        balance = blockchain.get_balance(wallet_address)
        logger.info(f"Token Balance for {wallet_address}: {balance} $MEME")

        # Transfer tokens
        recipient = Config.get("RECIPIENT_ADDRESS")
        sender_private_key = Config.get("PRIVATE_KEY")
        amount = 10  # Example amount

        logger.info(f"Transferring {amount} $MEME to {recipient}...")
        tx_hash = blockchain.transfer_tokens(sender_private_key, recipient, amount)
        logger.info(f"Transaction Hash: {tx_hash}")

    except (BlockchainError, AIServiceError) as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()