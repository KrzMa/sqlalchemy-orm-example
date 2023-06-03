from random import choice

from sqlalchemy.exc import IntegrityError

from models import Base, Author, Article, Hashtag
from session import session
from faker import Faker


def create_authors(count=100):
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


def create_articles(author_id, count=100):
    return [
        create_article(author_id)
        for _ in range(count)
    ]


def create_hashtag(count=10):
    fake = Faker()

    hashtags = set()
    while len(hashtags) < count:
        hashtags.add(fake.word())

    return [
        Hashtag(name=hashtag)
        for hashtag in hashtags
    ]


def assign_hashtag_to_article(hashtags, articles):
    for article in articles:
        hashtag = choice(hashtags)
        article.hashtags.append(hashtag)


def main():
    # create all tables
    Base.metadata.create_all()

    # create authors
    authors = create_authors(500)
    for author in authors:
        try:
            session.add(author)
            session.commit()
        except IntegrityError:
            session.rollback()
            print(f'Authors: {author.login} already exists')

    # create articles
    author = choice(authors)
    articles = create_articles(author_id=author.id)
    session.add_all(articles)
    session.commit()

    # Create hashtags
    hashtags = create_hashtag(count=100)
    try:
        session.add_all(hashtags)
        session.commit()
    except IntegrityError:
        session.rollback()

    # Assign hashtags to articles
    assign_hashtag_to_article(hashtags, articles)
    session.commit()


if __name__ == "__main__":
    main()
