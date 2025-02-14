// scripts/airdrop_tokens.js

const { ethers } = require("hardhat");
const { logger } = require("../utils/logger");

/**
 * Executes a token airdrop to multiple recipients.
 * 
 * Usage:
 *   node scripts/airdrop_tokens.js --network <network_name> <recipient_addresses> <amounts>
 * 
 * Example:
 *   node scripts/airdrop_tokens.js --network testnet "0xAddr1,0xAddr2" "100,200"
 */
async function main() {
    const args = process.argv.slice(2);
    if (args.length < 2) {
        logger.error("Usage: node scripts/airdrop_tokens.js <recipient_addresses> <amounts>");
        process.exit(1);
    }

    const [recipientsStr, amountsStr] = args;
    const recipients = recipientsStr.split(",");
    const amounts = amountsStr.split(",").map((amt) => ethers.utils.parseEther(amt));

    try {
        // Load accounts
        const [deployer] = await ethers.getSigners();
        logger.info(`Executing airdrop with account: ${deployer.address}`);
        logger.info(`Account balance: ${(await deployer.getBalance()).toString()}`);

        // Load MementumToken contract
        const MementumToken = await ethers.getContractFactory("MementumToken");
        const memeToken = await MementumToken.attach(process.env.CONTRACT_ADDRESS);

        // Perform airdrop
        for (let i = 0; i < recipients.length; i++) {
            const tx = await memeToken.transfer(recipients[i], amounts[i]);
            await tx.wait();
            logger.info(`Airdropped ${ethers.utils.formatEther(amounts[i])} $MEME to ${recipients[i]}`);
        }
    } catch (error) {
        logger.error(`Airdrop failed: ${error.message}`);
        process.exit(1);
    }
}

main().catch((error) => {
    logger.error(`Unexpected error: ${error.message}`);
    process.exit(1);
});