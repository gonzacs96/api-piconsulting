from typing import TypedDict
from src.exceptions.bad_request_exception import BadRequestException
from src.entities.base_entity import BaseEntity
from pydantic import BaseModel


class BaseResponse(BaseModel):
    pass
