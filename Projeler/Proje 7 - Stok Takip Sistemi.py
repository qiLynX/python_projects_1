#Bir işletmenin deposunda bulunan ürünlerin isimleri basit bir stok listesinde tutulmaktadır.
# Depo sorumlusu yeni ürün eklemek, stoktan çıkan ürünü silmek ve mevcut ürünleri
# görüntülemek istemektedir. Bu işlemleri kolaylaştırmak için menü tabanlı küçük bir Python
# uygulaması geliştirmeniz istenmektedir.

stok = ["Elma", "Armut", "Çilek"]

print("*" * 20 + " STOK TAKİP SİSTEMİ " + "*" * 20)

while True:
    print("\n*** STOK TAKİP SİSTEMİ ***")
    print("1 - Ürün Ekle")
    print("2 - Ürün Sil")
    print("3 - Ürün Ara")
    print("4 - Stokları Listele")
    print("5 - Çıkış")

    secim = input("Seçiminiz (1/2/3/4/5): ")

    if secim == '1':
        eklenecek_urun = input("Eklenecek ürünü giriniz: ")
        stok.append(eklenecek_urun)
    elif secim == '2':
        silinecek_urun=input("Silinecek ürünü giriniz: ")
        if silinecek_urun in stok:
            stok.remove(silinecek_urun)
        else:
            print("Silmek istediğiniz ürün stokta bulunmamaktadır.")
    elif secim == '3':
        aranacak_urun = input("Aramak istediğiniz ürünü giriniz: ")
        if aranacak_urun in stok:
            print(f"Aradığınız {aranacak_urun} ürünü stokta bulunmaktadır.")
        else:
            print(f"Aradığınız {aranacak_urun} ürünü stokta bulunmamaktadır.")
    elif secim == '4':
        for urun in stok:
            print(urun)
    elif secim == '5':
        print(f"Stoktaki ürünler: {stok}")
        print("Sistemden çıkılıyor.")
        break
