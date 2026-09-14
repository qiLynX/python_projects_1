'''x = 6
hak = 5
devam = 'e'
result= 5 < x < 10

#and 

#True, True = True
#True, False = False
result = x > 5 and x < 10
result= (hak >5) and (devam == 'e')

#or

#True, False = True
result = (x > 0) or (x % 2 == 0)

#not

#Terslik için kullanılır
result= not (x > 0)



print(result)

# x, 5-10 arasında olan bir çift sayı mı ?
result=((x>5 and x<10) and x % 2 == 0)
print(result)'''



#1
'''sayi1=float(input("Bir sayı giriniz: "))
result= (sayi1>0 and sayi1<100)
print(result)'''#Doğru

#2
'''sayi2=float(input("Bir sayı giriniz: "))
result= (sayi2>0) and (sayi2 % 2 == 0)
print(result)'''#Doğru

#3 
'''email='bora06519@gmail.com'
sifre='q123'
girilenEmail=input("Bir email giriniz: ".lower().strip())
girilenSifre=input("Bir şifre giriniz: ")
result1= (girilenEmail==email)
result2= (girilenSifre==sifre)
print(result1)
print(result2)'''#Doğru

#4 
'''a=input("a: ")
b=input("b: ")
c=input("c: ")

result= (a >b) and (a > c)
print(f"a en büyük sayıdır: {result} ")

result= (b > a ) and (b > c)
print(f"b en büyük sayıdır: {result} ")

result= (c >a ) and (c > b)
print(f"c en büyük sayıdır: {result} ")''' #Doğru