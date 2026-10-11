from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int 
    weight :float #kg
    height: float #mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    

    @computed_field #decorator is used to create a computed field in the model. It is used to calculate the BMI of the patient based on their weight and height.
    @property  #decorator is used to create a property in the model. It is used to calculate the BMI of the patient based on their weight and height.
    def calculate_bmi(self) -> float:
        bmi_value = round(self.weight / (self.height ** 2), 2) #bmi round mtlb ki decimal ke baad 2 digit tk rakhna hai roundoff kr rhe
        return bmi_value

       # Changed 'patient' to 'self' right here
    def update_patient_data(self):
        print(self.name)
        print(self.age)
        print(self.allergies)
        print(self.married)
        print('bmi:', self.calculate_bmi)  
        print("updated successfully") 
        print('contact details:', self.contact_details)  
 # Accessing the computed field directly


patient_info = {
    'name': 'John Doe',
    'email': 'john.doe@example.com',
    'age': 30,
    'weight': 70.5,
    'height': 1.75,
    'married': True,
    'allergies': ['Peanuts', 'Shellfish'],
    'contact_details': {'phone': '123-456-7890', 'emergency': '987-654-3210'
    
    }
}
patient1 = Patient(**patient_info)
patient1.update_patient_data()