# operasi logika
# NOT,OR ,AND ,XOR

# NOT (kebalikan dari nilai oeprasi logika)
print("=====NOT=====")
a = True
d = False
print("operasi a =", a, "operasi d =", d)

hasil = not a
print("NOT a =", hasil)
hasil = not d
print("NOT d =", hasil)

# OR (jika salah satu bernilai true maka hasil akan true)
print("====OR====")
x = False
z = False
hasil = x or z
print(x, "or", z, "=", hasil)

x = True
z = False
hasil = x or z
print(x, "or", z, "=", hasil)

x = True
z = True
hasil = x or z
print(x, "or", z, "=", hasil)

x = False
z = True
hasil = x or z
print(x, "or", z, "=", hasil)

# AND (semuanya harus bernilai true maka hasil akan true)
print("====AND====")
x = False
z = False
hasil = x and z
print(x, "and", z, "=", hasil)

x = True
z = False
hasil = x and z
print(x, "and", z, "=", hasil)

x = True
z = True
hasil = x and z
print(x, "and", z, "=", hasil)

x = False
z = True
hasil = x and z
print(x, "and", z, "=", hasil)

# XOR (jika hanya satu nilai bernilai true maka hasil true,jika dua nilai bernilai sama maka hasil false )
print("====XOR====")
x = False
z = False
hasil = x ^ z
print(x, "^", z, "=", hasil)

x = True
z = False
hasil = x ^ z
print(x, "^", z, "=", hasil)

x = True
z = True
hasil = x ^ z
print(x, "^", z, "=", hasil)

x = False
z = True
hasil = x ^ z
print(x, "^", z, "=", hasil)
