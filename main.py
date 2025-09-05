import os
import logging
import telebot

logging.basicConfig(
    filename="C:\\Нова папка\\telegram_log.txt",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8"
)

TOKEN = "8212665615:AAF_OjkAL4x-Fn-GkBb-kcKtfbK2DX-AiQw"
CHAT_ID = -4670307948
fname = "C:\\Нова папка\\test.txt"

if not os.path.exists(fname):
    logging.error(f"Файл не знайдено: {fname}")
    raise SystemExit(1)

with open(fname, "r", encoding="utf-8") as f:
    text = f.read()

bot = telebot.TeleBot(TOKEN)

try:
    bot.send_message(CHAT_ID, text)
    logging.info("Повідомлення успішно надіслано в Telegram.")
except Exception as e:
    logging.error(f"Помилка при надсиланні повідомлення: {e}")
