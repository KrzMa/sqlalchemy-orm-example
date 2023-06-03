from random import choice

from faker import Faker
from sqlalchemy.exc import IntegrityError

from models import Base, Author, Article
from session import session


def create_authors(count=50):
    fake = Faker()
    return [
        Author(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            login=fake.user_name(),
            salary=fake.pyfloat(
                min_value=4000,
                max_value=10_000
            ),
            email=fake.email(),
        )
        for _ in range(count)
    ]


def create_article(author_id):
    fake = Faker()
    return Article(
        title=fake.sentence(),
        content=fake.text(),
        author_id=author_id,
    )


def create_articles(author_id, count=10):
    return [
        create_article(author_id)
        for _ in range(count)
    ]


def main():
    # Create all tables
    Base.metadata.create_all()

    # Create authors
    authors = create_authors(count=1000)
    for author in authors:
        print(f"Adding author {author.login}")
        try:
            session.add(author)
            session.commit()
        except IntegrityError:
            session.rollback()
            print(f"Author {author.login} already exists")

    # Create articles
    author = choice(authors)
    articles = create_articles(author_id=author.id)
    session.add_all(articles)
    session.commit()


if __name__ == "__main__":
    main()