'''name = "Bora Aydın"

for letter in name:
    if letter == 'a':
        break
    print(letter) #Bor çıktısını verir Bora Aydın Yerine 

for letter in name:
    if letter == 'r':
        continue #r'yi atlayıp devam eder ve Boa Aydın yazar.
    print(letter)

x = 0 
while x <5:
    x+=1
    if x == 2:
        continue
    print(x)'''

x=0
result=0
while x<=100:
    x+=1
    if x % 2 ==1:
        continue
    result += x
print(f"Toplam: {result}") #Bu işlemle tek sayılar dahil edilmemiş olur.