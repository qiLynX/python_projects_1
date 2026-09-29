#Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
#open(dosya_adi,dosya_erişme_modu)
# "w": Write modu

'''file = open("newfile.txt","w")
file.close() #Aynı dizinde dosya açma
'''

'''file = open("C:/users/bora0/desktop/newfile.txt","w")
print(file) #Farklı konumda dosya açma
''' 

#file = open("newfile.txt","w", encoding='utf-8') #utf-8 encode edersek Türkçe karakterleri de tanımamız sağlanır
#file.write("Bora Aydın")
#file.close()

# "a": append modu

#file = open("newfile.txt","a", encoding='utf-8')
#file.write("Onur Aydın")

# "x": create modu

file = open("newfile2.txt","x", encoding='utf-8')


# "r": read modu

