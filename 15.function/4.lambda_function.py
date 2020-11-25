# function biasa
print("===function biasa===")
def tambah(a,b):
    c = a + b
    return c

hasil = tambah(5,7)
print(hasil)


# anonymous lambda adalah membuat fungsi dalam satu baris dan bersifat anonymous atau fungsi tanpa nama
# contoh 1
print("====contoh 1 lambda====")
kali = lambda argument1,argument2: argument1 * argument2
hasil_kali = kali(8,9)
print(hasil_kali)

# contoh 2
print("====contoh 2 lambda====")
# menggunakan method map()
angkaList = [2,4,6,8,10]
kali = map(lambda x : x * x,angkaList) # angkaList berfungsi sbagai value argumen lambda
print(list(kali))


# contoh 3
# menggunakan method filter dan di masukan ke dalam list
print("====contoh 3 lambda====")
mod = lambda x : x % 2 == 0
print(list(filter(mod,range(20))))