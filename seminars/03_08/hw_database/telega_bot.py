from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_com import *

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token('5467090782:AAGmpzB3bDp0sbcAItgUMYgxbL4mIKI5O9c').build()
print('server start')

app.add_handler(CommandHandler("hello", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))


app.run_polling()