from random import randint
def rps_check(msg):
    rps = ["Камень", "Ножницы", "Бумага"]
    pcrnd = randint(0, 2)
    pcselect = rps[pcrnd]
    txt = f"Я выбрал {rps[pcrnd]}\n"
    if msg == rps[pcrnd]:
        txt += "Ничья"
    elif msg == "Камень":
        if rps[pcrnd] == "Ножницы":
            txt += "Ты выиграл"
        else:
            txt += "Ты проиграл"
    elif msg == "Ножницы":
        if rps[pcrnd] == "Бумага":
            txt += "Ты выиграл"
        else:
            txt += "Ты проиграл"
    elif msg == "Бумага":
        if rps[pcrnd] == "Камень":
            txt += "Ты выиграл"
        else:
            txt += "Ты проиграл"
    else:
        txt += "Спать не хочешь?"
    return txt
