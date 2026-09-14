numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y']

'''val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]'''

numbers[4]=40

numbers.append(49) #En sona sayı, kelime eklemeyi sağlar
numbers.insert(3,78)#3.indeksten sonra 78 sayısını eklememi sağlar

#numbers.pop() pop() metodu bir veri yapısından eleman silmeye yarar, içine yazılan indeksi siler numbers.pop(1)=1. indeksi siler...gibi
#numbers.remove() ise içine yazılan karakteri siler örneğin .remove(16) yazarsam 16 silinir

print(numbers)

numbers.sort() #Sayısal Sıralı şekilde yazmamızı sağlar 
letters.sort() #Alfabetik Sıralı şekilde yazmamızı sağlar 
#numbers.reverse() listeyi tam tersine çevirmemizi sağlar 
print(numbers)
print(letters)

print(numbers.count(10)) #numbers'ın içinde kaç tane 10 var (2 cevabını verir)

# numbers.clear() tüm liste elemanlarını siler