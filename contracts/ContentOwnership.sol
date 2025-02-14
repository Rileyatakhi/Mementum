// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

contract ContentOwnership {
    struct Content {
        uint256 nftId; // Associated NFT ID
        string contentHash; // IPFS hash or similar identifier
        address creator; // Original creator
    }

    IERC721 public memeNFT; // Reference to the NFT contract
    mapping(uint256 => Content) public contents; // NFT ID -> Content

    event ContentRegistered(uint256 indexed nftId, string contentHash, address creator);

    constructor(address nftAddress) {
        memeNFT = IERC721(nftAddress);
    }

    /**
     * @notice Register content ownership.
     * @param nftId The NFT ID associated with the content.
     * @param contentHash Hash of the content (e.g., IPFS hash).
     */
    function registerContent(uint256 nftId, string memory contentHash) external {
        require(memeNFT.ownerOf(nftId) == msg.sender, "Not the owner of the NFT");
        require(bytes(contentHash).length > 0, "Invalid content hash");

        contents[nftId] = Content({
            nftId: nftId,
            contentHash: contentHash,
            creator: msg.sender
        });

        emit ContentRegistered(nftId, contentHash, msg.sender);
    }

    /**
     * @notice Verify ownership of content.
     * @param nftId The NFT ID to check.
     */
    function verifyOwnership(uint256 nftId) external view returns (address) {
        return contents[nftId].creator;
    }
}