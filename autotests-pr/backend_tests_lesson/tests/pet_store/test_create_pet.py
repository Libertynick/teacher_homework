import random

import allure

from src.backend.services.pet_store.models.request_models import PetDataRequestModel
from src.utils.validators.assert_wrappers import assert_eq


@allure.title("Тест на создание питомца с валидными данными")
def test_create_valid_pet(pet_store_service):
    pet_data = PetDataRequestModel(id=random.randint(1000, 10000),
                                   name="Jorik")
    response = pet_store_service.create_pet(pet_data=pet_data)
    assert_eq(actual_value=response.id,
              expected_value=pet_data.id,
              allure_title="Проверка id созданного питомца",
              error_msg="id созданного питомца не равен переданному")
