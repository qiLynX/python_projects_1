#range()
'''for i in range(10):
    print(i) #1'den 10'a kadar sayıları yazmamızı sağlar.

for x in range (50,100,10):
    print(x) #50'den 100'e kadar 10'ar 10'ar yazmamızı sağlar
print(list(range(5,100,10))) #Liste halinde yazmamızı sağlar'''

#enumerate()

greeting = "Hello"

for item in enumerate(greeting):
    print(item)

#zip 

list1= [1,2,3,4,5]
list2= ['a','b','c','d','e']

print(list(zip(list1,list2)))