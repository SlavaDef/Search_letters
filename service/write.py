from utils.constants import directory, log_file, file_from_pc


def write_message(phrase, letters, results): # записує задане слово, задані букви і результат пошуку
    with open(directory, "a", encoding="utf-8") as file:  # а - це дозапис
        file.writelines('Word = ' + phrase + ', finding letters {' + letters + '} *' + results+'*'+'\n')

    print("Success! ")


def log_request (req:'flask request', res: str) -> None: # book version записує запит і відповідь
    try:
        with open('vsearch.log', 'a') as log:
            # записуемо (дозаписуємо) до файлу ті параметри які хочемо бачити в журналі
            print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='***')

    except Exception as e:
        print(e)


def reading_log_file(file_dir):
    try:
        with open(file_dir, 'r', encoding="utf-8") as files:
            read_content = files.read()
    except FileNotFoundError:
        print("Файл не знайдено.")

    return str(read_content)



#print(reading_log_file(file_from_pc))