# Объедините студентов в команды по 2-5 человек в сессионных залах.
#
# Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
# • Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
# • Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
# • Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
#
# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц (итого шесть моделей).
# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API (итого 15 маршрутов).
# * Чтение всех
# * Чтение одного
# * Запись
# * Изменение
# * Удаление

from hashlib import sha256
from typing import List
from fastapi import FastAPI
from starlette.responses import HTMLResponse
from base import *
from models import User, UserIn, Product, ProductIn, Order, OrderIn
from datetime import datetime

app = FastAPI()

#users #####################################################

@app.get('/users/', response_model=List[User])
async def show_users():
	query = users.select()
	return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User)
async def show_users(user_id: int):
	query = users.select().where(users.c.id == user_id)
	return await database.fetch_one(query)


@app.post('/users/', response_model=User)
async def create_user(user: UserIn):
	user.password = sha256(user.password.encode("utf-8")).hexdigest()
	query = users.insert().values(**user.model_dump())
	record_id = await database.execute(query)
	return {**user.model_dump(), "id": record_id}


@app.put('/users/{user_id}', response_class=HTMLResponse)
async def change_user(user_id: int, new_user: UserIn):
	if await database.fetch_one(users.select().where(user_id == users.c.id)):
		new_user.password = sha256(new_user.password.encode("utf-8")).hexdigest()
		query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
		await database.execute(query)
		return f'Пользователь { {**new_user.model_dump()} } с id {user_id} изменен. '
	return f'Пользователь с id {user_id} не найден'


@app.delete('/users/{user_id}', response_class=HTMLResponse)
async def delete_user(user_id: int):
	if await database.fetch_one(users.select().where(user_id == users.c.id)):
		query = users.delete().where(users.c.id == user_id)
		await database.execute(query)
		return f'Пользователь с id {user_id} удален'
	return f'Пользователь с id {user_id} не найден'

# products #####################################################

@app.get('/products/', response_model=List[Product])
async def show_products():
	query = products.select()
	return await database.fetch_all(query)


@app.get('/products/{product_id}', response_model=Product)
async def show_products(product_id: int):
	query = products.select().where(products.c.id == product_id)
	return await database.fetch_one(query)


@app.post('/products/', response_model=Product)
async def create_product(product: ProductIn):
	query = products.insert().values(**product.model_dump())
	record_id = await database.execute(query)
	return {**product.model_dump(), "id": record_id}


@app.put('/products/{product_id}', response_class=HTMLResponse)
async def change_product(product_id: int, new_product: ProductIn):
	if await database.fetch_one(products.select().where(product_id == products.c.id)):
		query = users.update().where(users.c.id == product_id).values(**new_product.model_dump())
		await database.execute(query)
		return f'Товар { {**new_product.model_dump()} } с id {product_id} изменен'
	return f'Товар с id {product_id} не найден'


@app.delete('/products/{product_id}', response_class=HTMLResponse)
async def delete_product(product_id: int):
	if await database.fetch_one(products.select().where(product_id == products.c.id)):
		query = users.delete().where(users.c.id == product_id)
		await database.execute(query)
		return f'Товар с id {product_id} удален'
	return f'Товар с id {product_id} не найден'

# orders #####################################################

@app.get('/orders/', response_model=List[Order])
async def show_orders():
	query = orders.select()
	return await database.fetch_all(query)


@app.get('/orders/{order_id}', response_model=Order)
async def show_order(order_id: int):
	query = orders.select().where(orders.c.id == order_id)
	return await database.fetch_one(query)


@app.post('/orders/', response_class=HTMLResponse)
async def create_order(order: OrderIn):
	if await database.fetch_one(users.select().where(order.user_id == users.c.id)):
		if await database.fetch_one(products.select().where(order.product_id == products.c.id)):
			order.created = datetime.now()
			print(f'time {order.created}')
			query = orders.insert().values(**order.model_dump())
			record_id = await database.execute(query)
			return f'"id": {record_id}, { {**order.model_dump()} }'
		return f'Товара с id {order.product_id} не существует'
	return f'Пользователя с id {order.user_id} не существует'


@app.put('/orders/{order_id}', response_class=HTMLResponse)
async def change_order(order_id: int, new_order: OrderIn):
	if await database.fetch_one(orders.select().where(order_id == orders.c.id)):
		if await database.fetch_one(users.select().where(new_order.user_id == users.c.id)):
			if await database.fetch_one(products.select().where(new_order.product_id == products.c.id)):
				new_order.created = datetime.now()
				query = orders.update().where(orders.c.id == order_id).values(**new_order.model_dump())
				await database.execute(query)
				return f'"id": {order_id}, { {**new_order.model_dump()} }'
			return f'Товара с id {new_order.product_id} не существует'
		return f'Пользователя с id {new_order.user_id} не существует'
	return f'Заказа с id {order_id} не существует'


@app.delete('/orders/{order_id}', response_class=HTMLResponse)
async def delete_order(order_id: int):
	if await database.fetch_one(orders.select().where(order_id == orders.c.id)):
		query = orders.delete().where(order_id == orders.c.id)
		await database.execute(query)
		return f'Заказ с id {order_id} удален'
	return f'Заказа с id {order_id} не существует'
