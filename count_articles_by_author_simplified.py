from sqlalchemy import func

from session import session
from models import Author, Article


def main():
    result = session.query(
        Author.first_name.label('first_name'),
        Author.last_name.label('last_name'),
        func.count('*').label('total')
    ).join(Article).group_by(
        Author.id
    )
    # for author in authors:
    #     if len(author.articles) == 0:
    #         continue
    #     print(
    #         author.first_name,
    #         author.last_name,
    #         len(author.articles)
    #     )
    for record in result:
        print(
            record.first_name,
            record.last_name,
            record.total

        )


if __name__ == '__main__':
    main()
