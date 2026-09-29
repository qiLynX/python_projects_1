# try:
#     file = open("newfile.txt","r")
# except FileNotFoundError:
#     print("Dosya Okuma Hatası")
# finally:
#     print("Dosya Kapandı.")
#     file.close()
# print(file)

file = open("newfile.txt", "r", encoding = "utf-8")

#for döngüsü

# for i in file:
#     print(i, end="")

#********************read() fonksiyonu********************

# content1 = file.read()
# print("İçerik 1")
# print(content1)

# content2 = file.read()

# print("İçerik 2")
# print(content2)

# content=file.read(5) #5. karaktere kadar yazar
# content=file.read(3) #Sonraki 3.karakteri alır
# print(content)

#********************readline() fonksiyonu********************

# print(file.readline(),end="") #end sondaki boşluğu silmeyi sağlar
# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())

#Satırları sırayla okur

#********************readlines() fonksiyonu********************

# liste = file.readlines()
# print(liste) #her satır elemanını dizi elemanını olarak karşımıza çıkartır 
# print(liste[0])

file.close()