'''Senaryo: Öğrenci Kayıt Sistemi Veri Temizliği'''
#Üniversitenin öğrenci işleri otomasyonunda çalışıyorsun.
#Sisteme kayıt olan bir öğrenci, formdaki isim kutusuna adını yazarken klavyede epey dikkatsiz davranmış ve boşluk tuşuna basılı tutmuş.
#Veritabanına kaydedilmeden önce bu dağınık metni string metotlarıyla standart ve resmi bir formata sokman gerekiyor.
#Eldeki Ham Veri:
girilen_isim = "  boRa aYdIn   "
degisiklik1=girilen_isim.strip()
son_veri=degisiklik1.title()
print(son_veri)
