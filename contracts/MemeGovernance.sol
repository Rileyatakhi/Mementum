// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemeGovernance is Ownable {
    using SafeMath for uint256;

    struct Proposal {
        uint256 id;
        string description;
        uint256 deadline;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    IERC20 public memeToken; // Reference to the $MEME token contract
    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;

    event ProposalCreated(uint256 indexed id, string description, uint256 deadline);
    event Voted(uint256 indexed id, address voter, bool support);
    event ProposalExecuted(uint256 indexed id);

    constructor(address tokenAddress) {
        memeToken = IERC20(tokenAddress);
    }

    /**
     * @notice Create a new proposal.
     * @param description Description of the proposal.
     * @param duration Duration of the voting period in seconds.
     */
    function createProposal(string memory description, uint256 duration) external onlyOwner {
        uint256 id = proposalCount++;
        uint256 deadline = block.timestamp + duration;

        proposals[id] = Proposal({
            id: id,
            description: description,
            deadline: deadline,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        });

        emit ProposalCreated(id, description, deadline);
    }

    /**
     * @notice Vote on a proposal.
     * @param id Proposal ID.
     * @param support True if voting in favor, false otherwise.
     */
    function vote(uint256 id, bool support) external {
        Proposal storage proposal = proposals[id];
        require(proposal.deadline > block.timestamp, "Voting period has ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");

        uint256 votingPower = memeToken.balanceOf(msg.sender);
        require(votingPower > 0, "No voting power");

        proposal.hasVoted[msg.sender] = true;

        if (support) {
            proposal.votesFor += votingPower;
        } else {
            proposal.votesAgainst += votingPower;
        }

        emit Voted(id, msg.sender, support);
    }

    /**
     * @notice Execute a proposal if it passes.
     * @param id Proposal ID.
     */
    function executeProposal(uint256 id) external onlyOwner {
        Proposal storage proposal = proposals[id];
        require(!proposal.executed, "Proposal already executed");
        require(proposal.deadline <= block.timestamp, "Voting period not over");

        if (proposal.votesFor > proposal.votesAgainst) {
            proposal.executed = true;
            emit ProposalExecuted(id);
            // Add logic here to execute the proposal (e.g., update parameters, call other contracts)
        } else {
            revert("Proposal did not pass");
        }
    }
}