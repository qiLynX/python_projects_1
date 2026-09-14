#7.Pythonda Fonksiyonlar
#7.1 Metotlar (Bir Sınıf Grubudur)

'''list = [1,2,3]
list.append(4)

print(list)
print(type(list))

myString = "hello"
print(myString.capitalize())
print(type(myString))'''

#########################################################################################

#7.2 Fonksiyon Kullanımı
#fonksiyon

'''def sayHello(name):
    print("Hello " + name)

sayHello("Rafael")
#sayHello() yazıp bırakırsam çalışmaz çünkü "name" parametresini girmedik

def sH(name="user"):
    return "Hello" + name
msg = sH(" Leao")
print(msg) #Aynı yazının tersten yazımı. Verinin fonksiyona dönmesi

def total(num1, num2):
    return num1 + num2

result= total(1900,5)
print(result)'''

#########################################################################################

#7.3 Fonksiyon Parametreleri

'''def changeName(n):
    n = "ada"

name = "yiğit"

changeName(name)
print(name)

def change(n):
    n[0] = "istanbul"

sehirler=["ankara", "izmir"]

change(sehirler[:]) #slicing

print(sehirler)'''

'''def add(a,b, c=0): #burada c = 0 yazmamız 3 tane değer girilirse de fonksiyonun çalışmasını sağlar
    return sum((a,b,c))

print(add(10,20))
print(add(10,20,30))

def add(*params):
    print(params)
    return sum((params))

print(add(10,20))
print(add(10,20,30,15,3,5,6,7,11,12,33))'''

'''def displayUser(**args): #Buradaki ** ifadesi keyword argument anlamına gelir, ** istediğimiz kadar parametre eklememizi sağlar.
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name='Bora', age=22,city = 'İzmir')
displayUser(name='Onur', age=14,city = 'Fethiye')

def myfunc(a,b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(10,20,30,40,50, key1 = 'value 1', key2 = 'value 2')'''
#########################################################################################

#7.4 Uygulama
#1
def kelimeGoster(kelime, adet):
    print(kelime * adet)

kelimeGoster('Merhaba \n',10)
#########################################################################################

#2
def yazdir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste

result=yazdir(10,20,30)
print(result)
#########################################################################################

#3
#İki değer arasındaki asal sayıları bulma
def asalSayi(sayi1, sayi2):
    for sayi in range(sayi1,sayi2):
        if sayi > 1:
            for i in range (2,sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)

sayi1 = int(input("sayi 1: "))
sayi2 = int(input("sayi2: "))
asalSayi(sayi1,sayi2)