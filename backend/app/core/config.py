from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Money Tracker"
    API_V1_PREFIX: str = "/api/v1"
    DATABASE_URL: str = "postgresql://admin:admin@db:5433/moneytracker"
    JWT_SECRET: str = "CHANGE_ME"
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()
