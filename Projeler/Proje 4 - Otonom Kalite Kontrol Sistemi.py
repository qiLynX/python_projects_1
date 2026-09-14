#Senaryo: Üretim bandından çıkan parçaların (örneğin millerin) çap ölçümleri sana ham bir liste halinde gelecek.
# Yazacağın algoritma bu koca listeyi tek tek gezecek;
# ölçüleri belirlediğin tolerans sınırlarına göre değerlendirip "Kabul", "Hurda" veya "Rework (Yeniden İşlem)"
# olarak sınıflandıracak. En sonunda da fire oranını hesaplayıp raporlayacak.
'''Proje Gereksinimleri
Kullanıcıdan parçanın ölçüm değerini milimetre cinsinden alın.
Ölçüm 9,80–10,20 mm arasındaysa KABUL yazdırın.
Ölçüm 9,50–10,50 mm arasındaysa ve kabul aralığında değilse ŞARTLI KABUL yazdırın.
Bu aralıkların dışında kalan değerler için RED yazdırın.
Sonuçla birlikte girilen ölçüm değerini de ekranda gösterin.
Koşulları en dar toleranstan en geniş toleransa doğru sıralayın.'''
olcum=float(input("Parçanın yarıçap değerini giriniz: "))
tolerans=float(input("Parçanın yarıçapı için istenen tolerans değerini giriniz: "))
hedef_olcu = 10.0
alt_sinir = hedef_olcu - tolerans
ust_sinir = hedef_olcu + tolerans
print('*' * 30 + "\nKalite Kontrol Sistemi\n" + "*" * 30)

if alt_sinir <= olcum <= ust_sinir:
    print(f"Kontrol sonucu: Girmiş olduğunuz {olcum} mm yarıçap değeri KABUL olarak sınıflandırılmıştır")
elif 9.50 <= olcum <= 10.50:
    print(f"Kontrol sonucu: Girmiş olduğunuz {olcum} mm yarıçap değeri ŞARTLI KABUL olarak sınıflandırılmıştır")
else:
    print(f"Kontrol sonucu: Girmiş olduğunuz {olcum} mm yarıçap değeri RED olarak sınıflandırılmıştır")