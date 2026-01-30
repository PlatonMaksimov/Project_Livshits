# Организовать словарь 10 русско- английских слов, обеспечивающий "перевод"
# русского слова на английского.

def create_translation_dictionary():
    translation = {
        'дом': 'house',
        'кот': 'cat',
        'солнце': 'sun',
        'вода': 'water',
        'книга': 'book',
        'яблоко': 'apple',
        'школа': 'school',
        'машина': 'car',
        'окно': 'window',
        'друг': 'friend'
    }
    return translation


def translate(translation_dict, russian_word):
    try:
        word_lower = russian_word.strip().lower()

        if not word_lower:
            return "Ошибка: введена пустая строка"

        if word_lower in translation_dict:
            return translation_dict[word_lower]
        else:
            return f"Ошибка: слово '{russian_word}' не найдено в словаре"

    except AttributeError:
        return "Ошибка: введено некорректное значение (ожидается строка)"
    except Exception as e:
        return f"Неожиданная ошибка: {e}"


def main():
    dict_data = create_translation_dictionary()

    print("=" * 50)
    print("РУССКО-АНГЛИЙСКИЙ ПЕРЕВОДЧИК")
    print("=" * 50)
    print(f"Словарь содержит {len(dict_data)} слов:")

    for i, (russian, english) in enumerate(dict_data.items(), 1):
        print(f"{i:2}. {russian:10} -> {english}")

    print("\n" + "=" * 50)
    print("ПРИМЕРЫ ПЕРЕВОДА:")
    print("=" * 50)

    test_words = ['дом', 'кот', 'солнце', 'собака', '', 123]

    for word in test_words:
        result = translate(dict_data, word)
        print(f"'{word}' -> {result}")

    print("\n" + "=" * 50)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ")
    print("=" * 50)
    print("Введите русское слово для перевода (или 'выход' для завершения):")

    while True:
        try:
            user_input = input("\nВаше слово: ").strip()

            if user_input.lower() == 'выход':
                print("Работа переводчика завершена. До свидания!")
                break

            # Передаем словарь dict_data, а не перезаписываем его
            result = translate(dict_data, user_input)
            print(f"Перевод: {result}")

        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            break
        except EOFError:
            print("\n\nЗавершение работы.")
            break
        except Exception as e:
            print(f"\nОшибка ввода: {e}")


if __name__ == "__main__":
    main()