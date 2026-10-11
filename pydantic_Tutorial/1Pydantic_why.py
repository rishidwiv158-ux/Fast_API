from pydantic import BaseModel,EmailStr, AnyUrl, Field  #step 1 isse hmesa krnge
from typing import List,Dict,Optional, Annotated

class Patient(BaseModel): #pydantic model class
    
    name: Annotated[str, Field(max_length=50, title='Name of the Patient', description='The name of the patient 50 char',example='John Doe')] # Field means name ka max length 50 hoga
    email: EmailStr # yha ham field ka use krke name  metadata btya constraint v lgya and data validation
    linkedin_url: AnyUrl
    age: int=Field(gt=0, lt=120) #gt means greater than 0 and lt means less than 120 its possible to use Field for validation
    weight: float=Field(gt=0)
    married: Annotated[bool, Field(default=None, description='Whether the patient is married')] # yha ham custom description btya h and default value none h and married ka data type bool h
    allergies: Annotated[Optional[List[str]], Field(max_length=5)] = None  # optional me rakhma hoto kuch ue optional none ,  list me hoga allergiies but uska har item list m hoga
    contact_details: Dict[str, str] # Field() ka mtlb max 5 se jada koui enter ni kr skte

def update_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print("updated successfully")


patient_info = {'name' :'John Doe','email':'abc@gmail.com','linkedin_url':'http://linkedin.com/1322' ,'age' : '30' ,'weight': 75.2, 'married': True, 
 'contact_details':{'phone':'6388968998'}}


patient1 = Patient(**patient_info)

update_patient_data(patient1)
