# OPERASI DAN MANIPULASI STRING


nama_awal = "razil"
nama_tengah = "syah"
nama_terakhir = "arihardjo"

nama_panjang = nama_awal+" " + nama_tengah +" "+ nama_terakhir
print(nama_panjang)

# 1.menghitung panjang karakter
# length (len)
print("=====LENGTH=======")
menghitung_panjangNama = len(nama_panjang)
print(menghitung_panjangNama)


# 2.mengecek apakah ada komponen string di dalam string
# in
print("======= IN ========")
mengecek_hurufRaz = "raz"
caranya = mengecek_hurufRaz in nama_panjang
print("apakah huruf " + mengecek_hurufRaz+" ada di "+nama_panjang +" = "+str(caranya))


mengecek_hurufRAZ = "RAZ"
caranya = mengecek_hurufRAZ in nama_panjang
print("apakah huruf " + mengecek_hurufRAZ+" ada di "+nama_panjang +" = "+str(caranya))

# not in
print("======= not in ========")
mengecek_hurufRAZ = "RAZ"
caranya = mengecek_hurufRAZ not in nama_panjang
print("apakah huruf " + mengecek_hurufRAZ+" ada di "+nama_panjang +" = "+str(caranya))



# 3.MENGULANG STRING
print("======= MENGULANG STRING ========")
print("ha"*10)
print(15*"ha")


# 4.INDEXING
print("======= INDEXING ========")

full_name = "sandiaga uno"

# mengambil index
print("======= MENGAMBIL INDEX ========")

print("panjang karakter "+full_name+ " = "+str(len(full_name)))
print("mengambil index ke-3 : "+full_name[4])
print("mengambil index ke-10 : "+full_name[11])

# mengambil index dengan range
print("======= MENGAMBIL INDEX DENGAN RANGE ========")

print("mengambil index ke-[1:10]  : "+full_name[1:11])
print("mengambil index ke-[3:8]  : "+full_name[3:9])

# mengambil index dengan berkelipatan
print("======= MENGAMBIL INDEX  DG BERKELIPATAN ========")

print("mengambil index ke-[2,4,6,8,10]  : "+full_name[2:11:2])
print("mengambil index ke-[3,6,9,11]  : "+full_name[3:12:3])


# 5.MENGAMBIL charakter DARI YANG KECIL DAN BESAR
print("======= MENGAMBIL KARAKTER DARI YANG KECIL ========")

full_name = "jalaludin muhammah akbar"
print("karakter paling kecil :"+ min(full_name))

full_name = "jalaludin muhammah akbar"
print("karakter paling besarl :"+ max(full_name))

ascii_code = ord(" ")
print("ASCII code untuk spasi :"+str(ascii_code))
charakter = 200
print("charakter ascii 200 adalah : "+chr(charakter))

























