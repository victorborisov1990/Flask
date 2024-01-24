# '''
# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль"
# и кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных,
# а пароль должен быть зашифрован.
# '''

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash
# from werkzeug.security import check_password_hash

from models import db, User
from forms import Registration

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.secret_key = b'7435220954b80e033873947b65db8d28fd9d5d8b3f90ea952a73f60fd76c2366'
csrf = CSRFProtect(app)
# csrf.init_app(app)

db.init_app(app)


@app.cli.command('create')
def create():
	db.create_all()
	print('CREATION COMPLETE')


@app.route('/', methods=['GET', 'POST'])  # 
def index():
	form = Registration()
	# if form.validate_on_submit():  # если нажата кнопка (она может быть нажата, только если все поля проверены)
	# этот вариант выдавал ошибку "flask method not allowed"
	if request.method == 'POST' and form.validate():
		user = User(name=form.name.data, surname=form.surname.data, email=form.email.data,
					password=generate_password_hash(form.password.data))
		db.session.add(user)
		db.session.commit()
		flash('Пользователь успешно зарегистрирован!')
		return redirect(url_for('index'))  # после сохранения данных из формы переходим на стартовую с чистой формой
	for field in form:
		for error in field.errors:
			flash(error)
	return render_template('index.html', form=form)  # если не нажата (get запрос) - передаем пустую форму


if __name__ == '__main__':
	app.run(debug=True)
