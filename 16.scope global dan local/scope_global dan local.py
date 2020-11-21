# scope variable local

namaKucing = "sheliii"

def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru
    print("saya rubah nama kucing menjadi",namaKucing)

rubahNamaKucing("udinnn")

print("nama kucing di luar function :",namaKucing)


# scope variable global
print(10*"=","scope global","="*10)
def rubahNamaKucing(namaBaru):
    global namaKucing # ini akan merubah yang di luar function / global
    namaKucing = namaBaru
    print("saya rubah nama kucing menjadi",namaKucing)

rubahNamaKucing("udinnn")
print("nama kucing di luar function :",namaKucing)
