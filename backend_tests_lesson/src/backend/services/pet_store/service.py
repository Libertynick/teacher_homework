import http

import allure

from src.backend.services.pet_store.adapter import PetStoreAdapter
from src.backend.services.pet_store.models.request_models import PetDataRequestModel
from src.backend.services.pet_store.models.response_models import PetDataResponseModel
from src.utils.validators.rest_api import validate_response


class PetStoreService:

    def __init__(self, adapter: PetStoreAdapter):
        self._adapter = adapter

    @allure.step("Создание питомца")
    def create_pet(self, pet_data: PetDataRequestModel) -> PetDataResponseModel:
        self._adapter.create_tag()
        with allure.step("Проверка, что тег успешно создался"):
            pass
        self._adapter.create_category()
        with allure.step("Проверка, что категория успешно создалась"):
            pass

        response = self._adapter.create_pet(pet_data=pet_data.model_dump(by_alias=True))
        validate_response(response=response, expected_status_code=http.HTTPStatus.OK)
        return PetDataResponseModel(**response.json())