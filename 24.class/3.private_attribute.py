class mencari_nilai():
    __nilai = 0 # private
    nilai = 0 # publik
    def uts(self,nilai_uts):
        self.__nilai += nilai_uts

    def uas(self,nilai_uas):
        self.__nilai += nilai_uas

    def hasil_uts_dan_uas(self):
        if self.__nilai >= 50:
            print("anda lulus")
        else:
            print("anda tidak lulus")


razil = mencari_nilai()
razil.uts(10)
razil.uas(20)
razil.hasil_uts_dan_uas()
# print(razil.__nilai) ini akan error karna mengakses variable private
# print(razil.nilai) ini tidak akan error karna variable publik