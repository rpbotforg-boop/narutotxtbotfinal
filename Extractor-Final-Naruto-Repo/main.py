from config import bot_token,api_id,api_hash
from database.naruto import *
from pyrogram import Client, idle
import asyncio, logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
LOGGER.info("Live log streaming to telegram.")
plugins = dict(root="plugins")
if __name__ == "__main__":
    bot = Client(
        "Master",
        bot_token="8225118430:AAEOFTRcVH3Au1LR0iFyasUb4U5CGATuoT4",
        api_id="22447622",
        api_hash="543b62d58d3e723e766ba57a984ab65d",
        sleep_threshold=120,
        plugins=plugins,
        workers=10000,
    )
    async def main():
        await bot.start()
        bot_info = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started --->")
        await idle()
    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info("<--- Bot Stopped --->")
