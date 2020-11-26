# Set adalah salah satu tipe data di Python yang tidak berurut (unordered). Set memiliki anggota yang unik (tidak ada duplikasi). Jadi misalnya kalau kita meletakkan dua anggota yang sama di dalam set, maka otomatis set akan menghilangkan yang salah satunya
# Set bisa digunakan untuk melakukan operasi himpunan matematika seperti gabungan, irisan, selisih, dan lain – lain.

### contoh menambah data pada set
print("======MENAMBAH DATA =======")
set1 = {1,2,3,4,5}
print(set1)


# set1.add([6]) => ini akan error karna list tidak bisa di masukan ke dalam set
set1.add(6)
print(set1)

set1.add("gatot kaca")
set1.update([22,33,44,55,66]) # untuk update() harus memasukan list,string,tuple untuk inisialisasi agar tidak error
print(set1)

### menghapus data pada set
# remove() atau discard()
print("====== MENGHAPUS DATA =======")

set2 = set("gorengan")
set2.discard("z") # ini tidak akan error bila menggunakan discard()
set2.remove("g")
print(set2)


### menggabungkan data set
# union() atau bitwise logika |
# 1
print("====== GABUNGAN SET ======")
set3 = {1,2,3,4,5}
set4 = {4,5,6,7,8,9}
data_awal = set3.union(set4)
print("data awal =",data_awal)
gabuangan_set = set3.union(set4)
print(gabuangan_set)

# 2
gabuangan_set = set3 | set4
print(gabuangan_set)



### mengiris pada set
# intersection() atau bitwise logika &
# 1
print("====== MENGIRIS SET ======")
set3 = {1,2,3,4,5}
set4 = {4,5,6,7,8,9}
data_awal = set3.union(set4)
print("data awal =",data_awal)
gabuangan_set = set3.intersection(set4)
print(gabuangan_set)

# 2
gabuangan_set = set3 & set4
print(gabuangan_set)


### selisih pada set
# difference() atau operator -
print("====== SELISIH SET ======")
set3 = {1,2,3,4,5}
set4 = {4,5,6,7,8,9}
data_awal = set3.union(set4)
print("data awal =",data_awal)
gabuangan_set = set3.difference(set4)
print(gabuangan_set)

# 2
gabuangan_set = set4 - set3
print(gabuangan_set)


### komplemen
# symmetric difference atau operator bitwise ^
print("====== komplemen SET ======")
set3 = {1,2,3,4,5}
set4 = {4,5,6,7,8,9}
data_awal = set3.union(set4)
print("data awal =",data_awal)
gabuangan_set = set3.symmetric_difference(set4)
print(gabuangan_set)

# 2
gabuangan_set = set4 ^ set3
print(gabuangan_set)
























