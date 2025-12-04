import argparse
import re
import os

def parse_line(line: str):
    parts = re.split(r"[;,\t ]+", line.strip())
    if len(parts) != 6:
        raise ValueError(f"Неверное количество полей: {len(parts)}, ожидалось 6")

    year, month, day, hour, minute, temp = parts

    # Проверяем формат
    if not year.isdigit() or len(year) != 4:
        raise ValueError(f"Некорректный год: {year}")

    if not month.isdigit() or not (1 <= int(month) <= 12):
        raise ValueError(f"Некорректный месяц: {month}")

    if not day.isdigit() or not (1 <= int(day) <= 31):
        raise ValueError(f"Некорректный день: {day}")

    if not hour.isdigit() or not (0 <= int(hour) <= 23):
        raise ValueError(f"Некорректный час: {hour}")

    if not minute.isdigit() or not (0 <= int(minute) <= 59):
        raise ValueError(f"Некорректная минута: {minute}")

    if not re.match(r"^-?\d+$", temp):
        raise ValueError(f"Некорректная температура: {temp}")

    temp = int(temp)
    if not (-99 <= temp <= 99):
        raise ValueError(f"Температура вне диапазона: {temp}")

    return (
        int(year),
        int(month),
        int(day),
        int(hour),
        int(minute),
        temp
    )


def process_file(filename: str):
    if not os.path.exists(filename):
        print(f"Ошибка: файл '{filename}' не найден.")
        return None

    stats = {m: {"sum": 0, "min": 999, "max": -999, "count": 0} for m in range(1, 13)}

    with open(filename, "r") as f:
        for lineno, line in enumerate(f, start=1):
            if not line.strip():
                continue

            try:
                y, m, d, h, mi, t = parse_line(line)
            except ValueError as e:
                print("\nФорматная ошибка:")
                print(f"  строка {lineno}: {e}")
                return None

            stats[m]["sum"] += t
            stats[m]["min"] = min(stats[m]["min"], t)
            stats[m]["max"] = max(stats[m]["max"], t)
            stats[m]["count"] += 1

    return stats


def print_stats(stats, month=None):
    if month:
        month = int(month)
        s = stats[month]
        if s["count"] == 0:
            print("Нет данных за этот месяц.")
            return
        print(f"\nСтатистика за месяц {month:02d}:")
        print(f"  Средняя: {s['sum']/s['count']:.2f}")
        print(f"  Минимальная: {s['min']}")
        print(f"  Максимальная: {s['max']}")
        return

    # Печать всех месяцев
    print("\n=== ПОМЕСЯЧНАЯ СТАТИСТИКА ===\n")
    for m in range(1, 13):
        s = stats[m]
        if s["count"] == 0:
            print(f"Месяц {m:02d}: данных нет.\n")
            continue
        print(f"Месяц {m:02d}:")
        print(f"  Средняя температура: {s['sum']/s['count']:.2f}")
        print(f"  Минимальная: {s['min']}")
        print(f"  Максимальная: {s['max']}\n")


def main():
    parser = argparse.ArgumentParser(description="CSV temperature parser")
    parser.add_argument("-f", "--file", help="CSV файл для обработки")
    parser.add_argument("-m", "--month", help="Показать статистику только за месяц (1-12)")
    args = parser.parse_args()

    if not args.file:
        parser.print_help()
        return

    stats = process_file(args.file)
    if stats:
        print_stats(stats, month=args.month)


if __name__ == "__main__":
    main()
