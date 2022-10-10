import telebot
from telebot import types
import shutil
from datetime import datetime

import threading
import time
from time import sleep

import sqlite3

admins = [543256966]

db = sqlite3.connect('base.db', check_same_thread=False)
sql = db.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS users (
    id INT,
    username TEXT,
    client BOOLEAN,
    ava_bot_num INT,
    ava_now INT,
    bun BOOLEAN,
    admin BOOLEAN
)''')
sql.execute('''CREATE TABLE IF NOT EXISTS clients_id (
    id INT
)''')
for admin in admins:
    sql.execute(f'SELECT id FROM users WHERE id = {admin}')
    if sql.fetchone() is None:
        sql.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)', (543256966, None, None, None, None, None, 1))
    db.commit()
db.commit()

bots_picks=['AgACAgIAAxkBAAIDpWND3AN_1s1Ft-yzSiWLUSlCwBcoAAJkwzEbc8IhSkQuCh_0JO-_AQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDpmND3Am_A74i1te5V5E0PvUVypCyAAJmwzEbc8IhSn7_xJzBMeKaAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDp2ND3A32uQqv__fiTqeoUg-NUs3KAAJnwzEbc8IhSua5zTqXFxsAAQEAAwIAA3kAAyoE',
'AgACAgIAAxkBAAIDqGND3BEkCqRDiDAkkBcf1Dy4ORFhAAJowzEbc8IhSv2oSs_t3UOcAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDqWND3BVPDFyAsAIMNr-At07Hd4mlAAJpwzEbc8IhSilpZCPIyy85AQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDqmND3BgcaL7M5nfg3pNSjhd4X6m4AAJqwzEbc8IhSkxuXbsfAqNyAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDq2ND3BwmX1gjJtH93ENkXgE4DDLVAAJrwzEbc8IhSuCA0hei3cbZAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDrGND3B5OcyXNyA2B4L1QvIdixlvEAAJswzEbc8IhShktg84PgvZcAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDrWND3CFGM0yOL1Cx2MEpERhL9ZyEAAJtwzEbc8IhStN06cVcPzhCAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDrmND3CSUm6Jbj_twEa_USQ0vENjIAAJuwzEbc8IhSiEe9hBoAZHiAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDr2ND3CdzFc2CJqooSdgNVZZpcaCDAAJvwzEbc8IhSm8c020lwIyCAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDsGND3CrU_2tsEi_EwGZs6ztM6KieAAJxwzEbc8IhSlah3D4xv6jYAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDsWND3C3HFHqNnIohcHjCwmrWyhkjAAJywzEbc8IhSjzkCE-ypRduAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDsmND3C9NmrZREw0ByGiYrD6sSZC_AAJzwzEbc8IhSg33y8DagqohAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDs2ND3DmZLAITLHOVpLzEzgyjOElqAAJ1wzEbc8IhSgeuOnec6YT7AQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDtGND3DyZMTi2SQTEmz9kJpC3_PK7AAJ2wzEbc8IhSkVnLmBwqS7pAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDtWND3D-BeBqU2IdNEpm6tiivFQZ4AAJ3wzEbc8IhSm7liA_r-Bz1AQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDtmND3EGyNiVm-MqI3uWXJTZYYNBxAAJ4wzEbc8IhSsDDIWwwdok7AQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDt2ND3ERnY_GaG2S0X6pxp4I05WyzAAJ5wzEbc8IhSg2M_7ATmYlgAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDuGND3EcgjxFrT12kU5V_6sfPD9iLAAJ6wzEbc8IhSpb_NFjE49_iAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDuWND3ErBpxZbMIxbtJ4DJCpBhIE3AAJ7wzEbc8IhSuEZY4Qrb3_vAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDumND3Ew0VwqaubBwjulIMaTyCzjKAAJ8wzEbc8IhSuHvRBIQ47LtAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDu2ND3E65JZPh21CZ1cog_kIBKWC3AAJ9wzEbc8IhShEZ4qD7HrfYAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDvGND3FCmtchGdd-1-WdC9f0q9AbSAAJ-wzEbc8IhSnKZYxz5WX4pAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDvWND3Fbz_niMdL5GViz7rtESBWdZAAJ_wzEbc8IhSir4VEPJ_cDLAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDvmND3Fiw1Xzko50X_HkMXFWrSxIqAAKAwzEbc8IhSjIblxEZluMvAQADAgADeQADKgQ',
'AgACAgIAAxkBAAIDv2ND3Fuq509nWvIf26FsJuWCQHyWAAKCwzEbc8IhSqPae0o2Cl2IAQADAgADeQADKgQ']
annotation = '👾Бот `VK_HELPER` \- это тот, кто будет вести твою группу *за тебя*\!\n\n🥳Можешь забыть про ежедневный поиск контента для новых постов\. Просто скажи ему, __откуда__ брать контент, и он сделает всю работу *за тебя\!*'
annotation_not_admin = '👾Бот `VK_HELPER` \- это тот, кто сам делает посты для групп во *Вконтакте\.*\n\nЕсли у тебя есть знакомые *админы групп вк,* напиши @UnicChan\!'
pricelist_text = '*«до *`N`* пабликов» \-* сколько можно указать боту пабликов, из которых будет ||вороваться|| контент\.\n\n*«отправка раз в *`N`* часов» \-* каждые `N` часов посты будут приходить __тебе в группу__\.\n\n*«booster» \-* уменьшает время отправки постов в твою группу\.'
referal_text = 'С помощью `реферальной системы` ты сможешь не только __сэкономить__ на покупке бота, но и получить бота *бесплатно\!*\n\n||Если у тебя есть знакомые админы, то и заработать\! Уточняй у @UnicChan\.||'
what_i_will_get = '👩🏻‍🎤Ты *бесплатно* получишь *уникальную* аватарку с одним из наших `ботов`. Тебе будет предложено *3* разных наряда для него, и ты сможешь выбрать *любого!*\n\n🌟Цена за *анимированную* gif\'ку составляет *300₽*. Для владельцев `VK_HELPER` и трафферов анимированные аватарки создаются *бесплатно!*\n\n_Примеры аватарок:_'

bot = telebot.TeleBot('5695964341:AAEdDWX8E58p8F73pYRVVc6Brl-mVEeqn5k')

def print_time_now():
    time = datetime.now()
    time = time.strftime('%m-%d %H:%M:%S')
    print(f'--{time}--')

def make_user(message):
    sql.execute(f'SELECT id FROM users WHERE id = {message.from_user.id}')
    if sql.fetchone() is None: #если впервые запускает
        sql.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)', (message.from_user.id, f'@{message.from_user.username}', False, None, None, False, 0))
        db.commit()
        print(f'{print_time_now()}\n@{message.from_user.username} ({message.from_user.id}) впервые запускает бота!')
    else:
        sql.execute(f'SELECT id FROM clients_id WHERE id = {message.from_user.id}')
        if not sql.fetchone() is None: #если клиент
            sql.execute(f'UPDATE users SET client = {True} WHERE id = {message.from_user.id}')
            db.commit()
        db.commit()
    db.commit()

while True:
    try:
        @bot.message_handler(commands=['start']) #старт
        def start(message):
            bot.delete_message(message.chat.id, message.message_id)
            if message.chat.type == 'private':
                make_user(message)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                client = types.KeyboardButton('🧬\nЯ владелец VK_HELPER')
                guest = types.KeyboardButton('👀\nЯ просто гость')

                markup.add(client, guest)
                bot.send_message(message.chat.id, '🦾')
                bot.send_message(message.chat.id, '<b>Боты приветствуют тебя!</b>\nЗдесь ты сможешь узнать о том, что такое <b>VK_HELPER</b> и выбрать себе <u>бота</u>, который тебе понравится!', parse_mode='html', reply_markup=markup)
            else:
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id, 'Переходи в личные сообщения со мной 🦾')

        @bot.message_handler(commands=['faq']) #старт
        def faq(message):
            bot.delete_message(message.chat.id, message.message_id)
            markup = types.InlineKeyboardMarkup(row_width=2)
            group_admin = types.InlineKeyboardButton('да', callback_data='group_admin')
            not_group_admin = types.InlineKeyboardButton('нет', callback_data='not_group_admin')

            markup.add(group_admin, not_group_admin)
            bot.send_message(message.chat.id, 'Ты админ *вк группы/групп?*', parse_mode='Markdown', reply_markup=markup)

        @bot.message_handler(content_types=["photo"])
        def confirming(message):
            photo = max(message.photo, key=lambda x: x.height)
            print(photo.file_id)

        @bot.message_handler(content_types=['text']) #обработка сообщений
        def bot_message(message):
            bot.delete_message(message.chat.id, message.message_id)
            if message.chat.type == 'private':
                sql.execute(f'SELECT bun FROM users WHERE id = {message.from_user.id}')
                bun = sql.fetchone()[0]
                db.commit()
                if not bun:
                    if 'владелец' in message.text:
                        client = False
                        sql.execute(f'SELECT client FROM users WHERE id = {message.from_user.id}')
                        if sql.fetchone()[0] == True:
                            client = True
                        db.commit()

                        if client:
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                            avatar = types.KeyboardButton('👾\nБоты')

                            markup.add(avatar)
                            bot.send_message(message.chat.id, '<b>💻 Меню</b>', parse_mode='html', reply_markup=markup)
                            db.commit()
                        else:
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                            guest = types.KeyboardButton('👀\nЯ просто гость')

                            markup.add(guest)
                            bot.send_message(message.chat.id, '🚨 `ошибка` 🚨\n\n*Боты* извиняются, но не могут найти тебя в своей *базе данных.*', parse_mode='Markdown', reply_markup=markup)

                    elif 'гость' in message.text:
                        client = False
                        sql.execute(f'SELECT client FROM users WHERE id = {message.from_user.id}')
                        if sql.fetchone()[0] == True:
                            client = True
                        db.commit()

                        if not client:
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                            wtf = types.KeyboardButton('🧐\nЧто я получу?')
                            avatar = types.KeyboardButton('👾\nБоты')
                            what_is = types.KeyboardButton('Что такое VK_HELPER❓')

                            markup.add(wtf, avatar, what_is)
                            bot.send_message(message.chat.id, '<b>💻 Меню</b>', parse_mode='html', reply_markup=markup)
                        else:
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                            avatar = types.KeyboardButton('👾\nБоты')

                            markup.add(avatar)
                            bot.send_message(message.chat.id, '<b>Боты узнают тебя и не могут относиться к тебе как к гостю.</b>', parse_mode='html', reply_markup=markup)

                    elif 'Боты' in message.text:
                        # sql.execute(f'SELECT client FROM users WHERE id = {message.from_user.id}')
                        markup = types.InlineKeyboardMarkup(row_width=5)
                        bot_1 = types.InlineKeyboardButton('1', callback_data='av_1')
                        bot_2 = types.InlineKeyboardButton('2', callback_data='av_2')
                        bot_3 = types.InlineKeyboardButton('3', callback_data='av_3')
                        bot_4 = types.InlineKeyboardButton('4', callback_data='av_4')
                        bot_5 = types.InlineKeyboardButton('5', callback_data='av_5')
                        bot_6 = types.InlineKeyboardButton('6', callback_data='av_6')
                        bot_7 = types.InlineKeyboardButton('7', callback_data='av_7')
                        bot_8 = types.InlineKeyboardButton('8', callback_data='av_8')
                        bot_9 = types.InlineKeyboardButton('9', callback_data='av_9')
                        bot_10 = types.InlineKeyboardButton('10', callback_data='av_10')
                        bot_next = types.InlineKeyboardButton('==>', callback_data='next_2')

                        markup.add(bot_1, bot_2, bot_3, bot_4, bot_5, bot_6, bot_7, bot_8, bot_9, bot_10, bot_next)
                        bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIDmmND2ft4vQOra-wQWrLp_Z0hhlf1AAJWwzEbc8IhSu3iRCmmwuwVAQADAgADeQADKgQ', reply_markup=markup)

                    elif 'Что такое' in message.text:
                        markup = types.InlineKeyboardMarkup(row_width=2)
                        group_admin = types.InlineKeyboardButton('да', callback_data='group_admin')
                        not_group_admin = types.InlineKeyboardButton('нет', callback_data='not_group_admin')

                        markup.add(group_admin, not_group_admin)
                        bot.send_message(message.chat.id, 'Ты админ *вк группы/групп?*', parse_mode='Markdown', reply_markup=markup)

                    elif 'получу' in message.text:
                        markup = types.InlineKeyboardMarkup(row_width=2)
                        free_avatars = types.InlineKeyboardButton('✨бесплатная✨', callback_data='free_avatars')
                        animated_avatars = types.InlineKeyboardButton('⚡️анимированная⚡️', callback_data='animated_avatars')

                        markup.add(free_avatars, animated_avatars)
                        bot.send_message(message.chat.id, what_i_will_get, parse_mode='Markdown', reply_markup=markup)

                    elif 'чекадмин' in message.text:
                        if message.from_user.id in admins:
                            markup = types.InlineKeyboardMarkup(row_width=2)
                            add_client_id = types.InlineKeyboardButton('добавить client_id', callback_data='add_client_id')

                            markup.add(add_client_id)

                            bot.send_message(message.chat.id, 'чё надо?', reply_markup=markup)

                    else:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        client = types.KeyboardButton('🧬\nЯ владелец VK_HELPER')
                        guest = types.KeyboardButton('👀\nЯ просто гость')

                        markup.add(client, guest)
                        bot.send_message(message.chat.id, 'Боты помогают тебе!', reply_markup=markup)
                else:
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIDm2ND2hiVm8VGaPSa--PuRynWZTdwAAJYwzEbc8IhSjQPGYrZXhrQAQADAgADeQADKgQ', caption='Твоё поведение _не понравилось_ *ботам*. Они `не будут` реагировать на тебя, пока @UnicChan не поговорит с тобой 😡', parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove())
            else:
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id, 'Переходи в личные сообщения со мной 🦾')

        @bot.callback_query_handler(func=lambda call: True) #обработка inline кнопок
        def callback_inline(call):
            try:
                if call.message:
                    sql.execute(f'SELECT bun FROM users WHERE id = {call.from_user.id}')
                    bun = sql.fetchone()[0]
                    db.commit()
                    if not bun:
                        if call.data == 'next_1' or ( call.data.startswith('back_') and int(call.data.replace('back_', '')) in range(1, 11)):
                            bot.answer_callback_query(call.id)
                            markup = types.InlineKeyboardMarkup(row_width=5)
                            bot_1 = types.InlineKeyboardButton('1', callback_data='av_1')
                            bot_2 = types.InlineKeyboardButton('2', callback_data='av_2')
                            bot_3 = types.InlineKeyboardButton('3', callback_data='av_3')
                            bot_4 = types.InlineKeyboardButton('4', callback_data='av_4')
                            bot_5 = types.InlineKeyboardButton('5', callback_data='av_5')
                            bot_6 = types.InlineKeyboardButton('6', callback_data='av_6')
                            bot_7 = types.InlineKeyboardButton('7', callback_data='av_7')
                            bot_8 = types.InlineKeyboardButton('8', callback_data='av_8')
                            bot_9 = types.InlineKeyboardButton('9', callback_data='av_9')
                            bot_10 = types.InlineKeyboardButton('10', callback_data='av_10')
                            page_count = types.InlineKeyboardButton('1/3', callback_data='pass')
                            bot_next = types.InlineKeyboardButton('==>', callback_data='next_2')

                            markup.add(bot_1, bot_2, bot_3, bot_4, bot_5, bot_6, bot_7, bot_8, bot_9, bot_10, page_count,bot_next)
                            photo = 'AgACAgIAAxkBAAID0mND4eW9xTiRdL3oGRiK4P9a2YKIAAJWwzEbc8IhSu3iRCmmwuwVAQADAgADeQADKgQ'
                            try:
                                bot.edit_message_media(types.InputMediaPhoto(photo), call.message.chat.id, call.message.message_id, reply_markup=markup)
                            except:
                                bot.answer_callback_query(call.id, '💬 Не так быстро, пожалуйста 💬', show_alert=True)
                        elif call.data == 'next_2' or ( call.data.startswith('back_') and int(call.data.replace('back_', '')) in range(11, 21)):
                            bot.answer_callback_query(call.id)
                            markup = types.InlineKeyboardMarkup(row_width=5)
                            bot_11 = types.InlineKeyboardButton('1', callback_data='av_11')
                            bot_12 = types.InlineKeyboardButton('2', callback_data='av_12')
                            bot_13 = types.InlineKeyboardButton('3', callback_data='av_13')
                            bot_14 = types.InlineKeyboardButton('4', callback_data='av_14')
                            bot_15 = types.InlineKeyboardButton('5', callback_data='av_15')
                            bot_16 = types.InlineKeyboardButton('6', callback_data='av_16')
                            bot_17 = types.InlineKeyboardButton('7', callback_data='av_17')
                            bot_18 = types.InlineKeyboardButton('8', callback_data='av_18')
                            bot_19 = types.InlineKeyboardButton('9', callback_data='av_19')
                            bot_20 = types.InlineKeyboardButton('10', callback_data='av_20')
                            bot_prev = types.InlineKeyboardButton('<==', callback_data='next_1')
                            page_count = types.InlineKeyboardButton('2/3', callback_data='pass')
                            bot_next = types.InlineKeyboardButton('==>', callback_data='next_3')

                            markup.add(bot_11, bot_12, bot_13, bot_14, bot_15, bot_16, bot_17, bot_18, bot_19, bot_20, bot_prev, page_count, bot_next)
                            photo = 'AgACAgIAAxkBAAIDoWND2sz9_0dVUNvqfmDb3vbhzJ5UAAJcwzEbc8IhSuHhO-rBDqeMAQADAgADeQADKgQ'
                            try:
                                bot.edit_message_media(types.InputMediaPhoto(photo), call.message.chat.id, call.message.message_id, reply_markup=markup)
                            except:
                                bot.answer_callback_query(call.id, '💬 Не так быстро, пожалуйста 💬', show_alert=True)

                        elif call.data == 'next_3' or ( call.data.startswith('back_') and int(call.data.replace('back_', '')) in range(21, 28)):
                            bot.answer_callback_query(call.id)
                            markup = types.InlineKeyboardMarkup(row_width=5)
                            bot_21 = types.InlineKeyboardButton('1', callback_data='av_21')
                            bot_22 = types.InlineKeyboardButton('2', callback_data='av_22')
                            bot_23 = types.InlineKeyboardButton('3', callback_data='av_23')
                            bot_24 = types.InlineKeyboardButton('4', callback_data='av_24')
                            bot_25 = types.InlineKeyboardButton('5', callback_data='av_25')
                            bot_26 = types.InlineKeyboardButton('6', callback_data='av_26')
                            bot_27 = types.InlineKeyboardButton('7', callback_data='av_27')
                            empty_28 = types.InlineKeyboardButton('8', callback_data='empty')
                            empty_29 = types.InlineKeyboardButton('9', callback_data='empty')
                            empty_30 = types.InlineKeyboardButton('10', callback_data='empty')
                            bot_prev = types.InlineKeyboardButton('<==', callback_data='next_2')
                            page_count = types.InlineKeyboardButton('3/3', callback_data='pass')

                            markup.add(bot_21, bot_22, bot_23, bot_24, bot_25, bot_26, bot_27, empty_28, empty_29, empty_30, bot_prev, page_count)
                            photo = 'AgACAgIAAxkBAAIDomND2uijG__ZqFzEy28J6alBrwoVAAJdwzEbc8IhSj9VUobsJi_PAQADAgADeQADKgQ'
                            try:
                                bot.edit_message_media(types.InputMediaPhoto(photo), call.message.chat.id, call.message.message_id, reply_markup=markup)
                            except:
                                bot.answer_callback_query(call.id, '💬 Не так быстро, пожалуйста 💬', show_alert=True)
                                
                        elif call.data.startswith('av_'):
                            bot.answer_callback_query(call.id)
                            avatar_num = call.data.replace('av_', '')
                            sql.execute(f'UPDATE users SET ava_now = {int(avatar_num)} WHERE id = {call.from_user.id}')
                            db.commit()
                            markup = types.InlineKeyboardMarkup(row_width=2)
                            yes = types.InlineKeyboardButton('этого!', callback_data='yes')
                            sql.execute(f'SELECT ava_now FROM users WHERE id = {call.from_user.id}')
                            ava_now = sql.fetchone()[0]
                            db.commit()
                            back = types.InlineKeyboardButton('назад', callback_data=f'back_{ava_now}')

                            markup.add(yes, back)
                            photo = bots_picks[int(avatar_num)-1]
                            bot.edit_message_media(types.InputMediaPhoto(photo), call.message.chat.id, call.message.message_id, reply_markup=markup)

                        elif call.data == 'yes':
                            bot.answer_callback_query(call.id)
                            markup = types.InlineKeyboardMarkup(row_width=2)
                            commit = types.InlineKeyboardButton('да', callback_data='commit')
                            no = types.InlineKeyboardButton('нет', callback_data='no')

                            markup.add(commit, no)
                            bot.send_message(call.message.chat.id, 'Ты уверен в выборе своего бота?', reply_markup=markup)

                        elif call.data == 'no':
                            bot.answer_callback_query(call.id, 'Не беспокойся, он не расстроился 👾')
                            bot.delete_message(call.message.chat.id, call.message.id)

                        elif call.data == 'commit':
                            sql.execute(f'SELECT ava_now FROM users WHERE id = {call.from_user.id}')
                            ava_now = sql.fetchone()[0]
                            db.commit()
                            sql.execute(f'UPDATE users SET ava_bot_num = {ava_now} WHERE id = {call.from_user.id}')
                            db.commit()
                            bot.answer_callback_query(call.id, 'Хорошо!\n\nСкоро с тобой свяжется UnicChan!', show_alert=True)

                            bot.delete_message(call.message.chat.id, call.message.id)

                            markup = types.InlineKeyboardMarkup(row_width=2)
                            bun = types.InlineKeyboardButton('бан нахуй', callback_data='bun')
                            unbun = types.InlineKeyboardButton('разбан', callback_data='unbun')

                            markup.add(bun, unbun)
                            sql.execute(f'SELECT client FROM users WHERE id = {call.from_user.id}')
                            if sql.fetchone()[0] == True:
                                bot.send_message(543256966, f'@{call.from_user.username} (`{call.from_user.id}`)\nхочет бота *№{ava_now}*!', parse_mode='Markdown', reply_markup=markup)
                            else:
                                bot.send_message(543256966, f'@{call.from_user.username} (`{call.from_user.id}`)\nхочет бота *№{ava_now}* `не client`', parse_mode='Markdown', reply_markup=markup)

                        elif call.data == 'group_admin':
                            bot.answer_callback_query(call.id)
                            markup = types.InlineKeyboardMarkup(row_width=2)
                            trailer = types.InlineKeyboardButton('трейлер 🎥', callback_data='trailer')
                            pricelist = types.InlineKeyboardButton('прайслист 🧾', callback_data='pricelist')
                            referal = types.InlineKeyboardButton('рефералка 🫂', callback_data='referal')
                            coming_soon = types.InlineKeyboardButton('скоро появится 🌚', callback_data='coming_soon')
                            close = types.InlineKeyboardButton('закрыть ❌', callback_data='del')

                            markup.add(trailer, pricelist, referal, coming_soon, close)
                            try:
                                bot.edit_message_text(annotation, call.message.chat.id, call.message.id, parse_mode='MarkdownV2', reply_markup=markup)
                            except:
                                bot.delete_message(call.message.chat.id, call.message.message_id)
                                bot.send_message(call.message.chat.id, annotation, parse_mode='MarkdownV2', reply_markup=markup)

                        elif call.data == 'not_group_admin':
                            bot.answer_callback_query(call.id)
                            markup = types.InlineKeyboardMarkup(row_width=2)
                            trailer = types.InlineKeyboardButton('трейлер 🎥', callback_data='trailer_not_admin')
                            traffer = types.InlineKeyboardButton('для трафферов', callback_data='traffer')
                            close = types.InlineKeyboardButton('закрыть ❌', callback_data='del')

                            markup.add(trailer, traffer, close)
                            try:
                                bot.edit_message_text(annotation_not_admin, call.message.chat.id, call.message.id, parse_mode='MarkdownV2', reply_markup=markup)
                            except:
                                bot.delete_message(call.message.chat.id, call.message.message_id)
                                bot.send_message(call.message.chat.id, annotation_not_admin, parse_mode='MarkdownV2', reply_markup=markup)

                        elif 'trailer' in call.data:
                            bot.delete_message(call.message.chat.id, call.message.message_id)
                            markup = types.InlineKeyboardMarkup(row_width=2)
                            if not 'not_admin' in call.data:
                                back = types.InlineKeyboardButton('назад 🔙', callback_data='group_admin')
                            else:
                                back = types.InlineKeyboardButton('назад 🔙', callback_data='not_group_admin')

                            markup.add(back)
                            trailer = 'BAACAgIAAxkBAAIDDGNDVhDT3Volfq62-KY6HXSMlXNuAAKkHgACeRoYStrKdx3sKaykKgQ'
                            bot.send_video(call.message.chat.id, trailer, reply_markup=markup)

                        elif call.data == 'pricelist':
                            bot.delete_message(call.message.chat.id, call.message.message_id)
                            markup = types.InlineKeyboardMarkup(row_width=2)
                            back = types.InlineKeyboardButton('назад 🔙', callback_data='group_admin')

                            markup.add(back)
                            bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIDjmND2VUtbth_9BEkrxzJVsHj8c_tAAJOwzEbc8IhShwqn5RmaUq-AQADAgADeQADKgQ', reply_markup=markup, caption=pricelist_text, parse_mode='MarkdownV2')

                        elif call.data == 'referal':
                            bot.delete_message(call.message.chat.id, call.message.message_id)
                            markup = types.InlineKeyboardMarkup(row_width=2)
                            back = types.InlineKeyboardButton('назад 🔙', callback_data='group_admin')

                            markup.add(back)
                            bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIDj2ND2XUM3_ilfSb5tgPmfNHbC4_kAAJPwzEbc8IhSr3w_l_rywypAQADAgADeQADKgQ', reply_markup=markup, caption=referal_text, parse_mode='MarkdownV2')

                        elif call.data == 'coming_soon':
                            bot.delete_message(call.message.chat.id, call.message.message_id)
                            markup = types.InlineKeyboardMarkup(row_width=2)
                            back = types.InlineKeyboardButton('назад 🔙', callback_data='group_admin')

                            markup.add(back)
                            bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIDiWND2SUgfyi0C2I1AAF-xs6KlM8DlQACTMMxG3PCIUoV8rDQSX3AqgEAAwIAA3kAAyoE', reply_markup=markup, caption='`Находится в разработке`', parse_mode='MarkdownV2')

                        elif call.data == 'traffer':
                            bot.answer_callback_query(call.id, 'Напиши @UnicChan.\nУ него есть для тебя предложение!', show_alert=True)

                        elif call.data == 'avatars':
                            bot.delete_message(call.message.chat.id, call.message.message_id)
                            markup = types.InlineKeyboardMarkup(row_width=2)
                            free_avatars = types.InlineKeyboardButton('✨бесплатная✨', callback_data='free_avatars')
                            animated_avatars = types.InlineKeyboardButton('⚡️анимированная⚡️', callback_data='animated_avatars')

                            markup.add(free_avatars, animated_avatars)
                            bot.send_message(call.message.chat.id, 'Ты *бесплатно* получишь *уникальную* аватарку с одним из наших `ботов`. Тебе будет предложено _3 разных наряда_ для него, и ты сможешь выбрать *любого!*\n\nЦена за _анимированную_ gif\'ку составляет 300*₽*. Для владельцев `VK_HELPER` анимированные аватарки создаются *бесплатно!*\n\nПримеры аватарок:', parse_mode='Markdown', reply_markup=markup)

                        elif call.data == 'free_avatars':
                            bot.delete_message(call.message.chat.id, call.message.message_id)
                            markup = types.InlineKeyboardMarkup(row_width=2)
                            back = types.InlineKeyboardButton('назад 🔙', callback_data='avatars')

                            markup.add(back)
                            bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIDnGND2j_vw-CnUMyVX73FxWO8y9MfAAJZwzEbc8IhSlsqrp2Q-GjzAQADAgADeQADKgQ', reply_markup=markup)

                        elif call.data == 'animated_avatars':
                            bot.delete_message(call.message.chat.id, call.message.message_id)
                            markup = types.InlineKeyboardMarkup(row_width=2)
                            back = types.InlineKeyboardButton('назад 🔙', callback_data='avatars')

                            markup.add(back)
                            animated_avatars = 'CgACAgIAAxkBAAIDz2ND4L_lTDkCw2XE-N-eL9UD1j7fAAIQHQACc8IhSodhvkQNcGRZKgQ'
                            bot.send_animation(call.message.chat.id, animated_avatars, reply_markup=markup)

                        elif call.data == 'del':
                            bot.delete_message(call.message.chat.id, call.message.message_id)

                        elif call.data == 'pass':
                            bot.answer_callback_query(call.id)

                    else:
                        bot.delete_message(call.message.chat.id, call.message.message_id)
                        bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIDm2ND2hiVm8VGaPSa--PuRynWZTdwAAJYwzEbc8IhSjQPGYrZXhrQAQADAgADeQADKgQ', caption='Твоё поведение _не понравилось_ *ботам*. Они `не будут` реагировать на тебя, пока @UnicChan не поговорит с тобой 😡', parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove())
                    
                    if call.data == 'add_client_id':
                        bot.answer_callback_query(call.id)
                        # sql.execute(f'SELECT client FROM users WHERE id = {message.from_user.id}')
                        @bot.message_handler(func=lambda message: True)
                        def input_id(message):
                            sent = bot.send_message(message.chat.id, "Кинь <b>id</b> клиента:", parse_mode='html')
                            bot.register_next_step_handler(sent, reg_id)
                        def reg_id(message):
                            client_id = int(message.text)
                            sql.execute(f'INSERT INTO clients_id VALUES ({client_id})')
                            db.commit()
                            bot.send_message(message.chat.id, 'Добавил')
                        input_id(call.message)

                    elif call.data == 'bun':
                        user_id = call.message.text.partition('(')[2]
                        user_id = user_id.partition(')')[0]
                        sql.execute(f'UPDATE users SET bun = {True} WHERE id = {int(user_id)}')
                        db.commit()
                        bot.answer_callback_query(call.id, f'{user_id} забанен', show_alert=True)

                    elif call.data == 'unbun':
                        user_id = call.message.text.partition('(')[2]
                        user_id = user_id.partition(')')[0]
                        sql.execute(f'UPDATE users SET bun = {False} WHERE id = {int(user_id)}')
                        db.commit()
                        bot.answer_callback_query(call.id, f'{user_id} разбанен', show_alert=True)

                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        client = types.KeyboardButton('🧬\nЯ владелец VK_HELPER')
                        guest = types.KeyboardButton('👀\nЯ просто гость')

                        markup.add(client, guest)
                        bot.send_photo(user_id, 'AgACAgIAAxkBAAIDnmND2oyN7PxSlEzfuStuWl7VGCvNAAJawzEbc8IhSvWfW47Xd_X-AQADAgADeQADKgQ', caption='Ты был *разбанен*. Больше так _не делай_ 🙂', parse_mode='Markdown', reply_markup=markup)

            except Exception as e:
                print_time_now()
                print(f'ошибка в обработке inline кнопки!\n{repr(e)}')

        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        print(print_time_now(), 'Ошибка в боте. Рестарт через 1 секунду')
        sleep(1)
