# perbandingan struktur data list dan tuple
# tuple di mulai dengan ()
# tuple bersifat constanta atau tidak bisa di rubah
# kecepatan dan mengambil memori, lebih kencang dan sedikit
# wort it untuk menyimpan data id,nik,dll yang sifatnya permanen

# list dan tuple
data_list = [1,2,3,4,5,6]
data_tuple = (1,2,3,4,5,6)
print(data_list)
print(data_tuple)

data_list.append(9)
print(data_list)

# data_tuple.append() => data tuple tidak bisa di tambah datanya ,akan terjadi error



# cara mengetahui apa saja yang bisa di lakukan oleh struktur data
print("========= method data list ==========")

method_list = dir(data_list)
print(method_list)

print("========= method data tuple ===========")

method_tuple = dir(data_tuple)
print(method_tuple)






