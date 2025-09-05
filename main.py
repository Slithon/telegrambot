
import os
import telebot


TOKEN = "8212665615:AAF_OjkAL4x-Fn-GkBb-kcKtfbK2DX-AiQw"
CHAT_ID = -4670307948


fname = "C:\\Нова папка\\test.txt"
if not os.path.exists(fname):
    print("Файл не знайдено:", fname); raise SystemExit(1)

with open(fname, "r", encoding="utf-8") as f:
    text = f.read()

bot = telebot.TeleBot(TOKEN)

with open(fname, "r", encoding="utf-8") as f:
    text = f.read()
bot.send_message(CHAT_ID, text)

