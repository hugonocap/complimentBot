import telebot
import requests
import datetime
from telebot import types
from random import randrange

bot = telebot.TeleBot("5780136154:AAGHHbY4wS4P68rNxCHfm1X5uy8Us3JJd5o")
open_weather_token = "e3ec7e9be9b524a53fd2d768ef584c88"

start_emoji = u"\U0001F618"
cats_emoji = u"\U0001F431"
comp_emoji = u"\U0001F48C"
bye_emoji = u"\U0001F609"
good_night_emoji = u"\U0001F48B"
error_emoji = u"\U0001F97A"
angel_emoji = u"\U0001F607"
love_emoji = u"\U0001F970"
drunk_emoji = u"\U0001F974"
luv_sign_emoji = u"\U0001FAF6"
hug_emoji = u"\U0001F917"
smile_emoji = u"\U0001F638"
monkey_emoji = u"\U0001F64A"
smiling_eyes_emoji = u"\U0001F60A"
smile_to_ears_emoji = u"\U0001F604"
robot_emoji = u"\U0001F916"
savoring_emoji = u"\U0001F60B"
weather_emoji = u"\U0001F324"
rose_emoji = u"\U0001F339"

#----------------------------------------------------------------

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    comp_button = types.KeyboardButton(f"/Compliments")
    cats_button = types.KeyboardButton(f"/Kitties")
    commands_button = types.KeyboardButton(f"/Commands")
    weather_button = types.KeyboardButton(f"/Weather")
    myweather_button = types.KeyboardButton(f"/YourWeather")
    hug_button = types.KeyboardButton(f"/Hug")
    pres_button = types.KeyboardButton(f"/Present")

    markup.add(comp_button, cats_button, commands_button, weather_button, myweather_button, hug_button, pres_button)

    bot.send_message(message.chat.id,
    f"Hi <b>Nina</b>, I made this bot especially for you. He will write you compliments and send kittens{start_emoji} type /commands",
    reply_markup=markup, parse_mode="html")

