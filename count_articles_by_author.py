from sqlalchemy import func

from session import session
from models import Article, Author


def main():
    # result = session.query(Article.author_id.label('author_id'),
    #                        func.count(Article.author_id).label('total')).group_by(Article.author_id)
    # for record in result:
    #     print(record)

    authors_articles_subquery = session.query(
        Article.author_id.label('author_id'),
        func.count('*').label('total')).group_by(
        Article.author_id
    ).subquery()

    # result = session.query(authors_articles_subquery)
    # print(result)
    #
    # for record in result:
    #     print(record)

    result = session.query(
        Author.first_name,
        Author.last_name,
        authors_articles_subquery.c.total
    ).join(authors_articles_subquery)

    for record in result:
        # print(record, type(record))
        # print(record.first_name)
        print(record.first_name,
              record.last_name,
              record.total)


if __name__ == '__main__':
    main()
