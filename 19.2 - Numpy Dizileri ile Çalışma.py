import numpy as np

result = np.array([1,3,5,7,9])

print(result)

result = np.arange(1,100,3) #1 ile 100 arasında üçerli artan dizi oluşturma
print(result)
#np.zeros(10) ve np.ones(10) sırasıyla 0'lardan oluşan dizi ve 1'lerden oluşasn dizi oluşturur

result = np.linspace(0,100,5) #başlangıçta bitiş değerlerini eşit olarak bölerek yazar
print(result)

result = np.random.randint(20)
print(result)
result = np.random.randint(1,20,3)
print(result)

np_array = np.arange(50)
np_multi = np_array.reshape(5,10)
print(np_multi.sum(axis=1))

rnd_numbers = np.random.randint(0,100,10)
result=rnd_numbers.max()
print(result)
