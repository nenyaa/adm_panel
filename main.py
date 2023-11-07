from data.data import users


def show_users(users: list) -> None:
    for item in user_generator(users):
        print(item)


def user_generator(userlist: list):
    for user in userlist:
        yield user


def main() -> None:
    show_users(users)


if __name__ == '__main__':
    main()
