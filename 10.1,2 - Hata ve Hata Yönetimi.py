# error(hata)

'''
#print(a) => NameError
#int('1a2') => ValueError
#print(10/0) => ZeroDivisionError
#print('denem'e) => SyntaxError
'''

#  error handling (hata yönetimi)
'''
try:
    x = int(input('x: '))
    y= int(input('y: '))
    print(x/y)
except (ZeroDivisionError,ValueError) as e:
    print("Yanlış bilgi girdiniz")
    print(e) #burdaki print e hangi sebepten yanlış bilgi girdiğimizi gösterir
'''
while True:
    try:
        x = int(input('x: '))
        y= int(input('y: '))
        print(x/y)
    except Exception as ex:
        print("Yanlış bilgi girdiniz", ex)
    else:
        break
    finally:
        print("try except sonlandı")

