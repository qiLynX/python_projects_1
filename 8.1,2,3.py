# Object Oriented Programming (OOP)
# Nesne Tabanlı Programlama 


#class=> Person
 
'''class Person:
    pass #Tanımlama yapmadan önce yazarsak hata almamızı engeller 
    #class attributes
    address = 'No information'
    #constructor (yapıcı metod)
    def __init__(self,name,year):
#__init__ metodu, bir sınıftan (class) yeni bir nesne oluşturulduğunda
#otomatik olarak çalışan özel bir yapıcı (constructor) fonksiyondur
        #object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı.')
    #instance methods
    def intro(self):
        print("Hello There, I am "+ self.name )
    def calculateAge(self):
        return 2026 - self.year


#instance(object)
p1 = Person('Bora', 2004)
p2 = Person('Sude', 2005)

p1.intro()
p2.intro()

print(f"Ben {p1.name} ve Yaşım {p1.calculateAge()} ")
print(f"Ben {p2.name} ve Yaşım {p2.calculateAge()} ")
#updating
p1.name = 'Onur'
p1.address = 'İzmir'

print(f'p2_name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p1_name: {p2.name} year: {p2.year} address: {p2.address}')
print(type(p1))
print(type(p2))
print(p1==p2)'''

class Circle:
    #class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    #Methods
    def cevreHesap(self):
        return 2*self.pi+self.yaricap
    def alanHesap(self):
        return self.pi* (self.yaricap**2)

c1 = Circle() # yaricap =1 başta 1 yazdığımız ve değiştirmediğimiz için
c2 = Circle(10) # yaricap = 5

print(f"c1: alan = {c1.alanHesap()}, çevre = {c1.cevreHesap()}")
print(f"c2: alan = {c2.alanHesap()}, çevre = {c2.cevreHesap()}")