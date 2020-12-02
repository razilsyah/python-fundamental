nilai_awal = ""
while nilai_awal != "hasil":
    for i in range(1,2):
        input_nama = input("nama anda :")
        user1 = float(input("masukan nilai bahasa indonesia :"))
        user2 = float(input("masukan nilai bahasa inggris : :"))
        user3 = float(input("masukan nilai bahasa matematika :"))
        user4 = float(input("masukan nilai ipa :"))

    nilai_awal = "hasil"

class mencari_nem():


    def __init__(self,input_nama):
        self.nama = input_nama
        print(self.nama, "nilai anda adalah sebagai berikut :")

    def mata_pelajaran(self,nilai_indo,nilai_eng,nilai_mtk,nilai_ipa):
        nama_pelajaran = [{"nama pelajaran": [{"bahasa indonesia": nilai_indo,
                                                    "bahasa inggris": nilai_eng,
                                                    "matematika": nilai_mtk,
                                                    "ipa": nilai_ipa}
                                                   ]}]
        for i, val in nama_pelajaran[0]["nama pelajaran"][0].items ():
            print(i,":",val)

        total = nilai_indo + nilai_eng + nilai_mtk + nilai_ipa
        return total



    def nem(self,mata_pelajaran):
        if mata_pelajaran >= 27:
            grade = "A"
        else:
            grade = "B"

        print(f"nem anda adalah {mata_pelajaran} dan mendapatkan grade = {grade}")


razil = mencari_nem(input_nama)
# print(razil.nama)
a = razil.mata_pelajaran(nilai_indo=user1,nilai_eng=user2,nilai_mtk=user3,nilai_ipa=user4)
razil.nem(a)
