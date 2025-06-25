from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ البوت راهو يخدم!")

app = ApplicationBuilder().token("7899176193:AAFqHUhYpdUZY_Zv9R1O1VfKMZqdjsyDrOU").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
