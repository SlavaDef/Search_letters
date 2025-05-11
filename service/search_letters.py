def find_letters_in_words(phrase: str, letters: str):
    return sorted(set(phrase).intersection(set(letters)))


 # this method return list of [letter that found in the word and it's count]
def find_letters_in_words_version_second(word, letters):

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

#print(find_letters_in_words_version_second('sunnyday', 'uny'))