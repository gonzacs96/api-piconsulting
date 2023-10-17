from src.dtos.base_dto import BaseDTO


class CreateCharacterDTO(BaseDTO):
    id: int
    name: str
    height: int
    mass: int
    birth_year: str
    hair_color: str
    skin_color: str
    eye_color: str
