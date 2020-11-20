# list sebagai iterable
buah = ["mangga","durian","pisang","buah naga","alpukat"]

for nama_buah in buah:
    print(nama_buah)
    print(len(nama_buah))
print(len(nama_buah))

# string sebagai iterable
mangga = "mangga"

for i  in mangga:
    print(i)


# for di dalam for
buah = ["mangga","durian","pisang","buah naga","alpukat"]
gorengan = ["bakwan","goreng pisang","gehu","goreng tempe"]
sayur = ["kangkung","wortel","kentang","terong"]

daftar_belanja =[ buah , gorengan , sayur]
print(daftar_belanja)

for subDaftarBelanja in daftar_belanja:
    print(subDaftarBelanja)
    for i in subDaftarBelanja:
        print(i)
        for j in i:
            print(j)




