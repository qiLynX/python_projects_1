#Senaryo: İnsan Kaynakları departmanı çalışanların sicil numarası, 
#adı, bölümü ve görevini tek bir sistemde tutmak istemektedir. 
#Her personel için bilgiler bir sözlükte saklanacak ve gerektiğinde 
#görüntülenebilecektir.

personel = {
    "101": {"ad": "Ali", "soyad": "Yılmaz", "bolum": "Üretim", "gorev": "Operatör"},
    "102": {"ad": "Ayşe", "soyad": "Kaya", "bolum": "Kalite", "gorev": "Mühendis"},
    "103": {"ad": "Mehmet", "soyad": "Demir", "bolum": "Lojistik", "gorev": "Sorumlu"}}


while True:
    print("\n*** PERSONEL SİSTEMİ ***")
    print("1 - PERSONEL Ekle")
    print("2 - PERSONEL SİL")
    print("3 - PERSONEL ARA")
    print("4 - Tüm Personeli Listele")
    print("5 - Çıkış")

    secim = input("Seçiminiz: (1/2/3/4/5): ")
    if secim == '1':
        ad=input("Personel Adını Giriniz: ")
        soyad=input("Personel Soyadını Giriniz: ")
        sicilNo=input("Personel Sicil Numarasını Giriniz: ")
        bolum=input("Personel Bölümünü Giriniz: ")
        gorev=input("Personel Görevini Giriniz: ")

        personel[sicilNo] = {
             "ad": ad,
            "soyad":soyad,
            "bolum":bolum,
            "gorev":gorev
        }
        print("Sistem Mesajı: Personel başarıyla eklendi !")

    elif secim == '2':
        silinecek = input("Silinecek personelin Sicil Numarasını giriniz: ")
        if silinecek in personel:
            silinen_kisi = personel.pop(silinecek)
            print(f"Sistem Mesajı: {silinen_kisi['ad']} {silinen_kisi['soyad']} sistemden silindi.")
        else:
            print("Sistem Mesajı: Bu sicil numarasına ait bir personel bulnamamıştır.")

    elif secim == '3':
        aranan = input("Aranacak personelin Sicil Numarasını giriniz: ")
        if aranan in personel:
            kisi = personel[aranan]

            print("\n******** PERSONEL SİSTEMİ ********\n")
            print(f"Sicil No : {aranan}")
            print(f"Ad Soyad : {kisi['ad']} {kisi['soyad']}")
            print(f"Bölüm    : {kisi['bolum']}")
            print(f"Görev    : {kisi['gorev']}")
            
        else:
            print("Sistem Mesajı: Bu sicil numarasına ait bir personel bulnamamıştır.")
    elif secim == '4':
        print("\n--- TÜM PERSONEL LİSTESİ ---")
        if len(personel) == 0:
            print("Sistemde kayıtlı personel bulunmamaktadır.")
        else:
            for sicil, bilgiler in personel.items():
                print(f"Sicil: {sicil} | İsim: {bilgiler['ad']} {bilgiler['soyad']} | Bölüm: {bilgiler['bolum']}") #biraz yardım aldım burada

    elif secim == '5':
        print("Sistemden çıkılıyor. İyi günler!")
        break
        
    else:
        print("Hatalı tuşlama yapıldı, lütfen tekrar deneyin.")

