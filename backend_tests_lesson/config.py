import os


class TestConfig:
    PET_STORE_BASE_URL = os.getenv("PET_STORE_BASE_URL", "https://petstore.swagger.io")
