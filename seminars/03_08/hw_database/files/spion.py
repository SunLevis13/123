from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import datetime

def log(update: Update, context: CallbackContext):
    file = open('log_telbase.csv','a')
    file.write(f'date: {datetime.datetime.now().date()}, User: {update.effective_user.first_name}, id: {update.effective_user.id},{update.message.text}\n')
    file.close()