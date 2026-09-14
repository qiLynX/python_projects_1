'''Senaryo: Florya Ekstra Antrenman Takibi'''
#Okan Hoca, takımın fiziksel durumunu artırmak için Pazartesi ve Salı günleri ekstra "şut ve kondisyon" antrenmanları koydu.
#Bu antrenmanlar zorunlu değil, isteyen katılıyor. Tesislerdeki kart basma sisteminden sana iki günlük katılım listesi (Set formatında) düştü.
#Eldeki Ham Veri:
pazartesi_gelenler = {'Osimhen', 'Sane', 'Nhaga', 'Barış'}
sali_gelenler = {'Uğurcan', 'Torreira', 'Osimhen', 'Yunus'}
pazartesi_gelenler.add("Icardi")
her_iki_gun_gelenler=pazartesi_gelenler.intersection(sali_gelenler)
kampa_katilan_tumu=pazartesi_gelenler.union(sali_gelenler)
print(kampa_katilan_tumu)