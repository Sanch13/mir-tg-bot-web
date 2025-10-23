import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramNetworkError, TelegramUnauthorizedError

from src.config import settings
from src.infrastructure.db import init_db_engine
from src.presentation.api.handlers.start import router as start_router

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)

logger = logging.getLogger(__name__)


async def main():
    init_db_engine()
    try:
        logger.info("=== BOT STARTING ===")

        token = settings.tg.API_TELEGRAM_TOKEN.get_secret_value()

        logger.info("Initializing bot...")
        bot = Bot(token=token)
        dp = Dispatcher()

        logger.info("Setting up routers...")
        dp.include_router(start_router)

        logger.info("=== STARTING POLLING ===")
        await dp.start_polling(bot)

    except TelegramUnauthorizedError as e:
        logger.exception(f"❌ INVALID BOT TOKEN: {e}")
        logger.exception("Please check your API_TELEGRAM_TOKEN")
    except TelegramNetworkError as e:
        logger.exception(f"🌐 NETWORK ERROR: {e}")
    except Exception as e:
        logger.exception(f"💥 UNEXPECTED ERROR: {e}")
    finally:
        logger.info("=== BOT STOPPED ===")
        if "bot" in locals():
            await bot.session.close()


if __name__ == "__main__":
    try:
        logger.info("Application starting...")
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user (KeyboardInterrupt)")
    except Exception as e:
        logger.exception(f"Fatal error in main: {e}")
