from typing import Any
from src.exceptions.base_exception import BaseException
from fastapi import status


class BadRequestException(BaseException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail)
