import logging
from aiogram import Bot, Dispatcher, executor, types
import parse
import trans

logging.basicConfig(level=logging.INFO)

bot = Bot(token="1795620507:AAE7K35UW0HbFHqH0-4IuuxbaRrNythAwy4")
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
		if(message.text[:len("кинь картинку")].lower() == "кинь картинку" or (message.text[0:len("cкинь картинку")].lower() == "скинь картинку")):
			await message.reply(parse.search_google_img(message.text[len("кинь картинку ")+message.text.find("кинь картинку "):]), reply=True)
		elif(message.text[:len("що таке")].lower() == "що таке"):
			await message.reply(parse.parse_wiki(message.text[len("що таке"):]))
		elif(len(message.text)>10 and trans.test(message.text) != 'uk'):
			await message.reply(trans.do_trans(message.text,'uk'))
		
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
