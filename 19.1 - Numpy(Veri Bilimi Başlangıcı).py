import numpy as np



#python list
py_list = [1,2,3,4,5,6,7,8,9]

#numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(np_array))

py_multi = ([1,2,3],[4,5,6],[7,8,9])
np_multi = np_array.reshape(3,3) #yeniden düzenleme # (3,3) => 3'e 3'lük matris oluiturmayı sağlar

print(py_multi)
print(np_multi)

print(np_array.ndim) #dizinin toplam boyut sayısını verir
print(np_multi.ndim)

print(np_array.shape) #dizinin her bir boyutundaki eleman sayısını gösterir (3,4) => 3 satır, 4 sütun
print(np_multi.shape)

