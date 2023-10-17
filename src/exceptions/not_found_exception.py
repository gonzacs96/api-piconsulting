from typing import Any
from fastapi import status
from src.exceptions.base_exception import BaseException


class NotFoundException(BaseException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail)
