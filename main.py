from fastapi import FastAPI, status
from src.config.database import test_db_connection_and_create_tables
from src.handlers.internal_exception_handler import internal_exception_handler
from src.routers.character_router import router as character_router

# Test database connection and create tables
test_db_connection_and_create_tables()

app = FastAPI()

app.include_router(character_router)
app.add_exception_handler(
    status.HTTP_500_INTERNAL_SERVER_ERROR, internal_exception_handler
)
