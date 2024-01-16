from flask_sqlalchemy import SQLAlchemy


'''
Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" 
и кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных, 
а пароль должен быть зашифрован.
'''

db = SQLAlchemy()


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	surname = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(40), nullable=False, unique=True)
	password = db.Column(db.String(20), nullable=False)
