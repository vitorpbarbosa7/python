from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Alice", age=30)

# automatic conversion
userl = User(name="Alice", age="42")

# error
user2 = User(name="Alice", age="thirsty")

