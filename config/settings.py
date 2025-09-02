import shutil
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Define project root
ROOT = Path(__file__).resolve().parent.parent

# Paths to .env and .env.example
ENV_PATH = ROOT / ".env"
ENV_EXAMPLE_PATH = ROOT / ".env.example"

# If .env does not exist, create it from .env.example
def sync_env():
    """Sync .env with .env.example before tests"""

    example_vars = {}
    if not ENV_PATH.exists():
        if ENV_EXAMPLE_PATH.exists():
            shutil.copy(ENV_EXAMPLE_PATH, ENV_PATH)
            print(f"[ENV SYNC] Created .env from .env.example")
        else:
            with open(ENV_PATH, 'w') as f:
                pass
            print("[ENV SYNC] Empty .env created")


# Run sync before loading env
sync_env()


# Settings with Pydantic
class Settings(BaseSettings):
    """App settings with type validation & IDE autocompletion"""

    BASE_URL: str
    HEADLESS: bool
    PAUSE_TEST: bool  # pause test execution for debugging

    model_config = SettingsConfigDict(
        env_file=str(ENV_PATH),
        env_file_encoding="utf-8"
    )


# Initialize settings
settings = Settings()
