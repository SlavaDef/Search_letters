import csv
import pprint # для виведення не в рядок
from datetime import datetime


file_directory = 'C:/Users/Admin/Desktop/Files/fly.csv'

def convert2ampm(time24: str) -> str: # Функція приймає час і конвертує його у 12 годинний + додає PM чи AM
 return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


#with open(file_directory, 'r') as f: # звичайне считання
    #print(f.read())



#with open(file_directory, 'r') as file: # звичайне считання
   # for line in csv.reader(file):
    #for line in csv.reader(file, delimiter=''):
     #   print(line) # ['TIME', 'DESTINATION'] make massiv



#with open(file_directory, 'r') as data: # звичайне считання
  #  for line in csv.DictReader(data):
     #   print(line) #  {'TIME': '09:35', 'DESTINATION': 'FREEPORT'} make dictionary


with open(file_directory, 'r') as f:
    ignore = f.readline() # ігноримо перший рядок (заголовок) TIME,DESTINATION
    flights={}
    for line in f:
        k, v = line.strip().split(',') # '09:35': 'FREEPORT'
        flights[k] = v # make a dictionary with keys = TIME and values = DESTINATION
        # flights[k] = v.replace('\n', '') # '09:35': 'FREEPORT', # another way to delete \n

    #just_freeport2 = {convert2ampm(k): v.title()
                       # for k, v in flights.items()
                       # if v == 'FREEPORT'} # book vers
    #pprint.pprint(just_freeport2)
    #print()

    pprint.pprint(flights)
    flights2 = {}

    #flights3 = {} # another way
    #[flights3.setdefault(v.title(), []).append(convert2ampm(k)) for k, v in flights.items()]
    print()

    for k, v in flights.items():
        # lower().title() робить першу букву в кожному слові великою інші малими
        # створюємо новий словник але значення стають вже ключами + нові значення це вже список
        # до часу додаємо PM якщо час більше 12 (int(k.split(':')[0]) >= 12 розбиваємо по : отримуючи час [0] перші цифри
        #flights2.setdefault(v.lower().title(), []).append(k+'PM' if int(k.split(':')[0]) >= 12 else k+'AM')
        #flights2[convert2ampm(k)] = v.title() book version
        flights2.setdefault(v.title(), []).append(convert2ampm(k))
    pprint.pprint(flights2)
    print()
    for k, v in flights2.items():
        print(k + ' ->', v)
    print()
    #res = [k + ' -> ' + str(v).strip('[]') for k, v in flights2.items()] # позбавляємося дужок + додали ->
    #res2=[str(i.replace("[", "").replace("]", "")) for i in res]
    res = [f"{k} -> {', '.join(v)}" for k, v in flights2.items()]

    for i in res:
        print(i)



#pprint.pprint(flights2) # '09:35': 'FREEPORT\n', one dictionary with
