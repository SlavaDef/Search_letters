
def division(numb, numb2):
    res=0
    try:
         res =  numb/numb2
    except ZeroDivisionError:
           numb2=1
           res = numb / numb2
           print("Can't divide by zero")
    return res


def division2(numb, numb2):
    try:
        return numb / numb2
    except ZeroDivisionError:
        print("Can't divide by zero")
        return numb #  При діленні на нуль просто повертаємо перше число (`numb`)




print(division(10, 0))
print(division2(10, 0))
