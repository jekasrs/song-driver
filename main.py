import os
import random
from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = ''
PATH_TO_MUSIK = '*/musik'
SPECIAL_PATH_PUTIN = '*/musik/putin.mp3'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Добро пожаловать! Этот бот предоставляет пацанский музон для дрифта и не только. \n"
    )
    await update.message.reply_text(
        "Команды: \n"
        "/random для случайной песни. \n"
        "/putin для особенной песни. \n"
        "/five для пяти случайных песен. \n"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Добро пожаловать! Этот бот предоставляет пацанский музон для дрифта и не только. \n"
    )
    await update.message.reply_text(
        "Команды: \n"
        "/random для случайной песни. \n"
        "/putin для особенной песни. \n"
        "/five для пяти случайных песен. \n"
    )

async def random_song(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    files = os.listdir(PATH_TO_MUSIK)
    if files:
        random_file = random.choice(files)
        file_path = os.path.join(PATH_TO_MUSIK, random_file)
        await update.message.reply_text("Загружаю случайную песню...")
        await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open(file_path, 'rb'))
    else:
        await update.message.reply_text("Нет доступных песен в папке.")

async def putin_song(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if os.path.exists(SPECIAL_PATH_PUTIN):
        await update.message.reply_text("Загружаю Путин песню для вас...")
        await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open(SPECIAL_PATH_PUTIN, 'rb'))
    else:
        await update.message.reply_text("Путин песня не найдена.")

async def next_five_songs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    files = os.listdir(PATH_TO_MUSIK)
    if len(files) >= 5:
        random_files = random.sample(files, 5)
        await update.message.reply_text("Загружаю пять случайных песен...")
        for random_file in random_files:
            file_path = os.path.join(PATH_TO_MUSIK, random_file)
            await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open(file_path, 'rb'))
    else:
        await update.message.reply_text("Недостаточно песен в папке для выбора пяти случайных.")

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("random", random_song))
    application.add_handler(CommandHandler("putin", putin_song))
    application.add_handler(CommandHandler("five", next_five_songs))

    application.run_polling()

if __name__ == '__main__':
    main()