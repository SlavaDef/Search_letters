from itertools import count


class CountFromBy:

    #start = 0

    def __init__(self, step=1):
            self.count = 0
            self.step = step


    def __repr__(self) -> str: # метод на кшталт toString
        return str(self.count)+" And "+str(self.step)



    def increase(self):
            self.count +=1
            return self.count


    def increase2(self, custom_step=None):
        if custom_step is not None:
            self.count += custom_step
        else:
            self.count += self.step
        return self.count


a = CountFromBy(step=10)
b = CountFromBy() # в конструкторі задили значення за замоічуванням отже обькт можна створювати як з так і без
b.increase()
print(b)
a.increase2()
a.increase2()
a.increase2()
print(a.count)
#a.increase2()

#print(a.increase2(100, 10))


# - В додано параметр з значенням за замовчуванням 1 `__init__``step`
# - Метод тепер може приймати необов'язковий параметр `custom_step` `increase`
# - Якщо `custom_step` не вказано, використовується значення з конструктора `step`
# - Якщо `custom_step` вказано, використовується саме воно
#
# Тепер ви можете:
# 1. Створювати лічильник з будь-яким кроком збільшення
# 2. Змінювати крок збільшення при кожному виклику методу `increase`
# 3. Використовувати стандартний крок (1), якщо інше не вказано