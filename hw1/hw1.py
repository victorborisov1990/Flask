from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    context = {'title': 'Магазин. Главная'}
    return render_template('index.html', **context)


@app.route('/clothes/')
def clothes():
	clothes_list = [
		{'title': 'Куртка',
		 'text': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Totam laudantium sed  voluptate necessitatibus? 
			 Fugit ipsam dolorem doloribus ratione laborum ut  aliquam delectus quos. Provident corrupti placeat quibusdam, 
			 temporibus fugit  corporis quis officia beatae maiores cum sapiente veritatis minus, voluptatem'''},
		{'title': 'Свитер', 'text': '''Esse numquam hic natus rerum nisi ipsum earum
		  suscipit neque distinctio voluptatem adipisci optio sit, quibusdam saepe
		  veritatis doloremque enim incidunt in eligendi corrupti quo illum qui! Magnam
		  rerum ea, sint veniam, quo voluptatum iusto ab, earum eaque velit accusantium
		  aliquid! Harum maiores rerum mollitia'''},
		{'title': 'Штаны',
		 'text': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Totam laudantium sed  voluptate necessitatibus? 
			 Fugit ipsam dolorem doloribus ratione laborum ut  aliquam delectus quos. Provident corrupti placeat quibusdam, 
			 temporibus fugit  corporis quis officia beatae maiores cum sapiente veritatis minus, voluptatem'''},
		{'title': 'Пиджак', 'text': ''' Necessitatibus iusto nihil, quam
		  asperiores esse recusandae. Eaque alias facere fugiat voluptates.'''}
	]
	context = {'title': 'Одежда',
				'items': clothes_list}
	return render_template('clothes.html', **context)  


@app.route('/shoes/')
def shoes():
	shoes_list = [
		{'title': 'Сапоги',
		 'text': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Totam laudantium sed  voluptate necessitatibus? 
			 Fugit ipsam dolorem doloribus ratione laborum ut  aliquam delectus quos. Provident corrupti placeat quibusdam, 
			 temporibus fugit  corporis quis officia beatae maiores cum sapiente veritatis minus, voluptatem'''},
		{'title': 'Ботинки', 'text': '''Esse numquam hic natus rerum nisi ipsum earum
		  suscipit neque distinctio voluptatem adipisci optio sit, quibusdam saepe
		  veritatis doloremque enim incidunt in eligendi corrupti quo illum qui! Magnam
		  rerum ea, sint veniam, quo voluptatum iusto ab, earum eaque velit accusantium
		  aliquid! Harum maiores rerum mollitia'''},
		{'title': 'Кроссовки',
		 'text': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Totam laudantium sed  voluptate necessitatibus? 
			 Fugit ipsam dolorem doloribus ratione laborum ut  aliquam delectus quos. Provident corrupti placeat quibusdam, 
			 temporibus fugit  corporis quis officia beatae maiores cum sapiente veritatis minus, voluptatem'''},
		{'title': 'Тапки', 'text': ''' Necessitatibus iusto nihil, quam
		  asperiores esse recusandae. Eaque alias facere fugiat voluptates.'''}
	]
	context = {'title': 'Обувь',
			   'items': shoes_list}
	return render_template('shoes.html', **context)


@app.route('/phones/')
def phones():
	phones_list = [
		{'title': 'Смартфон Samsung Galaxy A53 5G 8/256 ГБ',
		 'text': '''Samsung Galaxy A53 SM-A536 - смартфон с привлекательным дизайном синего цвета. Диагональ 6.5 дюймового 
	            AMOLED-экрана разрешением 2400х1080 позволит наслаждаться качественными изображениями и видео. 
	            Устройство обладает 8-ядерным процессором Exynos 1280. Поддерживаются стандарты связи 2G, 3G, 4G (LTE),
	                5G. На экране есть сканер отпечатков пальцев. Смартфон обладает основной четырехкамерной камерой 
	                на 64+12+5+5 Мп, слот для microSD поддерживает максимальный объем карты памяти в 1024 Гб. 
	                Преимуществом данной модели является модуль бесконтактной оплаты и аккумулятор на 5000 мАч, 
	                которого хватает на несколько дней работы.'''},
		{'title': 'Смартфон HONOR 50 Lite 6/128 ГБ',
		 'text': '''Смартфон Honor 50 Lite 128 ГБ выделяется привлекательным оформлением в корпусе синего цвета и технологичностью 
			 высокого класса. Процессор Snapdragon 662 игрового уровня в сочетании с 6 ГБ оперативной памяти обеспечивает высокое быстродействие
			  системы при выполнении различных задач. Память 128 ГБ может быть увеличена с помощью карты microSD. На экране 6.67 дюйма
			   IPS отображается реалистичная картинка. Для комфортного использования реализованы функции автоматической настройки 
			   цветовой температуры и регулировки уровня яркости.На тыловой стороне расположена камера 64+8+2+2 Мп с
			    фазовым автофокусом и вспышкой'''},
		{'title': 'Смартфон Samsung Galaxy S23 8/256 ГБ',
		 'text': '''Galaxy S23 выделяется тем, что переопределяет основные элементы мобильного 
	                    интерфейса премиум-класса. Переосмысленный для разных увлечений и стилей жизни – от создателей 
	                    до сотрудников – Galaxy S23 предлагает свободу выбора подходящего устройства для вашей жизни, 
	                    чтобы развить повседневные увлечения. Galaxy S23 имеет культовый дизайн задней камеры с чистыми, 
	                    линейными и плавающими объективами, создающими единство в серии S. Точно запечатлейте красоту вашего 
	                    мира с помощью новой универсальной основной камеры на 50 МП и фронтальной камеры на 12 МП, 
	                    дополненной технологией Super HDR'''}
	]
	context = {'title': 'Смартфоны',
			   'items': phones_list}
	return render_template('phones.html', **context)


if __name__ == '__main__':
	app.run(debug=True)