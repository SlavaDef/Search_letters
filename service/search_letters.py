def find_letters_in_words(phrase: str, letters: str):
    return sorted(set(phrase).intersection(set(letters)))


def find(phrase: str, letters: str) -> list:
    return sorted(list(letter for letter in letters.lower() if letter in phrase.lower()))


 # this method return list of [letter that found in the word and it's count]
def find_letters_in_words_version_second(word, letters) -> list:

        count_dictionary = {}  # empty dictionary
        res = []
        for letter in letters:
            count_dictionary[letter] = 0 # make dictionary with input letters(key) and value = 0
        for letter in word:  # for every letter in word
            if letter in letters:
               count_dictionary[letter] += 1

        for k, v in sorted(count_dictionary.items()):
                #print(k, 'was found ', v, ' time(s)')
              #res.append(''.join(str(k) + ' - was found '+ str(v) + ' time(s),\n'))
              res.append(str(k) + '-' + str(v))

        #return "".join(res)
        return res


def find_letters_in_words_ai(word: str, letters: str) -> list:
    """
    Підраховує кількість входжень заданих літер у слові.

    Args:
        word: Слово для аналізу
        letters: Літери, які потрібно знайти

    Returns:
        Список рядків у форматі 'літера-кількість'
    """
    # Нормалізуємо вхідні дані
    word = word.lower()
    letters = letters.lower()

    # Використовуємо collections.Counter для підрахунку
    from collections import Counter

    # Створюємо словник з початковими нулями для всіх шуканих літер
    count_dictionary = {letter: 0 for letter in letters}

    # Підраховуємо тільки потрібні літери
    word_counter = Counter(char for char in word if char in letters)

    # Оновлюємо словник знайденими значеннями
    count_dictionary.update(word_counter)

    # Формуємо результат
    return [f"{k}-{v}" for k, v in sorted(count_dictionary.items())]


#print(find('hello', 'lo'))

# 1. Додано підтримку кирилиці через нормалізацію введених даних методом `lower()`
# 2. Використано `collections.Counter` для ефективного підрахунку
# 3. Використано словникове включення для ініціалізації
# 4. Додано анотації типів
# 5. Додано докстрінг з описом функції
# 6. Спрощено формування результуючого списку за допомогою list comprehension

#print(find_letters_in_words_ai('привітїївнаувазі', 'іпЇ'))
#print(find_letters_in_words_version_second('7799888', '7'))