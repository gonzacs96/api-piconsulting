from src.responses.base_response import BaseResponse
from src.entities.character_entity import CharacterEntity


class CharacterPartialResponse(BaseResponse):
    id: int
    name: str
    height: int
    mass: int
    birth_year: str
    eye_color: str

    @classmethod
    def from_entity(
        cls, character_entity: CharacterEntity
    ) -> "CharacterPartialResponse":
        return cls(
            id=character_entity.id,
            name=character_entity.name,
            height=character_entity.height,
            mass=character_entity.mass,
            birth_year=character_entity.birth_year,
            eye_color=character_entity.eye_color,
        )
