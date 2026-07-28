from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "NexusAgent"
    API_V1_STR: str = "/api/v1"
    REDIS_URL: str = "redis://redis:6379"
    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
