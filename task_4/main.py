from hash_table import HashTable


# Инициализация словаря
cache = HashTable(20)

while True:
    url = input("Введите URL страницы (или 'exit' для выхода): ")
    if url.lower() == 'exit':
        break
    html = cache.get_html(url)
    print(html)
    cache.print_table()  # Вывод хэш-таблицы


#  https://www.google.com/
#  https://www.wikipedia.org/
#  https://www.python.org/
#  https://www.google.com/search?q=secret_information