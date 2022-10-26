# диспетчер улавливает сообщения
from aiogram.dispatcher import Dispatcher 
# импорт бота и типов
from aiogram import Bot, types
# чтоб выходил в сеть
from aiogram.utils import executor
#  чтоб прочесть токен
import os 
import emoji


# бот инит
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
	print('Бот вышел в онлайн')


@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
	await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}! Я бот-помощник, который решает математические примеры. Введите выражение, например "2+2*2", и я легко с ним справлюсь!')
		

@dp.message_handler()

# асинхр метод - ЭВАЛ -наше ФСЕ
async def eval_calk(message : types.Message):
	global x
	try:
		x = eval(message.text)
 # пауза и ответ
		await message.answer(f'{message.text} = {x} 👍')
	except:
		await message.answer('Где-то Вы ошиблись, попробуйте еще раз...')
# запуск бота в сеть, (ботДиспетчер, скип - чтоб не отвечал на сообщения ОФЛАЙН, запись в бате что бот работает
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)



