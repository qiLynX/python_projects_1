import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]
print(result)

result = numbers[:3] #başlangıçtan üçüncüye kadar
print(result)

result = numbers[::-1]
print(result)

'''

'''
numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
print(numbers2)

result = numbers2[0,2]
print(result)

result = numbers2[:,2]
print(result)

arr1 = np.arange(0,10)
arr2 = arr1 #referans
print(arr1)
print(arr2)
arr2[0] = 20 #bellek üstündeki iki objenin de değerleri değiştirilir. 
print(arr1)
print(arr2)

arr1 = np.arange(0,10)
arr2 = arr1.copy() #bu sefer değişim sadece arr2'yi etkiler

arr2[0] = 20

print(arr1)
print(arr2)