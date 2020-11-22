# program menentukan bilangan genap ganjil

angka = int(input("mencari angka ganjil genap!!\nmasukan angka: "))

for i in range(1,angka+1):
    if i % 2 == 0 :
        print(i,"= bilangan genap")
    else:
        print(i," = bilangan ganjil")