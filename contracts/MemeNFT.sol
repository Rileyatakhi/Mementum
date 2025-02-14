// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemeNFT is ERC721, Ownable {
    uint256 public tokenCounter;
    string public baseURI;

    event NFTMinted(address indexed owner, uint256 tokenId);

    constructor(string memory name, string memory symbol, string memory _baseURI) ERC721(name, symbol) {
        baseURI = _baseURI;
        tokenCounter = 1; // Start token IDs from 1
    }

    /**
     * @notice Mint a new NFT.
     * @param recipient Address to receive the NFT.
     */
    function mintNFT(address recipient) external onlyOwner {
        require(recipient != address(0), "Invalid recipient");
        _safeMint(recipient, tokenCounter);
        emit NFTMinted(recipient, tokenCounter);
        tokenCounter++;
    }

    /**
     * @notice Set the base URI for all tokens.
     * @param _newBaseURI New base URI.
     */
    function setBaseURI(string memory _newBaseURI) external onlyOwner {
        baseURI = _newBaseURI;
    }

    /**
     * @notice Override to return the base URI.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }
}