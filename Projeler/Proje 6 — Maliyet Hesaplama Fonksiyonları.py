#Bir işletmede farklı ürünlerin maliyetleri aynı yöntemle hesaplanmaktadır.
# Her ürün için aynı kodu tekrar yazmak yerine, maliyet hesabını yapan
# bir fonksiyon geliştirmeniz istenmektedir. Fonksiyon; hammadde, işçilik, enerji ve
# diğer giderleri parametre olarak alacak ve toplam maliyeti döndürecektir.





class Gider_Hesap():
    def __init__(self,hammadde_gider,enerji_gider,iscilik_gider,diger_gider):
        self.hammadde = hammadde_gider
        self.enerji = enerji_gider
        self.diger = diger_gider
        self.iscilik = iscilik_gider
    def maliyet_hesapla(self):
        return self.hammadde + self.enerji + self.diger + self.iscilik

u1 = Gider_Hesap(13250, 14330, 7310, 3000)
u2 = Gider_Hesap(8902, 2121, 3547,2000)

print("*" * 15 + " Maliyet Raporu " + "*" * 15)

print(f"Ürün A Toplam Maliyeti: {u1.maliyet_hesapla()}")
print(f"Ürün B Toplam Maliyeti: {u2.maliyet_hesapla()}")
    


