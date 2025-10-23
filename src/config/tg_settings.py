from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class TGSettings(BaseSettings):
    API_TELEGRAM_TOKEN: SecretStr

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        extra="ignore",
    )
