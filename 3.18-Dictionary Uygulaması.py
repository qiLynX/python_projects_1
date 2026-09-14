'''ogrenciler = { 
    '120': {
        'ad' : 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532 000 00 01',
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02',
    },
    '128': {
        'ad':'Volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 00 03',
    },
}
'''


ogrenciler = {} 

# 1. Öğrenci
number = input("1. öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")
# Veriyi hemen sözlüğe ekliyoruz
ogrenciler[number] = {
    'ad': name,
    'soyad': surname,
    'telefon': phone
}

# 2. Öğrenci
number = input("2. öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")
# Veriyi hemen sözlüğe ekliyoruz
ogrenciler[number] = {
    'ad': name,
    'soyad': surname,
    'telefon': phone
}

# 3. Öğrenci
number = input("3. öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")
# Veriyi hemen sözlüğe ekliyoruz
ogrenciler[number] = {
    'ad': name,
    'soyad': surname,
    'telefon': phone
}

print(ogrenciler) 


ogrNO = input('Aranacak öğrenci no: ')
# Burada 'number' yerine kullanıcının az önce girdiği 'ogrNO' değişkenini kullanıyoruz.

# get() metodu kullanmak, olmayan bir numara girildiğinde kodun çökmesini engeller.
ogrenci = ogrenciler.get(ogrNO, "Öğrenci bulunamadı.") 
print(ogrenci)