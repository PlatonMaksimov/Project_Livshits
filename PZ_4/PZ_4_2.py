# Дано целое число N (> 1). Вывести наименьшее из целых чисел K, для которых
# сумма 1 + 2 + . . . + K будет больше или равна N, и саму эту сумму.

while True:
    try:
        N = int(input("Введите целое число N (> 1): "))

        if N <= 1:
            print("Ошибка: N должно быть больше 1. Попробуйте снова.")
            continue

        K = 0
        total_sum = 0

        while total_sum < N:
            K += 1
            total_sum += K

        print(f"\nРезультат:")
        print(f"Наименьшее целое число K: {K}")
        print(f"Сумма 1 + 2 + ... + {K} = {total_sum}")
        print(f"Условие выполнено: {total_sum} >= {N}")
        break

    except ValueError:
        print("Ошибка: Введите целое число. Попробуйте снова.")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        break