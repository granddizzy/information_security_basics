import hashlib


def hash_string(input_string, algorithm='sha256'):
    """
    Вычисляет хэш строки.
    :param input_string: строка для хэширования
    :param algorithm: алгоритм хэширования (например, 'md5', 'sha1', 'sha256')
    :return: хэш-значение
    """
    try:
        hasher = hashlib.new(algorithm)
        hasher.update(input_string.encode('utf-8'))
        return hasher.hexdigest()
    except ValueError:
        return f"Ошибка: алгоритм '{algorithm}' не поддерживается."


def hash_file(file_path, algorithm='sha256'):
    """
    Вычисляет хэш файла.
    :param file_path: путь к файлу
    :param algorithm: алгоритм хэширования (например, 'md5', 'sha1', 'sha256')
    :return: хэш-значение
    """
    try:
        hasher = hashlib.new(algorithm)
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return f"Ошибка: файл '{file_path}' не найден."
    except ValueError:
        return f"Ошибка: алгоритм '{algorithm}' не поддерживается."


if __name__ == '__main__':
    print("Выберите режим:")
    print("1. Хэшировать строку")
    print("2. Хэшировать файл")
    choice = input("Введите ваш выбор (1/2): ").strip()

    if choice == '1':
        input_string = input("Введите строку для хэширования: ").strip()
        algorithm = input("Введите алгоритм (md5, sha1, sha256, и т.д.) [по умолчанию sha256]: ").strip() or 'sha256'
        hash_result = hash_string(input_string, algorithm)
        print(f"Результат хэширования: {hash_result}")
    elif choice == '2':
        file_path = input("Введите путь к файлу: ").strip()
        algorithm = input("Введите алгоритм (md5, sha1, sha256, и т.д.) [по умолчанию sha256]: ").strip() or 'sha256'
        hash_result = hash_file(file_path, algorithm)
        print(f"Результат хэширования: {hash_result}")
    else:
        print("Неверный выбор!")
