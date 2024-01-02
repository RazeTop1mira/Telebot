from DicMader import DicMader
def userid_func(id, username):
    userids = DicMader()
    if username != 0:
        '''
        for exist_id, exist_username in userid.items():
            if id != exist_id:
                with open('usersid.txt', 'a') as file:
                    file.write(f'{id} {username}\n')
                break
        '''
        if str(id) not in userids:
            print('New user')
            with open('usersid.txt', 'a') as file:
                file.write(f'{id} {username}\n')

    return userids
