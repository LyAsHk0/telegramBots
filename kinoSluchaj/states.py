from aiogram.fsm.state import State , StatesGroup


class choose_movie(StatesGroup):
    number_of_people=State()
    genre=State()
    film_length=State()
    state_after_selecting_movie=State()