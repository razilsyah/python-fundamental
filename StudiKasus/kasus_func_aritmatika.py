


def menu():
    print("----inputkan yang ingin di pilih----")
    print("1.penjumalahan")
    print("2.pengurangan")
    print("3.perkalian")
    print("4.pembagian")

def inputtt():
    user = 0
    while user != 6:
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




# def aritmatikaPenjumlahan(a,b):
#     hasil = a + b
#     print(a, "+", b ,"=",hasil)
#     return hasil
#
# def aritmatikaPengurangan(a,b):
#     hasil = a - b
#     print(a, "+", b ,"=",hasil)
#     return hasil
#
# def aritmatikaPerkalian(a,b):
#     hasil = a * b
#     print(a, "+", b ,"=",hasil)
#     return hasil
#
# def aritmatikaPerkalian(a,b):
#     hasil = a / b
#     print(a, "+", b ,"=",hasil)
#     return hasil



# output
menu()
inputtt()