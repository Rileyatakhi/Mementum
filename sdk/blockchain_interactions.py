# sdk/blockchain_interactions.py

from web3 import Web3
from .errors import BlockchainError
from .logging_config import logger

class BlockchainInteractions:
    def __init__(self, provider_url=None, contract_address=None, abi=None):
        self.web3 = Web3(Web3.HTTPProvider(provider_url or Config.get("BLOCKCHAIN_PROVIDER_URL")))
        if not self.web3.isConnected():
            raise BlockchainError("Could not connect to the blockchain provider.")
        self.contract = self.web3.eth.contract(address=contract_address or Config.get("CONTRACT_ADDRESS"), abi=abi)

    def get_balance(self, address: str) -> float:
        """Get the token balance of an address."""
        try:
            address = self.web3.toChecksumAddress(address)
            return self.contract.functions.balanceOf(address).call() / 10**18
        except Exception as e:
            logger.error(f"Error fetching balance: {e}")
            raise BlockchainError("Failed to fetch balance.") from e

    def transfer_tokens(self, sender_private_key: str, recipient: str, amount: float):
        """Transfer tokens from one address to another."""
        try:
            sender = self.web3.eth.account.from_key(sender_private_key).address
            recipient = self.web3.toChecksumAddress(recipient)
            amount_wei = int(amount * 10**18)
            nonce = self.web3.eth.getTransactionCount(sender)
            tx = self.contract.functions.transfer(recipient, amount_wei).buildTransaction({
                "chainId": self.web3.eth.chain_id,
                "gas": 200000,
                "gasPrice": self.web3.toWei("50", "gwei"),
                "nonce": nonce,
            })
            signed_tx = self.web3.eth.account.sign_transaction(tx, sender_private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return self.web3.toHex(tx_hash)
        except Exception as e:
            logger.error(f"Error transferring tokens: {e}")
            raise BlockchainError("Failed to transfer tokens.") from e