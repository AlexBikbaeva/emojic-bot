#Импортируем нужные нам библиотеки и модули
import sqlite3
from datetime import datetime
import time
from telethon import TelegramClient, events
from telethon import functions
from SQLite_database import sqlite_database, database_insert

#Вся нужная информация для инициализации
api_id = 2323834
api_hash = '4c6aca5a318267ab2be56c5a484b30be'
bot = 'new session'
bot_name = '@emojic_bot'
token = '1401875600:AAF6ADe7jiosCU4GchUSLDFv_KRV8KyNb9Q'
client = TelegramClient(bot, api_id, api_hash)
sqlite_database()
client.start(bot_token=token)

#Группируем коды эмодзи в 3 списка
happy_emotes = ['\U0001F600','\U0001F604', '\U0001F601', '\U0001F606', '\U0001F602', '\U0001F60A', '\U0001F929', '\U0001F973']
sad_emotes = ['\U0001F644', "\U0001F614", "\U0001F61E", "\U0001F61F", "\U0001F615", "\U0001F641", "\U0001F629", "\U0001F62B", "\U0001F613"]
angry_emotes = ['\U0001F47F', "\U0001F62C", "\U0001F624", "\U0001F621", "\U0001F47A", "\U0001F480", "\U0001F620", "\U0001F92F", "\U0001F928"]

@client.on(events.NewMessage)
async def my_event_handler(event):
    data = []
    #Находим id сообщения, время сообщения, id сессии, текст сообщения, идентификатор (id) клиента
    mess_id = event.message.to_dict()['id']
    mess_date = event.message.to_dict()['date']
    start_time = mess_date.strftime("%H:%M:%S")
    mess_text = event.message.to_dict()['message']
    user_id = event.message.sender_id
    data.append((mess_id, mess_date, bot, mess_text, user_id))
    #Та же информация только касательно бота
    result = await client(functions.users.GetFullUserRequest(bot_name))
    bot_info = result.bot_info
    bot_id = bot_info.to_dict()['user_id']

    #Ответ в зависимости от присланного клиентом эмодзи, если в сообщении не эмодзи из одного из списков, то бот "не понимает" о чём идёт речь.
    if event.raw_text in happy_emotes:
        bot_reply = await event.reply('Привет, я смотрю ты в хорошем настроении!')
        bot_mess_text = bot_reply.to_dict()['message']
        bot_mess_date = bot_reply.to_dict()['date']
        bot_mess_id = bot_reply.to_dict()['id']
        data.append((bot_mess_id, bot_mess_date, bot, bot_mess_text, bot_id))
    elif event.raw_text in sad_emotes:
        bot_reply = await event.reply('Привет, не грусти, всё будет хорошо!')
        bot_mess_text = bot_reply.to_dict()['message']
        bot_mess_date = bot_reply.to_dict()['date']
        bot_mess_id = bot_reply.to_dict()['id']
        data.append((bot_mess_id, bot_mess_date, bot, bot_mess_text, bot_id))
    elif event.raw_text in angry_emotes:
        bot_reply = await event.reply('Привет, не злись, остынь!')
        bot_mess_text = bot_reply.to_dict()['message']
        bot_mess_date = bot_reply.to_dict()['date']
        bot_mess_id = bot_reply.to_dict()['id']
        data.append((bot_mess_id, bot_mess_date, bot, bot_mess_text, bot_id))
    else:
        bot_reply = await event.reply('Прости, но я не понимаю.')
        bot_mess_text = bot_reply.to_dict()['message']
        bot_mess_date = bot_reply.to_dict()['date']
        bot_mess_id = bot_reply.to_dict()['id']
        data.append((bot_mess_id, bot_mess_date, bot, bot_mess_text, bot_id))
    database_insert(data)

client.run_until_disconnected()

