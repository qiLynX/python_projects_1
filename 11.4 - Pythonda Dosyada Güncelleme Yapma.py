# #with open("newfile.txt","r+", encoding ="utf-8")as file:
#     file.seek(20)
#     #"r+" okuma ve yazmayı temsil eder
#     file.write("deneme ")
# with open("newfile.txt","r+", encoding ="utf-8")as file:
#     #"r+" okuma ve yazmayı temsil eder
#     print(file.read())
# '''
#************** SAYFA SONUNDA GÜNCELLEME **************
# with open("newfile.txt","a", encoding ="utf-8") as file:
#     file.write("\nQWQ")
#************** SAYFA BAŞINDA GÜNCELLEME **************
# with open("newfile.txt","r+", encoding ="utf-8") as file:
#     content = (file.read())
#     content = "Efe\n" + content 
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt","r", encoding ="utf-8") as file:
#     print(file.read())

#************** SAYFA ORTASINDA GÜNCELLEME **************
with open("newfile.txt","r+", encoding ="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Ali\n") #1.indexten itibaren "Ali'yi eklememizi sağlar."
    file.seek(0)
    for i in list:
        file.write(i)
with open("newfile.txt","r", encoding ="utf-8") as file:
    print(file.read())