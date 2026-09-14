'''my_list = ['bir',2,True, 5.6]
print(my_list)'''

list1= ['one','two','three']
list2= ['four', 'five', 'six']
numbers= list1 + list2
print(numbers)
print(len(numbers))
print(numbers[2])

userA=['Bora', 21]
userB=['Sude',20]
users=[userA,userB]
print(users) #Böyle yazarsak da [1] yazdığımda ilk listeyi istemiş olurum 
print(users[0][1]) #21'yı yazmamızı sağlar

####################################################################################
#1
araba_listesi=['Bugatti','Mercedes','Opel','Mazda']
print(araba_listesi)
#2
length=len(araba_listesi)
print(length)
#3
ilk_eleman=[araba_listesi[0]]
son_eleman=[araba_listesi[-1]]
print(ilk_eleman)
print(son_eleman)
#4
#araba_listesi[-1]='Toyota'
#print(araba_listesi) #Listedeki son elemanı Toyota ile değiştirir

#5
mercedes_listede_var_mi= 'Mercedes' in araba_listesi
print(mercedes_listede_var_mi)
#6
print(araba_listesi[-2])#Tek bir matrise bakılır 0,1,2 mantığına göre bakılırken
#7
print(araba_listesi[0:3])
#slicing (-e kadar) yaparken [0'dan 3'e] gibi düşünülüp [0,3] yazılır
#Tek eleman seçerken indeks doğrudan o elemanı gösterir, dilimlemede ([başlangıç:bitiş]) 
#ise bitiş değeri dahil olmadığı için ilk 3 elemanı almak adına liste[0:3] yazılır.
#8
araba_listesi[-2]='Toyota'
araba_listesi[-1]='Renault'
print(araba_listesi)
#9 
del araba_listesi[-1]
print(araba_listesi)
#10
print(araba_listesi[::-1])
#11
studentA= ['Yigit Bilgi', 2010, [70,60,70]]
studentB= ['Sena Turan', 1999, [80,80,70]]
studentC= ['Ahmet Turan', 1998, [80,70,90]]

result = f"{studentA[0]} {2026 - studentA[1]} yaşında ve not ortalaması {(studentA[2][0] + studentA[2][1] + studentA[2][2]) / 3}"
print(result)
