from enum import StrEnum
from typing import Any

import allure
import requests

from src.backend.clients.http_client.client import HTTPClient

class Routes(StrEnum):
    __API = "v2"
    PET = f"{__API}/pet"

class PetStoreAdapter:
    def __init__(self, host: str):
        self._http_client = HTTPClient(host=host)

    @allure.step("Получение питомца с id {pet_id}")
    def get_pet(self, pet_id: int | str) -> requests.Response:
        return self._http_client.get(route=f"{Routes.PET}/{pet_id}")

    @allure.step("Отправка запроса на создание питомца")
    def create_pet(self, pet_data: dict[str, Any]) -> requests.Response:
        return self._http_client.post(route=f"{Routes.PET}", json=pet_data)

    @allure.step("Отправка запроса на создание тега")
    def create_tag(self):
        pass

    @allure.step("Отправка запроса на создание категории")
    def create_category(self):
        pass
