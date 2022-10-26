# диспетчер улавливает сообщения
from re import X
from aiogram.dispatcher import Dispatcher 
# импорт бота и типов
from aiogram import Bot, types
# чтоб выходил в сеть
from aiogram.utils import executor
#  чтоб прочесть токен
import os 
import random

# бот инит
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
player1 = ''
player2 = ''
count = 150
winner = player1
i = 29
lot = 0


async def on_startup(_):
	print('Бот вышел в онлайн')


@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
	await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}, На столе лежит 150 конфет. Играют два игрока, делая ход друг после друга. Первый ход определяется жеребьёвкой /lot. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
		

@dp.message_handler(commands=['lot'])
async def command_lot(message : types.Message):
		
	global player1 
	global player2 
	global lot
	global winner
	global count

	player1 = (f'{message.from_user.first_name}')
	player2 = ('МЕГАБОТ')
	lot = random.randint (1, 2)

	if lot == 2:
		await bot.send_message(message.from_user.id, f'Первым ходит - {player1}')
		winner = player1
	else:
		await bot.send_message(message.from_user.id, f'Первым ходит - {player2}')
		await bot.send_message(message.from_user.id, '5')
		count = count - 5
		await bot.send_message(message.from_user.id, f'Остаток - {count}')
		winner = player2

# ПРОБЛЕМА ТУТ!!!!!!!!!!!!!!!
@dp.message_handler()
async def echo_send(message : types.Message):
	while count > 0:
		msg = str(message.text)
		print (msg)
		items = msg.split()
		x = int (items[0])
		# ПРОБЛЕМА ТУТ!!!!!!!!!=====================================
		count = int(count - x)
		await bot.send_message(message.from_user.id, f'Остаток - {count}')
		winner = player1
		# ================================================
		if count > 0:
			if count%i == 0:
				steep2 = random.randint (1, 28)
			else:
				steep2 = count%i
			count = count - steep2
			await bot.send_message(message.from_user.id, f'{steep2}')
			await bot.send_message(message.from_user.id, f'Остаток - {count}')
			winner = player2
		else:
			winner = player1
	await bot.send_message(message.from_user.id, f'ПОБЕДИТЕЛЬ - {winner}!!!!')

    


# запуск бота в сеть, (ботДиспетчер, скип - чтоб не отвечал на сообщения ОФЛАЙН, запись в бате что бот работает
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
