from pydantic import BaseModel, EmailStr, AnyUrl, field_validator
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    link: AnyUrl
    married: bool
    allergies: Optional[List[str]] = None
    contact: Dict[str, str]
    email: EmailStr

    @field_validator("email")
    @classmethod
    def validate_email_domain(cls, value: EmailStr):
        valid_domains = {"hdfc.com", "icici.com"}
        domain = value.split("@")[1]
        if domain not in valid_domains:
            raise ValueError("email domain must be hdfc.com or icici.com")
        return value

    @field_validator("name")
    @classmethod
    def transform_name(cls, value: str):
        return value.upper()

    @field_validator("age", mode="before")
    @classmethod
    def age_validate(cls, value):
        value = int(value)
        if 0 < value < 100:
            return value
        raise ValueError("age must be between 1 and 99")

def insert(p1: Patient):
    print(p1.name)
    print(p1.age)
    print(p1.weight)
    print(p1.married)
    print(p1.allergies)
    print(p1.contact)
    print(p1.email)
    print(p1.link)

def update(p1: Patient):
    print(p1.name)
    print(p1.age)

patient_info = {
    "name": "ali",
    "age": "30",
    "weight": 57.11,
    "married": True,
    "link": "https://jobs.digsilent.de/en/jobposting/60d4ea2d55382f589065d10e39643e67cb5849ee0/apply",
    "contact": {"email": "abc@hdfc.com", "phone": "4u39247"},
    "email": "abc@hdfc.com"
}

p1 = Patient(**patient_info)
insert(p1)
update(p1)
