from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int 
    weight: float #float is used to store decimal values like 70.5, 80.2 etc
    height: float #mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

@model_validator(mode='after') #we usehere after because we want to validate the model after it has been created
def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
              raise ValueError('Patient older than 60 must have an emergency contact')
        return model

def update_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print('BMI:', patient.calculate_bmi)
        print("updated successfully")

Patient_info = {
    'name': 'John Doe',
    'email': 'john.doe@hdfc.com',
    'age': 90,
    'weight': 70.5,
    'height': 1.75,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '123-456-7890', 'emergency': '987-654-3210'}}


patient1 = Patient(**Patient_info)
update_patient_data(patient1)