// scripts/mint_tokens.js

const { ethers } = require("hardhat");
const { logger } = require("../utils/logger");

/**
 * Mints $MEME tokens or distributes them to specified addresses.
 * 
 * Usage:
 *   node scripts/mint_tokens.js --network <network_name> <recipient_address> <amount>
 * 
 * Example:
 *   node scripts/mint_tokens.js --network testnet 0xRecipientAddress 1000
 */
async function main() {
    const args = process.argv.slice(2);
    if (args.length < 2) {
        logger.error("Usage: node scripts/mint_tokens.js <recipient_address> <amount>");
        process.exit(1);
    }

    const [recipient, amount] = args;
    const amountInWei = ethers.utils.parseEther(amount);

    try {
        // Load accounts
        const [deployer] = await ethers.getSigners();
        logger.info(`Minting tokens with account: ${deployer.address}`);
        logger.info(`Account balance: ${(await deployer.getBalance()).toString()}`);

        // Load MementumToken contract
        const MementumToken = await ethers.getContractFactory("MementumToken");
        const memeToken = await MementumToken.attach(process.env.CONTRACT_ADDRESS);

        // Mint tokens
        const tx = await memeToken.mint(recipient, amountInWei);
        await tx.wait();
        logger.info(`Minted ${amount} $MEME tokens to ${recipient}`);
    } catch (error) {
        logger.error(`Minting failed: ${error.message}`);
        process.exit(1);
    }
}

main().catch((error) => {
    logger.error(`Unexpected error: ${error.message}`);
    process.exit(1);
});