from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
import text_for_bot as tfb
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


select_language=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="English🇺🇸", callback_data="en"), InlineKeyboardButton(text="Русский🇷🇺", callback_data="ru"), InlineKeyboardButton(text="Українська🇺🇦", callback_data="ua"),InlineKeyboardButton(text="Čeština🇨🇿", callback_data="cz")]])


async def after_select_language(_keyboard):
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text=_keyboard))
    return keyboard.adjust(1).as_markup(resize_keyboard=True)

async def generate_the_movie_again(keyboards):
    keyboard = ReplyKeyboardBuilder()
    for _keyboard in keyboards:
        keyboard.add(KeyboardButton(text=_keyboard))
    return keyboard.adjust(2).as_markup(resize_keyboard=True)

async def get_coosing_number_of_people_keyboard(knopky):
    keyboard = ReplyKeyboardBuilder()
    for knopka in knopky:
        keyboard.add(KeyboardButton(text=knopka))
    return keyboard.adjust(4).as_markup(resize_keyboard=True)

async def get_genre_first_page(knopky):
    index =0
    
    keyboard = ReplyKeyboardBuilder()
   
    for knopka in knopky:
        keyboard.add(KeyboardButton(text=knopka))
        index +=1
        if index==8:
            break
    keyboard.add(KeyboardButton(text="⬅️"),KeyboardButton(text="➡️"))
    return keyboard.adjust(4).as_markup(resize_keyboard=True)


async def get_genre_second_page(knopky):

    keyboard = ReplyKeyboardBuilder()
    index=0
    for knopka in knopky[8:]:
        keyboard.add(KeyboardButton(text=knopka))
        index +=1
        if index==8:
            break
    keyboard.add(KeyboardButton(text="⬅️"),KeyboardButton(text="➡️"))
    return keyboard.adjust(4).as_markup(resize_keyboard=True)


async def get_genre_third_page(knopky):

    keyboard = ReplyKeyboardBuilder()
    index=0
    for knopka in knopky[16:]:
        keyboard.add(KeyboardButton(text=knopka))
        index +=1
        if index==8:
            break
    keyboard.add(KeyboardButton(text="⬅️"),KeyboardButton(text="➡️"))
    return keyboard.adjust(4).as_markup(resize_keyboard=True)


async def get_film_length(knopky):
    keyboard = ReplyKeyboardBuilder()
    for knopka in knopky:
        keyboard.add(KeyboardButton(text=knopka))
    return keyboard.adjust(3).as_markup(resize_keyboard=True)
