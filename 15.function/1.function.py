# def untuk mendeklarasi function
# function dapat di panggil berulang-ulang
# contoh sederhana aplikasi harga ayam


# input
user = int(input("masukan kg yang akan di beli:"))

# proses
def suaraAyam():
    print("kukuruyukkkkk")

def hargaTotal(kg):
    suaraAyam()
    harga = 20000
    hargaTotal = kg*harga
    print("harga",kg,"kg ayam adalah",hargaTotal)

# output
hargaTotal(user)