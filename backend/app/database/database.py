from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URL)

db = client["Plante"]

users_collection = db["users"]
history_collection = db["prediction_history"]  # ✅ NOUVEAU
alerts_collection = db["alerts_history"]