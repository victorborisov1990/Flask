'''
Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание.
Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
Для этого использовать библиотеку Pydantic.
'''

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
import pandas as pd
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()

tasks = []

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class Task(BaseModel):
	id: int
	title: str
	text: str
	done: bool = False


@app.post('/add_task/', response_model=Task)
async def add_task(task: Task):
	tasks.append(task)
	return task


@app.get('/tasks/', response_class=HTMLResponse)
async def show_tasks(request: Request):
	task_table = pd.DataFrame([vars(task) for task in tasks]).to_html()
	return templates.TemplateResponse("tasks.html", {"request": request, "table": task_table})


@app.get('/tasks/{task_id}', response_class=HTMLResponse)
async def show_task(task_id: int, request: Request):
	task_table = None
	for store_task in tasks:
		if store_task.id == task_id:
			task_table = pd.DataFrame([vars(store_task)]).to_html()
	return templates.TemplateResponse("tasks.html", {"request": request, "table": task_table})


@app.put('/tasks/{id}', response_model=Task)
async def change_user(task_id: int, task: Task):
	for i, store_task in enumerate(tasks):
		if store_task.id == task_id:
			task.id = task_id
			tasks[i] = task
			return task


@app.delete('/tasks/{id}', response_class=HTMLResponse)
async def delete_user(user_id: int):
	for i, store_task in enumerate(tasks):
		if store_task.id == user_id:
			return pd.DataFrame([vars(tasks.pop(i))]).to_html()


# to start: terminal >>>  uvicorn hw5:app --reload
