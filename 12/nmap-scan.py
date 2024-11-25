import nmap

def scan_host(host):
    nm = nmap.PortScanner()

    try:
        print(f"Проверка доступности хоста {host}...")
        nm.scan(hosts=host, arguments='-sn')
        if nm.all_hosts() and nm[host].state() == 'up':
            print(f"Хост {host} доступен. Начинаем сканирование...\n")
        else:
            print(f"Хост {host} недоступен.")
            return

        # Основное сканирование портов
        nm.scan(hosts=host, arguments='-Pn -sV -O')  # Параметры: сканирование портов, сервисов, ОС
        print(f"IP хоста: {host}")
        print(f"Статус хоста: {nm[host].state()}")

        # Открытые порты и сервисы
        print("\nОткрытые порты и сервисы:")
        results = {"host": host, "state": nm[host].state(), "ports": [], "os": []}
        for proto in nm[host].all_protocols():
            print(f"\nПротокол: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                service = nm[host][proto][port].get('name', 'Неизвестно')
                version = nm[host][proto][port].get('version', 'Неизвестно')
                state = nm[host][proto][port]['state']
                print(f"  Порт: {port}, Сервис: {service}, Версия: {version}, Состояние: {state}")
                results["ports"].append({
                    "port": port,
                    "service": service,
                    "version": version,
                    "state": state
                })

        # Определение операционной системы
        if 'osmatch' in nm[host]:
            print("\nОперационная система хоста:")
            for os in nm[host]['osmatch']:
                print(f"  {os['name']} (точность: {os['accuracy']}%)")
                results["os"].append({
                    "name": os['name'],
                    "accuracy": os['accuracy']
                })

    except Exception as e:
        print(f"Ошибка при сканировании: {e}")


if __name__ == "__main__":
    target_host = input("Введите IP-адрес или хост для сканирования: ")
    scan_host(target_host)
