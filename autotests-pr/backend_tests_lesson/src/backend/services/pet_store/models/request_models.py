from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class PetDataRequestModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True
    )

    id: int
    name: str
    photo_urls: Optional[list] = Field(alias="photoUrls", default=None)
