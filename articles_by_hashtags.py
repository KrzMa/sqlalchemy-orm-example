from session import session
from models import Hashtag


def main():
    hashtags = session.query(Hashtag).order_by(Hashtag.name)
    for hashtag in hashtags:
        print(f'{hashtag.name}: ')
        if len(hashtag.articles) == 0:
            print('No articles')
            continue

        for article in hashtag.articles:
            print(f'\t- {article.title}')


if __name__ == '__main__':
    main()
