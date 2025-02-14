// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MementumToken is ERC20, Ownable {
    // Events for minting and burning
    event TokensMinted(address indexed to, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);

    constructor(uint256 initialSupply) ERC20("Mementum", "MEME") {
        _mint(msg.sender, initialSupply); // Mint initial supply to deployer
    }

    /**
     * @notice Mint new tokens.
     * @param to The address to receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @notice Burn tokens from sender's balance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @notice Override transfer function to include additional checks.
     */
    function transfer(address to, uint256 amount) public override returns (bool) {
        require(to != address(0), "Invalid recipient");
        return super.transfer(to, amount);
    }

    /**
     * @notice Override transferFrom function to include additional checks.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override returns (bool) {
        require(to != address(0), "Invalid recipient");
        return super.transferFrom(from, to, amount);
    }
}