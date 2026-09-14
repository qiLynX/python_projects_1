#Senaryo: Üretim Hattı Barkod Ayrıştırma
#Bir fabrikanın kalite kontrol bandında çalışıyorsun. 
#Lazer okuyucudan geçen ürünlerin barkod bilgileri veritabanına tek parça bir metin olarak düşüyor. 
#Raporlama yapabilmek için bu metni parçalaman isteniyor.
#Eldeki Ham Veri:
barkod ="PRD-Motor-098-TR"
parca_adi=barkod[4:9]
parca_numarasi=barkod[10:14]
barkod_uzunlugu=len(barkod)
print(f"Üretim hattından {parca_numarasi} numaralı {parca_adi} parçası geçti. Toplam barkod uzunluğu: {barkod_uzunlugu} karakter")
