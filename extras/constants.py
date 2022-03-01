from decouple import config, Csv


class Constants:
    # DB settings
    DB_USER = config('DB_USER')
    DB_PASSWORD = config('DB_PASSWORD')
    DB_HOST = config('DB_HOST')
    DB_PORT = config('DB_PORT')
    DB_NAME = config('DB_NAME')

    # Django settings
    SECRET_KEY = config('SECRET_KEY')
    ATOMIC_REQUESTS = config('ATOMIC_REQUESTS')
    DEBUG = config('DEBUG', cast=bool)
    ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
    SERVER_PORT = config('SERVER_PORT')

    # Extra settings
    SEEDED_ELEMENTS = config('SEEDED_ELEMENTS', cast=int)
