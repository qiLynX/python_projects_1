sayi=int(input("Bir sayı değeri giriniz: "))
asalmi=True

if sayi==1:
    asalmi=False

for i in range(2,sayi):
    if sayi % i == 0:
        asalmi=False
        break

if asalmi:
    print("Sayı asaldır")
else:
    print("Sayı asal değildir.")