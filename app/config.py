from decouple import config

class DBConfig:
    DB_PATH: str = config('DB_PATH')

class APIConfig:
    API_KEY: str = config('API_KEY')
    API_KEY_SECRET: str = config('API_KEY_SECRET')
    BEARER_TOKEN: str = config('BEARER_TOKEN')
    ACCESS_TOKEN: str = config('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET: str = config('ACCESS_TOKEN_SECRET')

class SAConfig:
    SENTIMENT_ANALIZER: str = config('SENTIMENT_ANALIZER')
