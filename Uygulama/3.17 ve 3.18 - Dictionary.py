#Senaryo: Oyuncu Profil Veritabanı Güncellemesi
#Teknik heyet senden takımın yıldız forvetinin detaylı profilini sisteme girmeni ve sezon sonu güncellemesini yapmanı istiyor. 
#Listelerde sadece isimleri yan yana tutabiliyorduk, ama Dictionary (Sözlük) yapısı sayesinde oyuncunun tüm özelliklerini etiketleyerek bir veritabanı kaydı oluşturabiliriz.

#Eldeki Ham Veri:
oyuncu_profili = {
    'isim': 'Osimhen',
    'mevki': 'Pivot Santrafor',
    'yas': 26,
    'gol_sayisi' : 24,
}
oyuncu_profili['yas'] = oyuncu_profili['yas'] + 1   
oyuncu_profili['form durumu'] = 'Zirvede'
print(oyuncu_profili)
print(f"{oyuncu_profili['isim']}, adlı oyuncumuz {oyuncu_profili['yas']} yaşına girmiş olup mevcut form durumu {oyuncu_profili['form durumu']}, ve bu takımın her şeyi \nUmarım bu takımdan gitmez.")