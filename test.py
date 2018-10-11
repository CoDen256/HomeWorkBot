import config
from data import grouped, subject_list, full_names
from localization import local
import telebot
import time
import datetime

bot = telebot.TeleBot(config.token)
s = datetime.datetime.now()
while True:
	time.sleep(5)
	print(s)



	print((datetime.datetime.now() - s).seconds)

bot.polling(none_stop=True)
