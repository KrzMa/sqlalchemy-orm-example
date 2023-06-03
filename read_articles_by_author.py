from models import Author, Article
from session import session


def main():
    login = input('Input author login: ')

    author = session.query(Author).filter(Author.login == login).first()
    if author is None:
        print('Author with id 1617 not found')
        return

    articles = session.query(Article).filter_by(author_id=author.id)
    print(f'The list of articles of {author}:')
    for article in articles:
        print(f'- {article}')


if __name__ == '__main__':
    main()
