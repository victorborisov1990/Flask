'''
Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение
должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию об общем времени выполнения программы.
Синхронный подход.
'''
import argparse
import asyncio
import aiohttp
import aiofiles
import os
import time


def timer(func):  # декоратор бенчмарк
	async def wrapper(*args):
		start_time = time.time()
		await func(*args)
		end_time = time.time() - start_time
		print(f'время выполнения {end_time:.2f} с')
	return wrapper


async def parse(url: str, path):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as response:
			if response.status == 200:  # если статус ОК
				name = url.replace('https://', '').split('/')[-1:-2:-1][0]
				filename = f'{path}//{name}'
				async with aiofiles.open(filename, mode='wb') as file:
					await file.write(await response.read())
				print(f'{filename} parsed successfully')
			else:
				print(f'{url} : access problems')


@timer
async def download(file_urls, path):
	tasks = []
	for url in file_urls:
		task = asyncio.ensure_future(parse(url, path))
		tasks.append(task)
	await asyncio.gather(*tasks)


if __name__ == '__main__':

	PATH = 'downloads'

	urls = ['https://w.forfun.com/fetch/a4/a4e26c34171c24e24ea51d5f6055b4ba.jpeg',
			'https://w.forfun.com/fetch/c1/c1a750c1697048cbe48198b96b414d1f.jpeg',
			'https://w.forfun.com/fetch/17/17e4e7a98ce8e7fd4e003ac4f1fe2b4a.jpeg',
			'https://w.forfun.com/fetch/64/645ec1c5343630240e1a73c7ecbd087a.jpeg',
			'https://www.fonstola.ru/images/201309/fonstola.ru_112965.jpg',
			'https://w.forfun.com/fetch/d5/d5a33a395b1864264f4e29980219598b.jpeg',
			'https://3dnews.ru/assets/external/illustrations/2023/12/30/1098222/02.jpg',
			'https://3dnews.ru/assets/external/illustrations/2023/12/30/1098222/01.jpg',
			'https://images.wallpaperscraft.ru/image/single/avtomobil_sportkar_noch_826148_1920x1080.jpg',
			'https://images.wallpaperscraft.ru/image/single/gory_pejzazh_sumerki_139582_1920x1080.jpg'
			]

	parser = argparse.ArgumentParser(description='urls to images to be downloaded')
	parser.add_argument('urls', metavar='U', type=str, nargs='*', help='input urls separated by a space')

	parsed = parser.parse_args()
	parsed_urls = parsed.urls

	if parsed_urls:
		urls = parsed_urls

	if not os.path.exists(PATH):
		os.mkdir(PATH)

	loop = asyncio.get_event_loop()
	loop.run_until_complete(download(urls, PATH))

# >>> hw4_async.py 'https://w.forfun.com/fetch/a4/a4e26c34171c24e24ea51d5f6055b4ba.jpeg' 'https://w.forfun.com/fetch/c1/c1a750c1697048cbe48198b96b414d1f.jpeg'
