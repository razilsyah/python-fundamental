# 1.menghitung konversi satuan celcius ke satuan lain

print("=====MENGHITUNG KONVERSI SATUAN SUHU CELCIUS======= ")

celcius = float(input("masukan nilai suhu anda :"))
print("suhu anda :", celcius, "celcius", " type data:", type(celcius))


# konversi satuan celcius ke reamur
reamur = (4/5) * celcius
print("suhu anda :", reamur, "reamur", "type data:", type(reamur))

# konversi satuan celcius ke kelvin
kelvin = celcius + 273
print("suhu anda :", kelvin, "kelvin", "type data:", type(kelvin))

# konversi satuan celcius ke fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu anda :", fahrenheit, "fahrenheit", "type data:", type(fahrenheit))
