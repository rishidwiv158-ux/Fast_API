from pathlib import Path
from typing import Annotated, Literal
import json

from fastapi import FastAPI, HTTPException, Path as FastAPIPath
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field

app = FastAPI()
DATA_FILE = Path(__file__).with_name("patients.json")


class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Unique identifier for the patient", example=["P001"])]
    name: Annotated[str, Field(..., description="Name of the patient", example=["John Doe"])]
    city: Annotated[str, Field(..., description="City of the patient", example=["New York"])]
    age: Annotated[int, Field(..., gt=0, lt=150, description="Age of the patient", example=[30])]
    gender: Annotated[Literal["Male", "Female"], Field(..., description="Gender of the patient", example=["Male"])]
    height: Annotated[float, Field(..., description="Height of the patient in cm", example=[175.5])]
    weight: Annotated[float, Field(..., description="Weight of the patient in kg", example=[70.0])]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / ((self.height / 100) ** 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "underage"
        if self.bmi < 25:
            return "adult"
        return "senior"


def load_data():
    if not DATA_FILE.exists():
        return {}

    with DATA_FILE.open("r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
        except json.JSONDecodeError:
            return {}


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


@app.get("/")
def hello_world():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"message": "A Fully functional API to manage your patient records"}


@app.get("/view")
def view():
    return load_data()


@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = FastAPIPath(..., description="ID OF THE PATIENT IN THE DB", example="P001")
):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/top-patients")
def top_patients():
    data = load_data()
    return sorted(data.values(), key=lambda item: item.get("bmi", 0), reverse=True)


@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")

    data[patient.id] = patient.model_dump()
    save_data(data)
    return JSONResponse(status_code=201, content={"message": "Patient created successfully", "patient": patient.model_dump()})

