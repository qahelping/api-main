from datetime import datetime
from typing import Optional, Literal, List

from pydantic import BaseModel, Field, field_validator, AliasChoices, AfterValidator, HttpUrl


class Order(BaseModel):
    id_: int = Field(validation_alias=AliasChoices("id", "id_"), strict=True)
    petId: int
    quantity: int
    shipDate: str
    status: Literal['placed', 'approved', 'delivered']
    complete: Optional[bool] = None

    @field_validator("id_")
    def id_must_be_7_chars(cls, value: int):
        if len(str(value)) < 7:
            raise ValueError("ID less than 7 chars")
        return value

    @field_validator('shipDate')
    def validate_datetime_format(cls, value):
        try:
            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f%z')
            return value
        except ValueError:
            raise ValueError('Invalid datetime format. Expected: YYYY-MM-DDTHH:MM:SS.sss+ZZZZ')


class Tag(BaseModel):
    id: int
    name: str = Field(max_length=100)


class Category(BaseModel):
    id: int
    name: str = Field(max_length=100)


class Pet(BaseModel):
    id: int
    category: Optional[Category] = None
    name: str = Field(max_length=50)
    photoUrls: List[HttpUrl] = Field()
    tags: Optional[List[Tag]] = None
    status: Optional[Literal["available", "pending", "sold"]]
