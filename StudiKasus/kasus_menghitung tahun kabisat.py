tahun = int(input("masukan tahun :"))

if tahun % 4 == 0:
    if tahun % 100 == 0:
        if tahun % 400 == 0:
            print("tahun ini kabisat")
        else:
            print("tahun ini bukan kabisat")
    else:
        print("tahun ini kabisat 1")
else:
    print("sudah pasti bukan tahun kabisat")























#
# tahun = int(input("Input tahun: "))
#
# if (tahun % 4) == 0:
#     if (tahun % 100) == 0:
#         if (tahun % 400) == 0:
#             print( "Tahun Kabisat")
#         else:
#             print( "Bukan Tahun Kabisat 1")
#     else:
#         print( "Tahun Kabisat 1")
# else:
#     print( "Bukan Tahun Kabisat")