# luas persegi panjang
def luas_persegiPanjang(p,l):
    luas = p * l
    return luas
luas = luas_persegiPanjang(p=7,l=3)
print(luas)


# menghitung keliling lingkaran
def keliling_lingkaran(r):
    keliling = 2 * 3.14 * r
    return keliling

keliling = keliling_lingkaran(14)
print(keliling)

# nilai terkecil
list = [90,85,80,75,70,65,55,34]

def nilai_terkecil(l):
    terkecil = l[0]
    for index in range(1,len(l)):
        nilai = l[index]
        if nilai < terkecil:
            terkecil = nilai
    return terkecil

hasilnya = nilai_terkecil(list)
print(hasilnya)

# nilai terbesar
def nilai_terbesar(l):
    terbesar = l[0]
    for index in range(1,len(l)):
        nilai = l[index]
        if nilai > terbesar:
            terbesar = nilai
    return terbesar

hasil = nilai_terbesar(list)
print(hasil)


