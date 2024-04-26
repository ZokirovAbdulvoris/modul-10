# import os
# import asyncio
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.filters import CommandStart, Command
# from aiogram.fsm.context import FSMContext
# from dotenv import load_dotenv
#
# from commands import commands
# from db import db_get_all_products, db_insert_product, db_insert_user, db_insert_orders, db_get_all_orders
# from keyboards import kb, ikb, buy_ikb
# from states import ProductStatesGroup, UserRegisterStatesGroup
# from aiogram.client.session.aiohttp import AiohttpSession
#
#
# # session = AiohttpSession(proxy="http://proxy.server:3128")
#
# load_dotenv()
# BOT_TOKEN = os.getenv('BOT_TOKEN')
#
# # bot = Bot(token=BOT_TOKEN, session=session)
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()
#
#
# @dp.message(CommandStart())
# async def cmd_start(message: types.Message):
#     await message.answer("Assalomu Aleykum!\n Do'konimizga xush kelibsiz!\n"
#                          "Iltimos ro'yxatdan o'ting /registration", reply_markup=kb)
#
#
# @dp.message(Command('products'))
# async def cmd_products(message: types.Message):
#     await message.answer("Mahsulotlarni boshqarish!", reply_markup=ikb)
#
#
# @dp.message(Command('registration'))
# async def cmd_registration(message: types.Message, state: FSMContext):
#     await state.set_state(UserRegisterStatesGroup.full_name)
#     await message.answer("Ism Familiya kiriting: ")
#
#
# @dp.message(Command('orders'))
# async def cmd_orders(message: types.Message):
#     user_id = message.from_user.id
#     user, products = await db_get_all_orders(int(user_id))
#     for product in products:
#         if product not in None:
#          await message.answer_photo(text=f"{user[1]}\n"
#                                   f"Zakazlaringiz\n"
#                                   f"Nomi: {product[1]}")
#
#
# @dp.message(UserRegisterStatesGroup.full_name)
# async def user_fullname(message: types.Message, state: FSMContext):
#     await state.update_data(full_name=message.text)
#     await state.set_state(UserRegisterStatesGroup.phone)
#     await message.answer("Telefon raqamingizni yuboring: ")
#
#
# @dp.message(UserRegisterStatesGroup.phone)
# async def user_phone(message: types.Message, state: FSMContext):
#     await state.update_data(phone=message.text)
#     data = await state.get_data()
#     await db_insert_user(data["full_name"], data['phone'], message.from_user.id)
#     await message.answer("Ro'yxatdan o'tdingiz! ")
#
#
# @dp.callback_query(F.data == 'savatchaga')
# async def savatchaga(call: types.CallbackQuery):
#     product_id = int(call.message.caption.split('id:')[-1])
#     user_id = call.from_user.id
#     await db_insert_orders(product_id, user_id)
#     await call.message.answer("Mahsulot savatchaga joylandi!")
#
#
# @dp.callback_query(F.data == 'get_all_product')
# async def get_all_product(call: types.CallbackQuery):
#     product = db_get_all_products()
#     await call.message.delete()
#     if not product:
#         await call.message.answer("Mahsulot mavjud emas!")
#     for product in product:
#         await call.message.answer_photo(photo=product[3],
#                                         caption=f"Mahsulot nomi: {product[1]}\n"
#                                                 f"Mahsulot narxi: {product[2]}\n"
#                                                 f"Product id: {product[0]}",
#                                         reply_markup=buy_ikb)
#
#
# @dp.callback_query(F.data == 'add_product')
# async def add_product(call: types.CallbackQuery, state: FSMContext):
#     await state.set_state(ProductStatesGroup.title)
#     await call.message.answer("Mahsulot nomini kiriting: ")
#
#
# @dp.message(ProductStatesGroup.title)
# async def create_product_title(message: types.Message, state: FSMContext):
#     await state.update_data(title=message.text)
#     await state.set_state(ProductStatesGroup.price)
#     await message.answer("Mahsulot narxini kiriting: ")
#
#
# @dp.message(ProductStatesGroup.price)
# async def create_product_price(message: types.Message, state: FSMContext):
#     await state.update_data(price=message.text)
#     await state.set_state(ProductStatesGroup.photo)
#     await message.answer("Mahsulot rasmini yuboring: ")
#
# @dp.message(ProductStatesGroup.photo)
# async def create_product_photo(message: types.Message, state: FSMContext):
#     await state.update_data(photo=message.photo[-1].file_id)
#     data = await state.get_data()
#     await message.answer("Mahsulot yaratildi!")
#     await db_insert_product(data['title'], data['price'], data['photo'])
#
#
# async def main():
#     print("Started....")
#     await bot.set_my_commands(commands=commands)
#     await dp.start_polling(bot)
#
#
# if __name__== '__main__':
#     asyncio.run(main())