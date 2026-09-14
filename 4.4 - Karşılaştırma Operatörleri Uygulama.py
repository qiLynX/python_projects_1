#1
'''sayi1=int(input("Bir sayı giriniz: "))
sayi2=int(input("Bir sayı giriniz: "))
print(sayi1>sayi2)'''

#2
'''vize=float(input("Vize notunuzu giriniz: "))
final=float(input("Final notunuzu giriniz: "))
ortalama= (vize*0.40) + (final*0.60)
print(ortalama>=50)'''

#3 
'''tek_mi_cift_mi=int(input("Bir sayı giriniz: "))
print((tek_mi_cift_mi % 2) == 0)'''

#4 
'''pozitif_mi=int(input("Bir sayı giriniz: "))
print(pozitif_mi>0)'''

#5

email = 'bora06519@gmail.com'
password = '12345'

girilenEmail = input('email: ')
girilenPassword = input('password: ')
isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower())
print(isEmail)
print(isPassword)