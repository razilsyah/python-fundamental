data = [2,4,6,8,10,12,14,16]
print(data)

# mengakses value pada list
subdata = data[2]
print(subdata)

# memotong value pada list
subdata2 = data[2:7]
subdata3 = data[1:3]
print(subdata2)
print(subdata3)

# menambahkan value pada list
data2 = [3,6,9,12,15,18,21]
tambah_data = data + data2
print(tambah_data)

# merubah value pada list
data2[3]= 1222334
print(data2)

# mengcopy list ke variable baru
copy_list = data2[:]
print(copy_list)
copy_list[4] = 6666
print(copy_list)
print(data2)

# merubah value pada list dg metode slicing
data2 [2:5]= [77,87]
print(data2)

# list dalam list / multidimensional list
list1 = [data,data2]
print(list1)

# mengakses multidimensional list
akses_multiList = list1[0] [1] # dalam variable list akses list 0 index ke-1
print(akses_multiList)
akses_multiList = list1[1] [4] # dalam variable list akses list 1 index ke-4
print(akses_multiList)

# contoh method dalam list append()

alist = [123,'razil']
alist.append(100)
print(alist)


















