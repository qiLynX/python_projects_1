#Senaryo:Bir üretim hattında operatör her saat sonunda üretilen parça sayısını sisteme girmektedir.
#Vardiya sonunda toplam üretim ve saatlik ortalama üretim otomatik olarak hesaplanmalıdır.
vardiya_saati=int(input("Gerekli Vardiya Saatini Giriniz: "))
toplam_uretim=0
uretim_listesi = []
if vardiya_saati > 0:
    hedef=int(input("Hedeflenen üretim değerini giriniz: "))
    for i in range(vardiya_saati):
        uretim=int(input("Saatlik Üretim Çıktısını Giriniz: "))
        uretim_listesi.append(uretim)
        toplam_uretim=toplam_uretim+uretim
    zirve_saati = uretim_listesi.index(max(uretim_listesi)) + 1
    dip_saati = uretim_listesi.index(min(uretim_listesi)) + 1
    ort_uretim=toplam_uretim/vardiya_saati
    print("*" * 30 + "\n Vardiya Raporu\n" + "*" * 30 )
    print(f"Saat Sayısı: {vardiya_saati}")
    print(f"Toplam Üretim: {toplam_uretim}")
    print(f"Ortalama Üretim: {ort_uretim}")
    print("*" * 50)
    print(f"En verimli saatimiz: {zirve_saati}.saat.")
    print(f"En verimsiz saatimiz: {dip_saati}. saat.")
    if toplam_uretim >= hedef:
        print("Hedefe ulaşıldı.")
    else:
        print("Hedefe Ulaşılamadı")
else:
    print("Vardiya Saatini Yanlış Girdiniz")