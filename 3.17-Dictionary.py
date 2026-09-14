#key - value 
#41 - kocaeli vb.

'''sehirler = ['kocaeli', 'istanbul']
plakalar = [41,34]

print(plakalar[sehirler.index('kocaeli')]) #Uzun yolu gibi

#plakalar = {'key': 'value'}
plakalar = {'kocaeli' : 41, 'istanbul' : 34}
print(plakalar['kocaeli']) #Bu ise dictionary 

plakalar['ankara'] = 6 #yeni eleman ekleme

print(plakalar)'''

users = {
    'sadikturan' : {
        'age' : 36,
        'email': 'sadik@gmail.com'

    },
    'boraaydın' : {
        'age' : 21,
        'email': 'bora06519@gmail.com'
    }
}

print(users)
print(users['boraaydın']['email'])