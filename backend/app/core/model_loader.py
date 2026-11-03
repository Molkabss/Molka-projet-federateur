import json
import os
from pathlib import Path

os.environ["KERAS_BACKEND"] = "tensorflow"
import keras

from app.core.config import (
    MODEL_PATH, LABELS_PATH,
    APPLE_MODEL_PATH, APPLE_LABELS_PATH,
    CORN_MODEL_PATH, CORN_LABELS_PATH,
    GRAPE_MODEL_PATH, GRAPE_LABELS_PATH,
    TOMATO_MODEL_PATH, TOMATO_LABELS_PATH,
    POTATO_MODEL_PATH, POTATO_LABELS_PATH,
)


def load_model(path):
    return keras.saving.load_model(path)


class ModelManager:
    def __init__(self, model_path, labels_path):
        self.model_path = model_path
        self.labels_path = labels_path
        self.model = None
        self.labels = None

    def load(self):
        if not Path(self.model_path).exists():
            raise FileNotFoundError(f"Modèle introuvable : {self.model_path}")
        if not Path(self.labels_path).exists():
            raise FileNotFoundError(f"Labels introuvable : {self.labels_path}")
        self.model = load_model(self.model_path)
        with open(self.labels_path, "r", encoding="utf-8") as f:
            self.labels = json.load(f)

    def is_loaded(self):
        return self.model is not None and self.labels is not None


model_manager = ModelManager(MODEL_PATH, LABELS_PATH)
apple_model_manager = ModelManager(APPLE_MODEL_PATH, APPLE_LABELS_PATH)
corn_model_manager = ModelManager(CORN_MODEL_PATH, CORN_LABELS_PATH)
grape_model_manager = ModelManager(GRAPE_MODEL_PATH, GRAPE_LABELS_PATH)
tomato_model_manager = ModelManager(TOMATO_MODEL_PATH, TOMATO_LABELS_PATH)
potato_model_manager = ModelManager(POTATO_MODEL_PATH, POTATO_LABELS_PATH)