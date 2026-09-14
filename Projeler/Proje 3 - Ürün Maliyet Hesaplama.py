#Senaryo: Bir üretim işletmesinde yeni üretilecek bir parçanın birim maliyetinin ve kârlı satış fiyatının hesaplanması istenmektedir.
# Ürünün maliyet kalemleri sisteme tek tek girilecek, program bu kalemleri toplayacak ve istenen kâr oranını ekleyerek satış fiyatını otomatik olarak hesaplayacaktır.
print("*" * 10 + "Maliyet Hesaplama Sistemi" + "*" * 10)
hammadde_m=float(input("Hammadde maliyetini giriniz: "))
iscilik_m=float(input("İşçilik maliyetini giriniz: "))
enerji_m=float(input("Enerji giderini giriniz:"))
diger_m=float(input("Diğer maliyetleri giriniz: "))
toplam_m=hammadde_m + iscilik_m + enerji_m + diger_m
print(f"Toplam maliyet değerimiz: {toplam_m}")
istenen_kar_yuzdesi=float(input("İstenen kâr yüzdesi değerini giriniz: "))
satis_fiyatı=toplam_m + (toplam_m* (istenen_kar_yuzdesi/100))
print(f"İstenen kâra göre belirlenen satış fiyatı: {satis_fiyatı:.2f}")
