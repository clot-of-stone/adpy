from scrapper import find_in_preview, find_in_article, issue_results

if __name__ == '__main__':
    # определяем список ключевых слов
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    # Ваш код
    issue_results(find_in_preview(KEYWORDS))
    print()
    issue_results(find_in_article(KEYWORDS))
