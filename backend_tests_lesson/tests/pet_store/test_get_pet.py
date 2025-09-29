import http

import allure

from src.utils.validators.assert_wrappers import assert_eq
from src.utils.validators.rest_api import validate_response


@allure.title("Тест на получение несуществующего питомца")
def test_get_not_existed_pet(pet_store_adapter):
    response = pet_store_adapter.get_pet(pet_id=1232133)
    with allure.step("Проверка ответа"):
        validate_response(response=response, expected_status_code=http.HTTPStatus.NOT_FOUND)
        assert_eq(actual_value=response.json()["message"],
                  expected_value="Pet not found",
                  allure_title="Проверка message из тела ответа",
                  error_msg="Некорректная ошибка в теле ответа")

@allure.title("Тест на получение питомца с невалидным id")
def test_get_not_valid_pet(pet_store_adapter):
    response = pet_store_adapter.get_pet(pet_id="2fds$")
    with allure.step("Проверка ответа"):
        validate_response(response=response, expected_status_code=http.HTTPStatus.NOT_FOUND)
        assert_eq(actual_value=response.json()["message"],
                  expected_value='java.lang.NumberFormatException: For input string: "2fds$"',
                  allure_title="Проверка message из тела ответа",
                  error_msg="Некорректная ошибка в теле ответа")
