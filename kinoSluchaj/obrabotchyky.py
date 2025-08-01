from aiogram import F , Router
from aiogram.filters import CommandStart , Command
from aiogram.types import Message, CallbackQuery, LinkPreviewOptions
import keyboards as kb
from kinoSluchaj.states import choose_movie
from aiogram.fsm.context import FSMContext
import text_for_bot as tfb
import sqlite3 
import random

conn= sqlite3.connect("data_base_of_movies.db")
cur = conn.cursor()

router=Router()

page_of_genre1=None
page_of_genre2=None
page_of_genre3=None
local_genres_text=[]
main_error_message=None
cur.execute("SELECT * FROM movies")
data_of_movies=cur.fetchall()


@router.message(CommandStart())#1st step: launching the bot
async def start(message: Message):
    await message.answer("Select your language", reply_markup=kb.select_language)
    
    
@router.callback_query(F.data == "en")# 2nd step: select language
async def start_en(callback: CallbackQuery, state: FSMContext):
    global main_error_message
    await callback.message.delete()
    tfb.mainText=tfb.english_messages
    tfb.main_Text_number_of_people=tfb.EN_number_of_people
    tfb.main_text_genres=tfb.EN_genre
    tfb.main_Text_film_length=tfb.EN_film_length
    tfb.main_secondary_buttons=tfb.EN_secondary_buttons
    main_error_message=tfb.error_message[0]
    await state.update_data(language_of_title_and_description=[1,2])
    await callback.message.answer(text=tfb.mainText[0], reply_markup= await kb.after_select_language(tfb.main_secondary_buttons[0]))
    await callback.answer()
    await state.set_state(choose_movie.number_of_people) 
    
    
@router.callback_query(F.data == "ru")# 2nd step: select language
async def start_ru(callback: CallbackQuery, state: FSMContext):
    global main_error_message
    await callback.message.delete()
    tfb.mainText=tfb.russian_messages
    tfb.main_Text_number_of_people=tfb.RU_number_of_people
    tfb.main_text_genres=tfb.RU_genre
    tfb.main_Text_film_length=tfb.RU_film_length
    tfb.main_secondary_buttons=tfb.RU_secondary_buttons
    main_error_message=tfb.error_message[1]
    await state.update_data(language_of_title_and_description=[3,4])
    await callback.message.answer(text=tfb.mainText[0], reply_markup= await kb.after_select_language(tfb.main_secondary_buttons[0]))
    await callback.answer()
    await state.set_state(choose_movie.number_of_people) 
    
    
@router.callback_query(F.data == "ua")# 2nd step: select language
async def start_ua(callback: CallbackQuery, state: FSMContext):
    global main_error_message
    await callback.message.delete()
    tfb.mainText=tfb.ukrainian_messages
    tfb.main_Text_number_of_people=tfb.UA_number_of_people
    tfb.main_text_genres=tfb.UA_genre
    tfb.main_Text_film_length=tfb.UA_film_length
    tfb.main_secondary_buttons=tfb.UA_secondary_buttons
    main_error_message=tfb.error_message[2]
    await state.update_data(language_of_title_and_description=[5,6])
    await callback.message.answer(text=tfb.mainText[0], reply_markup= await kb.after_select_language(tfb.main_secondary_buttons[0]))
    await callback.answer()
    await state.set_state(choose_movie.number_of_people) 
    
    
@router.callback_query(F.data == "cz")# 2nd step: select language
async def start_cz(callback: CallbackQuery, state: FSMContext):
    global main_error_message
    await callback.message.delete()
    tfb.mainText=tfb.czeck_messages
    tfb.main_Text_number_of_people=tfb.CZ_number_of_people
    tfb.main_text_genres=tfb.CZ_genre
    tfb.main_Text_film_length=tfb.CZ_film_length
    tfb.main_secondary_buttons=tfb.CZ_secondary_buttons
    main_error_message=tfb.error_message[3]
    await state.update_data(language_of_title_and_description=[7,8])
    await callback.message.answer(text=tfb.mainText[0], reply_markup= await kb.after_select_language(tfb.main_secondary_buttons[0]))
    await callback.answer()
    await state.set_state(choose_movie.number_of_people) 
    
    
@router.message(choose_movie.number_of_people)#3rd step: select the number of people
async def reply_for_continueButton(message: Message, state: FSMContext):
    await state.set_state(choose_movie.genre)
    await message.answer(
        text=tfb.mainText[1],
        reply_markup=await kb.get_coosing_number_of_people_keyboard(tfb.main_Text_number_of_people))


@router.message(F.text == "➡️")#auxiliary function for switching between genres !!! It must be here because for some reason it doesn't work correctly in other places in the code. !!!
async def forward_arrow(message: Message, state: FSMContext):
    
    await message.delete()
    data = await state.get_data()
    genres = data.get("local_genres_text", [])
    page = data.get("genre_page", 1)
    if page == 1 and len(genres) > 8:
        await message.answer(text=tfb.mainText[3], reply_markup=await kb.get_genre_second_page(genres))
        await state.update_data(genre_page=2)
    elif page == 2 and len(genres) > 16:
        await message.answer(text=tfb.mainText[3], reply_markup=await kb.get_genre_third_page(genres))
        await state.update_data(genre_page=3)


