from typing import Dict 

from pydantic import BaseModel, EmailStr, field_validator


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: bool
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def validate_email(cls, value: str) -> str:
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('not a valid email domain')
        return value

    def update_patient_data(self):
        print(self.name)
        print(self.age)
        print(self.allergies)
        print(self.married)
        print("updated successfully")


patient_info = {
    'name': 'John Doe',
    'email': 'john.doe@hdfc.com',
    'age': 30,
    'weight': 70.5,
    'married': True,
    'allergies': False,
    'contact_details': {'phone': '123-456-7890'}
}

patient1 = Patient(**patient_info)
patient1.update_patient_data()

