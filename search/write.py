from constants.constants import directory, log_file


def write_message(phrase, letters, results): # записує задане слово, задані букви і результат пошуку
    with open(directory, "a", encoding="utf-8") as file:  # а - це дозапис
        file.writelines('In word ' + phrase + " we find such letters " + letters + " result is " + results + "\n")

    print("Success! ")


def log_request (req:'flask request', res: str) -> None: # book version записує запит і відповідь
    with open('vsearch.log', 'a') as log:
        print( str(dir(req)) , res,  file=log)



def reading_log_file():
    try:
        with open('vsearch.log', 'r', encoding="utf-8") as file:
            read_content = file.read()
            #print(read_content)
    except FileNotFoundError:
        print("Файл не знайдено.")

    return read_content


reading_log_file()