from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.core.config import SECRET_KEY, ALGORITHM
from app.services.weather_service import get_weather, analyze_risks
from app.crud.history_crud import get_user_plants_summary

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=403, detail="Token invalide")
        return username
    except JWTError:
        raise HTTPException(status_code=403, detail="Token invalide")


@router.get("/alerts", tags=["Alerts"])
async def get_climate_alerts(
    lat: float,
    lon: float,
    username: str = Depends(get_current_user)
):
    """
    Retourne les alertes climatiques pour les plantes de l'utilisateur.
    Le frontend envoie lat et lon depuis la géolocalisation mobile.
    """
    try:
        # Récupère la météo actuelle
        weather = get_weather(lat, lon)
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Erreur météo: {str(e)}")

    # Récupère les plantes de l'utilisateur
    user_plants = await get_user_plants_summary(username)

    if not user_plants:
        return {
            "success": True,
            "username": username,
            "location": {"lat": lat, "lon": lon, "city": weather["city"]},
            "weather": weather,
            "alerts": [],
            "message": "Aucune plante dans votre historique."
        }

    # Analyse les risques
    alerts = analyze_risks(weather, user_plants)

    return {
        "success": True,
        "username": username,
        "location": {"lat": lat, "lon": lon, "city": weather["city"]},
        "weather": weather,
        "alerts": alerts,
        "total_alerts": len(alerts),
        "high_risk_count": sum(1 for a in alerts if a["risk_level"] == "HIGH"),
        "message": f"{len(alerts)} alerte(s) détectée(s) pour vos plantes."
    }