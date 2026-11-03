from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer

from app.core.config import ALLOWED_EXTENSIONS, SECRET_KEY, ALGORITHM
from app.schemas.prediction import PredictionResponse, AutoPredictionResponse
from app.services.prediction_service import (
    predict_image,
    predict_apple_disease,
    predict_corn_disease,
    predict_grape_disease,
    predict_tomato_disease,
    predict_potato_disease,
    predict_auto,
)
from app.crud.history_crud import save_prediction, get_user_history, get_user_plants_summary

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def _validate_file(file: UploadFile):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Nom de fichier invalide.")
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Format non supporté. Utilisez jpg, jpeg ou png.")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=403, detail="Token invalide")
        return username
    except JWTError:
        raise HTTPException(status_code=403, detail="Token invalide")


# ✅ NOUVEAU — Route principale auto
@router.post("/predict/auto", response_model=AutoPredictionResponse, tags=["Prediction"])
async def predict_auto_route(
    file: UploadFile = File(...),
    username: str = Depends(get_current_user)
):
    _validate_file(file)
    try:
        image_bytes = await file.read()
        result = predict_auto(image_bytes)

        # Sauvegarder dans l'historique
        await save_prediction(
            username=username,
            plant_type=result["plant_type"],
            disease=result["disease"],
            confidence=result["disease_confidence"],
        )

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur : {str(e)}")


# ✅ NOUVEAU — Historique utilisateur
@router.get("/history", tags=["History"])
async def get_history(username: str = Depends(get_current_user)):
    history = await get_user_history(username)
    return {
        "success": True,
        "history": history,
        "total": len(history)
    }


# ✅ NOUVEAU — Résumé des plantes de l'utilisateur
@router.get("/history/summary", tags=["History"])
async def get_summary(username: str = Depends(get_current_user)):
    summary = await get_user_plants_summary(username)
    return {
        "success": True,
        "username": username,
        "plants_summary": summary
    }


@router.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
async def predict_plant_image(file: UploadFile = File(...)):
    _validate_file(file)
    try:
        return predict_image(await file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur : {str(e)}")


@router.post("/predict/apple", response_model=PredictionResponse, tags=["Prediction"])
async def predict_apple_image(file: UploadFile = File(...)):
    _validate_file(file)
    try:
        return predict_apple_disease(await file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur Apple : {str(e)}")


@router.post("/predict/corn", response_model=PredictionResponse, tags=["Prediction"])
async def predict_corn_image(file: UploadFile = File(...)):
    _validate_file(file)
    try:
        return predict_corn_disease(await file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur Corn : {str(e)}")


@router.post("/predict/grape", response_model=PredictionResponse, tags=["Prediction"])
async def predict_grape_image(file: UploadFile = File(...)):
    _validate_file(file)
    try:
        return predict_grape_disease(await file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur Grape : {str(e)}")


@router.post("/predict/tomato", response_model=PredictionResponse, tags=["Prediction"])
async def predict_tomato_image(file: UploadFile = File(...)):
    _validate_file(file)
    try:
        return predict_tomato_disease(await file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur Tomato : {str(e)}")


@router.post("/predict/potato", response_model=PredictionResponse, tags=["Prediction"])
async def predict_potato_image(file: UploadFile = File(...)):
    _validate_file(file)
    try:
        return predict_potato_disease(await file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur Potato : {str(e)}")