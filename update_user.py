from session import session
from models import Author


def main():
    user = session.query(Author).get(42)
    if user is None:
        print('User with id 42 not found')
        return

    print(f'Found {user}')
    print(f'Previous salary: {user.salary}')

    user.salary *= 1.15

    session.add(user)
    session.commit()

    user = session.query(Author).get(42)
    print(f'Previous salary: {user.salary}')


if __name__ == "__main__":
    main()
