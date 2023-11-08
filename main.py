from data.data import users


def show_users(users):
    for user in users:
        print(user)

def main() -> None:
    show_users(users)


if __name__ == '__main__':
    main()
