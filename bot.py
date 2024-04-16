from aiogram import Bot, Dispatcher, types
import asyncio

from aiogram.filters import CommandStart

bot = Bot(token='BOT TOKEN')
dp = Dispatcher()

async def main():
    print("Bot started")
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())