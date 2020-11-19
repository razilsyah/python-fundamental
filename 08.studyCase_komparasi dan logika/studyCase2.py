

# ------0++++++5------8++++++11-------
inputUser = float(input("masukan angka \n lebih besar dari 0 dan lebih kecil dari 5 :\n atau \n lebih besar dari 8 dan lebih kecil dari 11 :"))
# mencari angka lebih besar 0
besar1 = inputUser > 0 and inputUser <5
print("angka yang anda masukan ,lebih besar dari 0:",besar1)

# mencari angka lebih kecil 5
kecil1 = inputUser < 5 and inputUser >0
print("angka yang anda masukan,lebih kecil dari 5 :",kecil1)

# mencari angka lebih besar dari 8
besar = inputUser > 8 and inputUser <=11
print("angka yang anda masukan lebih besar dari 8 :",besar)

# mencari angka lebih kecil dari 11
kecil = inputUser < 11 and inputUser >=8
print("angka yang anda masukan lebih kecil dari 11 :",kecil)

# irisan kondisi >0 dan <5
hasil1 = besar1 and kecil1
print("hasilnya :",hasil1)

# irisan kondisi >8 <11
hasil = besar and kecil
print("hasilnya :",hasil)

# di gabungkan semua kondisi
gabung = (besar1 and kecil1) or (besar and kecil)
print("hasil dari keseluruhan :",gabung)