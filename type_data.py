# type data

# 1.tipe data integer ,bilangan satuan tanpa koma
from ctypes import c_double
integer = 1
nomor = 2
nomor2 = 3
print(nomor, integer)
print(type(nomor))


# 2. tipe data float ,bilangan angka desimal/koma
data_float = 5.1

print(data_float)
print(type(data_float))


# 3.tipe data boolean , true/false
data_bool = True
print(data_bool)
print(type(data_bool))


# TIPE DATA KHUSUS
# bilangan complex
bilangan_complex = complex(5, 10)
print(bilangan_complex)
print(type(bilangan_complex))


# tipe data mengambil dari bahasa C
# import library bahasa C terlebih dahulu
data_c_double = c_double(11.1)
print(data_c_double)
print(type(data_c_double))
