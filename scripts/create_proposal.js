// scripts/create_proposal.js

const { ethers } = require("hardhat");
const { logger } = require("../utils/logger");

/**
 * Creates a governance proposal for voting.
 * 
 * Usage:
 *   node scripts/create_proposal.js --network <network_name> "Proposal Description" <duration_in_seconds>
 * 
 * Example:
 *   node scripts/create_proposal.js --network testnet "Increase staking rewards" 86400
 */
async function main() {
    const args = process.argv.slice(2);
    if (args.length < 2) {
        logger.error("Usage: node scripts/create_proposal.js <description> <duration_in_seconds>");
        process.exit(1);
    }

    const [description, duration] = args;

    try {
        // Load accounts
        const [deployer] = await ethers.getSigners();
        logger.info(`Creating proposal with account: ${deployer.address}`);
        logger.info(`Account balance: ${(await deployer.getBalance()).toString()}`);

        // Load MemeGovernance contract
        const MemeGovernance = await ethers.getContractFactory("MemeGovernance");
        const memeGovernance = await MemeGovernance.attach(process.env.GOVERNANCE_CONTRACT_ADDRESS);

        // Create proposal
        const tx = await memeGovernance.createProposal(description, parseInt(duration));
        await tx.wait();
        logger.info(`Proposal created: "${description}" with voting duration of ${duration} seconds`);
    } catch (error) {
        logger.error(`Proposal creation failed: ${error.message}`);
        process.exit(1);
    }
}

main().catch((error) => {
    logger.error(`Unexpected error: ${error.message}`);
    process.exit(1);
});