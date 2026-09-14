#Inheritance (Kalıtım): Miras Alma, önceden yazılan özellikleri başka bir şeye aktarma
''' 8.4
class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName=lname
        print("Person Created")
    def who_am_i(self):
        print("I am a person")
    def eat(self):
        print("I am eating")
class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Student Created")
    #overrride aynı isimdeki metod temel seviye metodu ezer
    def who_am_i(self):
        print("I am a student")

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname) #Yapıcı metodun çağırılmasını super() fonksiyonu sağlar.
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

p1 = Person('Bora', 'Aydın')
s1=Student('Sude Naz', 'Samancı', 1024)
t1 = Teacher('Metin', 'Kahraman', 'Math')

t1.who_am_i()

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
'''
#####################################################################################
#8.5
'''mylist = [1,2,3]
#print(len(mylist))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu")
    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    def __del__(self):
        return self.duration

m = Movie('film adı', 'yönetmen adı', 120)

#print(len(mylist))
#print(len(m))
print(str(m))
'''

##################################################################################

#8.6
#Question

#Quiz
