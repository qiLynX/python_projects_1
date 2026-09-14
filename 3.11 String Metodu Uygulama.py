website = "http://www.sadıkturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)" 

#1
message = "Hello World"
message = message.strip()
print(message)
#2
print(website[11:21])
#3
course1 = course.lower()
print(course1)
#4
terim=website
a_sayısı=terim.count("a")
print(a_sayısı)
#5
if website.startswith("www") and website.endswith(".com"):
    print("Yes")
else:
    print("No")
#6
com_var_mi=website.find('.com')
print(com_var_mi)
#7
alfabetik_mi = course.isalpha()
print(alfabetik_mi)
a='3'
a_sayisal_mi = a.isdigit()
print(a_sayisal_mi)

#8
content="Python"
content=content.center(100,'*')
print(content)

#9
course2= course.replace('', '-')
print(course2)
#10
a="Hello World"
a1=a.replace('World','There')
print(a1)
#11
course3 = course.replace(' ', '')
print(course3)