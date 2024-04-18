from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_all_products_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Barcha mahsulotlar!', callback_data='get_all_products_ikb')]

    ])
    