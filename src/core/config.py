from pydantic_settings import BaseSettings, SettingsConfigDict

class Env(BaseSettings):
    app_name: str = "My FastAPI App"
    debug: bool = True
    
    host: str = "127.0.0.1"
    port: int = 8000
    reload: bool = True

    model_config = SettingsConfigDict(env_file=(".env"), env_file_encoding="utf-8", env_ignore_empty=True)
    