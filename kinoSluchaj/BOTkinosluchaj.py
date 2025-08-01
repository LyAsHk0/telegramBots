import asyncio 
from aiogram import Bot , Dispatcher, F
from configg import TOKEN    
from obrabotchyky import router
import sqlite3 
bot = Bot(token=TOKEN)
dp=Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
  


if __name__=="__main__":
    try:
        asyncio.run(main())     
    except KeyboardInterrupt:
        print("exit")   