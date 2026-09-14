name='Bora'
surname='Aydın'
age=21
greeting="Hello, my name is " + name + " " + surname + "\nand I am " + str(age) + " years old."
length=len(greeting)

'''Buradaki \n karakteri, metin içinde yeni bir satır başlatmak için kullanılır. 
Bu sayede, "I am 21 years old." ifadesi bir alt satırda görüntülenir.'''

print(greeting)
'''print(greeting[0])

#Buradaki [0] ifadesi, greeting değişkeninin ilk karakterini temsil eder.
#[1] ifadesi ikinci karakteri, [2] ifadesi üçüncü karakteri temsil eder ve bu şekilde devam eder.
#Sondan başlanarak karakterlere erişmek için negatif indeksler kullanılabilir. Örneğin, greeting[-1] ifadesi son karakteri temsil eder.'''

'''print(length)
print(greeting[length-1])
#Buradaki length-1 ifadesi, greeting değişkeninin son karakterine erişmek için kullanılır.
#Çünkü indeksler 0'dan başladığı için, son karakterin indeksi length-1 olur.'''

'''print(greeting[0:5])
#Buradaki [0:5] ifadesi, greeting değişkeninin 0. indeksinden başlayarak 5. indekse kadar olan karakterleri temsil eder.
'''
