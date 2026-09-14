x=0

while x <= 100: # -e kadar
    if x % 2 ==1:
        print(f"Sayımız tek: {x}")
    else:
        print(f"Sayımız çift: {x}")
    x+=1

name = '' #False
while not name.strip(): #Sadece boşluk yazılmasını yani "Merhaba,  " olmasını engeller
    name = input('İsminizii Giriniz: ')

print(f"Merhaba {name}")
