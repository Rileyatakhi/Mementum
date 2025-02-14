# tests/test_meme_governance.py

import pytest
from sdk.mementum_api import MementumAPI
from sdk.errors import AIServiceError

@pytest.fixture
def api():
    return MementumAPI()

def test_create_proposal(api):
    """Test creating a proposal."""
    try:
        response = api.submit_content({
            "title": "Proposal to Increase Staking Rewards",
            "description": "Increase staking rewards by 10%.",
            "content_url": "https://example.com/proposal.pdf"
        })
        assert response.get("status") == "success", "Proposal creation failed."
    except AIServiceError as e:
        pytest.fail(f"Proposal creation failed: {e}")

def test_vote_on_proposal(api):
    """Test voting on a proposal."""
    try:
        user_id = "test_user_id"
        proposal_id = "proposal_123"
        vote_data = {
            "user_id": user_id,
            "proposal_id": proposal_id,
            "vote": "yes"
        }
        response = api.submit_content(vote_data)
        assert response.get("status") == "success", "Voting failed."
    except AIServiceError as e:
        pytest.fail(f"Voting failed: {e}")