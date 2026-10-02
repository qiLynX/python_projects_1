def my_decorator(func):
    def wrapper(name):
        print("Fonksiyondan önceki işlemler")
        func(name)
        print("Fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator # @ işareti sayesinde sayHello fonksiyonun içine gönderilir.
def sayHello(name):
    print("Hello",name)
sayHello("Bora")


import math
import time

def calculate_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        time.sleep(1)

        func(*args,**kwargs)

        finish = time.time()
        print("Fonksiyon"+ func.__name__ +" " + str(finish - start)+ "saniye sürdü.")
    return wrapper
@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(number):
    print(math.factorial(number))

usalma(2,3)
faktoriyel(4)



