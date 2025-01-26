
import telebot
from telebot import types

bot = telebot.TeleBot('7920016033:AAFjIldC2rR9Ij8gOTluqMXoU2zy2UkdHZA')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>!✌️\n<i>Я бот - координатор, который будет могать тебе узнавать новости Школы №5 </i>\nНажми 🠖 /go , чтобы увидеть список команд'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['go'])
def comm(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Советник')
    btn2 = types.KeyboardButton('Председатель')
    btn3 = types.KeyboardButton('Совет')
    btn4 = types.KeyboardButton('Группа VK')



    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Выберите нужный пункт:\n/deputy - Советник\n/chairman - Председатель ДП\n/soviet - Совет\n/vk - Группа ВК', reply_markup=markup)

@bot.message_handler(commands=['deputy'])
def deputy(message):
    photo1 = open('deputy.jpg', 'rb')
    bot.send_photo(message.chat.id, photo1, f'<i><b>Романова Марина Геннадьевна</b> - советник директора по воспитанию и взаимодействию с детскими общественными объединениями.</i>\n\nСоветник директора по воспитанию - это человек, который помогает ученикам раскрывать их таланты, мотивировать на участие в конкурсах и помогает духовно развиваться.\n\n По всем возникающим вопросами обращаться в <u>309 кабинет</u>.', parse_mode='html')
    bot.send_message(message.chat.id,'Вы можете также узнать о:\nПредседатель Совета Первых -> /chairman\nШкольный совет -> /soviet\nГруппа ВК -> /vk')

@bot.message_handler(commands=['chairman'])
def chairman(message):
    photo2 = open('chairman.jpg', 'rb')
    bot.send_photo(message.chat.id, photo2, '<i><b>Богачева Ольга Юрьевна</b> - председатель первичного отделения МБОУ «СОШ №5» и муниципального отделения по г.о. Ступино.</i>\n<i> Участник Движения Первых.</i>\n\nПредседатель первичного отделения организовывает деятельность совета, привлекает учащихся учавствовать в мероприятиях и взаимодействует с местными региональными отделениями Движения Первых', parse_mode='html')
    bot.send_message(message.chat.id,
                     'Вы можете также узнать о:\nСоветник директора по воспитанию -> /deputy\nШкольный совет -> /soviet\nГруппа ВК -> /vk')

@bot.message_handler(commands=['vk'])
def vk(message):
    soob = f'<i>Переходи в нашу школьную группу в ВКонтакте, чтобы узнать больше</i> ⚡️\n https://vk.com/club217139989'
    bot.send_message(message.chat.id, soob, parse_mode='html')

@bot.message_handler(commands=['soviet'])
def soviet(message):
    media = [
        telebot.types.InputMediaPhoto(open('soviet1.jpg', 'rb'), caption='<b>Ученический совет</b> - это орган школьного самоуправления, который создан для решения различных вопросов и организации мероприятий в школе. В его состав входят наиболее активные представители 8-11 классов, которые берут на себя ответственность за определенные направления работы.', parse_mode='html'),
        telebot.types.InputMediaPhoto(open('s2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('s3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('s4.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('s5.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('s6.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('s7.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('s8.jpg', 'rb')),
    ]

    bot.send_media_group(message.chat.id, media)
    bot.send_message(message.chat.id,
                     'Вы можете также узнать о:\nСоветник директора по воспитанию -> /deputy\nПредседатель Совета Первых -> /chairman\nГруппа ВК -> /vk')


@bot.message_handler()
def user_message(message):
    if message.text == 'Группа ВК':
        soob = f'<i>Переходи в нашу школьную группу в ВКонтакте, чтобы узнать больше</i> ⚡️\n https://vk.com/club217139989'
        bot.send_message(message.chat.id, soob, parse_mode='html')
    if message.text == 'Советник':
        photo1 = open('deputy.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1,
                       f'<i><b>Романова Марина Геннадьевна</b> - советник директора по воспитанию и взаимодействию с детскими общественными объединениями.</i>\n\nСоветник директора по воспитанию - это человек, который помогает ученикам раскрывать их таланты, мотивировать на участие в конкурсах и помогает духовно развиваться.\n\n По всем возникающим вопросами обращаться в <u>309 кабинет</u>.',
                       parse_mode='html')
        bot.send_message(message.chat.id,
                         'Вы можете также узнать о:\nПредседатель Совета Первых -> /chairman\nШкольный совет -> /soviet\nГруппа ВК -> /vk')
    if message.text == 'Председатель':
        photo2 = open('chairman.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2,
                       '<i><b>Богачева Ольга Юрьевна</b> - председатель первичного отделения МБОУ «СОШ №5» и муниципального отделения по г.о. Ступино.</i>\n<i> Участник Движения Первых.</i>\n\nПредседатель первичного отделения организовывает деятельность совета, привлекает учащихся учавствовать в мероприятиях и взаимодействует с местными региональными отделениями Движения Первых',
                       parse_mode='html')
        bot.send_message(message.chat.id,
                         'Вы можете также узнать о:\nСоветник директора по воспитанию -> /deputy\nШкольный совет -> /soviet\nГруппа ВК -> /vk')
    if message.text == 'Совет':
        media = [
            telebot.types.InputMediaPhoto(open('soviet1.jpg', 'rb'),
                                          caption='<b>Ученический совет</b> - это орган школьного самоуправления, который создан для решения различных вопросов и организации мероприятий в школе. В его состав входят наиболее активные представители 8-11 классов, которые берут на себя ответственность за определенные направления работы.',
                                          parse_mode='html'),
            telebot.types.InputMediaPhoto(open('s2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('s3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('s4.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('s5.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('s6.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('s7.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('s8.jpg', 'rb')),
        ]

        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id,
                     'Вы можете также узнать о:\nСоветник директора по воспитанию -> /deputy\nПредседатель Совета Первых -> /chairman\nГруппа ВК -> /vk')

bot.polling(none_stop=True)