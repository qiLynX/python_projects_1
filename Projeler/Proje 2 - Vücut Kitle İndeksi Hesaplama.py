print("*" * 10 + "Vücut Kitle İndeksi Hesaplayıcı" + "*" * 10 )
boy=float(input("Boyunuzu metre cinsinden giriniz: "))
kilo=float(input("Kütlenizi kilogram cinsinden giriniz: "))
vki=kilo/(boy*boy)
print(f"Vücut kütle indeksi hesaplamasına göre çıkan sonucunuz: {vki:.2f}") #:.2f virgülden sonra 2 basamağın yazılmasını sağlar. 