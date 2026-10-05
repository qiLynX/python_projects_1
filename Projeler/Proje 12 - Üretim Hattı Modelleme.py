#Senaryo: Bir üretim tesisinde farklı makineler bulunmaktadır.
# Her makinenin adı, saatlik kapasitesi, çalışma durumu ve ürettiği
# toplam adet bilgisi tutulmaktadır. İşletme, makineleri yazılım
# ortamında modelleyerek üretim bilgilerini daha düzenli takip etmek
# istemektedir.

'''
Proje Gereksinimleri
1-Makine adında bir sınıf oluşturun.
2-Sınıfta makine adı, saatlik kapasite, çalışma durumu ve toplam üretim bilgilerini tutun.
3-Makineyi çalıştıran ve durduran metotlar yazın.
4-Belirli bir çalışma süresine göre üretim miktarını hesaplayan bir metot oluşturun.
5-En az iki farklı makine nesnesi oluşturun.
6-Her makinenin bilgilerini ve üretim sonucunu ekrana yazdırın.'''

class Makine():
    def __init__(self,name,capacity,hour,status,total):
        self.name = name
        self.capacity = capacity
        self.hour = 0
        self.status = "Durduruldu"
        self.total = 0
        print("Rapor oluşturuluyor...\n")

    def calistir(self):
        self.status = "Çalışıyor"
        print(f"Sistem: {self.name} başlatıldı.")
    def durdur(self):
        self.status = "Durduruldu"
        print(f"Sistem: {self.name} durduruldu.")
    def uretim(self,calisma_saati):
        if calisma_saati>0:
            self.hour += calisma_saati
            self.total += self.capacity * calisma_saati
    def raporla(self):
        print('*' * 10 + "Üretim Hattı Raporu" + '*' * 10)
        print(f"Makine Adı: {self.name}\nSaatlik Kapasite: {self.capacity}\nÇalışma Süresi: {self.hour}\nToplam Üretim: {self.total}|\nDurum: {self.status}\n")

kesim_makinesi = Makine("Kesim Makinesi", 120, "8 Saat","Çalışıyor", "960 Adet")
bicki_makinesi = Makine("Bıçkı Makinesi", 230, "8 Saat", "Çalışıyor", "1080 Adet")

kesim_makinesi.calistir()
kesim_makinesi.uretim(8)
kesim_makinesi.raporla()

bicki_makinesi.calistir()
bicki_makinesi.uretim(5)
bicki_makinesi.durdur() # Bu makineyi işlem sonu durduralım
bicki_makinesi.raporla()
