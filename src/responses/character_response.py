from src.responses.base_response import BaseResponse
from src.entities.character_entity import CharacterEntity


class CharacterResponse(BaseResponse):
    id: int
    name: str
    height: int
    mass: int
    birth_year: str
    hair_color: str
    skin_color: str
    eye_color: str

    @classmethod
    def from_entity(cls, character: CharacterEntity) -> "CharacterResponse":
        return cls(
            id=character.id,
            name=character.name,
            height=character.height,
            mass=character.mass,
            birth_year=character.birth_year,
            hair_color=character.hair_color,
            skin_color=character.skin_color,
            eye_color=character.eye_color,
        )
