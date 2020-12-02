class Ojek():
    def __init__(self,nama,transmision,daerah):
        self.nama = nama
        self.transmision = transmision
        self.daerah = daerah


    def cek_status_ojek(self):
        print(f"nama : {self.nama}\nmotor : {self.transmision}\ndaerah : {self.daerah}")

class Grab(Ojek): # ini inheritance atau warisan => grab() mewarisi semua yang ada di dalam Ojek()

   def cek_status_ojek(self): # method grab menimpa method si ojek()
       print("cek aplikasi ")



ojek1 = Ojek("razilsyah","automatic","paramon")
ojek1.cek_status_ojek()

print("====================================")

ojek2 = Grab("chugong","manual","sawah dadap")
ojek2.cek_status_ojek()