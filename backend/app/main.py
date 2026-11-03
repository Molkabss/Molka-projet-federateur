from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.auth_routes import router as auth_router
from app.api.routes.router import api_router
from app.core.model_loader import (
    model_manager,
    apple_model_manager,
    corn_model_manager,
    grape_model_manager,
    tomato_model_manager,
    potato_model_manager,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    model_manager.load()
    print(" Modèle plante chargé avec succès")

    apple_model_manager.load()
    print(" Modèle Apple chargé avec succès")

    corn_model_manager.load()
    print(" Modèle Corn chargé avec succès")

    grape_model_manager.load()
    print(" Modèle Grape chargé avec succès")

    tomato_model_manager.load()
    print(" Modèle Tomato chargé avec succès")

    potato_model_manager.load()
    print(" Modèle Potato chargé avec succès")


app.include_router(auth_router)
app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {"status": "ok"}