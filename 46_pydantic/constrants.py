from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field(gt=0)


pro = Product(name="Phone", price=99)

pro2 = Product(name="Foo", price=-2)
