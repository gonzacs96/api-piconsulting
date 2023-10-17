from fastapi.responses import JSONResponse
from fastapi import Request


async def internal_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
        },
    )
