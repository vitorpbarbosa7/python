from pydantic import BaseModel, field_validator

class Person(BaseModel):
    name: str
    age: int

    @field_validator("age")
    def check_age(cls, v):
        if v < 0:
            raise ValueError("Age cannot be negative")
        return v

p = Person(name = "bar", age = -2)
