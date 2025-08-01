english_messages = [ 
    "🎬 This bot helps you find random movies based on your preferences — genre, length, and more. Perfect for chilling with friends or curing boredom alone. Ready? Click the button below to start! 🍿", 
    "👥 Who are you going to watch the movie with?", 
    "🎞️ What genre of movie do you want to watch?", 
    "🎭 Here are some more genres", 
    "⏱️ How long should the movie be?", 
    "✅ I recommend watching", 
    "📝 Description", 
    "▶️ Here is the trailer", 
    "📺 Platforms where you can watch the movie"
]

russian_messages = [ 
    "🎬 Это бот для поиска случайных фильмов по твоим критериям — жанр, продолжительность и т.д. Идеально для компании или когда скучно одному. Готов? Жми на кнопку снизу! 🍿", 
    "👥 С кем ты собираешься смотреть фильм?", 
    "🎞️ Какой жанр фильма ты хочешь посмотреть?", 
    "🎭 Вот ещё жанры", 
    "⏱️ Насколько долгим должен быть фильм?", 
    "✅ Рекомендую посмотреть", 
    "📝 Описание", 
    "▶️ Вот трейлер", 
    "📺 Платформы, на которых можно посмотреть фильм"
]

ukrainian_messages = [ 
    "🎬 Це бот для пошуку випадкових фільмів за твоїми критеріями — жанр, тривалість тощо. Ідеально для компанії або коли нудно самому. Готовий? Натисни кнопку нижче! 🍿", 
    "👥 З ким ти збираєшся дивитися фільм?", 
    "🎞️ Який жанр фільму ти хочеш подивитися?", 
    "🎭 Ось ще жанри", 
    "⏱️ Наскільки довгим має бути фільм?", 
    "✅ Рекомендую глянути", 
    "📝 Опис", 
    "▶️ Ось трейлер", 
    "📺 Платформи, на яких можна подивитися фільм"
]

czeck_messages = [ 
    "🎬 Tento bot ti pomůže najít náhodný film podle tvých kritérií — žánr, délka atd. Ideální pro partu přátel nebo když se nudíš sám. Připraven? Klikni na tlačítko! 🍿", 
    "👥 S kým se na film podíváš?", 
    "🎞️ Jaký žánr filmu chceš sledovat?", 
    "🎭 Zde je několik dalších žánrů", 
    "⏱️ Jak dlouhý by měl být film?", 
    "✅ Doporučuji ke shlédnutí", 
    "📝 Popis", 
    "▶️ Zde je trailer", 
    "📺 Platformy, kde si můžete film pustit"
]

main_text = [ "" for _ in range(9) ]

error_message = [ "Please use the buttons", 
                 "Пожалуйста пользуйтесь кнопками", 
                 "Будь ласка користуйтесь кнопками", 
                 "Prosím použijte tlačítka" ]

EN_number_of_people = [ "I am alone👤", 
                     "I am with a group of friends👥", 
                     "I am with my family👨‍👩‍👧‍👦", 
                     "I am with my girlfriend/boyfriend👩‍❤️‍👨" ]

RU_number_of_people = [ "Я один👤", 
                     "Я c компаниeй друзей👥", 
                     "Я с семьей👨‍👩‍👧‍👦", 
                     "Я со своей девушкой/парнем👩‍❤️‍👨" ]

UA_number_of_people = [ "Я один👤", 
                     "Я с компанією друзів👥", 
                     "Я з сім'єю👨‍👩‍👧‍👦", 
                     "Я зі своєю дівчиною/хлопцем👩‍❤️‍👨" ]

CZ_number_of_people = [ "Jsem sám👤", 
                     "Jsem s partou přátel👥", 
                     "Jsem s rodinou👨‍👩‍👧‍👦", 
                     "Jsem se svou přítelkyní/přítelem👩‍❤️‍👨" ]

main_text_number_of_people = [ "" for _ in range(4) ]

EN_secondary_buttons = [ "Continue⏩", 
                       "Choose another movie🔄", 
                       "Start all over again↩️" ]

