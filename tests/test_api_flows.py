# tests/test_api_flows.py

import pytest
from sdk import MementumAI, BlockchainInteractions
from sdk.errors import BlockchainError, AIServiceError

@pytest.fixture
def ai():
    return MementumAI()

@pytest.fixture
def blockchain():
    return BlockchainInteractions()

def test_end_to_end_flow(ai, blockchain):
    """Test end-to-end flow: AI content generation and token transfer."""
    try:
        # Step 1: Generate AI content
        prompt = "Create a market analysis report."
        text_content = ai.generate_text(prompt)
        assert isinstance(text_content, str), "Generated text should be a string."

        # Step 2: Transfer tokens
        sender_private_key = "test_private_key"
        recipient = "recipient_address"
        amount = 10
        tx_hash = blockchain.transfer_tokens(sender_private_key, recipient, amount)
        assert tx_hash is not None, "Transaction hash should not be None."
    except (BlockchainError, AIServiceError) as e:
        pytest.fail(f"End-to-end flow failed: {e}")