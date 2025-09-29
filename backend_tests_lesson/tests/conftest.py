import pytest

from config import TestConfig
from src.backend.services.pet_store.adapter import PetStoreAdapter
from src.backend.services.pet_store.service import PetStoreService


@pytest.fixture(scope="session")
def pet_store_adapter() -> PetStoreAdapter:
    return PetStoreAdapter(host=TestConfig.PET_STORE_BASE_URL)


@pytest.fixture(scope="session")
def pet_store_service(pet_store_adapter) -> PetStoreService:
    return PetStoreService(adapter=pet_store_adapter)