RU_secondary_buttons = [ "Продолжить⏩", 
                       "Выбрать другой фильм🔄", 
                       "Начать все сначала↩️" ]

UA_secondary_buttons = [ "Продовжити⏩", 
                       "Вибрати другий фільм🔄", 
                       "Почати все з початку↩️" ]

CZ_secondary_buttons = [ "Pokračovat⏩",  
                       "Vybrat jiný film🔄", 
                       "Začít znovu od začátku↩️" ]

main_secondary_buttons = [ "" for _ in range(3) ]

EN_genre = [ "Drama🎭", 
             "Comedy😂", 
             "Thriller😨", 
             "Horror👻", 
             "Sci-fi👽", 
             "Fantasy🧙‍♂️", 
             "Action💥", 
             "Adventure🧭", 
             "Melodrama😢", 
             "Detective🕵️‍♂️", 
             "Crime🔫", 
             "Military🪖", 
             "Historical📜", 
             "Biography👤", 
             "Documentary🎬", 
             "Musical🎶", 
             "Cartoon🐭", 
             "Family👨‍👩‍👧‍👦", 
             "Sports🏈", 
             "Western🤠" ]

RU_genre = [ "Драма🎭", 
             "Комедия😂", 
             "Триллер😨", 
             "Ужасы👻", 
             "Фантастика (Sci-fi)👽", 
             "Фэнтези🧙‍♂️", 
             "Боевик💥", 
             "Приключения🧭", 
             "Мелодрама😢", 
             "Детектив🕵️‍♂️", 
             "Криминал🔫", 
             "Военный🪖", 
             "Исторический📜", 
             "Биография👤", 
             "Документальный🎬", 
             "Мюзикл🎶", 
             "Мультфильм🐭", 
             "Семейный👨‍👩‍👧‍👦", 
             "Спортивный🏈", 
             "Вестерн🤠" ]

UA_genre = [ "Драма🎭", 
             "Комедія😂", 
             "Трилер😨", 
             "Жахи👻", 
             "Фантастика (Sci-fi)👽", 
             "Фентезі🧙‍♂️", 
             "Бойовик💥", 
             "Пригоди🧭", 
             "Мелодрама😢", 
             "Детектив🕵️‍♂️", 
             "Кримінал🔫", 
             "Військовий🪖", 
             "Історичний📜", 
             "Біографія👤", 
             "Документальний🎬", 
             "Мюзикл🎶", 
             "Мультфільм🐭", 
             "Сімейний👨‍👩‍👧‍👦", 
             "Спортивний🏈", 
             "Вестерн🤠" ]

CZ_genre = [ "Drama🎭", 
             "Komedie😂", 
             "Thriller😨", 
             "Horor👻", 
             "Sci-fi👽", 
             "Fantasy🧙‍♂️", 
             "Akční💥", 
             "Dobrodružný🧭", 
             "Melodrama😢", 
             "Detektivní🕵️‍♂️", 
             "Kriminální🔫", 
             "Vojenský🪖", 
             "Historický📜", 
             "Biografický👤", 
             "Dokumentární🎬", 
             "Muzikál🎶", 
             "Kreslený film🐭", 
             "Rodinný👨‍👩‍👧‍👦", 
             "Sportovní🏈", 
             "Western🤠" ]

main_text_genres = [ "" for _ in range(20) ]

EN_film_length = [ "About one hour⏳1️⃣", 
                 "About two hours⏳2️⃣", 
                 "About three hours⏳3️⃣" ]

RU_film_length = [ "Около одного часа⏳1️⃣", 
                 "Около двух часов⏳2️⃣", 
                 "Около трех часов⏳3️⃣" ]

UA_film_length = [ "Близько однієї години⏳1️⃣", 
                 "Близько двох годин⏳2️⃣", 
                 "Близько трьох годин⏳3️⃣" ]

CZ_film_length = [ "Asi hodinu⏳1️⃣", 
                 "Asi dvě hodiny⏳2️⃣", 
                 "Asi tři hodiny⏳3️⃣" ]

main_text_film_length = [ "" for _ in range(3) ]
