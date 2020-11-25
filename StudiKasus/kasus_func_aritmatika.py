


def menu():
    print("----inputkan yang ingin di pilih----")
    print("1.penjumalahan")
    print("2.pengurangan")
    print("3.perkalian")
    print("4.pembagian")

def inputtt():
    user = 0
    while user != 6:
        menu()
        user = int(input("input pilihan anda :"))
        if user == 1:
            print("===penjumlahan===")
            penjumlahan1 = int(input("masukan angka pertama: "))
            penjumlahan2 = int(input("masukan angka kedua  : "))
            hasil = penjumlahan1 + penjumlahan2
            print(penjumlahan1, "+", penjumlahan2, "=", hasil)
        elif user == 2:
            print("===pengurangan===")
            pengurangan1 = int(input("masukan angka pertama: "))
            pengurangan2 = int(input("masukan angka kedua  : "))
            hasil = pengurangan1 - pengurangan2
            print(pengurangan1, "-", pengurangan2, "=", hasil)
        elif user == 3:
            print("===perkalian===")
            perkalian1 = int(input("masukan angka pertama: "))
            perkalian2 = int(input("masukan angka kedua  : "))
            hasil = perkalian1 * perkalian2
            print(perkalian1, "*", perkalian2, "=", hasil)
        elif user == 4:
            print("===pembagian===")
            pembagian1 = int(input("masukan angka pertama: "))
            pembagian2 = int(input("masukan angka kedua  : "))
            hasil = pembagian1 / pembagian2
            print(pembagian1, "/", pembagian2, "=", hasil)
        elif user == 6:
            print("trimakasih")
            break
        else:
            print("inputan salah")

'''ALGORITMA YANG INI JUGA BISA'''
# def tambah(a,b):
#     return a + b
#
# def kurang(a,b):
#     return a - b
#
# def kali(a,b):
#     return a * b
#
# def bagi(a,b):
#     return a / b
#
#
# print("--- Program operator aritmatika ---")
# print("1. tambah")
# print("2. kurang")
# print("3. kali")
# print("4. bagi")
# menu = int(input("Input pilihan operator = "))
# bil1 = int(input("input bil pertama = "))
# bil2 = int(input("input bil kedua = "))
#
# if menu == 1:
#     hasil = tambah(bil1,bil2)
#     print(f"hasil dari penjumlahan {bil1} + {bil2} = {hasil}")
# elif menu == 2:
#     hasil = kurang(bil1, bil2)
#     print(f"hasil dari pengurangan {bil1} - {bil2} = {hasil}")
# elif menu == 3:
#     hasil = kali(bil1, bil2)
#     print(f"hasil dari perkalian {bil1} x {bil2} = {hasil}")
# else:
#     hasil = bagi(bil1, bil2)
#     print(f"hasil dari pembagian {bil1} / {bil2} = {hasil}")


# output
# menu()
inputtt()