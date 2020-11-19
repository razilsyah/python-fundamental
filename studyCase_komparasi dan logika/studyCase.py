# +++++++++3--------------10++++++++++++
# masukan angka kurang dari 3 atau lebih besar dari 10
inputUser = float(input(" masukan angka\n kurang dari 3\n atau\n lebih dari 10 :"))
kurangDari = inputUser < 3
lebihBesarDari = inputUser > 10
print("angka yang anda masukan \n kurang dari 3 :",kurangDari,"\n atau \n lebih besar dari 10 :",lebihBesarDari)

hasilKeduaBilangan = kurangDari or lebihBesarDari
print("angka yang anda masukan adalah :",hasilKeduaBilangan)

# ------3++++++++++++10---------------
# masukan angka lebih dari 3 dan kurang dari 10 (kasus irisan)
print("============================")
inputUser = float(input("masukan angka \n lebih besar dari 3 :\n dan \n lebih kecil dari 10 :"))

lebihBesarDari = inputUser > 3
kurangDari = inputUser < 10
print("angka yang anda masukan \n lebih dari 3 :",lebihBesarDari,"\n dan \n lebih kecil dari 10 :",kurangDari)


hasilKeduaBilangan = lebihBesarDari and kurangDari
print("angka yang anda masukan adalah :",hasilKeduaBilangan)


