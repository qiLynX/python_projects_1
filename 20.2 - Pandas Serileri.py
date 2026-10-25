import pandas as pd 

#data
numbers = [20,30,40,50]
# pandas_series = pd.Series()
pandas_series = pd.Series(numbers)
print(pandas_series)

letters = ['a','b','c','d'] #pandas'ta listeler heterojen yapıdadır 'd' silip yerine 20 yazsak bile bir problem çıkmaz
pandas_series = pd.Series(letters)
print(pandas_series)

pandas_series = pd.Series(5,[0,1,2,3]) #4 tane indeksin hepsinde 5 yazmasını sağlar 
print(pandas_series)

pandas_series =pd.Series(numbers, ['a','b','c','d'])
print(pandas_series)
#dictionary {} için key verisi girmeye gerek kalmaz 
#çünkü dictionary zaten kendiliğinden key değer verilmiş şekilde yazılır
#örneğin: 'a' = 10, dersek ilk key value 'a' karşılığı ise 10 olur

import pandas as pd 
import numpy as np
random_numbers = np.random.randint(10,100,6)
pandas_series = pd.Series(random_numbers)
print(pandas_series)

#pandas_series.ndim komutu ile kaç boyutlu bir veri elde ettiğimizi sorabiliriz
#ve bunun çıktısı 1 olur çünkü matris halinde yazmadık şuanki yazdığımız kod bloğunu 


opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","Grondland","insignia"])

total = opel2018 + opel2019
print(total)
print(total["astra"])