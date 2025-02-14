# sdk/mementum_ai.py

import requests
from .errors import AIServiceError
from .logging_config import logger

class MementumAI:
    def __init__(self, api_key=None):
        self.api_key = api_key or Config.get("AI_API_KEY")
        self.base_url = Config.get("AI_SERVICE_URL")

    def generate_text(self, prompt: str) -> str:
        """Generate text using an AI model."""
        try:
            response = requests.post(
                f"{self.base_url}/generate-text",
                json={"prompt": prompt},
                headers={"Authorization": f"Bearer {self.api_key}"},
            )
            response.raise_for_status()
            return response.json().get("text", "")
        except requests.RequestException as e:
            logger.error(f"Error generating text: {e}")
            raise AIServiceError("Failed to generate text.") from e

    def generate_image(self, prompt: str) -> str:
        """Generate an image using an AI model."""
        try:
            response = requests.post(
                f"{self.base_url}/generate-image",
                json={"prompt": prompt},
                headers={"Authorization": f"Bearer {self.api_key}"},
            )
            response.raise_for_status()
            return response.json().get("image_url", "")
        except requests.RequestException as e:
            logger.error(f"Error generating image: {e}")
            raise AIServiceError("Failed to generate image.") from e

    def generate_video(self, prompt: str) -> str:
        """Generate a short video using an AI model."""
        try:
            response = requests.post(
                f"{self.base_url}/generate-video",
                json={"prompt": prompt},
                headers={"Authorization": f"Bearer {self.api_key}"},
            )
            response.raise_for_status()
            return response.json().get("video_url", "")
        except requests.RequestException as e:
            logger.error(f"Error generating video: {e}")
            raise AIServiceError("Failed to generate video.") from e