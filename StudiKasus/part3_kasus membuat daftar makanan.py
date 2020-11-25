menu = ""
total_harga=0
def functionMakanan(menu,total_harga):
    while menu != "bayar":
        print("====daftar menu=====")
        print("Nasi goreng = 15000")
        print("Baso = 10000")
        print("bayar !!")

        menu = input("masukan menu yang ingin di beli :")
        if menu == "nasi goreng":
            harga = 15000
        elif menu == "baso":
            harga = 10000
        elif menu == "bayar":
            continue
        else:
            continue

        total_harga = total_harga + harga
        print("total=",total_harga)

    else:
        print("====pembayaran====")
        print("total=",total_harga)

functionMakanan(menu,total_harga)
