import os
from dataclasses import dataclass

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv("APP_ENV", "development")

    # NASA API key
    api_key: str = os.getenv("NASA_API_KEY", "")

    debug: bool = os.getenv("DEBUG", "False").lower() in (
        "true",
        "1",
        "yes",
    )

    def validate(self) -> None:
        """Validate required configuration."""

        if (
            not self.api_key
            or self.api_key.startswith("your_")
            or self.api_key == "DEMO_KEY"
        ):
            raise ValueError(
                "CRITICAL CONFIG ERROR: NASA API key is missing "
                "or invalid.\n"
                "Ensure your .env file contains a valid "
                "NASA_API_KEY."
            )


# Application configuration
config = Settings()