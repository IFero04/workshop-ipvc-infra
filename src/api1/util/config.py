from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API1_DATABASE_URL: str
    API1_USERNAME: str
    API1_PASSWORD: str
    API1_ADM_PASSWORD: str
    API1_NAME: str = "Mule BenficaAirClub API"
    API1_VERSION: str = "1.0.0"
    items_per_user: int = 50

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()