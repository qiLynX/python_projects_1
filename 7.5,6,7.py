#7.5-Lambda Expressions,Map,Filter
'''def square(num):
    return num ** 2

numbers = [1,3,5,9] #maps bloğu bir listedeki bütün elemanların fonksiyonu çalıştırabilmemizi sağlar

result = list(map(square,numbers))

for item in map(square,numbers):
    print(item) #for alt alta yazmamızı sağlar 

print(result)

numbers1=[1,3,5,9]

result = list(map(lambda num: num**2, numbers1))
print(result)
#Lambda komutu burda def yazmadan işlemi yapabilmemizi sağlar 
#Kısaca tek satırlık anonim fonksiyonlar yapmamızı sağlar 

def check_odd(num1): return num1 % 2 != 0
result = list(filter(check_odd, numbers))
print(result)'''
#filter fonksiyonu, bir liste veya veri dizisindeki elemanları belirlediğiniz bir koşula göre test ederek,
#yalnızca bu koşulu sağlayanları ayıklayıp yeni bir sonuç dizisi oluşturmaya yarar.

#7.6-Global ve Local Değişkenler

#global scope
'''
x= 'global x'

def function():
    #local scope
    x = 'local x'
    print(x)

function()
print(x)

#####################################################

name="Bora"

def changeName(new_name):
    name = new_name
    print(name)

changeName("Ada")
print(name)

#####################################################

name = "global string"

def greefing():
    name="Sude"

    def hello():
        print('Merhaba ' + name)
    hello()

greefing()

x=50
def test():
    global x
    print(f'x: {x}')

    x = 100
    print(f'Changed x to {x}')

test()
print(x)
'''

#######################################################

#7.7 Bankamatik Uygulaması 

boraHesap= {
    'ad': 'Bora Aydın',
    'hesapNo': '123',
    'bakiye': 1905,
    'ekHesap': 20303
}

onurHesap= {
    'ad': 'Onur Aydın',
    'hesapNo': '124',
    'bakiye': 2011,
    'ekHesap': 1905
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranızı alabilirsiniz.")
        bakiyeSorgu(hesap)
    else:
        toplam=hesap['bakiye'] + hesap['ekHesap']

        if (toplam >=miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı (E/H)")
            if ekHesapKullanimi == 'e':
                bakiye = hesap['bakiye']

                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -=ekHesapKullanilacakMiktar
                print('Paranızı alabilirsiniz.')
                bakiyeSorgu(hesap)
                print("Ek hesap kullanıldı")
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır")
        else:
            print("Üzgünüz bakiye yetersiz")
            bakiyeSorgu(hesap)

def bakiyeSorgu(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(boraHesap,100000000)

print('*' * 10)

paraCek(onurHesap,3000)

