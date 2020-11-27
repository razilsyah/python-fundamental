class mobil():

    def __init__(self,kondisi):
        self.Nama = kondisi

    def belajar(self,lokasi): #fungsi dalam class disebut method
        print(self.Nama,"sedang tes drive",lokasi)


# main programnya

classMobil = mobil("toyota")
print(classMobil.Nama)

classMobil.belajar("di sumedang")