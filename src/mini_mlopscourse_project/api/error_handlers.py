from fastapi import Request
from fastapi.responses import JSONResponse


async def prediction_error_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(
        status_code=500,
        content={
            "error": "PREDICTION_ERROR",
            "message": "Prediction failed"
        }
    )