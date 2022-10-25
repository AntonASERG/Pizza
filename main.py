# диспетчер улавливает сообщения
from aiogram.dispatcher import Dispatcher 
# импорт бота и типов
from aiogram import Bot, types
# чтоб выходил в сеть
from aiogram.utils import executor
#  чтоб прочесть токен
import os 


# бот инит
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)



async def on_startup(_):
	print('Бот вышел в онлайн')





# '''******************************КЛИЕНТСКАЯ ЧАСТЬ*******************************************'''
@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Приятного аппетита')
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Pizqabot')

@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'ул. Колбасная 15')


# @dp.message_handler(commands=['Меню'])
# async def pizza_menu_command(message : types.Message):
# 	for ret in cur.execute('SELECT * FROM menu').fetchall():
# 	   await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
# '''*******************************АДМИНСКАЯ ЧАСТЬ*******************************************'''

# '''*********************************ОБЩАЯ ЧАСТЬ*********************************************'''
# декоратор - когда в чат кто-то пишет
@dp.message_handler()

# асинхр метод - эхо
async def echo_send(message : types.Message):
	if message.text == 'Привет':
 # пауза и ответ
		await message.answer('И тебе привет!')

    # # пауза и ответ (с текстом на что ответ)
	# await message.reply(message.text)
    # # ответ бота - вличку (кому, text)
	# await bot.send_message(message.from_user.id, message.text)


# запуск бота в сеть, (ботДиспетчер, скип - чтоб не отвечал на сообщения ОФЛАЙН, запись в бате что бот работает)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)




