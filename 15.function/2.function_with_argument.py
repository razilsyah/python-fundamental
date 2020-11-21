# function menggunakan argumen sederhana

def siswa(nama):
    print("nama siswa ini adalah",nama)

siswa("razil")


# fungsi dengan menggunakan keyword argument

def guru(nama,mengajar):
    print("nama guru adalah :",nama)
    print("mengajar :",mengajar)

guru(nama="hamdan",mengajar="teknik informatika")
guru(mengajar="teknik informatika",nama="hamdan")



# fungsi menggunakan default argument

def penjagaSekolah(nama,shift="siang",sifat="galak"):
    print("nama penjaga sekola :",nama)
    print("shift :",shift)
    print("sifat :",sifat)

penjagaSekolah("bargo")
penjagaSekolah() #ini akan eror
