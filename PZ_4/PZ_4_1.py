# Дано целое число N (>0). Найти значение выражения 1.1 - 1.2 + 1.3 - ... (N слагаемых,
# знаки чередуются). Условный оператор не использовать.

while True:
    try:
        N = int(input("Введите целое число N (> 0): "))

        if N <= 0:
            raise ValueError("N должно быть больше 0")

        total = 0.0
        i = 1
        sign = 1

        while i <= N:
            term = 1 + i * 0.1
            total += sign * term
            sign *= -1
            i += 1

        print(f"Результат выражения для N = {N}: {total:.6f}")
        break

    except ValueError as e:
        if "N должно быть больше 0" in str(e):
            print("Ошибка: N должно быть целым числом больше 0!")
        else:
            print("Ошибка: Введите целое число!")