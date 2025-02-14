// scripts/deploy_contracts.js

const { ethers } = require("hardhat");
const { logger } = require("../utils/logger");

/**
 * Deploys or upgrades Mementum smart contracts.
 * 
 * Usage:
 *   node scripts/deploy_contracts.js --network <network_name>
 * 
 * Networks:
 *   - testnet: Use for testing purposes.
 *   - mainnet: Use for production deployment.
 */
async function main() {
    try {
        // Load accounts
        const [deployer] = await ethers.getSigners();
        logger.info(`Deploying contracts with account: ${deployer.address}`);
        logger.info(`Account balance: ${(await deployer.getBalance()).toString()}`);

        // Deploy MementumToken
        const MementumToken = await ethers.getContractFactory("MementumToken");
        const initialSupply = ethers.utils.parseEther("1000000"); // 1 million tokens
        const memeToken = await MementumToken.deploy(initialSupply);
        await memeToken.deployed();
        logger.info(`MementumToken deployed at: ${memeToken.address}`);

        // Deploy MemeGovernance
        const MemeGovernance = await ethers.getContractFactory("MemeGovernance");
        const memeGovernance = await MemeGovernance.deploy(memeToken.address);
        await memeGovernance.deployed();
        logger.info(`MemeGovernance deployed at: ${memeGovernance.address}`);

        // Log deployment details
        logger.info("Deployment completed successfully.");
    } catch (error) {
        logger.error(`Deployment failed: ${error.message}`);
        process.exit(1);
    }
}

main().catch((error) => {
    logger.error(`Unexpected error: ${error.message}`);
    process.exit(1);
});