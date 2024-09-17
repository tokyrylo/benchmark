from pydantic_settings import BaseSettings


class Config(BaseSettings):
    SUPERBENCHMARK_DEBUG: bool = True
    JSON_DB_PATH: str = "test_database.json"
    DATABASE_URL: str = ""

    class Config:
        env_file = ".env"
