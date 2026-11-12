
import sys
import math

MAX_VALUE = 10000

# Разбор параметров командной строки
args = sys.argv[1:]

if len(args) == 0 or args == ["--help"]:
    print("Решение уравнения A*x^2 + B*x + C = 0")
    print("Использование:")
    print("python mathtool.py")
    print("python mathtool.py --help")
    print("python mathtool.py solve")
    print("python mathtool.py solve -a 1 -b -3 -c 2")
    print(f"Коэффициенты A, B, C должны быть целыми числами до {MAX_VALUE}.")
    sys.exit(0)

if args[0] != "solve":
    print("ОШИБКА: неизвестная команда", file=sys.stderr)
    sys.exit(1)

# Получение коэффициентов
try:
    if len(args) == 1:
        A = int(input("Введите A: "))
        B = int(input("Введите B: "))
        C = int(input("Введите C: "))

    elif len(args) == 7:
        if args[1] != "-a" or args[3] != "-b" or args[5] != "-c":
            print("ОШИБКА: неизвестный параметр", file=sys.stderr)
            sys.exit(1)

        A = int(args[2])
        B = int(args[4])
        C = int(args[6])

    else:
        print("ОШИБКА: неверный набор параметров", file=sys.stderr)
        sys.exit(1)

except ValueError:
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)

except EOFError:
    print("ОШИБКА: ввод данных прерван", file=sys.stderr)
    sys.exit(1)

# Проверка допустимых значений
if abs(A) > MAX_VALUE or abs(B) > MAX_VALUE or abs(C) > MAX_VALUE:
    print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
    sys.exit(1)

# Решение линейного уравнения
if A == 0:
    if B == 0:
        print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
        sys.exit(1)

    print("Уравнение линейное")
    x = -C / B
    print(f"x = {x:.3f}")

# Решение квадратного уравнения
else:
    print("Уравнение квадратное")

    D = B ** 2 - 4 * A * C
    print(f"D = {D}")

    if D > 0:
        x1 = (-B + math.sqrt(D)) / (2 * A)
        x2 = (-B - math.sqrt(D)) / (2 * A)

        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")

    elif D == 0:
        x = -B / (2 * A)
        print(f"x = {x:.3f}")

    else:
        print("Действительных корней нет")

sys.exit(0)
