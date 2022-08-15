from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,filters, MessageHandler
from bot_com import *

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a database bot, please paste name ot telephone number!")

if __name__ == '__main__':
    app = ApplicationBuilder().token('5467090782:AAGmpzB3bDp0sbcAItgUMYgxbL4mIKI5O9c').build()
    print('server start')
   
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler("hello", hi_command))
    app.add_handler(CommandHandler("name", name_command))
    app.add_handler(CommandHandler("tel", tel_command))
    app.add_handler(CommandHandler("help", help_command))
    
    app.run_polling() 

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    
if __name__ == '__main__':
    ...
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(echo_handler)

    app.run_polling()


