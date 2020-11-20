# OPERATOR DALAM BENTUK METHOD
# mengtung jumlah karakter yang di inginkan pada string
print("======= MENGHITUNG JML STRING ==========")
nama = "bobobobobobbbbbbb"
jumlah = nama.count("b")
'''
nama = objek
count() = method 
'''
print("jumlah b pada "+ nama+ " = "+str(jumlah)+"\n")



# merubah string menjadi uppercase
print("======= UPPERCASE ==========")
salam = "hallo brooo!!"
print("normal = "+salam)
upper_salam = salam.upper()
print("uppercase = "+upper_salam+"\n")


# merubah string menjadi lower case
print("======= LOWER CASE ==========")
salam = "HALLOOOOO COOOYYYYYY!!"
print("normal = "+salam)
lower_salam = salam.lower()
print("uppercase = "+lower_salam+"\n")



# IS berfungsi mengcek kondisi yang terdapat di sebuah string
print("======= ISUPPER ==========")
salam = "HALLOOOOO COOOYYYYYY!!"
print("normal = "+salam)
upper_salam = salam.isupper()
print("apakah di "+salam+" memakai uppercase? "+str(upper_salam)+"\n")

# IS LOWER
print("======= ISLOWER ==========")
salam = "HALLOOOOO COOOYYYYYY!!"
print("normal = "+salam)
lower_salam = salam.islower()
print("apakah di "+salam+" memakai lowercase? "+str(lower_salam)+"\n")

# isalpha berfungsi mengecek apakah semuanya huruf
# isalnum berfungsi mengecek huruf angka
# isdecimal berfungsi mengecek angka saja
# isspace berfungsi mengcek  spasi,tab ,newline \n

# contoh istitle untuk mengecek setiap kalimat di awali kapital
print("======= ISTITLE ==========")
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print("apakah "+judul+" menggunakan istitle = "+str(cek_judul)+"\n")


# MENGCEK KOMPONEN STARTSWITH() DAN ENDSWITH()
print("======= STARTSWITH() ==========")
cek_start = "razil syah arihardjo".startswith("razil")
print("start = "+str(cek_start))

print("======= ENDSWITH() ==========")
cek_start = "razil syah arihardjo".endswith("razil")
print("end = "+str(cek_start)+"\n")


# PENGGABUNGAN KOMPONEN =>> join() split()
print("======= JOIN() ==========")
nama = ["razil","syah","arihardjo"]
print(nama)
nama_join = "-".join(nama)
print(nama_join)

# SPLIT()
print("======SPLIT========")
print(nama_join.split("-"))


# #ALOKASI KARAKTER rjust() ljust() center()
print("========ALOKASI KARAKTER=======")
# CONTOH
print(20*"=")

r_just = "razil".rjust(30) # maka razil akan di sudut kanan dg panjang karakter 30
print(" ' "+r_just+" ' ")

l_just = "razil".ljust(30) # maka razil akan di sudut kiri dg panjang karakter 30
print(" ' "+l_just+" ' ")

center = "razil".center(30,":")# maka razil akan di sudut kiri dg panjang karakter 30
print(" ' "+center+" ' ")

# KEBALIKANNYA STRIP()
strip = center.strip(":") # maka akan menghilangka :
print(" ' "+strip+" ' ")


