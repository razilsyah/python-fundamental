# input variable
gaji_poko = int(input("masukan gaji poko anda :"))
status_menikah = bool(int(input("masukan status menikah :")))
golongan = input("masukan golongan anda :")

# proses
if status_menikah is True:
    tunjangan_kelaurga = gaji_poko * 0.25
    print("status meikah")
else:
    tunjangan_kelaurga = 0

if golongan == "a" or golongan == "A":
    tunjangan_jabatan = gaji_poko * 0.3
elif golongan == "b" or golongan == "A":
    tunjangan_jabatan = gaji_poko * 0.25
else:
    tunjangan_jabatan = gaji_poko * 0.15

# output
gaji_pegawai = gaji_poko + tunjangan_kelaurga+ tunjangan_jabatan
print(tunjangan_jabatan)
print(gaji_pegawai)
