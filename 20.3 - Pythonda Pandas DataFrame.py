import pandas as pd 

# df = pd.DataFrame()
#df = pd.DataFrame([1,2,3,4])

data1 = [["Ahmet",50],["Ali",60],["Yağmur",70]]

df = pd.DataFrame(data1,index = [1,2,3], columns= ['Name','Grade'])
print(df)
#dtype = float yaparsak eğer notları 50.0 vs şeklinde yazar

dict = {"Name": ["Ahmet", "Ali", "Yağmur", "Çınar"], "Grade": [50,60,70,80]}
df = pd.DataFrame(dict, index = ["212","232","236","456"])
print(df)

dict_list = [
                {"Name":"Ahmet","Grade":50},
                {"Name":"Ali","Grade":60},
                {"Name":"Sude","Grade":80}
            ]

df = pd.DataFrame(dict_list)
print(df)



# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, oranges = s2)

# df = pd.DataFrame(data)

# print(df)

