from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class TopPrediction(BaseModel):
    label: str
    confidence: float


class PredictionResponse(BaseModel):
    success: bool
    predicted_class: str
    confidence: float
    top_predictions: List[TopPrediction]


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    message: str


class AutoPredictionResponse(BaseModel):
    success: bool
    plant_type: str
    plant_confidence: float
    disease: str
    disease_confidence: float
    top_disease_predictions: List[TopPrediction]
    message: str


class HistoryItem(BaseModel):
    id: Optional[str] = None
    username: str
    plant_type: str
    disease: str
    confidence: float
    created_at: datetime


class HistoryResponse(BaseModel):
    success: bool
    history: List[HistoryItem]
    total: int