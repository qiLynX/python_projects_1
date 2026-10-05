'''def cube():
    result = []

    for i in range(5): #bu 5 sayı için ideal ama mesela 5000 olsa işimiz sıkıntı olabilirdi
        #bu yüzden bellek üzerinde yer tutmayan generatorlar oluştururuz.
        result.append(i**3)
    return result

print(cube())'''

# def cube():
#     for i in range(5):
#         yield i ** 3 #yield bir değer üreticidir, bu değeri bana gönderir ve 
#         #bellek olarak tutmadığı için sıkıntı çıkaretmıyor.


# for i in cube():
#     print(i)

liste = [i**3 for i in range(5)] #bu liste formatındadır
generator = (i**3 for i in range(5)) #bu ise generation formatındadır.
print(liste)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))