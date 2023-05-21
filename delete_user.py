from  session import session
from models import User


def main():
    user = session.query(User).get(124)
    if user is None:
        print('User with id 124 not found')

    session.delete(user)
    session.commit()

    user = session.query(User).get(124)
    if user is None:
        print('User with id 124 deleted')
    else:
        print('User with id 124 not deleted')


if __name__ == '__main__':
    main()