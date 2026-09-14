sayilar = [1,3,5,7,9,12,19,21]

#1 
for i in sayilar:
    if i % 3 == 0:
        print(f"Sayılar listesindeki: {i}, 3'ün katıdır.")
    else:
        print(f"Sayılar listesindeki: {i}, 3'ün katı değildir.") #Doğru

#2
toplam = 0
for x in sayilar:
    toplam = toplam + x
print('toplam:', toplam)

#3
for a in sayilar:
    if a %2 == 0:
        print(f"Sayımız çift sayıdır. {a}")
    else:
        karesi= a*a
        print(f"Sayımız ({a}) tektir ve sayımızın karesi {karesi}")

sehirler =['kocaeli', 'istanbul', 'izmir', 'ankara', 'rize']

#4

for sehir in sehirler:
    if len(sehir) <= 5:
        print(sehir)



urunler = [
    {'name': 'samsung S6', 'price': '3000'},
    {'name': 'samsung S7', 'price': '4000'},
    {'name': 'samsung S8', 'price': '5000'},
    {'name': 'samsung S9', 'price': '6000'},
    {'name': 'samsung S10', 'price': '7000'}
]
#5
urun_toplami = 0
for urun in urunler:
    urun_toplami=urun_toplami + int(urun['price'])
print(f"Ürünlerimizin toplam fiyatı: {urun_toplami} TL'dir")

#6
for urun1 in urunler:
    if int(urun1['price']) <= 5000:
        print(urun1['name'])
