from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import logging
import httpx

BOT_TOKEN = "7150910133:AAHwRMS7PnD4FO_ijpIcn5M2g-Xyw3iO0l4"
CHANNEL_ID = "@ghujbd"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def add_reaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/setMessageReaction",
                json={
                    "chat_id": update.channel_post.chat.id,
                    "message_id": update.channel_post.message_id,
                    "reaction": [{"type": "emoji", "emoji": "👍"}]
                }
            )
            if response.status_code == 200:
                logger.info("تم التفاعل بنجاح!")
            else:
                logger.error(f"فشل التفاعل: {response.text}")
    except Exception as e:
        logger.error(f"خطأ: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, add_reaction))
    app.run_polling()

if __name__ == "__main__":
    main()