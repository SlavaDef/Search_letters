

def apply(func, value):
    return func(value)


print(apply(lambda x: x * 2, 5)) # функція приймає якусь функцію і значення


def another_func(value):
    return value * value

print(another_func(5)) # 25
print(apply(another_func, 5)) # 25

apply(print, 'hello')
print(apply(len, 'Marvin'))
print(apply(id, 'Marvin'))


def outer():
    def inner(): # вкладена функція яка визивається в зовнішній функції
        print('This is inner.')

    print('This is outer, invoking inner.')
    inner()

outer()

def outer2():
    def inner2(): # вкладена функція яка визивається в зовнішній функції
        print('This is inner.')

    print('This is outer, invoking inner.')
    return inner2 # важливо без дужок


#outer2() # ретурнім вивід функції inner2

i = outer2()
print(type(i))
i()