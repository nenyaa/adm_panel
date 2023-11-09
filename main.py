from data.data import users


# read
def show_users(users):
    for user in users:
        print(user)


# create
def add_to(users: list) -> None:
    name = input('podaj imie nowego uzytkownika')
    users.append({'name': name})


# update
def update_user(users: list) -> None:
    name = input('podaj imie uzytkownika do modyfiakcji')
    tmp_list = [user for user in users if user['name'] == name]
    for idx, tmp_user in enumerate(tmp_list):
        print(f'{idx + 1}: {tmp_user["name"]}')
    number = int(input('podaj numer uzytkownika do modyfikacji '))
    new_name = input('podaj nowe imie ')
    for user in users:
        if user == tmp_list[number - 1]:
            user['name'] = new_name


# delete
def remove_user_from(users: list) -> None:
    name = input('podaj imie uzytkownika do usuniecia')
    tmp_list = [user for user in users if user['name'] == name]
    for idx, tmp_user in enumerate(tmp_list):
        print(f'{idx + 1}: {tmp_user["name"]}')
    number = int(input('podaj numer uzytkownika do usuniecia '))
    for user in users:
        if user == tmp_list[number - 1]:
            users.remove(user)


if __name__ == '__main__':
    remove_user_from(users)
    # update_user(users)
    show_users(users)
