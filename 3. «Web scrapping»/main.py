from scrapper import find_in_preview, find_in_article

if __name__ == '__main__':
    # определяем список ключевых слов
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    # Ваш код
    find_in_preview(KEYWORDS)
    print()
    find_in_article(KEYWORDS)
