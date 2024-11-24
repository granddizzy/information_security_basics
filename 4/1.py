import pandas as pd

try:
    # Чтение исходного файла
    df = pd.read_excel('./list.xlsx')

    # Список для хранения всех мер
    all_measures = []

    # Разделение строки на отдельные меры и очистка данных
    for item in df['Меры защиты'].dropna():  # Пропускаем пустые значения
        measures = item.replace('_x000d_', '').split(';')  # Разделение по ';'
        all_measures.extend([measure.strip() for measure in measures if measure.strip()])  # Очистка пробелов

    # Подсчёт частоты мер
    measure_counts = {}
    for measure in all_measures:
        measure_counts[measure] = measure_counts.get(measure, 0) + 1

    # Создание итогового списка
    result = []
    for measure, count in measure_counts.items():
        code, *name_parts = measure.split(' ', 1)  # Разделяем код и название меры
        name = name_parts[0] if name_parts else ''  # Если название отсутствует
        result.append({'Код меры': code,
                       'Наименование меры': name,
                       'Частота совпадений': count})

    # Преобразуем результат в DataFrame
    df_result = pd.DataFrame(result)

    # Сортировка по убыванию частоты совпадений
    df_result.sort_values(by='Частота совпадений', ascending=False, inplace=True)

    # Сохранение результата в Excel
    df_result.to_excel('./result.xlsx', index=False)
    print("Результирующий файл успешно создан: 'result.xlsx'")

except FileNotFoundError:
    print("Ошибка: Файл 'list.xlsx' не найден.")
except KeyError:
    print("Ошибка: В исходном файле отсутствует колонка 'Меры защиты'.")
except Exception as e:
    print(f"Ошибка: Произошла непредвиденная ошибка: {e}")
