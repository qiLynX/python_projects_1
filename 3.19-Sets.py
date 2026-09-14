fruits = {'orange', 'apple', 'banana'} #Liste (indekslenemeyen bir liste)
#print(fruits[0]) yazılamaz

for x in fruits :
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape'])
print(fruits)

myList = [1,2,3,4,5]
print(myList)
print(set(myList))

fruits.remove('mango')
fruits.discard('apple')

fruits.pop()
print(fruits)