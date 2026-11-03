from fastapi import APIRouter
from app.schemas.prediction import HealthResponse
from app.core.model_loader import model_manager

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check():
    return HealthResponse(
        status="ok",
        model_loaded=model_manager.is_loaded(),
        message="API Plant Disease Detection opérationnelle"
    )