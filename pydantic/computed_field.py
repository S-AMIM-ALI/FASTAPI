from pydantic import BaseModel, EmailStr, AnyUrl, field_validator, model_validator,computed_field
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
    height:float

    # ---------------- Field Validators ---------------- #

    @field_validator("email")
    @classmethod
    def validate_email_domain(cls, value: EmailStr):
        """Allow only specific email domains."""
        valid_domains = {"hdfc.com", "icici.com"}
        domain = value.split("@")[1]
        if domain not in valid_domains:
            raise ValueError("email domain must be hdfc.com or icici.com")
        return value

    @field_validator("name")
    @classmethod
    def transform_name(cls, value: str):
        """Convert name to uppercase."""
        return value.upper()

    @field_validator("age", mode="before")
    @classmethod
    def age_validate(cls, value):
        """Ensure age is between 1 and 99, accepts string or int."""
        value = int(value)
        if 0 < value < 100:
            return value
        raise ValueError("age must be between 1 and 99")

    # ---------------- Model Validator ---------------- #

    @model_validator(mode="after")
    def check_emergency_contact(self):
        """Require 'emergency' in contact if age > 60."""
        if self.age > 60 and "emergency" not in self.contact:
            raise ValueError("Patients over 60 must have an emergency contact")
        return self
    @computed_field
    @property
    def bmi(self)-> float:
        return round(self.weight/(self.height**2),2)
# ---------------- Functions ---------------- #

def insert(p1: Patient):
    print("Inserting Patient Data:")
    print(f"Name      : {p1.name}")
    print(f"Age       : {p1.age}")
    print(f"Weight    : {p1.weight}")
    print(f"Married   : {p1.married}")
    print(f"Allergies : {p1.allergies}")
    print(f"Contact   : {p1.contact}")
    print(f"Email     : {p1.email}")
    print(f"Link      : {p1.link}")
    print(f"bmi is :     {p1.bmi}")
    print("-" * 40)

def update(p1: Patient):
    print("Updating Patient Data:")
    print(f"Name : {p1.name}")
    print(f"Age  : {p1.age}")
    print("-" * 40)

# ---------------- Test Example ---------------- #

patient_info = {
    "name": "ali",
    "age": "66",
    "weight": 57.11,
    "height":1.77,
    "married": True,
    "link": "https://jobs.digsilent.de/en/jobposting/60d4ea2d55382f589065d10e39643e67cb5849ee0/apply",
    "contact": {
        "email": "abc@hdfc.com",
        "phone": "4u39247",
        "emergency": "911"  # Must exist because age > 60
    },
    "email": "abc@hdfc.com"
}

# Create Patient object
p1 = Patient(**patient_info)

# Call functions
insert(p1)
update(p1)
