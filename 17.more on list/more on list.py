# method-method dalam list

barang = ["kunci",'setrika',"ps","handphone"]
# append() menambahkan data dalam list di akhir
barang.append("telephon")
print(barang)

# menghitung jumlah objek yang terdapat dalam list
jumlah_count = barang.count("kunci")
print(jumlah_count)

# menambahkan tiap karakter yang terdapat dalam kalimat kunci ke dalam list
barang.extend("kunci")
print(barang)

#cara untuk mengcopy suatu variable ke variable lain
copy_barang = barang.copy()
copy_barang.append("sosorodotan")
print(copy_barang)
print(barang)