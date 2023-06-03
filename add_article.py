from models import Article, Author
from session import session, commit_on_success


@commit_on_success
def main():
    answer = input('Do you want to add article? Y/N: ')

    if answer.lower() == 'y':
        run = True
    else:
        run = False

    while run:
        login = input('Provide author login: ')

        author = session.query(Author).filter_by(login=login).first()
        if author is None:
            print(f'Author {login} not found')
            continue

        title = input('Provide article title: ')
        content = input('Provide article content: ')

        article = Article(title=title, content=content)
        author.articles.append(article)

        print(f'Aritcle {title} added')

        answer = input('Do you want to add article? Y/N: ')

        if answer.lower() != 'y':
            run = False


if __name__ == '__main__':
    main()
