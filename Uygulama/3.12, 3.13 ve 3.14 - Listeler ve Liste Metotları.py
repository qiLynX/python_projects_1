'''Senaryo: Galatasaray Maç Kadrosu Güncellemesi'''
#Florya'da son antrenman bitti ve teknik heyet hafta sonu oynanacak maçın defans kurgusunu sana teslim etti. Sisteme başlangıç olarak şöyle bir liste girilmiş durumda:
#Eldeki Ham Veri:
kadro = ['Uğurcan', 'Nhaga', 'Osimhen', 'Sane']
kadro.append("Kaan")
kadro.remove('Sane')
kadro.sort()
kadro_kisi_sayisi=len(kadro)
print(f"Güncel takımda laktat testi yapılan oyuncularkaleci orta saha forvet kanatından bazı isimler olmak üzere : {kadro} bunlardır  ve toplam laktat testi yapılan oyuncu sayisi: {kadro_kisi_sayisi}")
