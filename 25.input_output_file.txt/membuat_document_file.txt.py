"""
w = write mode /mode menulis dan menghapus file lama ,jika tidak ada file maka akan di buatkan file baru
r = read mode only /hanya bisa baca
a = menambahkan data di akhir baris
r+ = write and read mode
"""
# membuat file txt
file = open("document","w")
file.write( 'ini adalah document yang di tulis menggunakan python\n' )
file.write( '\nini adalah document yang di tulis menggunakan python baris kedua' )
file.write( '\nini adalah document yang di tulis menggunakan python baris ketiga' )
file.write( '\nini adalah document yang di tulis menggunakan python baris keempat' )

file.close()

# membaca file txt
file2= open("document","r")
print(file2.read())
file2.close()

