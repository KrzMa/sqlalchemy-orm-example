from models import Base, User
from session import session
from faker import Faker


def create_user(count=50):
    fake = Faker()
    return [
        User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            user_name=fake.user_name(),
            salary=fake.pyfloat(
                min_value=4000,
                max_value=10_000,
            ),
            email=fake.email(),

        )
        for _ in range(count)
    ]


def main():
    # Create all tables
    Base.metadata.create_all()

    #Create users
    users = create_user()

    session.add_all(users)
    session.commit()


if __name__ == '__main__':
    main()
