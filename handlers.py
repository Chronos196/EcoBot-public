from bot import bot
from messages import *
from keyboards import *
from commands import *
from dictionary import *
from images import *
from articles import *

### Команды встроенные *начало   ___________________________________________________________

@bot.message_handler(commands=['start'])
def get_welcome(message):
    hello = 'Здравствуйте, <i>' + str(message.from_user.first_name) + '</i>\n\n'
    bot.send_message(message.chat.id, hello + HELLO_MESSAGE, reply_markup=menu_keyboard, parse_mode='html')

@bot.message_handler(commands=['help'])
def get_help(message):
    bot.send_message(message.chat.id, HELP_MESSAGE, reply_markup=back_to_menu_keyboard, parse_mode='html')

@bot.message_handler(commands=['menu'])
def get_menu(message):
    bot.send_message(message.chat.id, MENU_MESSAGE, reply_markup=menu_keyboard, parse_mode='html')

@bot.message_handler(commands=['about_bot'])
def get_bot(message):
    bot.send_message(message.chat.id, ABOUT_BOT_MESSAGE + ABOUT_BOT_IMAGE, reply_markup=back_to_menu_keyboard, parse_mode='html')

@bot.message_handler(commands=['why_is_bot'])
def get_why_is_bot(message):
    bot.send_message(message.chat.id, WHY_IS_BOT_MESSAGE + WHY_IS_BOT_IMAGE, reply_markup=back_to_menu_keyboard, parse_mode='html')

@bot.message_handler(commands=['eco'])
def get_ecology(message):
    bot.send_message(message.chat.id, ECOLOGY_MESSAGES, reply_markup=ecology_keyboard, parse_mode='html')

### Команды встроенные *конец    ___________________________________________________________


### Inline клавиатура *начало    ___________________________________________________________

