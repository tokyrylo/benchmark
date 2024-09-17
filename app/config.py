import os


class Config:
    DEBUG = os.getenv("SUPERBENCHMARK_DEBUG", "false").lower() == "true"
    JSON_DB_PATH = os.getenv("JSON_DB_PATH", "app/test_database.json")
