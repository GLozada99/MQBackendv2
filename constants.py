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
    DEBUG = config('DEBUG', cast=bool)
    ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

    # Extra settings
    SEEDED_ELEMENTS = config('SEEDED_ELEMENTS', cast=int)
