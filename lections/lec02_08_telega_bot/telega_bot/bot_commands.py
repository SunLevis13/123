from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from spy import *
import datetime

async def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def help_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/help')

async def time_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 122 45324
    x= int(items[1])
    y= int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')