@bot.message_handler(commands=["Compliments", "compliments"])
def send_comp(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    comp_button = types.KeyboardButton(f"/Compliments")
    cats_button = types.KeyboardButton(f"/Kitties")
    commands_button = types.KeyboardButton(f"/Commands")
    weather_button = types.KeyboardButton(f"/Weather")
    myweather_button = types.KeyboardButton(f"/YourWeather")
    hug_button = types.KeyboardButton(f"/Hug")
    pres_button = types.KeyboardButton(f"/Present")

    markup.add(comp_button, cats_button, commands_button, weather_button, myweather_button, hug_button, pres_button)

    comp_list = [f"And who said that angels are only in heaven?! This is not true, because I see an Angel on earth! {angel_emoji}",
    f"You are very beautiful without makeup, and your natural beauty is immediately visible. That's great rarity. {love_emoji}",
    f"It's much more interesting to communicate with you than with my peers! {drunk_emoji}",
    f"You are very kind to the people around you. {luv_sign_emoji}",
    f"I would like to meet you as a child. {error_emoji}",
    f"You deserve a hug right now. {hug_emoji}",
    f"With you I can talk about everything. {smile_emoji}",
    f"You are a great conversationalist. When I communicate with you, I don’t even notice how time flies. {monkey_emoji}",
    f"I get goosebumps from you. {monkey_emoji}",
    f"It is very easy and pleasant to talk with you, you know how to win over guys. {smiling_eyes_emoji}",
    f"I look at you and understand that a person can have a beautiful soul, body and thoughts. {smiling_eyes_emoji}",
    f"If I went on a trip now, I would take only you with me. {hug_emoji}",
    f"Thank you for making me believe that kindred spirits do exist. {smile_to_ears_emoji}",
    f"I am ready to follow you even to the ends of the world, just to look into your beautiful eyes and see your charming smile every day. {hug_emoji}",
    f"You occupy all my thoughts. {smile_to_ears_emoji}",
    f"You inspire me to new ideas. {angel_emoji}",
    f"There is no person more beautiful than you. You make this world a better place. {hug_emoji}",
    f"Thanks to your parents for giving the world such a perfect creature as you. {error_emoji}",
    f"I can't hide my delight when I look at you. {love_emoji}",
    f"I like absolutely everything about you. Your face, your beautiful eyes, your voice, your kind heart, your sensitivity and tenderness, your inner and outer beauty. {love_emoji}",
    f"Stay with me always and I will make you happy. {smiling_eyes_emoji}",
    f"I am ready to look at you 24 hours a day. {smile_emoji}",
    f"I can't wait to see you again. {monkey_emoji}"]
    var = randrange(0, 13)
    bot.send_message(message.chat.id, comp_list[var], reply_markup=markup)

@bot.message_handler(commands=["cats", "Cats"])
def send_cats(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    comp_button = types.KeyboardButton(f"/Compliments")
    cats_button = types.KeyboardButton(f"/Kitties")
    commands_button = types.KeyboardButton(f"/Commands")
    weather_button = types.KeyboardButton(f"/Weather")
    myweather_button = types.KeyboardButton(f"/YourWeather")
    hug_button = types.KeyboardButton(f"/Hug")
    pres_button = types.KeyboardButton(f"/Present")

    markup.add(comp_button, cats_button, commands_button, weather_button, myweather_button, hug_button, pres_button)

    cat1 = open("image/1.jpg", "rb"); cat2 = open("image/2.jpg", "rb"); cat3 = open("image/3.jpg", "rb"); cat4 = open("image/4.jpg", "rb")
    cat5 = open("image/5.jpg", "rb"); cat6 = open("image/6.jpg", "rb"); cat7 = open("image/7.jpg", "rb"); cat8 = open("image/8.jpeg", "rb")
    cat9 = open("image/9.jpeg", "rb"); cat10 = open("image/10.jpg", "rb"); cat11 = open("image/11.jpeg", "rb"); cat12 = open("image/12.jpeg", "rb")
    cat13 = open("image/13.jpeg", "rb"); cat14 = open("image/14.jpeg", "rb"); cat15 = open("image/15.jpeg", "rb")
    cat16 = open("image/16.jpeg", "rb"); cat17 = open("image/17.jpeg", "rb"); cat18 = open("image/18.jpeg", "rb")
    cat32 = open("image/32.jpg", "rb"); cat33 = open("image/33.jpg", "rb")
    cat34 = open("image/34.jpg", "rb"); cat35 = open("image/35.jpg", "rb"); cat36 = open("image/36.jpg", "rb")
    cat37 = open("image/37.jpg", "rb"); cat38 = open("image/38.jpg", "rb"); cat39 = open("image/39.jpg", "rb")
    cat40 = open("image/40.jpg", "rb"); cat41 = open("image/41.jpg", "rb"); cat42 = open("image/42.jpg", "rb")
    cat43 = open("image/43.jpg", "rb"); cat44 = open("image/44.jpg", "rb"); cat45 = open("image/45.jpg", "rb")
    cat46 = open("image/46.jpg", "rb"); cat47 = open("image/47.jpg", "rb"); cat48 = open("image/48.jpg", "rb")
    cat49 = open("image/49.jpg", "rb"); cat50 = open("image/50.jpg", "rb")

    cats = [cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10, cat11,
        cat12, cat13, cat14, cat15, cat16, cat17, cat18, cat32, cat33, cat34,
        cat35, cat36, cat37, cat38, cat39, cat40, cat41,cat42, cat43, cat44,
        cat45, cat46, cat47, cat48, cat49, cat50]

    var = randrange(0, 37)
    bot.send_photo(message.chat.id, cats[var], reply_markup=markup)

@bot.message_handler(commands=["present", "Present"])
def present(message):
    present = ""
    for me in (0, 101):
        present = me * rose_emoji

    bot.send_message(message.chat.id, present)

@bot.message_handler(commands=["commands", "Commands"])
def commands(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    comp_button = types.KeyboardButton(f"/Compliments")
    cats_button = types.KeyboardButton(f"/Kitties")
    commands_button = types.KeyboardButton(f"/Commands")
    weather_button = types.KeyboardButton(f"/Weather")
    myweather_button = types.KeyboardButton(f"/YourWeather")
    hug_button = types.KeyboardButton(f"/Hug")
    pres_button = types.KeyboardButton(f"/Present")

    markup.add(comp_button, cats_button, commands_button, weather_button, myweather_button, hug_button, pres_button)

    bot.send_message(message.chat.id, f"Just send me a command  {bye_emoji}\n<i><b>(Without emoji)</b></i>",
    parse_mode="html")
    bot.send_message(message.chat.id,
    f"1. <i>/сompliment</i> {comp_emoji}\n2. <i>/сats</i> {cats_emoji}\n 3. <i>/commands</i> {robot_emoji}\n 4. <i>/weather</i> {weather_emoji}\n"
    f"5. <i>/yourWeather</i> {love_emoji}\n6. <i>/hug</i> {hug_emoji}\n7. <i>/present</i> {rose_emoji}",
    parse_mode="html", reply_markup=markup)

@bot.message_handler(commands=["Weather", "weather"])
def weather(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    comp_button = types.KeyboardButton(f"/Compliments")
    cats_button = types.KeyboardButton(f"/Kitties")
    commands_button = types.KeyboardButton(f"/Commands")
    weather_button = types.KeyboardButton(f"/Weather")
    myweather_button = types.KeyboardButton(f"/YourWeather")
    hug_button = types.KeyboardButton(f"/Hug")
    pres_button = types.KeyboardButton(f"/Present")

    markup.add(comp_button, cats_button, commands_button, weather_button, myweather_button, hug_button, pres_button)
    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"
    }

    try:
        city = "naberezhnye chelny"
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data['main']['temp']

        weather_discription = data["weather"][0]["main"]
        if weather_discription in code_to_smile:
            wd = code_to_smile[weather_discription]
        else:
            wd = "look out the window I can't recognize the weather!"

        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])


        bot.send_message(message.chat.id, f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}***\n"
            f"Weather in your town, Sunshine:\nTemperature: {cur_weather}°C {wd}\n"
            f"humidity: {humidity}%\nwind: {wind} м/с\n"
            f"sunrise: {sunrise_timestamp}\nЗакат sunset: {sunset_timestamp}\n"
            f"Have a nice day!",
            reply_markup=markup
            )

    except:
        print("check your city")


