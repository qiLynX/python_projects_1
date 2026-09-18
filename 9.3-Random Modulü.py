import random
result = dir(random)
#result1 = help(random)

result = random.random() #0.0 - 1.0 arasında bir sayı üretir.
result1 = random.uniform(10,100) #10 ile 100 arasında sayı üretir.
result2 = random.randint(1,10) #1 ile 10 arasında integer(tam sayı) üretir.
names = ['ali', 'yağmur', 'deniz', 'cenk']

#result3= names[random.randint(0,len(names)-1)]

result4 = random.choice(names)

print(result)
print(result1)
print(result2)

#print(result3)

print(result4)

liste = list(range(10))

random.shuffle(liste) # listeyi karıştırarak yazmamızı sağlar
print(liste)

liste = range(100)
result5 = random.sample(liste,3) #3 tane 0 ile 100 arasında sayı yazmamızı sağlar.
print(result5)