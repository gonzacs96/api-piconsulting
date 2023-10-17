from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.dtos.create_character_dto import CreateCharacterDTO
from src.services.character_service import CharacterService
from src.config.database import get_db
from src.responses.character_partial_response import CharacterPartialResponse
from src.responses.character_response import CharacterResponse


router = APIRouter(prefix="/character", tags=["Character"])


@router.get("/getAll", response_model=list[CharacterPartialResponse])
def get_all_characters(
    db: Session = Depends(get_db),
    character_service: CharacterService = Depends(
        dependency=CharacterService.get_instance
    ),
):
    characters = character_service.get_all_characters(db)
    return [CharacterPartialResponse.from_entity(character) for character in characters]


@router.get("/get/{id}", response_model=CharacterResponse)
def get_character_by_id(
    id: int,
    db: Session = Depends(get_db),
    character_service: CharacterService = Depends(
        dependency=CharacterService.get_instance
    ),
):
    character = character_service.get_character_by_id(id, db)
    return CharacterResponse.from_entity(character)


@router.post("/add", status_code=status.HTTP_201_CREATED)
def create_character(
    character_dto: CreateCharacterDTO,
    db: Session = Depends(get_db),
    character_service: CharacterService = Depends(
        dependency=CharacterService.get_instance
    ),
):
    character = character_service.create_character(character_dto, db)
    return CharacterResponse.from_entity(character)


@router.delete("/delete/{id}")
def delete_character(
    id: int,
    db: Session = Depends(get_db),
    character_service: CharacterService = Depends(
        dependency=CharacterService.get_instance
    ),
):
    character_service.delete_character(id, db)
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "Character deleted"}
    )
