from sqlalchemy.orm import Session
from src.dtos.create_character_dto import CreateCharacterDTO
from src.entities.character_entity import CharacterEntity
from src.repositories.character_repository import CharacterRepository
from src.exceptions.bad_request_exception import BadRequestException
from src.exceptions.not_found_exception import NotFoundException


class CharacterService:
    _instance: "CharacterService" = None

    def __init__(self, character_repository: CharacterRepository) -> None:
        self._character_repository = character_repository

    def get_all_characters(self, db: Session) -> list[CharacterEntity]:
        return self._character_repository.get_all_characters(db)

    def get_character_by_id(self, id: int, db: Session) -> CharacterEntity | None:
        character = self._character_repository.get_character_by_id(id, db)
        if not character:
            raise NotFoundException("Character not found")
        return character

    def create_character(
        self, character_dto: CreateCharacterDTO, db: Session
    ) -> CharacterEntity:
        exist = self._character_repository.get_character_by_id(character_dto.id, db)
        if exist:
            raise BadRequestException("Character already exists")
        new_character = CharacterEntity(**character_dto.dict())
        return self._character_repository.create_character(new_character, db)

    def delete_character(self, id: int, db: Session) -> None:
        character = self._character_repository.get_character_by_id(id, db)
        if not character:
            raise BadRequestException("Character not deleted because it does not exist")
        self._character_repository.delete_character(character, db)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            character_repository = CharacterRepository.get_instance()
            cls._instance = cls(character_repository)
        return cls._instance
