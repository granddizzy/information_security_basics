import requests
import sys

API_KEY = '122b4076634f65eaaa585443bfb041d82d78395cd05da63724b4a05c093f63f7'
BASE_URL = 'https://www.virustotal.com/api/v3'


def scan_url(url_to_scan):
    headers = {
        'x-apikey': API_KEY
    }
    data = {
        'url': url_to_scan
    }
    response = requests.post(f'{BASE_URL}/urls', headers=headers, data=data)

    if response.status_code == 200:
        analysis_id = response.json().get('data', {}).get('id')
        print(f'URL успешно отправлен. ID анализа: {analysis_id}')
        return analysis_id
    else:
        print('Ошибка при отправке URL:', response.json())
        sys.exit(1)


def get_report(analysis_id):
    headers = {
        'x-apikey': API_KEY
    }
    response = requests.get(f'{BASE_URL}/analyses/{analysis_id}', headers=headers)

    if response.status_code == 200:
        report = response.json()
        print('Отчет:')
        print(report)
        return report
    else:
        print('Ошибка при получении отчета:', response.json())
        sys.exit(1)

if __name__ == '__main__':
    print("1. Отправить URL на проверку")
    print("2. Получить отчет")
    choice = input("Введите ваш выбор (1/2): ").strip()

    if choice == '1':
        url = input("Введите URL для анализа: ").strip()
        analysis_id = scan_url(url)
        print("Сохраните ID анализа для получения отчета.")
    elif choice == '2':
        analysis_id = input("Введите ID анализа: ").strip()
        get_report(analysis_id)
    else:
        print("Неверный выбор!")
