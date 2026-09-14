name='Bora'
surname='Aydın'
age=21
print('Benim adım {} {} and I am {} years old.'.format(name, surname, age))
'''print('Benim adım {1} {0}'.format(name, surname))
*Burada {0} ve {1} ifadeleri, format() metoduna verilen argümanların sırasını temsil eder.'''
'''print('Benim adım {n} {s}'.format(n=name, s=surname))
*Burada {n} ve {s} ifadeleri, format() metoduna verilen argümanların isimlerini temsil eder.'''

result=200/700
print('Result: {r:1.3}'.format(r=result))
#Buradaki :1.3 ifadesi, result değişkeninin 1 basamaklı ve 3 ondalık basamaklı olarak formatlanmasını sağlar.

print(f'Benim adım {name} {surname} and I am {age} years old.')
#f string formatlama yöntemi, değişkenleri doğrudan string içinde kullanmamıza olanak tanır.

