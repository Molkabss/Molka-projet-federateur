import random
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from app.database.database import db
from app.core.config import SECRET_KEY, ALGORITHM
from app.crud.history_crud import get_last_prediction

router = APIRouter()
plantes_collection = db["plantes"]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=403, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")


class ChatAnswerRequest(BaseModel):
    question_type: str  # description, symptoms, treatment, prevention, causes
    plant: str = None
    disease: str = None


async def _find_disease_doc(plant: str, disease: str):
    """Search for the disease document in MongoDB"""
    plant_cap = plant.capitalize()

    doc = await plantes_collection.find_one({
        "plant": plant_cap,
        "disease": disease
    })

    if doc:
        return doc

    all_docs = await plantes_collection.find(
        {"plant": plant_cap}
    ).to_list(length=100)

    for d in all_docs:
        if disease.lower() in d["disease"].lower() or \
           d["disease"].lower() in disease.lower():
            return d

    return None


@router.get("/chatbot/start", tags=["Chatbot"])
async def start_chatbot(username: str = Depends(get_current_user)):
    """
    Starts the chatbot with the user's last prediction.
    Automatically returns questions for that prediction.
    """
    last_prediction = await get_last_prediction(username)

    if not last_prediction:
        return {
            "success": False,
            "message": "No prediction found. Please make a prediction first.",
            "questions": []
        }

    plant = last_prediction["plant_type"].capitalize()
    disease = last_prediction["disease"]
    disease_label = disease.replace("_", " ")

    doc = await _find_disease_doc(plant, disease)

    questions = [
        {"id": "description", "question": f"What is {disease_label}?"},
        {"id": "symptoms",    "question": f"What are the symptoms of {disease_label}?"},
        {"id": "treatment",   "question": f"How to treat {disease_label}?"},
        {"id": "prevention",  "question": f"How to prevent {disease_label}?"},
        {"id": "causes",      "question": f"Where does {disease_label} come from?"},
    ]

    return {
        "success": True,
        "username": username,
        "last_prediction": {
            "plant": plant,
            "disease": disease,
            "confidence": last_prediction["confidence"],
            "created_at": last_prediction["created_at"],
        },
        "data_available": doc is not None,
        "message": f"Basic info for {plant} - {disease}" if not doc else "",
        "questions": questions
    }


@router.post("/chatbot/answer", tags=["Chatbot"])
async def get_answer(
    request: ChatAnswerRequest,
    username: str = Depends(get_current_user)
):
    """
    Returns a random answer for the given question type.
    If plant/disease are not provided, uses the last prediction.
    """
    if not request.plant or not request.disease:
        last_prediction = await get_last_prediction(username)
        if not last_prediction:
            raise HTTPException(status_code=404, detail="No prediction found.")
        plant = last_prediction["plant_type"].capitalize()
        disease = last_prediction["disease"]
    else:
        plant = request.plant.capitalize()
        disease = request.disease

    doc = await _find_disease_doc(plant, disease)

    if not doc:
        raise HTTPException(
            status_code=404,
            detail=f"No information found for {plant} - {disease}"
        )

    qt = request.question_type
    disease_label = disease.replace("_", " ")

    if qt == "description":
        answer = doc.get("description", "Information not available")
        question = f"What is {disease_label}?"

    elif qt == "symptoms":
        items = doc.get("symptoms", [])
        answer = random.choice(items) if items else "Information not available"
        question = "What are the symptoms?"

    elif qt == "treatment":
        items = doc.get("treatment", [])
        answer = random.choice(items) if items else "Information not available"
        question = "How to treat?"

    elif qt == "prevention":
        items = doc.get("prevention", [])
        answer = random.choice(items) if items else "Information not available"
        question = "How to prevent?"

    elif qt == "causes":
        answer = doc.get("causes", "Information not available")
        question = "Where does this disease come from?"

    else:
        raise HTTPException(status_code=400, detail="Invalid question_type.")

    return {
        "success": True,
        "plant": plant,
        "disease": disease,
        "question_type": qt,
        "question": question,
        "answer": answer
    }


@router.get("/chatbot/diseases/{plant}", tags=["Chatbot"])
async def get_plant_diseases(plant: str):
    """Returns all available diseases for a given plant"""
    docs = await plantes_collection.find(
        {"plant": plant.capitalize()}
    ).to_list(length=100)

    if not docs:
        raise HTTPException(status_code=404, detail=f"Plant '{plant}' not found.")

    diseases = [
        {
            "disease": d["disease"],
            "description": d.get("description", "")
        }
        for d in docs
    ]

    return {
        "success": True,
        "plant": plant.capitalize(),
        "diseases": diseases,
        "total": len(diseases)
    }