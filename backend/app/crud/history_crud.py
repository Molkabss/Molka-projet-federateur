from datetime import datetime
from app.database.database import history_collection


async def save_prediction(
    username: str,
    plant_type: str,
    disease: str,
    confidence: float,
):
    record = {
        "username": username,
        "plant_type": plant_type,
        "disease": disease,
        "confidence": confidence,
        "created_at": datetime.utcnow(),
    }
    result = await history_collection.insert_one(record)
    return str(result.inserted_id)


async def get_user_history(username: str):
    cursor = history_collection.find(
        {"username": username}
    ).sort("created_at", -1)
    history = []
    async for doc in cursor:
        history.append({
            "id": str(doc["_id"]),
            "username": doc["username"],
            "plant_type": doc["plant_type"],
            "disease": doc["disease"],
            "confidence": doc["confidence"],
            "created_at": doc["created_at"],
        })
    return history


async def get_user_plants_summary(username: str):
    """Retourne un résumé des plantes de l'utilisateur"""
    pipeline = [
        {"$match": {"username": username}},
        {"$group": {
            "_id": "$plant_type",
            "count": {"$sum": 1},
            "last_prediction": {"$max": "$created_at"}
        }},
        {"$sort": {"count": -1}}
    ]
    cursor = history_collection.aggregate(pipeline)
    summary = []
    async for doc in cursor:
        summary.append({
            "plant_type": doc["_id"],
            "count": doc["count"],
            "last_prediction": doc["last_prediction"],
        })
    return summary
from app.database.database import history_collection, db

alerts_collection = db["alerts_history"]

async def save_alert(
    username: str,
    plant_type: str,
    disease: str,
    risk_level: str,
    message: str,
    weather: dict,
    location: dict,
):
    record = {
        "username": username,
        "plant_type": plant_type,
        "disease": disease,
        "risk_level": risk_level,
        "message": message,
        "weather": weather,
        "location": location,
        "created_at": datetime.utcnow(),
    }
    await alerts_collection.insert_one(record)


async def get_user_alerts(username: str):
    cursor = alerts_collection.find(
        {"username": username}
    ).sort("created_at", -1)
    alerts = []
    async for doc in cursor:
        alerts.append({
            "id": str(doc["_id"]),
            "plant_type": doc["plant_type"],
            "disease": doc["disease"],
            "risk_level": doc["risk_level"],
            "message": doc["message"],
            "weather": doc["weather"],
            "location": doc["location"],
            "created_at": doc["created_at"],
        })
    return alerts
async def get_last_prediction(username: str):
    """Récupère la dernière prédiction de l'utilisateur"""
    doc = await history_collection.find_one(
        {"username": username},
        sort=[("created_at", -1)]
    )
    if not doc:
        return None
    return {
        "plant_type": doc["plant_type"],
        "disease": doc["disease"],
        "confidence": doc["confidence"],
        "created_at": doc["created_at"],
    }