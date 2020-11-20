'''
 looping while berfungsi melakukan perulangan terus menerus jika kondisinya bernilai true,dan akan berhenti jika bernilai false
'''
# contoh 1 menggunakan tipe syarat
print(5*"=","contoh 1","="*5)
angka = 0
while angka < 5 :
    print("angka") # jika sampai disini akan terus di jalankan
    angka += 1 # increement kondisinya sampai bernilai false
print("ini di luar while")

# contoh 2 menggunakan tipe boolean
print(5*"=","contoh 2","="*5)

bool = True
angka = 1
while bool:
    print("di dalam while")
    if angka is 20:
        bool = False
        print("angka berada di 20")
    angka += 1