@bot.message_handler(commands=["YourWeather", "yourweather", "Youreather","yourWeather"])
def weather(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    comp_button = types.KeyboardButton(f"/Compliments")
    cats_button = types.KeyboardButton(f"/Kitties")
    commands_button = types.KeyboardButton(f"/Commands")
    weather_button = types.KeyboardButton(f"/Weather")
    myweather_button = types.KeyboardButton(f"/YourWeather")
    hug_button = types.KeyboardButton(f"/Hug")
    pres_button = types.KeyboardButton(f"/Present")

    markup.add(comp_button, cats_button, commands_button, weather_button, myweather_button, hug_button, pres_button)

    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"
    }

    try:
        city = "varna"
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data['main']['temp']

        weather_discription = data["weather"][0]["main"]
        if weather_discription in code_to_smile:
            wd = code_to_smile[weather_discription]
        else:
            wd = "look out the window I can't recognize the weather!"

        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])


        bot.send_message(message.chat.id, f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}***\n"
            f"Weather in my town {angel_emoji}: \n\nTemperature: {cur_weather}°C {wd}\n"
            f"Humidity: {humidity}%\nВетер: {wind} м/с\n"
            f"Sunrice: {sunrise_timestamp}\nSunset: {sunset_timestamp}\n"
            f"Have a nice day!",
            reply_markup=markup
            )

    except:
        print("check your city")

@bot.message_handler(commands=["Hug", "hug"])
def hugs(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    comp_button = types.KeyboardButton(f"/Compliments")
    cats_button = types.KeyboardButton(f"/Kitties")
    commands_button = types.KeyboardButton(f"/Commands")
    weather_button = types.KeyboardButton(f"/Weather")
    myweather_button = types.KeyboardButton(f"/YourWeather")
    hug_button = types.KeyboardButton(f"/Hug")
    pres_button = types.KeyboardButton(f"/Present")

    markup.add(comp_button, cats_button, commands_button, weather_button, myweather_button, hug_button, pres_button)

    gif = open("gif/hug.gif", "rb")
    bot.send_animation(message.chat.id, gif)
    bot.send_message(message.chat.id, f"I love you {love_emoji}", reply_markup=markup)

#-------------------------------

@bot.message_handler()   
def get_user_text(message):
    if message.text:
        bot.send_message(message.chat.id, f"I’m sorry, I looked at you and I lost my thought. Could you do it again? {error_emoji}. <b>Напиши</b> /команды", parse_mode="html")


bot.polling(none_stop=True)