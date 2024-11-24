import hashlib
import re

def check_password_strength(password):
    """
    Проверяет сложность пароля.
    :param password: строка пароля
    :return: True, если пароль сложный, иначе False
    """
    if len(password) < 8:
        print("Пароль должен быть не менее 8 символов.")
        return False
    if not re.search(r'[A-Z]', password):
        print("Пароль должен содержать хотя бы одну заглавную букву.")
        return False
    if not re.search(r'[a-z]', password):
        print("Пароль должен содержать хотя бы одну строчную букву.")
        return False
    if not re.search(r'[0-9]', password):
        print("Пароль должен содержать хотя бы одну цифру.")
        return False
    return True

def hash_password(password):
    """
    Генерирует хэш пароля с использованием SHA-256.
    :param password: строка пароля
    :return: хэш-значение пароля
    """
    hasher = hashlib.sha256()
    hasher.update(password.encode('utf-8'))
    return hasher.hexdigest()

def main():
    password = input("Введите пароль: ").strip()
    if check_password_strength(password):
        hashed_password = hash_password(password)
        print(f"Пароль принят. Его хэш-значение: {hashed_password}")
    else:
        print("Попробуйте снова.")

if __name__ == "__main__":
    main()
