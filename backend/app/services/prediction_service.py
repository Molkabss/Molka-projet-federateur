import io
import numpy as np
from PIL import Image
from keras.applications.inception_v3 import preprocess_input
from app.core.config import IMAGE_SIZE
from app.core.model_loader import (
    model_manager,
    apple_model_manager,
    corn_model_manager,
    grape_model_manager,
    tomato_model_manager,
    potato_model_manager,
)

PLANT_TO_DISEASE_MANAGER = {
    "tomato": tomato_model_manager,
    "apple": apple_model_manager,
    "corn": corn_model_manager,
    "grape": grape_model_manager,
    "potato": potato_model_manager,
}


def prepare_image(image_bytes: bytes) -> np.ndarray:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize(IMAGE_SIZE)
    img_array = np.array(image, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array


def _run_prediction(image_bytes: bytes, manager) -> dict:
    if not manager.is_loaded():
        raise RuntimeError("Le modèle n'est pas chargé.")
    processed_image = prepare_image(image_bytes)
    predictions = manager.model.predict(processed_image)[0]
    labels = manager.labels
    if isinstance(labels, list):
        class_names = labels
    elif isinstance(labels, dict):
        class_names = [labels[str(i)] for i in range(len(labels))]
    else:
        raise ValueError("Format de labels invalide.")
    predicted_index = int(np.argmax(predictions))
    predicted_class = class_names[predicted_index]
    confidence = float(predictions[predicted_index])
    top_indices = np.argsort(predictions)[::-1][:3]
    top_predictions = [
        {"label": class_names[int(i)], "confidence": float(predictions[int(i)])}
        for i in top_indices
    ]
    return {
        "success": True,
        "predicted_class": predicted_class,
        "confidence": confidence,
        "top_predictions": top_predictions,
    }


def predict_image(image_bytes: bytes) -> dict:
    return _run_prediction(image_bytes, model_manager)

def predict_apple_disease(image_bytes: bytes) -> dict:
    return _run_prediction(image_bytes, apple_model_manager)

def predict_corn_disease(image_bytes: bytes) -> dict:
    return _run_prediction(image_bytes, corn_model_manager)

def predict_grape_disease(image_bytes: bytes) -> dict:
    return _run_prediction(image_bytes, grape_model_manager)

def predict_tomato_disease(image_bytes: bytes) -> dict:
    return _run_prediction(image_bytes, tomato_model_manager)

def predict_potato_disease(image_bytes: bytes) -> dict:
    return _run_prediction(image_bytes, potato_model_manager)


def predict_auto(image_bytes: bytes) -> dict:
    plant_result = _run_prediction(image_bytes, model_manager)
    plant_type = plant_result["predicted_class"].lower()
    plant_confidence = plant_result["confidence"]

    disease_manager = None
    matched_plant = None
    for key in PLANT_TO_DISEASE_MANAGER:
        if key in plant_type:
            disease_manager = PLANT_TO_DISEASE_MANAGER[key]
            matched_plant = key
            break

    if disease_manager is None:
        return {
            "success": True,
            "plant_type": plant_type,
            "plant_confidence": plant_confidence,
            "disease": "unknown",
            "disease_confidence": 0.0,
            "top_disease_predictions": [],
            "message": f"Plant '{plant_type}' détecté mais pas de modèle de maladie disponible.",
        }

    disease_result = _run_prediction(image_bytes, disease_manager)

    return {
        "success": True,
        "plant_type": matched_plant,
        "plant_confidence": plant_confidence,
        "disease": disease_result["predicted_class"],
        "disease_confidence": disease_result["confidence"],
        "top_disease_predictions": disease_result["top_predictions"],
        "message": f"Plant '{matched_plant}' détecté avec maladie '{disease_result['predicted_class']}'.",
    }