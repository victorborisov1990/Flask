from flask import Flask, render_template, request, make_response

'''
Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан 
cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия, где будет 
отображаться имя пользователя. На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён 
cookie-файл с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.
'''

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
	context = {'title': 'Аутентификация'}
	return render_template('login.html', **context)


@app.post('/login/')
def login():
	username = request.form.get('username')
	email = request.form.get('email')
	response = make_response('', 301)
	response.headers['Location'] = '/hello/'
	response.set_cookie('username', username)
	response.set_cookie('email', email)
	return response


@app.route('/hello/')
def hello():
	name = request.cookies.get('username', 'unknown')
	return render_template('hello.html', username=name)


@app.route('/logout/')
def logout():
	response = make_response(render_template('login.html'))
	response.delete_cookie('username')
	response.delete_cookie('email')
	return response


if __name__ == '__main__':
	app.run(debug=True)
