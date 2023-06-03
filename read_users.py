from models import Author
from session import session


def main():
    for user in session.query(Author):
        print(user)


if __name__ == '__main__':
    main()
