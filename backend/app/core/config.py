SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

MODEL_PATH = BASE_DIR / "models" / "plant_type" / "inception_plant_model_fixed.keras"
LABELS_PATH = BASE_DIR / "models" / "plant_type" / "plant_labels.json"

APPLE_MODEL_PATH = BASE_DIR / "models" / "apple" / "apple_model_fixed.keras"
APPLE_LABELS_PATH = BASE_DIR / "models" / "apple" / "appel_labels.json"

CORN_MODEL_PATH = BASE_DIR / "models" / "corn" / "corn_disease_fixed.keras"
CORN_LABELS_PATH = BASE_DIR / "models" / "corn" / "corn_labels.json"

GRAPE_MODEL_PATH = BASE_DIR / "models" / "grape" / "grape_disease_fixed.keras"
GRAPE_LABELS_PATH = BASE_DIR / "models" / "grape" / "grape_labels.json"

TOMATO_MODEL_PATH = BASE_DIR / "models" / "tomato" / "tomato_disease_fixed.keras"
TOMATO_LABELS_PATH = BASE_DIR / "models" / "tomato" / "tomato_labels.json"

POTATO_MODEL_PATH = BASE_DIR / "models" / "potato" / "potato_disease_fixed.keras"
POTATO_LABELS_PATH = BASE_DIR / "models" / "potato" / "potato_labels.json"

IMAGE_SIZE = (299, 299)
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}

# ✅ NOUVEAU
OPENWEATHER_API_KEY = "cdcaee248906b819b8258b25abccf009"