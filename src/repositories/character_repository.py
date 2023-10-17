from sqlalchemy.orm import Session
from src.entities.character_entity import CharacterEntity


class CharacterRepository:
    _instance: "CharacterRepository" = None

    def __init__(self, entity: CharacterEntity) -> None:
        self._entity = entity

    def get_all_characters(self, db: Session) -> list[CharacterEntity]:
        return db.query(self._entity).all()

    def get_character_by_id(self, id: int, db: Session) -> CharacterEntity | None:
        return db.query(self._entity).filter(self._entity.id == id).first()

    def create_character(
        self, character: CharacterEntity, db: Session
    ) -> CharacterEntity:
        db.add(character)
        db.commit()
        db.refresh(character)
        return character

    def delete_character(self, character: CharacterEntity, db: Session) -> None:
        db.delete(character)
        db.commit()

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls(CharacterEntity)
        return cls._instance
