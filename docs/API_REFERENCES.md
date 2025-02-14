This file serves as a reference for all public classes, functions, and endpoints in the SDK.

```markdown
# Mementum API Reference

## Table of Contents
1. [MementumAI](#mementumai)
2. [MementumAPI](#mementumapi)
3. [BlockchainInteractions](#blockchaininteractions)
4. [Config](#config)
5. [Errors](#errors)
6. [Logging](#logging)
7. [Utils](#utils)
```


#### Description

Handles AI logic for generating multi-modal content (text, images, videos).

#### Methods

- **generate_text(prompt: str) -> str**

  - Generates text using an AI model.
  - Example:
    ```python
    ai = MementumAI()
    text = ai.generate_text("Create a market analysis report.")
    ```
- **generate_image(prompt: str) -> str**

  - Generates an image using an AI model.
  - Example:
    ```python
    ai = MementumAI()
    image_url = ai.generate_image("A futuristic cityscape at sunset.")
    ```
- **generate_video(prompt: str) -> str**

  - Generates a short video using an AI model.
  - Example:
    ```python
    ai = MementumAI()
    video_url = ai.generate_video("A time-lapse of a bustling city.")
    ```

---

### MementumAPI

#### Description

Manages REST or GraphQL endpoints for interacting with the platform's backend.

#### Methods

- **get_user_profile(user_id: str) -> dict**

  - Fetches user profile data.
  - Example:
    ```python
    api = MementumAPI()
    profile = api.get_user_profile(user_id="12345")
    ```
- **submit_content(content_data: dict) -> dict**

  - Submits content to the platform.
  - Example:
    ```python
    api = MementumAPI()
    response = api.submit_content({
        "title": "AI-Generated Market Report",
        "description": "An analysis of recent market trends.",
        "content_url": "https://example.com/report.pdf"
    })
    ```

---

### BlockchainInteractions

#### Description

Provides utility functions for interacting with the blockchain.

#### Methods

- **get_balance(address: str) -> float**

  - Gets the token balance of an address.
  - Example:
    ```python
    blockchain = BlockchainInteractions()
    balance = blockchain.get_balance("your_wallet_address")
    ```
- **transfer_tokens(sender_private_key: str, recipient: str, amount: float) -> str**

  - Transfers tokens from one address to another.
  - Example:
    ```python
    blockchain = BlockchainInteractions()
    tx_hash = blockchain.transfer_tokens(
        sender_private_key="your_private_key",
        recipient="recipient_wallet_address",
        amount=100
    )
    ```

---

### Config

#### Description

Centralizes configuration loading.

#### Methods

- **get(key: str, default=None) -> Any**
  - Retrieves a configuration value.
  - Example:
    ```python
    api_key = Config.get("AI_API_KEY")
    ```

---

### Errors

#### Description

Custom exception classes for better error handling.

#### Classes

- **BlockchainError**
  - Raised for blockchain-related issues.
- **AIServiceError**
  - Raised for AI service-related issues.

---

### Logging

#### Description

Standardizes logging setup.

#### Usage

```python
from sdk.logging_config import logger

logger.info("This is an informational message.")
logger.error("This is an error message.")
```
