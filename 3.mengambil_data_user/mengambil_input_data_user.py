# # data yang di masukan pasti string
data = input("masukan apa saja :")
print("input dari user:", data, ",bertype: ", type(data))


# jika ingin mengambil integer ,maka

integer = int(input("masukan angka: "))
print("angka :", integer, "bertype", type(integer))

# FLOAT
f_loat = float(input("masukan angka"))
print("angka :", f_loat, "bertype", type(f_loat))

# jika boolean,jika bernilai 1=true / 0=false
boolean = bool(int(input("masukan nilai integer :")))
print("data yang di masukan user:", boolean, "bertype: ", type(boolean))
