#Yöntem 1 
import math as islem

# value = dir(math) math'e dahil olan fonksiyonları gösterir
#value = help(math.factorial) sadece faktöriyelin nasıl kullanıldığını açıklar

value = islem.factorial(5)
print(value)

#Yöntem 2 
from math import *

value = factorial(5)

from math import factorial,sqrt
value1 = factorial(4)
value2 = sqrt(4)
print(value)
print(value1)
print(value2)

def sqrt(x):
    print("x: "+ str(x))

from math import factorial,sqrt,ceil

value = sqrt(9)
print(value)