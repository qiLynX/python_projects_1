'''Senaryo: Osmangazi SK Veritabanı Entegrasyonu
Osmangazi SK teknik heyeti, sol bek adaylarının fiziksel verilerini kulübün eski (legacy) veritabanına aktarmak için senden bir Python betiği yazmanı istiyor. Ancak eski sistemin veri kabul formatları çok katı.

Eldeki Veriler ve İstenen İşlemler:

Veri 1: Sistem, kullanıcıdan maç başı ortalama koşu mesafesini ondalıklı bir sayı olarak girmesini istemeli (Örn: 11.4).

Veri 2: Sistem, kullanıcıdan haftalık antrenman sayısını tam sayı olarak girmesini istemeli (Örn: 5).

Veri 3 (Sabit Veri): Oyuncunun lisans durumu kodun içinde başlangıçta mantıksal bir doğru/yanlış değeri (True) olarak tutulmalıdır.

Problem 1: Kulübün veritabanı, koşu mesafesinde küsurat kabul etmiyor. Girilen ondalıklı koşu mesafesi verisi, küsuratı atılarak tam sayıya dönüştürülmeli ve yeni bir değişkende saklanmalıdır.

Problem 2: Kulübün veritabanı lisans durumunu kelime veya mantıksal değer olarak değil, sadece sayısal olarak okuyabiliyor. Elimizdeki True değeri, sistemin anlayacağı sayısal formata dönüştürülmelidir.'''

mbokm=input("Maç başı ortalama koşu mesafesini giriniz: ")
has=input("Haftalık antrenman sayısını giriniz:  ")
lisans_durumu = True
if lisans_durumu == True:
    print("Durum Doğru: Oyuncunun lisansı vardır")
else:
    print("Durum Yanlış: Oyuncunun lisansı yoktur")
print(mbokm)
print(has)

mbokm_int = int(float(mbokm))

Problem1=print(f"Kulübün veritabanı gereği Problem1'in cevabı {mbokm_int} cevabına eşdeğerdir.")

lisans_durumu_int=int(lisans_durumu)
Problem2=print(f"Kulübün veritabanı gereği Problem2'nin cevabı {lisans_durumu_int} cevabına eşdeğerdir.")
