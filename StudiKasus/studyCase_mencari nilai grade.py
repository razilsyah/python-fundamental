

# # mencari nilai
# siswa1 = int(input("siswa 1 ,masukan nilai anda :"))
# siswa2 = int(input("siswa 2 ,masukan nilai anda :"))
# siswa3 = int(input("siswa 3 ,masukan nilai anda :"))
#
#
# def nilaiSiswa(siswa):
#     if 90 <= siswa < 100 :
#         print(siswa,"=nilai anda grade A+")
#     elif 80 <= siswa <90:
#         print(siswa,"= nilai anda grade A")
#     elif 70 <= siswa <80:
#         print(siswa,"nilai anda grade B")
#     elif 60 <= siswa <70:
#         print(siswa,"nilai anda grade C")
#     elif 55 <= siswa <60:
#         print(siswa,"= nilai anda grade D")
#     else:
#         print(siswa,"nilai anda grade E")
#
# nilaiSiswa(siswa=siswa1)
# nilaiSiswa(siswa=siswa2)
# nilaiSiswa(siswa=siswa3)


# nilais = []
#
# jml_siswa = int(input("masukan jumlah siswa = "))
#
# for i in range(1, jml_siswa + 1):
#     nilai = int(input(f"masukan nilai siswa ke {i} = "))
#     nilais.append(nilai)
#
# for i in nilais:
#     nilai = i
#     if nilai >= 90:
#         grade = "A+"
#     elif nilai >= 80:
#         grade = "A"
#     elif nilai >= 70:
#         grade = "B"
#     elif nilai >= 60:
#         grade = "C"
#     elif nilai >= 55:
#         grade = "D"
#     else:
#         grade = "E"
#
#     print(f"grade {nilai} = {grade} ")



jumlah_siswa = int(input("masukan jumlah siswa :"))
array = []
for i in range(1,jumlah_siswa + 1):
    nilai = int(input("masukan nilai mahasiswa ke-"+str(i)+" :"))
    array.append(nilai)

for i in array:
    coba = i
    if coba >= 90:
        grade = "A"
    elif coba >= 80:
        grade = "B"
    elif coba >= 70:
        grade = "C"
    elif coba >= 60:
        grade = "D"
    else:
        grade = "anda tidak lulus"

    print(f"nilai anda {coba} {grade}")



























