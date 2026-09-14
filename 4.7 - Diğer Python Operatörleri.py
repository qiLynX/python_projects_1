# Identify Operator: is

'''x = y = [1,2,3]
z = [1,2,3]

print(x==y)
print(x==z)
print(x is y)
print(x is z)'''

#listeler aynı değerlere sahip olsa da aynı objelere sahip değildir 
#Dolayısıyla 'x is z' False cevabını verir

x = [1,2,3]
y = [2,4]

del x[2]
y[1]= 1
y.reverse()
print(x==y) #Elemanlar eşit yani True
print(x is y) #Ancak x y objesi mi aynı adresi mi gösterir cevabı ise False

# Membership Operator: in

x = ['apple', 'banana']
print('banana' in x) #Banana bilgisi x'te var mı sorusunu sorarız ve True cevabını alırız
