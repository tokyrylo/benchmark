from pydantic_settings import BaseSettings
import os

class Config(BaseSettings):
    SUPERBENCHMARK_DEBUG: bool
    JSON_DB_PATH: str
    DATABASE_URL: str 

    class Config:
        env_file = ".env"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Если режим отладки включен
        if self.SUPERBENCHMARK_DEBUG:
            os.environ["DEBUG"] = "True" 
        else:
            os.environ["DEBUG"] = "False"
            raise ValueError("Feature not ready for live yet. Please enable SUPERBENCHMARK_DEBUG.")

settings = Config()
