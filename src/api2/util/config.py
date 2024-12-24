from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API2_DATABASE_URL: str
    API2_USERNAME: str
    API2_PASSWORD: str
    API2_ADM_PASSWORD: str
    API2_NAME: str = "Mule PortoAirClub API"
    API2_VERSION: str = "2.0.0"
    items_per_user: int = 50

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()