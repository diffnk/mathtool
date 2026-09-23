import math
import sys

# Предельное значение модуля коэффициентов
MAX_VALUE = 10000

HELP_TEXT = """mathtool — решение уравнений вида A*x^2 + B*x + C = 0

Использование:
    cd mathtool                                если не находит файл
    python mathtool.py                         вывод справки
    python mathtool.py --help                  вывод справки
    python mathtool.py solve                   ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами

Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000."""


def fail(message):
    """Вывести сообщение об ошибке в поток ошибок и завершить работу с кодом 1."""
    print(message, file=sys.stderr)
    sys.exit(1)


def fmt(x):
    """Форматировать корень с тремя знаками после запятой (без «-0.000»)."""
    if round(x, 3) == 0:
        x = 0.0
    return f"{x:.3f}"

def parse_arguments(args):
    """Вернуть кортеж строк (A, B, C) либо None, если коэффициенты
    нужно запросить у пользователя."""
    if len(args) == 0 or args[0] == "--help":
        print(HELP_TEXT)
        sys.exit(0)

    if args[0] != "solve":
        fail(f"ОШИБКА: неизвестная команда '{args[0]}'")

    if len(args) == 1:
        return None

    if len(args) == 7:
        if args[1] != "-a" or args[3] != "-b" or args[5] != "-c":
            fail("ОШИБКА: неизвестный параметр (ожидается -a, -b, -c)")
        return args[2], args[4], args[6]

    fail("ОШИБКА: неверный набор параметров")

def read_coefficients(raw):
    """Получить коэффициенты (с клавиатуры или из параметров) как целые числа."""
    try:
        if raw is None:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        else:
            a, b, c = (int(value) for value in raw)
    except ValueError:
        fail("ОШИБКА: коэффициент не является целым числом")
    except EOFError:
        fail("ОШИБКА: ввод прерван, коэффициенты не получены")
    return a, b, c

def check_range(a, b, c):
    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
        fail("ОШИБКА: значение вне допустимого диапазона")

def solve_linear(b, c):
    """Случай A = 0: уравнение B*x + C = 0."""
    if b == 0:
        fail("ОШИБКА: это не уравнение, неизвестное отсутствует")
    print("Уравнение линейное")
    x = -c / b
    print(f"x = {fmt(x)}")


def solve_quadratic(a, b, c):
    """Случай A != 0: квадратное уравнение."""
    print("Уравнение квадратное")
    d = b * b - 4 * a * c
    print(f"D = {d}")

    if d > 0:
        root = math.sqrt(d)
        x1 = (-b + root) / (2 * a)
        x2 = (-b - root) / (2 * a)
        print(f"x1 = {fmt(x1)}")
        print(f"x2 = {fmt(x2)}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"x = {fmt(x)}")
    else:
        print("Действительных корней нет")


def main():
    raw = parse_arguments(sys.argv[1:])
    a, b, c = read_coefficients(raw)
    check_range(a, b, c)

    if a == 0:
        solve_linear(b, c)
    else:
        solve_quadratic(a, b, c)


if __name__ == "__main__":
    main()