from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str ="localhost"
    database_port: str ="5432"
    database_password: str= "asdfasdfad3as"
    database_name: str ="fastapi"
    database_username: str ="postgres"
    secret_key: str ="09f3b6c8c6e4d4e8a4f8e9e7e6f5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7"
    algorithm: str ="HS256"
    access_token_expire_minutes: int = 30
    
    class Config:
        env_file = ".env"
    
    
settings = Settings()