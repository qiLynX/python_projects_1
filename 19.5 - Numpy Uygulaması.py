import numpy as np
#1
result = np.array([10,15,30,45,60])
print(result)
#2
result = np.arange(5,15)
print(result)
#3
result = np.arange(50,100,5)
print(result)
#4
result = np.zeros(10)
print(result)
#5
result = np.ones(10)
print(result)
#6
result = np.linspace(0, 100, 5)
print(result)
#7
result = np.random.randint(10,30,5)
print(result)
#8
result = np.linspace(-1,1,10) #.uniform da kullanılabilir.
print(result)
#9
matris = np.random.randint(10,50,15).reshape(3,5)
print(matris)
#10
matris = np.random.randint(10,50,15).reshape(3,5)
rowTotal = matris.sum(axis = 1)
colTotal = matris.sum(axis = 0)
print(matris)
print(rowTotal)
print(colTotal)
#11
result = matris.max()
print(result)
result = matris.min()
print(result)
result = matris.mean()
print(result)
#12
result = matris.argmax()
print(result)
result = matris.argmin()
print(result)
#13
arr = np.arange(10,20)
print(arr)
result=arr[0:3]
print(result)
#14
result=arr[::-1]
print(result)
#15
result = matris[0] # [0,1] 1.satır 2.sütun
print(result)
#16
result=matris[1,2]
print(result)
#17
result = matris[:,0]
print(result)
#18
result = matris ** 2
print(result)
#19
ciftler = matris[matris % 2 == 0]
result = ciftler[ciftler>0]

print(result)