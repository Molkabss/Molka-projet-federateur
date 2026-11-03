from fastapi import APIRouter
from app.api.endpoints.health import router as health_router
from app.api.endpoints.prediction import router as prediction_router
from app.api.endpoints.alerts import router as alerts_router
from app.api.endpoints.chatbot import router as chatbot_router
api_router = APIRouter()

api_router.include_router(health_router, prefix="/system")
api_router.include_router(prediction_router, prefix="/plant")
api_router.include_router(alerts_router, prefix="/plant")
api_router.include_router(chatbot_router, prefix="/plant")