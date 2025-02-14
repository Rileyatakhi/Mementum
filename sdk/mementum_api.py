# sdk/mementum_api.py

import requests
from .errors import AIServiceError
from .logging_config import logger

class MementumAPI:
    def __init__(self, api_key=None):
        self.api_key = api_key or Config.get("PLATFORM_API_KEY")
        self.base_url = Config.get("PLATFORM_API_URL")

    def get_user_profile(self, user_id: str) -> dict:
        """Fetch user profile data."""
        try:
            response = requests.get(
                f"{self.base_url}/users/{user_id}",
                headers={"Authorization": f"Bearer {self.api_key}"},
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching user profile: {e}")
            raise AIServiceError("Failed to fetch user profile.") from e

    def submit_content(self, content_data: dict) -> dict:
        """Submit content to the platform."""
        try:
            response = requests.post(
                f"{self.base_url}/content",
                json=content_data,
                headers={"Authorization": f"Bearer {self.api_key}"},
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error submitting content: {e}")
            raise AIServiceError("Failed to submit content.") from e