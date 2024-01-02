from weekdays import week
from userid_func import userid_func
from DicMader import DicMader
def timetable_checker(msg, id, username):
    userid = userid_func(id, username)
    if len(msg.split()) == 2:
        try:
            if (msg.split()[1].capitalize() in week):
                if msg.split()[1].capitalize() in week:
                    botmsg = DicMader(id)[msg.split()[1].capitalize()]
                    tt = ""
                    for i in range(len(botmsg)):
                        tt += f'{i + 1}. {botmsg[i]}\n'
                    return tt
                else:
                    return 'Извините, такого дня нет в вашем расписании'
            else:
                return 'Пожалуйста, мне нужен день недели, например: "Понедельник"'
        except:
            return 'У вас ещё нет расписания, добавьте его с помощью команды - /timetablechange.\nИли вы отправили расписание в неправильном формате'
    else:
        return 'Будь добр написать день недели, а не просто слово расписание'