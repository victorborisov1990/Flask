# from sqlalchemy.orm import relationship
from sqlalchemy import Column, Table, Integer, String, Float, DateTime, MetaData, create_engine, ForeignKey
from databases import Database

metadata = MetaData()

DATABASE_URL = 'sqlite:///market.db'

database = Database(DATABASE_URL)

users = Table(
	"users",
	metadata,
	Column("id", Integer, primary_key=True),
	Column("name", String(40)),
	Column("surname", String(40)),
	Column("email", String(120)),
	Column("password", String(256)),
)

products = Table(
	"products",
	metadata,
	Column("id", Integer, primary_key=True),
	Column("name", String(40)),
	Column("description", String(512)),
	Column("price", Float)
)

orders = Table(
	"orders",
	metadata,
	Column("id", Integer, primary_key=True),
	Column("user_id", Integer, ForeignKey("users.id")),
	Column("product_id", Integer, ForeignKey("products.id")),
	Column("created", DateTime)
)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)
