#Bir üretim mühendisi gün içinde maliyet, üretim miktarı, fire ve stok gibi birçok sayısal hesaplama yapmaktadır.
# Bu işlemleri daha hızlı ve düzenli gerçekleştirmek için iki sayı üzerinde temel işlemleri yapan küçük bir Python uygulaması geliştirilmesi istenmektedir.
print("*" * 10 + " Hesap Makinesi " + "*" * 10)
sayi_degeri1=float(input("Bir sayı giriniz: "))
sayi_degeri2=float(input("Bir sayı giriniz: "))
toplama_islemi=sayi_degeri1 + sayi_degeri2
cikarma_islemi=sayi_degeri1 - sayi_degeri2
carpma_islemi=sayi_degeri1*sayi_degeri2
bolme_islemi=sayi_degeri1/sayi_degeri2
print(f"Girilen iki değerin toplamı: {toplama_islemi}")
print(f"Girilen iki değerin çıkarma işlemindeki karşılığı: {cikarma_islemi}")
print(f"Girilen iki değerin çarpmasının sonucu çıkan değer : {carpma_islemi}")
print(f"Girilen iki değerin birbirine bölünmesi sonucu çıkan değer: {bolme_islemi}")