@router.message(F.text == "⬅️")#auxiliary function for switching between genres !!! It must be here because for some reason it doesn't work correctly in other places in the code. !!!
async def back_arrow(message: Message, state: FSMContext):
    
    await message.delete()
    data = await state.get_data()
    genres = data.get("local_genres_text", [])
    page = data.get("genre_page", 1)
    if page == 2 and len(genres) > 8:
        await message.answer(text=tfb.mainText[3], reply_markup=await kb.get_genre_first_page(genres))
        await state.update_data(genre_page=1)
    elif page == 3 and len(genres) > 16:
        await message.answer(text=tfb.mainText[3], reply_markup=await kb.get_genre_second_page(genres))
        await state.update_data(genre_page=2)


@router.message(lambda message: message.text in tfb.main_text_genres)# It should work after the next function, but it must be before it in order to work correctly, I dont know why ¯\_(ツ)_/¯
async def set_genre(message: Message, state: FSMContext):
    for i in range(20):
        if message.text == tfb.main_text_genres[i]:
            genre = tfb.EN_genre[i]
            break
    genre = genre[:-1]
    await state.update_data(genre=genre)
    await state.set_state(choose_movie.film_length)  
    await message.answer(text=tfb.mainText[4], reply_markup= await kb.get_film_length(tfb.main_Text_film_length))
      
        
@router.message(choose_movie.genre)#4th step: select the movie genre
async def number_of_people(message: Message, state: FSMContext):
    if message.text == tfb.main_Text_number_of_people[0]:
        genres = tfb.main_text_genres
    elif message.text == tfb.main_Text_number_of_people[1]:
        exclude = [tfb.main_text_genres[0], tfb.main_text_genres[8], tfb.main_text_genres[12], tfb.main_text_genres[13], tfb.main_text_genres[14], tfb.main_text_genres[15], tfb.main_text_genres[16], tfb.main_text_genres[17]]
        genres = [g for g in tfb.main_text_genres if g not in exclude]
    elif message.text == tfb.main_Text_number_of_people[2]:
        exclude = [tfb.main_text_genres[0], tfb.main_text_genres[2], tfb.main_text_genres[3], tfb.main_text_genres[4], tfb.main_text_genres[6], tfb.main_text_genres[9], tfb.main_text_genres[10], tfb.main_text_genres[11], tfb.main_text_genres[12], tfb.main_text_genres[13], tfb.main_text_genres[14], tfb.main_text_genres[19]]
        genres = [g for g in tfb.main_text_genres if g not in exclude]
    elif message.text == tfb.main_Text_number_of_people[3]:
        exclude = [tfb.main_text_genres[11], tfb.main_text_genres[13], tfb.main_text_genres[14], tfb.main_text_genres[19]]
        genres = [g for g in tfb.main_text_genres if g not in exclude]
    else:
        await message.answer(text=main_error_message)
        return

    await state.update_data(local_genres_text=genres, genre_page=1)
    await message.answer(text=tfb.mainText[2], reply_markup=await kb.get_genre_first_page(genres))
    
    
@router.message(choose_movie.film_length)#5th step: select the movie length
async def chose_film_lenght_and_get_the_movie(message: Message, state: FSMContext):
    
    length=None
    error_indicator=0
    for i in range(3):
        if message.text == tfb.main_Text_film_length[i]:
            length=i+1
            break
        else :
            error_indicator+=1
            if error_indicator == 3:
                await message.answer(text=main_error_message)
                return
        
    await state.update_data(film_length=length) 
    await get_random_movie(message, state)
    await state.set_state(choose_movie.state_after_selecting_movie)


@router.message(choose_movie.state_after_selecting_movie)#6th step: Generation of a new film, or return to step 3
async def buttons_for_generate_new_movies(message: Message, state: FSMContext):
    if message.text == tfb.main_secondary_buttons[1]:
        await get_random_movie(message, state)
    if message.text == tfb.main_secondary_buttons[2]:
        await reply_for_continueButton(message, state)
    else:
        if  message.text != tfb.main_secondary_buttons[1]:
            await message.answer(text=main_error_message)
            return
        

async def get_random_movie(message: Message, state: FSMContext):#auxiliary function for step 5 and 6
    choosed_movies = []
    data = await state.get_data()
    for el in data_of_movies:
        choosed_genres = el[10].strip().split(",")
        if data['genre'] in choosed_genres and int(el[11]) == int(data["film_length"]):
            choosed_movies.append(el)
    await state.update_data(choosed_movie=choosed_movies)
    data2 = await state.get_data()
    final_movie = random.choice(data2["choosed_movie"])

    await state.update_data(final_movie=final_movie )
    data =await state.get_data()
    await message.answer(text=f"{tfb.mainText[5]} \"{data["final_movie"][data["language_of_title_and_description"][0]]}\"")
    await message.answer(text=f"""{tfb.mainText[6]}
{data["final_movie"][data["language_of_title_and_description"][1]]}""")
    await message.answer(text=f"""{tfb.mainText[7]}
{data["final_movie"][9]}""")
    await message.answer(text=f"""{tfb.mainText[8]}
{data["final_movie"][12]}""", link_preview_options=LinkPreviewOptions(is_disabled=True), reply_markup= await kb.generate_the_movie_again(tfb.main_secondary_buttons[1:3]))    
