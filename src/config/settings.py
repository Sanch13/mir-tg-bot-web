from pydantic_settings import BaseSettings

from src.config.db_settings import DBSettings
from src.config.tg_settings import TGSettings


class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    tg: TGSettings = TGSettings()


settings = Settings()
