import re
import bs4
from requests import get
from fake_headers import Headers


HEADERS = Headers(os='win', headers=True).generate()
url = 'https://habr.com'
target_url = '/ru/all/'
start_url = url + target_url


def cook_soup(link):
    res = get(link, headers=HEADERS)
    text = res.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    return soup


# вспомогательная функция - поиск из превью статей будет выполняться по первым 10 страницам ленты Habr
def repeat_find():
    page_count = 1
    all_urls = set()
    all_urls.add(start_url)
    while page_count < 10:
        page_count += 1
        repeating_url = f'{url}{target_url}page{page_count}/'
        all_urls.add(repeating_url)
    return all_urls


# вспомогательная функция - отбор уникальных слов внутри отдельной статьи
def dive_into_article(full_article_url):
    vocabulary = set()
    dish = cook_soup(full_article_url)
    text = dish.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2').find_all(
        'p')
    # сколько будет абзацев, столько и повторений цикла
    for i in range(len(text)):  # цикл преобразования абзацев в списки
        line = text[i].text.split()
        for item in line:  # цикл наполнения словаря уникальными словами из статьи
            pattern = re.compile(r'(\w+)')
            words = re.findall(pattern, item)
            vocabulary.update(words)
    return vocabulary


def find_in_preview(keywords):
    for link in repeat_find():
        soup = cook_soup(link)
        articles = soup.find_all('article')
        for article in articles:
            words = article.find_all(class_='tm-article-body tm-article-snippet__lead')
            words = [word.text.strip() for word in words]
            for book in words:
                book = tuple(book.split())
                for entity in book:
                    if entity.lower() in keywords:
                        date = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
                        title = article.find('h2').find('span').text
                        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                        res = f'<{date}> - <{title}> - <{url}{href}>'
                        print(res)
                        break


def find_in_article(keywords):
    soup = cook_soup(start_url)
    articles = soup.find_all('article')
    for article in articles:
        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
        full_article_url = url + href
        vocabulary = dive_into_article(full_article_url)
        for element in vocabulary:
            if element.lower() in keywords:
                wanted_title = article.find("h2").find("span").text
                wanted_href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                wanted_url = url + wanted_href
                res = f'Ключевое слово - "{element}". Статья - "{wanted_title}". Ссылка - {wanted_url} '
                print(res)
                break
