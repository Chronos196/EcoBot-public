from bot import bot, types


##### ГЛАВНОЕ МЕНЮ
MENU_BUT1_TEXT = 'Об экологии 🌱'
MENU_BUT2_TEXT = 'Для чего этот бот ❓'
MENU_BUT3_TEXT = 'О боте 🔧'
MENU_BUT4_TEXT = 'Помощь 🆘'
menu_but1 = types.KeyboardButton(MENU_BUT1_TEXT)
menu_but2 = types.KeyboardButton(MENU_BUT2_TEXT)
menu_but3 = types.KeyboardButton(MENU_BUT3_TEXT)
menu_but4 = types.KeyboardButton(MENU_BUT4_TEXT)
menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
menu_keyboard.add(menu_but1, menu_but2)
menu_keyboard.row_width = 2
menu_keyboard.add(menu_but3, menu_but4)


##### КНОПКА НАЗАД В ГЛАВНОЕ МЕНЮ
BACK_TO_MENU_BUT1_TEXT = 'Обратно в меню ↩'
back_to_menu_but1 = types.KeyboardButton(BACK_TO_MENU_BUT1_TEXT)
back_to_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_to_menu_keyboard.add(back_to_menu_but1)


##### МЕНЮ ОБ ЭКОЛОГИИ
ECOLOGY_BUT1_TEXT = 'Экологическая культура 🏡'
ECOLOGY_BUT2_TEXT = 'Статьи 🍃'
ECOLOGY_BUT3_TEXT = 'Словарь 📖'
ECOLOGY_BUT4_TEXT = BACK_TO_MENU_BUT1_TEXT
ecology_but1 = types.KeyboardButton(ECOLOGY_BUT1_TEXT)
ecology_but2 = types.KeyboardButton(ECOLOGY_BUT2_TEXT)
ecology_but3 = types.KeyboardButton(ECOLOGY_BUT3_TEXT)
ecology_but4 = types.KeyboardButton(ECOLOGY_BUT4_TEXT)
ecology_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
ecology_keyboard.add(ecology_but1)
ecology_keyboard.row_width = 2
ecology_keyboard.add(ecology_but2, ecology_but3)
ecology_keyboard.row_width = 1
ecology_keyboard.add(ecology_but4)


##### INLINE-КЛАВИАТУРА ПРИ СООБЩЕНИИ ОБ ЭКО-КУЛЬТУРЕ
INLINE_CULTURE_BUT1_TEXT = 'Почему необходима эко-культура?'
INLINE_CULTURE_BUT2_TEXT = 'Как формировать эко-культуру?'
INLINE_CULTURE_BUT3_TEXT = 'Эко-привычки'
CALLBACK_CULTURE_BUT1 = '1'
CALLBACK_CULTURE_BUT2 = '2'
CALLBACK_CULTURE_BUT3 = '3'
inline_culture_but1 = types.InlineKeyboardButton(INLINE_CULTURE_BUT1_TEXT, callback_data=CALLBACK_CULTURE_BUT1)
inline_culture_but2 = types.InlineKeyboardButton(INLINE_CULTURE_BUT2_TEXT, callback_data=CALLBACK_CULTURE_BUT2)
inline_culture_but3 = types.InlineKeyboardButton(INLINE_CULTURE_BUT3_TEXT, callback_data=CALLBACK_CULTURE_BUT3)
inline_culture_keyboard = types.InlineKeyboardMarkup(row_width=1)
inline_culture_keyboard.add(inline_culture_but1, inline_culture_but2, inline_culture_but3)

necessary_keyboard = types.InlineKeyboardMarkup(row_width=1)
necessary_keyboard.add(inline_culture_but2, inline_culture_but3)

how_to_form_keyboard = types.InlineKeyboardMarkup(row_width=1)
how_to_form_keyboard.add(inline_culture_but1, inline_culture_but3)

eco_habits_keyboard = types.InlineKeyboardMarkup(row_width=1)
eco_habits_keyboard.add(inline_culture_but1, inline_culture_but2)


##### КНОПКА НАЗАД В МЕНЮ ОБ ЭКОЛОГИИ
BACK_TO_ECOLOGY_BUT1_TEXT = 'Назад ↩'
back_to_ecology_but1 = types.KeyboardButton(BACK_TO_ECOLOGY_BUT1_TEXT)
back_to_ecology_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
back_to_ecology_keyboard.add(back_to_ecology_but1)


##### КЛАВИАТУРА СТАТЬИ
ARTICLES_BUT1_TEXT = 'Список статей 📝'
ARTICLES_BUT2_TEXT = 'Случайная статья 🎲'
ARTICLES_BUT3_TEXT = BACK_TO_ECOLOGY_BUT1_TEXT
articles_but1 = types.KeyboardButton(ARTICLES_BUT1_TEXT)
articles_but2 = types.KeyboardButton(ARTICLES_BUT2_TEXT)
articles_but3 = types.KeyboardButton(ARTICLES_BUT3_TEXT)
articles_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True ,row_width=1)
articles_keyboard.add(articles_but1, articles_but2, articles_but3)


##### INLINE-КЛАВИАТУРА В СЛОВАРЕ
INLINE_DICT_BUT1_TEXT = 'АБВГД'
INLINE_DICT_BUT2_TEXT = 'ЕЁЖЗИ'
INLINE_DICT_BUT3_TEXT = 'ЙКЛМН'
INLINE_DICT_BUT4_TEXT = 'ОПРСТ'
INLINE_DICT_BUT5_TEXT = 'УФХЦЧ'
INLINE_DICT_BUT6_TEXT = 'ШЩЭЮЯ'
CALLBACK_DICT_BUT1 = 'd1'
CALLBACK_DICT_BUT2 = 'd2'
CALLBACK_DICT_BUT3 = 'd3'
CALLBACK_DICT_BUT4 = 'd4'
CALLBACK_DICT_BUT5 = 'd5'
CALLBACK_DICT_BUT6 = 'd6'
inline_dict_but1 = types.InlineKeyboardButton(INLINE_DICT_BUT1_TEXT, callback_data=CALLBACK_DICT_BUT1)
inline_dict_but2 = types.InlineKeyboardButton(INLINE_DICT_BUT2_TEXT, callback_data=CALLBACK_DICT_BUT2)
inline_dict_but3 = types.InlineKeyboardButton(INLINE_DICT_BUT3_TEXT, callback_data=CALLBACK_DICT_BUT3)
inline_dict_but4 = types.InlineKeyboardButton(INLINE_DICT_BUT4_TEXT, callback_data=CALLBACK_DICT_BUT4)
inline_dict_but5 = types.InlineKeyboardButton(INLINE_DICT_BUT5_TEXT, callback_data=CALLBACK_DICT_BUT5)
inline_dict_but6 = types.InlineKeyboardButton(INLINE_DICT_BUT6_TEXT, callback_data=CALLBACK_DICT_BUT6)
inline_dict_keyboard = types.InlineKeyboardMarkup(row_width=3)
inline_dict_keyboard.add(inline_dict_but1, inline_dict_but2, inline_dict_but3, inline_dict_but4, inline_dict_but5, inline_dict_but6)
