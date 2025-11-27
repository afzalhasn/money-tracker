from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Money Tracker"
    API_V1_PREFIX: str = "/api/v1"
    DATABASE_URL: str = "postgresql://admin:admin@db:5432/moneytracker"
    JWT_SECRET: str = "CHANGE_ME"
    JWT_ALGORITHM: str = "HS256"
    access_token_expire_minutes: int = 30 
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
