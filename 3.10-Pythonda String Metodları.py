#message = 'Hello There. My name is Bora Aydın'

'''message1 = message.upper()                 #Hepsini büyük harfe çevirir
message2= message.lower()                     #Hepsi küçük...
message3 = message.title()                    #Baş harfleri büyük
message4 = message.capitalize()               #İlk Kelimenin ilk harfi büyük '''

'''message = message.strip() #Başlangıçtaki ve sondaki boşluk karakterini siler
message = message.split() #Her bir kelimeyi ayırır "Hello", "There"... gibi
#Ayırdıktan sonra print(message[0]) yazarsam eğer "Hello" mesajını alırım .split(.)  yaparsak eğer 
noktalardan itibaren cümleyi ayırır

message= ' '.join(message) ile tekrar dan birleştirirken boşluk ekleyebiliriz.'''

'''index=message.find('Bora')
print(index) #mesela cevap olarak 24 aldıysak bu bize 24.indeksten itibaren bu kelimenin olduğunu gösterir -1 ssonucunu
alırsak eğer bu indeks yoktur'''

'''isFound = message.startswith('H')
print(isFound) #Eğer True cevabını alıyosak bu metinde H ile başlayan kelime yani veri vardır.Aynısını
.endswith yaparsak kelimenin bitişine bakarız'''

'''message = message.replace('Bora', 'Onur').replace(' ', '*')
print(message) #kelimeleri değiştirmemize yarar böylece Bora yerine Onur yazdık boşluk yerine de yıldız koydurttuk'''

'''message=message.center(100,'*')
print(message)
#*********************************Hello There. My name is Bora Aydın*********************************# ifadesini almamızı
sağlar yani ortalar da denilebilir.'''
