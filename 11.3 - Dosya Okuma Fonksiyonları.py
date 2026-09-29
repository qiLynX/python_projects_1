with open("newfile2.txt","r", encoding ="utf-8") as file:
    content = file.read()
    print(content)
    file.seek(0) #okuma sonrası içine yazılan bloğa (sıfıra) dönülmeyi sağlar
    print(file.tell())
    content2 = file.read()
    print(content2)
