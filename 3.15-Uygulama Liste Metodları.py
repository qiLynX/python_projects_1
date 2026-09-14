names= ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998,2000,1998,1987]
#1
names.append('Cenk')
print(names) #Doğru
#2
names.insert(0,'Sena')
print(names) #Doğru
#3
names.remove('Deniz')
print(names) #Doğru
#4
print(names.index('Yağmur')) #Doğru
#5(?)

#6
'''names.reverse()
print(names)
years.reverse()
print(years)''' #Doğru

#7
'''names.sort()
print(names)'''

#8
'''years.sort()
print(years)''' #Doğru

#9(?)
str = "Chevrolet,Dacia"
result=str.split(',')
#print(result)

#10
min=min(years)
print(min)
max=max(years)
print(max)

#11
print(years.count(1998))

#12
'''years.remove()
print(years)'''

#13
'''marka1=input("Bir değer giriniz")
marka2=input("Bir değer giriniz")
marka3=input("Bir değer giriniz")
marka=[]
marka.append(marka1)
marka.append(marka2)
marka.append(marka3)
print(marka)''' #Doğru