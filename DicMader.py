def DicMader(id=None):
    if id == None:
        file = open("usersid.txt")
    else:
        file = open(f"texts/text{id}.txt")
    onstring = file.read().split("\n")[:-1]
    dict = {}

    for item in onstring:
        key = item.split(" ")[0]
        value = item.split(" ")[1:]
        dict[key] = value
    file.close()
    return dict