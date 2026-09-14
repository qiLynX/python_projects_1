website= "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"
#1
print(len(course))
#2
print(website[7:10])
#3
print(website[22:])
#4
print(course[0:15]+ '' + course[50:65])
#5
print(course[ : : -1])

#########################################################################################################################

name, surname, age, job = 'Bora', 'Aydın', 21, 'Engineer'
#6
print(f'My name ıs {name} {surname}, I am {age} years old, and I am an {job}')

a1='Hello world'
a1=a1[0:6]+ 'W' + a1[7:11]
print(a1)