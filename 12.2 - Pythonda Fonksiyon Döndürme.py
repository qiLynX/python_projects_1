def us_alma(number): #number değerinin üssü alınacak
    #two = us_alma(2)
    #three = us_alma(3)

    def inner(power):
        return number ** power

    return inner  
#inner fonksiyonunu two = ..., veya three =... şeklinde belirtmemizi sağlar
# two = us_alma(2)
# print(two(3)) için fonksiyonumuz 2³ ifadesini verir.

two = us_alma(2)
print(two(3)) #2 üssü 3 bilgisini bana geri döndürür
three = us_alma(3)
print(three(4)) #3 üssü 4 bilgisini gönderir

def yetki_sorgu(page):
   def inner(role):
        if role == 'Admin':
           return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
        else:
           return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
   return inner
user1 = yetki_sorgu("Product Edit")
print(user1("Admin"))
print(user1("User"))