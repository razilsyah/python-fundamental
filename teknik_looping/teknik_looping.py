
nama_band = ["fiersa besari",
             "noah",
             "sheila on 7",
             "d'masih"]

for band in nama_band:
    print(band)

### untuk menampilkan index dan valuenya
# 1.enumerate()
print("====== enumerate =======")
nama_band = ["fiersa besari",
             "noah",
             "sheila on 7",
             "d'masip"]

for index,valuenya in enumerate(nama_band):
    print(index,":",valuenya)

# zip()
print("====== zip =======")
lagu = ["april",
        "wanitaku",
        "dan",
        "dmasip"]
for band_ini,nyanyi_lagu in zip(nama_band,lagu):
    print(band_ini,"menyanyikan lagu",nyanyi_lagu)



# set
print("======= set ========")
himpunanGorengan = {"combro","tahu","surabi","kue putu"}
for i in sorted(himpunanGorengan):
    print(i)

# dictionary
print("======= dictionary ========")
kamusLagu = {"fiersa besari":"april",
             "noah":"wanitaku",
             "sheila on 7":"dan",
             "d'masip":"dmasip"}

for i,v in kamusLagu.items():
    print(i,v)
print("===== jika ingin di balik ======")
for i in reversed(kamusLagu):
    print(i)