@bot.callback_query_handler(func=lambda call: True)
def get_query_handler(call):

    if call.data == CALLBACK_CULTURE_BUT1:
        bot.answer_callback_query(callback_query_id=call.id, text=INLINE_CULTURE_BUT1_TEXT)
        bot.send_message(call.message.chat.id, NECESSARY_MESSAGE + NECESSARY_IMAGE, reply_markup=necessary_keyboard, parse_mode='html')

    elif call.data == CALLBACK_CULTURE_BUT2:
        bot.answer_callback_query(callback_query_id=call.id, text=INLINE_CULTURE_BUT2_TEXT)
        bot.send_message(call.message.chat.id, HOW_TO_FORM_MESSAGE + HOW_TO_FORM_IMAGE, reply_markup=how_to_form_keyboard, parse_mode='html')

    elif call.data == CALLBACK_CULTURE_BUT3:
        bot.answer_callback_query(callback_query_id=call.id, text=INLINE_CULTURE_BUT3_TEXT)
        bot.send_message(call.message.chat.id, ECO_HABITS_MESSAGE + ECO_HABITS_IMAGE, reply_markup=eco_habits_keyboard, parse_mode='html')

    elif call.data == CALLBACK_DICT_BUT1:
        bot.answer_callback_query(callback_query_id=call.id, text=INLINE_DICT_BUT1_TEXT)
        string = ''
        for term, ref in sorted(dictionary.items()):
            if(term[0] >= INLINE_DICT_BUT1_TEXT[0] and term[0] <= INLINE_DICT_BUT1_TEXT[4]):
                string += '<a href="' + ref[1] + '">' + term + '</a>\n'
            else:
                continue
        bot.send_message(call.message.chat.id, string, reply_markup=inline_dict_keyboard, parse_mode='html')

    elif call.data == CALLBACK_DICT_BUT2:
        bot.answer_callback_query(callback_query_id=call.id, text=INLINE_DICT_BUT2_TEXT)
        string = ''
        for term, ref in sorted(dictionary.items()):
            if(term[0] >= INLINE_DICT_BUT2_TEXT[0] and term[0] <= INLINE_DICT_BUT2_TEXT[4]):
                string += '<a href="' + ref[1] + '">' + term + '</a>\n'
            else:
                continue
        bot.send_message(call.message.chat.id, string, reply_markup=inline_dict_keyboard, parse_mode='html')

    elif call.data == CALLBACK_DICT_BUT3:
        bot.answer_callback_query(callback_query_id=call.id, text=INLINE_DICT_BUT3_TEXT)
        string = ''
        for term, ref in sorted(dictionary.items()):
            if(term[0] >= INLINE_DICT_BUT3_TEXT[0] and term[0] <= INLINE_DICT_BUT3_TEXT[4]):
                string += '<a href="' + ref[1] + '">' + term + '</a>\n'
            else:
                continue
        bot.send_message(call.message.chat.id, string, reply_markup=inline_dict_keyboard, parse_mode='html')

    elif call.data == CALLBACK_DICT_BUT4:
        bot.answer_callback_query(callback_query_id=call.id, text=INLINE_DICT_BUT4_TEXT)
        string = ''
        for term, ref in sorted(dictionary.items()):
            if(term[0] >= INLINE_DICT_BUT4_TEXT[0] and term[0] <= INLINE_DICT_BUT4_TEXT[4]):
                string += '<a href="' + ref[1] + '">' + term + '</a>\n'
            else:
                continue
        bot.send_message(call.message.chat.id, string, reply_markup=inline_dict_keyboard, parse_mode='html')

    elif call.data == CALLBACK_DICT_BUT5:
        bot.answer_callback_query(callback_query_id=call.id, text=INLINE_DICT_BUT5_TEXT)
        string = ''
        for term, ref in sorted(dictionary.items()):
            if(term[0] >= INLINE_DICT_BUT5_TEXT[0] and term[0] <= INLINE_DICT_BUT5_TEXT[4]):
                string += '<a href="' + ref[1] + '">' + term + '</a>\n'
            else:
                continue
        bot.send_message(call.message.chat.id, string, reply_markup=inline_dict_keyboard, parse_mode='html')

    elif call.data == CALLBACK_DICT_BUT6:
        bot.answer_callback_query(callback_query_id=call.id, text=INLINE_DICT_BUT6_TEXT)
        string = ''
        for term, ref in sorted(dictionary.items()):
            if(term[0] >= INLINE_DICT_BUT6_TEXT[0] and term[0] <= INLINE_DICT_BUT6_TEXT[4]):
                string += '<a href="' + ref[1] + '">' + term + '</a>\n'
            else:
                continue
        bot.send_message(call.message.chat.id, string, reply_markup=inline_dict_keyboard, parse_mode='html')

    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

### Inline клавиатура *конец     ___________________________________________________________


@bot.message_handler(content_types=['text'])
def get_message(message):

