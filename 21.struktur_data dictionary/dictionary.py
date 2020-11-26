# Dictionary adalah tipe data yang anggotanya terdiri dari pasangan kunci:nilai (key:value), Dictionary bersifat tidak berurut (unordered) sehingga anggotanya tidak memiliki indeks.

# key:value

### membuat dictionary
print("===== membuat dictionary ========")
penduduk = {"ID":123445,
            "Nama":"razilsyah",
            "alamat":"sumedang"
            }
print(penduduk)


### mengakses properti dalam dictionary
# bisa langsung key atau fungsi get()
print("===== mengakses dictionary ========")
print(penduduk["ID"])
print(penduduk.get("alamat"))


### mengubah properti dictionary
print("===== mengubah dictionary ========")
penduduk = {"ID":123445,
            "Nama":"razilsyah",
            "alamat":"sumedang"
            }
#1
penduduk["Nama"]= "khalinda"
print(penduduk)

#2
penduduk["No hp"] = 123456
print(penduduk)


### menghapus properti dictionary
print("===== menghapus dictionary ========")

penduduk = {"ID":123445,
            "Nama":"razilsyah",
            "alamat":"sumedang"
            }
print(penduduk)
print("penduduk.pop('nama') = ",penduduk.pop("Nama"))
print(penduduk.popitem())
print(penduduk)




















