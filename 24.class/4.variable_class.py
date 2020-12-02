# variable class contoh sedernana untuk counter
# yang ada self berarti punyanya si instensi = razil,chugong
class mahasiswa():

    jumlah_mahasiswa = 0
    def __init__(self,input_nama,input_nim):
        self.nama = input_nama
        self.nim = input_nim

        mahasiswa.jumlah_mahasiswa += 1

razil = mahasiswa("razilsyah",123455)
chugong = mahasiswa("robby rama",1233445)
print(razil.nama)
print(razil.nim)
print(chugong.nama)
print(chugong.nim)
print(mahasiswa.jumlah_mahasiswa)







