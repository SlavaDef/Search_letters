def find_letters_in_words(phrase: str, letters: str):
    return sorted(set(phrase).intersection(set(letters)))  # SET єто множество


print(str(find_letters_in_words('assasins', 'ai')))
#print(find_letters_in_words('ai', 'assasins'))