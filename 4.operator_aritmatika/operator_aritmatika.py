# OPERASI ARITMATIKA

# operator penjumlahan
a = 10
b = 5
hasil = a + b

print(a, "+", b, "=", hasil)


# operator pengurangan
hasil = a - b
print(a, "-", b, "=", hasil)


# operator perkalian *
hasil = a * b
print(a, "*", b, "=", hasil)


# operator pembagian /
hasil = a / b
print(a, "/", b, "=", hasil)


# operator eksponen (pangkat) **
hasil = a ** b
print(a, "**", b, "=", hasil)


# operator modulus (sisa bagi) %
c = 11
d = 3

hasil = c % d
print(c, "%", d, "=", hasil)


# operasi floor division // (hasil bagi di bulatkan ke bawah)
hasil = c // d
print(c, "//", d, "=", hasil)


# PRIORITAS OPERASI / OPERASI PRECEDENSE

# kurung ()
# exponen **
# perkalian * / % //
# pertambahan dan pengurangan + -

x = 5
y = 7
z = 10

hasil = x * y - z ** x / y % z // x
print(x, "*", y, "-", z, "**", x, "/", y, "%", z, "//", x, "=", hasil)
