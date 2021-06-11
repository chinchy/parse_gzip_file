import gzip
from os.path import exists


def parse_gzip_file(path: str) -> dict:
    data = {}

    if not exists(path) and path.endswith('.gz'):
        print(f'Файл {path} не найден!')
        return data

    with gzip.open(path, mode='rt') as f:
        key = ""
        for line in f:
            if not line.strip():  # Защита от пустой строки
                key = ""
                continue
            elif line.count(':'):  # Обработка строки с ключом
                key, value = line.split(':')
                value = value.strip()
            else:                  # Обработка строки без ключа
                value = line.strip()

            if key in data:  # Сохранение многострочности
                value = '\n' + value

            if key and not value.startswith('#'):  # Защита от комментариев
                data[key] = data.get(key, '') + value
    return data


def load_data(path: str):
    parsed_data = parse_gzip_file(path)

    for document in parsed_data:
        pass
        # load document to database (or do something else)
