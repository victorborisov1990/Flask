from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
	id: int
	name: str = Field(max_length=40)
	surname: str = Field(max_length=40)
	email: str = Field(max_length=120)
	password: str = Field(max_length=256)

class UserIn(BaseModel):
	name: str = Field(max_length=40)
	surname: str = Field(max_length=40)
	email: str = Field(max_length=120)
	password: str = Field(max_length=256)

class Product(BaseModel):
	id: int
	name: str = Field(max_length=40)
	description: str = Field(max_length=512)
	price: float

class ProductIn(BaseModel):
	name: str = Field(max_length=40)
	description: str = Field(max_length=512)
	price: float

class Order(BaseModel):
	id: int
	user_id: int
	product_id: int
	created: datetime

class OrderIn(BaseModel):
	user_id: int
	product_id: int
	created: datetime