### Команды боту *начало         ___________________________________________________________

    if message.text.lower() == HELLO_COMMAND:
        hello = 'Здравствуйте, <i>' + str(message.from_user.first_name) + '</i>\n\n'
        bot.send_message(message.chat.id, hello + HELLO_MESSAGE, reply_markup=menu_keyboard, parse_mode='html')

    elif message.text.lower() == HELP_COMMAND:
        bot.send_message(message.chat.id, HELP_MESSAGE, reply_markup=back_to_menu_keyboard, parse_mode='html')

    elif message.text.lower() == MENU_COMMAND:
        bot.send_message(message.chat.id, MENU_MESSAGE, reply_markup=menu_keyboard, parse_mode='html')

    elif message.text.lower().split() == ABOUT_BOT_COMMAND:
        bot.send_message(message.chat.id, ABOUT_BOT_MESSAGE + ABOUT_BOT_IMAGE, reply_markup=back_to_menu_keyboard, parse_mode='html')

    elif message.text.lower() == WHY_IS_BOT_COMMAND:
        bot.send_message(message.chat.id, WHY_IS_BOT_MESSAGE + WHY_IS_BOT_IMAGE, reply_markup=back_to_menu_keyboard, parse_mode='html')

    elif message.text.lower() == ECOLOGY_COMMAND:
        bot.send_message(message.chat.id, ECOLOGY_MESSAGES, reply_markup=ecology_keyboard, parse_mode='html')

    elif message.text.lower().split(' ')[0] == DICTIONARY_COMMAND and message.text != ECOLOGY_BUT3_TEXT:
        string = list(filter(lambda x: x != '', message.text.lower().split(' ')))
        if len(string) == 1:
            bot.send_message(message.chat.id, DICTIONARY_MESSAGE, reply_markup=inline_dict_keyboard, parse_mode='html')
        else:
            if len(string) == 2:
                if string[1].title() in dictionary:
                    answer = '<b>' + string[1].title() + '</b> - <i>' + dictionary.get(string[1].title())[0]  + '</i>'
                    bot.send_message(message.chat.id, answer, parse_mode='html')
                else:
                    answer = DICTIONARY_UNFOUND + ': <b>' + string[1] + '</b>'
                    bot.send_message(message.chat.id, answer, parse_mode='html')
            else:
                key = string[1].title() + ' ' + ' '.join(string[2:])
                if key in dictionary:
                    answer = '<b>' + key + '</b> - <i>' + dictionary.get(key)[0] + '</i>'
                    bot.send_message(message.chat.id, answer, parse_mode='html')
                else:
                    answer = DICTIONARY_UNFOUND + ': <b>' + key + '</b>'
                    bot.send_message(message.chat.id, answer, parse_mode='html')

### Команды боту *конец          ___________________________________________________________


### Нажатие на кнопки *начало    ___________________________________________________________

    elif message.text == BACK_TO_MENU_BUT1_TEXT:
        bot.send_message(message.chat.id, MENU_MESSAGE, reply_markup=menu_keyboard, parse_mode='html')

    elif message.text == MENU_BUT4_TEXT:
        bot.send_message(message.chat.id, HELP_MESSAGE, reply_markup=back_to_menu_keyboard, parse_mode='html')

    elif message.text == MENU_BUT3_TEXT:
        bot.send_message(message.chat.id, ABOUT_BOT_MESSAGE + ABOUT_BOT_IMAGE, reply_markup=back_to_menu_keyboard, parse_mode='html')

    elif message.text == MENU_BUT2_TEXT:
        bot.send_message(message.chat.id, WHY_IS_BOT_MESSAGE + WHY_IS_BOT_IMAGE, reply_markup=back_to_menu_keyboard, parse_mode='html')

    elif message.text == MENU_BUT1_TEXT:
        bot.send_message(message.chat.id, ECOLOGY_MESSAGES, reply_markup=ecology_keyboard, parse_mode='html')

    elif message.text == BACK_TO_ECOLOGY_BUT1_TEXT:
        bot.send_message(message.chat.id, ECOLOGY_MESSAGES, reply_markup=ecology_keyboard, parse_mode='html')

    elif message.text == ECOLOGY_BUT1_TEXT:
        bot.send_message(message.chat.id, CULTURE_MESSAGES + CULTURE_IMAGE, reply_markup=inline_culture_keyboard, parse_mode='html')

    elif message.text == ECOLOGY_BUT2_TEXT:
        bot.send_message(message.chat.id, ARTICLES_MESSAGE, reply_markup=articles_keyboard, parse_mode='html')

    elif message.text == ARTICLES_BUT1_TEXT:
        bot.send_message(message.chat.id, get_list_of_articles(), reply_markup=articles_keyboard, parse_mode='html')

    elif message.text == ARTICLES_BUT2_TEXT:
        bot.send_message(message.chat.id, get_random_article(), reply_markup=articles_keyboard, parse_mode='html')
    
    elif message.text == ECOLOGY_BUT3_TEXT:
        bot.send_message(message.chat.id, DICTIONARY_MESSAGE, reply_markup=inline_dict_keyboard, parse_mode='html')

### Нажатие на кнопки *конец     ___________________________________________________________

    else:
        bot.send_message(message.chat.id, UNKNOWN_COMMAND_MESSAGE, parse_mode='html')


if __name__ == '__main__':
    bot.polling(none_stop=True)