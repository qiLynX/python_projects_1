numbers = [1,2,3,4,5]

for i in numbers:
    print(i)

names = ['Bora', 'Onur', 'Aydın']

for name in names:
    print(f'my name is {name}') #Alt alta sırayla cğmleleri yazmayı sağlar

name = 'Bora Aydın'

for n in name: 
    print(n) #Burada ise string ifadeyi bir küme olarak alıp her harfi alt alta tek tek yazar


tuple = [(1,2),(3,4),(5,6)]

for t in tuple:
    print(t)

for a,b in tuple:
    print(a,b)

d = {'k1':1, 'k2':2, 'k3':3}

for key,value in d:
    print(key, value)