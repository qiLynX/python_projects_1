import numpy as np 

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2
print(result)

result = np.sin(numbers1)
print(result)

result = np.cos(numbers2)
print(result)

result = np.sqrt(numbers1)
print(result)

result = np.log(numbers2)
print(result)

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)
print(mnumbers1)
print(mnumbers2)

result = np.vstack((mnumbers1,mnumbers2))#dikey olarak sonuçları birleştirir.
print(result)

result = np.hstack((mnumbers1,mnumbers2))#yatay olarak sonuçları birleştirir.
print(result)


result = numbers1 >= 50 #True/False olarak listede bir  dönüt çıkar.
print(result)