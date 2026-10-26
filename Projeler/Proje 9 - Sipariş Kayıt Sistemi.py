# Bir işletme günlük müşteri siparişlerini bilgisayarda saklamak 
# istemektedir. Sipariş numarası, müşteri adı ve sipariş miktarı 
# dosyaya kaydedilecek; daha sonra kayıtlar okunarak raporlanacaktır.

siparis_no = 1000

print("--- Sipariş Sistemi ---")

while True:
    urun = input("Ürün adı girin (Çıkmak için 'dur' yazın): ")
    if urun == "dur":
        print("Sistem kapatıldı.")
        break
    print(f"Sipariş No: {siparis_no} - Ürün: {urun}\n")
    siparis_no += 1
    firma_adi = input("Firma Adını Giriniz: ")
    siparis_adet = input("Sipariş adetini giriniz: ")

    siparis = {
        "firma_adi": firma_adi,
        "urun" : urun,
        "siparis_adet" : siparis_adet,
}

    file = open("C:/users/bora0/desktop/siparis_kayit.txt","a", encoding = "utf-8")
    file.write(f"{siparis_no} | {firma_adi} | {urun} | {siparis_adet} Adet\n")
    file.close()

