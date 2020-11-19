# operasi komparasi akan menghasilkan true/false
# <,>,<=,>=,==,!=,is,isnot

# 1.kurang dari ( < )
a = 4
b = 2
hasil = a < b
print(a, "<", b, "=", hasil)
hasil = b < a
print(b, "<", a, "=", hasil)
hasil = b < b
print(b, "<", b, "=", hasil)


# 2.lebih besar dari ( > )
print("======lebih besar dari >")
a = 4
b = 2
hasil = a > b
print(a, ">", b, "=", hasil)
hasil = b > a
print(b, ">", a, "=", hasil)
hasil = b > b
print(b, ">", b, "=", hasil)

# 3.kurang dari sama dengan  ( <= )
print("========kurang dari sama dengan <=")
hasil = a <= b
print(a, "<=", b, "=", hasil)
hasil = b <= a
print(b, "<=", a, "=", hasil)
hasil = b <= b
print(b, "<=", b, "=", hasil)

# 4.lebih besar dari sama dengan ( >= )
print("========lebih besar sama dengan >=")
hasil = a >= b
print(a, ">=", b, "=", hasil)
hasil = b >= a
print(b, ">=", a, "=", hasil)
hasil = b >= b
print(b, ">=", b, "=", hasil)


# 5.sama dengan dari ( == )
# membandingkan dg objek literal yaitu objek yang tidak di simpan pada variabel/memory
print("========sama dengan dari == ")
hasil = a == 4
print(a, "==", 4, "=", hasil)
hasil = b == 4
print(b, "==", 4, "=", hasil)
hasil = b == 2
print(b, "==", 2, "=", hasil)

# 6.tidak sama dengan dari ( != )
# membandingkan dg objek literal yaitu objek yang tidak di simpan pada variabel/memory
print("======== tidak sama dengan dari != ")
hasil = a != 4
print(a, "!=", 4, "=", hasil)
hasil = b != 4
print(b, "!=", 4, "=", hasil)
hasil = b != 4
print(b, "!=", 4, "=", hasil)

# 7.komparasi objek identity ( is )
# membandingan dg objek yang di assignment/disimpan pada memory
print("======komparasi objek identity (is)")
r = 4
a = 4
print("nilai r :", r, " id:", hex(id(r)))
print("nilai a :", a, " id:", hex(id(a)))
hasil = r is a
print("r is a =", hasil)

z = 5
print("nilai r :", r, " id:", hex(id(r)))
print("nilai z :", z, " id:", hex(id(z)))
hasil = r is z
print("r is z =", hasil)

# 8.komparasi objek identity ( is not )
# membandingan dg objek yang di assignment/disimpan pada memory
print("======komparasi objek identity (is not)")
r = 4
a = 4
print("nilai r :", r, " id:", hex(id(r)))
print("nilai a :", a, " id:", hex(id(a)))
hasil = r is not a
print("r is not a =", hasil)

z = 5
print("nilai r :", r, " id:", hex(id(r)))
print("nilai z :", z, " id:", hex(id(z)))
hasil = r is not z
print("r is not z =", hasil)
