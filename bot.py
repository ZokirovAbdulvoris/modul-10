from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.client.session.aiohttp import AiohttpSession

from aiogram.filters import CommandStart

session = AiohttpSession(proxy="http://proxy.server:3128")

bot = Bot(token='BOT TOKEN', session=session)
dp = Dispatcher()


async def main():
    print("Bot started")
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())