import requests
from app.core.config import OPENWEATHER_API_KEY

# Risques climatiques par maladie
DISEASE_CLIMATE_RISKS = {
    # Tomate
    "Late_blight": {
        "conditions": ["high_humidity", "low_temp"],
        "message": "Risque élevé de Mildiou (Late Blight) — humidité élevée et température fraîche favorisent cette maladie.",
        "level": "HIGH"
    },
    "Early_blight": {
        "conditions": ["high_humidity", "warm_temp"],
        "message": "Risque de Brûlure précoce (Early Blight) — chaleur et humidité favorisent cette maladie.",
        "level": "MEDIUM"
    },
    "Leaf_Mold": {
        "conditions": ["high_humidity"],
        "message": "Risque de Moisissure des feuilles — humidité très élevée.",
        "level": "HIGH"
    },
    "Septoria_leaf_spot": {
        "conditions": ["high_humidity", "rain"],
        "message": "Risque de Septoriose — pluie et humidité favorisent cette maladie.",
        "level": "MEDIUM"
    },
    "Spider_mites": {
        "conditions": ["low_humidity", "high_temp"],
        "message": "Risque d'Acariens — temps chaud et sec favorise leur développement.",
        "level": "MEDIUM"
    },
    "Target_Spot": {
        "conditions": ["high_humidity", "warm_temp"],
        "message": "Risque de Tache cible — chaleur et humidité élevées.",
        "level": "MEDIUM"
    },
    "Yellow_Leaf_Curl_Virus": {
        "conditions": ["high_temp", "dry"],
        "message": "Risque de Virus de l'enroulement jaune — temps chaud et sec.",
        "level": "HIGH"
    },
    "Mosaic_virus": {
        "conditions": ["high_temp"],
        "message": "Risque de Virus mosaïque — températures élevées.",
        "level": "MEDIUM"
    },
    # Pomme de terre
    "Potato___Late_blight": {
        "conditions": ["high_humidity", "low_temp"],
        "message": "Risque élevé de Mildiou de la pomme de terre — conditions humides et fraîches.",
        "level": "HIGH"
    },
    "Potato___Early_blight": {
        "conditions": ["high_humidity", "warm_temp"],
        "message": "Risque de Brûlure précoce — chaleur et humidité.",
        "level": "MEDIUM"
    },
    # Apple
    "Apple___Apple_scab": {
        "conditions": ["high_humidity", "rain"],
        "message": "Risque de Tavelure — pluie et humidité élevée.",
        "level": "HIGH"
    },
    "Apple___Black_rot": {
        "conditions": ["high_humidity", "warm_temp"],
        "message": "Risque de Pourriture noire — chaleur et humidité.",
        "level": "HIGH"
    },
    "Apple___Cedar_apple_rust": {
        "conditions": ["high_humidity", "warm_temp"],
        "message": "Risque de Rouille — humidité et chaleur modérée.",
        "level": "MEDIUM"
    },
    # Corn
    "Corn___Common_rust": {
        "conditions": ["high_humidity", "low_temp"],
        "message": "Risque de Rouille commune du maïs — humidité et fraîcheur.",
        "level": "MEDIUM"
    },
    "Corn___Northern_Leaf_Blight": {
        "conditions": ["high_humidity", "warm_temp"],
        "message": "Risque de Brûlure des feuilles — humidité et chaleur.",
        "level": "HIGH"
    },
    # Grape
    "Grape___Black_rot": {
        "conditions": ["high_humidity", "warm_temp"],
        "message": "Risque de Pourriture noire de la vigne — chaleur et humidité.",
        "level": "HIGH"
    },
    "Grape___Esca": {
        "conditions": ["high_temp", "dry"],
        "message": "Risque d'Esca — temps chaud et sec.",
        "level": "MEDIUM"
    },
    "Grape___Leaf_blight": {
        "conditions": ["high_humidity", "warm_temp"],
        "message": "Risque de Brûlure des feuilles de vigne.",
        "level": "MEDIUM"
    },
}


def get_weather(lat: float, lon: float) -> dict:
    """Récupère la météo depuis OpenWeatherMap"""
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "fr"
    }
    response = requests.get(url, params=params, timeout=10)
    if response.status_code != 200:
        raise Exception(f"Erreur météo: {response.status_code}")
    data = response.json()
    return {
        "city": data.get("name", "Inconnu"),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
        "rain": "rain" in data,
    }


def _get_climate_conditions(weather: dict) -> list:
    """Détermine les conditions climatiques actuelles"""
    conditions = []
    humidity = weather["humidity"]
    temperature = weather["temperature"]
    rain = weather["rain"]

    if humidity > 70:
        conditions.append("high_humidity")
    elif humidity < 40:
        conditions.append("low_humidity")
        conditions.append("dry")

    if temperature > 25:
        conditions.append("high_temp")
        conditions.append("warm_temp")
    elif temperature < 15:
        conditions.append("low_temp")

    if rain:
        conditions.append("rain")

    return conditions


def analyze_risks(weather: dict, user_plants: list) -> list:
    """Analyse les risques climatiques pour les plantes de l'utilisateur"""
    current_conditions = _get_climate_conditions(weather)
    alerts = []

    for plant_summary in user_plants:
        plant_type = plant_summary["plant_type"]

        for disease, risk_info in DISEASE_CLIMATE_RISKS.items():
            disease_lower = disease.lower()
            plant_lower = plant_type.lower()

            if plant_lower not in disease_lower and plant_lower not in disease.replace("___", "_").lower():
                if not any(plant_lower in d.lower() for d in [disease]):
                    continue

            matching = [
                c for c in risk_info["conditions"]
                if c in current_conditions
            ]

            if matching:
                alerts.append({
                    "plant_type": plant_type,
                    "disease": disease,
                    "risk_level": risk_info["level"],
                    "message": risk_info["message"],
                    "triggered_by": matching,
                    "prediction_count": plant_summary["count"],
                })

    alerts.sort(key=lambda x: (x["risk_level"] == "HIGH"), reverse=True)
    return alerts