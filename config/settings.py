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
    if ENV_EXAMPLE_PATH.exists():
        with open(ENV_EXAMPLE_PATH, 'r') as example_file:
            for line in example_file:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    example_vars[key] = value

    if not ENV_PATH.exists():
        with open(ENV_PATH, 'w') as f:
            pass
        print("[ENV SYNC] Empty .env created")

    with open(ENV_PATH, 'r+') as env_file:
        env_content = env_file.read()
        for key, value in example_vars.items():
            if key not in env_content:
                env_file.write(f"\n{key}={value}")
                print(f"[ENV SYNC] {key} added to .env")

    with open(ENV_PATH, 'r') as f:
        lines = [line for line in f if line.strip()]
    with open(ENV_PATH, 'w') as f:
        f.writelines(lines)


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
