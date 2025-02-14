# tests/test_mementum_token.py

import pytest
from sdk.blockchain_interactions import BlockchainInteractions
from sdk.errors import BlockchainError

@pytest.fixture
def blockchain():
    return BlockchainInteractions()

def test_mint_tokens(blockchain):
    """Test minting tokens."""
    try:
        sender_private_key = "test_private_key"
        recipient = "recipient_address"
        amount = 100
        tx_hash = blockchain.transfer_tokens(sender_private_key, recipient, amount)
        assert tx_hash is not None, "Transaction hash should not be None."
    except BlockchainError as e:
        pytest.fail(f"Token minting failed: {e}")

def test_transfer_tokens(blockchain):
    """Test transferring tokens."""
    try:
        sender_private_key = "test_private_key"
        recipient = "recipient_address"
        amount = 50
        initial_balance = blockchain.get_balance(recipient)
        blockchain.transfer_tokens(sender_private_key, recipient, amount)
        final_balance = blockchain.get_balance(recipient)
        assert final_balance == initial_balance + amount, "Balance mismatch after transfer."
    except BlockchainError as e:
        pytest.fail(f"Token transfer failed: {e}")

def test_burn_tokens(blockchain):
    """Test burning tokens."""
    try:
        sender_private_key = "test_private_key"
        amount = 20
        initial_balance = blockchain.get_balance("sender_address")
        blockchain.transfer_tokens(sender_private_key, "burn_address", amount)
        final_balance = blockchain.get_balance("sender_address")
        assert final_balance == initial_balance - amount, "Balance mismatch after burn."
    except BlockchainError as e:
        pytest.fail(f"Token burn failed: {e}")