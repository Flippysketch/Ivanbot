import telebot
import random
from datetime import datetime, timedelta
# Створюємо об'єкт бота з токеном
bot = telebot.TeleBot('6090119402:AAFjmUvvr1PfL6xKrCSFw6_cnE1_AbOQslk')
# Функція, що відповідає на команду /start
@bot.message_handler(commands=["start"])

def command_start(message):
  
  bot.send_message(message.chat.id, "Привіт... Я найкраще працюю в чаті, дай мені право писати повідомлення і я з радістю з вами поспілкуюсь!")

# Функція, що відповідає на текстові повідомлення
@bot.message_handler(func=lambda message: True, content_types=['text'])
def reply(message):
  if "Як справи?" in message.text:
    answers = ['Погано😭', 'Добре🫤', 'Супер😎', 'Нафіга питаєш🙄', 'Та обісрися🤬']
    response = random.choice(answers)
    # відправляємо відповідь користувачу
    bot.send_message(message.chat.id, response)
  #elif "Мут" in message.text:
    #bot.reply_to(message, "Сам себе замути⛔️")
  #elif "Бан" in message.text:
    #bot.reply_to(message, "Сам себе забань⛔️")
  #elif "мут" in message.text:
   # bot.reply_to(message, "Сам себе замути⛔️")
 # elif "бан" in message.text:
   # bot.reply_to(message, "Сам себе забань⛔️")
  elif "http" in message.text:
    bot.reply_to(message, "Я не буду перевіряти, що там, вірус якийсь")
  #@bot.message_handler(regexp='Бот')
  elif "Бот" in message.text:
  #def smart_handler(message):
    bot.send_message(message.chat.id, "Я тут✅️")
 # if "бот" in message.text:
   # bot.send_message(message.chat.id, "Я тут✅️")
  elif "він топ" in message.text:
    bot.send_message(message.chat.id, "Я знаю")
  elif "Ти топ" in message.text:
    bot.reply_to(message, "Дякую😘")
  #@bot.message_handler(regexp='Іване')
  #def ivan(message):
   # bot.send_message(message.chat.id, "Та що ти хочеш?!😤")
  elif "Ічо" in message.text:
    bot.reply_to(message, "А нічо!😜")
  elif "Слава Україні" in message.text:
    bot.send_message(message.chat.id, "Героям Слава!🇺🇦")
  elif "АХА" in message.text:
    bot.send_message(message.chat.id, "Розсміявся, ледь не всрався🥰")
  elif "Аха" in message.text:
    bot.send_message(message.chat.id, "Ахахахах🤣")
  elif "аха" in message.text:
    bot.send_message(message.chat.id, "Ахахахах🤣")
  elif "Ти тупий" in message.text:
    bot.send_message(message.chat.id, "А ти... е, забувся😲")
  elif "постаратись" in message.text:
    bot.send_message(message.chat.id, "Постарайся😁")
  elif "постарайся" in message.text:
    bot.send_message(message.chat.id, "Постарайся😁")
  elif "Постарайся" in message.text:
    bot.send_message(message.chat.id, "Постарайся😁")
  elif "Ало" in message.text:
    bot.send_message(message.chat.id, "Ми його втратили, вже в пошуках👀")
  elif "нічо" in message.text:
    bot.reply_to(message.chat.id, "Не смій так казати!")
  elif "Я обісрався" in message.text:
    bot.reply_to(message, "Я за тебе радий😃")
  elif "лінь" in message.text:
    bot.reply_to(message, "Треба поборити лінь! Борись!")
  #elif "Спам" in message.text:
    #bot.reply_to(message, "Ок😏")
    #for  in :
       #pass
 #i in range(100):
     #bot.send_message(message.chat.id, "Спам")
    # для чату
 # elif "+" in message.text:
    #bot.reply_to(message, "Повага (+1)")
  #def answer_question(message):
  elif "Іван інфа" in message.text:
    # генеруємо випадковий відсоток від 0 до 100
    percent = random.randint(0, 100)
    username = message.from_user.first_name
    response = f"{username} Я думаю, що {percent}%"
    bot.reply_to(message, response)
  elif "Іван скільки відсотків" in message.text:
    percent = random.randint(0, 100)
    username = message.from_user.first_name
    response = f"{username} Я думаю, що {percent}%"
    bot.reply_to(message, response)
  elif "Іван скільки процентів" in message.text:
    percent = random.randint(0, 100)
    username = message.from_user.first_name
    bot.reply_to(message, f"{username} я російської не розумію🫣")
  elif "!калл" in message.text:
    bot.reply_to(message, "Ок📢")
    for i in range(random.randint(3, 30)):
      bot.send_message(message.chat.id, "Калл")
  elif "Іван анекдот" in message.text:
    bot.reply_to(message, "Колобок повісився💀")
    
    # для чату
 # elif message.reply_to_message and '!Мут5' in message.text:
   # chat_id = message.chat.id
      #  muting_times[user_id] = datetime.now() + timedelta(minutes=5)
       # bot.send_message(chat_id, f"Користувач {message.reply_to_message.from_user.first_name} замучений на 5 хвилин."
  if message.reply_to_message and '!пін' in message.text:
    username = message.from_user.first_name
    bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    #bot.reply_to(message, f"Користувач {username} закріпив повідомлення")
  if "+" in message.text:
    bot.reply_to(message, "Повага (+1)")
  elif "!видалитись" in message.text:
    chat_id = message.chat.id
    user_id = message.from_user.id
    bot.kick_chat_member(chat_id, user_id)
  elif "!видалити" in message.text:
    bot.delete_message(chat_id=message.chat.id, message_id=message.reply_to_message.message_id)

  elif "!шип" in message.text:
    reply_message = message.reply_to_message
    if reply_message is not None:
      username = message.from_user.first_name
      user_name = reply_message.from_user.username
      bot.reply_to(message, f"Шиперим {username} і {user_name}, любіть один одного❤")

   # for member in members:
     # if not member.user.is_bot:
        #group_users.append(member.user.username)

   # return group_users
   # if not group1_users or not group2_users:
     # bot.reply_to(message, "У групі немає достатньо учасників.")
    #  return

   # user1 = random.choice(group1_users)
    #user2 = random.choice(group2_users)

   # bot.reply_to(message, f"@{user1} і @{user2}, любіть один одного ❤️")


    # Список користувачів у групі
  #@bot.message_handler(commands=['mute'])
  #def mute_member(message):
    #if message.from_user.id not in [ADMIN_ID, MODERATOR_ID]:
      #bot.reply_to(message, "Ця команда доступна тільки для адміністраторів і модераторів.")
      #return

    # перевірка чи команда була введена правильно
    #try:
     # member_id, duration = message.text.split()
      #duration = int(duration)
    #except ValueError:
      #bot.reply_to(message, "Неправильний формат команди. Приклад: /mute @username 5")
      #return

    # отримання користувача, якого треба замутити
    #user = bot.get_chat_member(message.chat.id, member_id).user

    # мутування користувача на вказаний час
    #bot.restrict_chat_member(message.chat.#id, user.id, until_date=time.time() + duration * 60)
    #bot.reply_to(message, f"@{user.username} було замутено на {duration} хвилин.")
    #moderator
  #elif "Мут" in message.text:
   # command_args = message.text.split(' ')
   # min = int(command_args[1])
  #  user_id = command_args[2]
    
    # Замутити користувача
   # bot.restrict_chat_member(
        #message.chat.id,
       # user_id,
     #   until_date=time.time() + mute_time * 60  # Обмеження на вказану кількість хвилин
  #  )
    #дії рп
  elif "Вбити" in message.text:
    reply_message = message.reply_to_message
    if reply_message is not None:
      username = message.from_user.first_name
      user_name = reply_message.from_user.username
      bot.reply_to(message, f"{username} вбив користувача {user_name}")
  elif "Потиснути руку" in message.text:
    reply_message = message.reply_to_message
    if reply_message is not None:
      username = message.from_user.first_name
      user_name = reply_message.from_user.username
      bot.reply_to(message, f"{username} потиснув руку користувачеві {user_name}")
  elif "Зайнятись інтимом" in message.text:
    reply_message = message.reply_to_message
    if reply_message is not None:
      username = message.from_user.first_name
      user_name = reply_message.from_user.username
      bot.reply_to(message, f"{username} примусив до інтиму користувача {user_name}")
  #нкція, що відповідає на голосові повідомлення
#@bot.message_handler(content_types=['voice'])
#def reply_voice(message):
 # bot.reply_to(message, "Ти думаєш, я це слухатиму?🤨")
# стікер
@bot.message_handler(content_types=['sticker'])
def reply_link(message):
  stickers = ["Що за тупий стікер🤮", "Вау🤩"]
  bot.reply_to(message, random.choice(stickers))
# Запускаємо бота
bot.polling(none_stop=True)
