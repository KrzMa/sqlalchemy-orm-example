from session import session
from models import Article


def main():
    articles = session.query(Article).order_by(Article.publication_date.desc())
    for article in articles:
        print(f'{article.title}: ')
        if len(article.hashtags) == 0:
            print('No hashtags in the article')

        for hashtag in article.hashtags:
            print(f'\t- {hashtag.name}')



if __name__ == '__main__':
    main()
