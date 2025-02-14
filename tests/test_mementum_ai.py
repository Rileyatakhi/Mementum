# tests/test_mementum_ai.py

import pytest
from sdk.mementum_ai import MementumAI
from sdk.errors import AIServiceError

@pytest.fixture
def ai():
    return MementumAI()

def test_generate_text(ai):
    """Test generating text."""
    try:
        prompt = "Explain blockchain technology."
        response = ai.generate_text(prompt)
        assert isinstance(response, str), "Generated text should be a string."
        assert len(response) > 0, "Generated text should not be empty."
    except AIServiceError as e:
        pytest.fail(f"Text generation failed: {e}")

def test_generate_image(ai):
    """Test generating an image."""
    try:
        prompt = "A futuristic cityscape at sunset."
        response = ai.generate_image(prompt)
        assert isinstance(response, str), "Generated image URL should be a string."
        assert response.startswith("http"), "Generated image URL should start with 'http'."
    except AIServiceError as e:
        pytest.fail(f"Image generation failed: {e}")