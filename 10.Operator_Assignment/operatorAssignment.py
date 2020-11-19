# Operator assignment adalah operasi penyingkatan

# OPERASI ASSIGNMENT PENJUMLAHAN
print("========OPERASI ASSIGNMENT PENJUMLAHAN======")

a = 5
print("nilai a =",a)
a += 5 # jadi maksudnya a = a + 5
print("nilai a += 5,menjadi :",a)


# OPERASI ASSIGNMENT PENGURANGAN
print("========OPERASI ASSIGNMENT PENGURANGAN======")
a -= 5
print("nilai a -= 5,menjadi :",a)


# OPERASI ASSIGNMENT PERKALIAN
print("========OPERASI ASSIGNMENT PERKALIAN======")
a *= 5
print("nilai a *= 5,menjadi :",a)


# OPERASI ASSIGNMENT PEMBAGIAN
print("========OPERASI ASSIGNMENT PEMBAGIAN======")
a /= 5
print("nilai a /= 5,menjadi :",a)


# OPERASI ASSIGNMENT MODULUS
print("========OPERASI ASSIGNMENT MODULUS======")
a %= 2
print("nilai a &= 2,menjadi :",a)


# OPERASI ASSIGNMENT FLOOR DIVISION
print("========OPERASI ASSIGNMENT DIVISION======")
b = 9
print("angka b =",b)
b //= 2
print("nilai b //= 2,menjadi :",b)



# OPERASI ASSIGNMENT BITWISE
print("========OPERASI ASSIGNMENT BITWISE=========")

# BITWISE OR |
print("======= BITWISE OR |==========")
d = True
print("nilai d = ",d)
d |= False
print("nilai d |= false =",d)
d = True
print("nilai d = ",d)
d |= True
print("nilai d |= True =",d)


# BITWISE AND &
print("======= BITWISE AND &==========")
d = True
print("nilai d = ",d)
d &= False
print("nilai d &= false =",d)
d = True
print("nilai d = ",d)
d |= True
print("nilai d ^= True =",d)


# BITWISE XOR
print("======= BITWISE XOR ^==========")
d = True
print("nilai d = ",d)
d ^= False
print("nilai d ^= false =",d)
d = True
print("nilai d = ",d)
d ^= True
print("nilai d ^ = True =",d)


# SHIFTING
print("==========SHIFTING RIGHT=========")
z = 10
print("nila z =",z ,"bytes = ",format(z,"04b"))
z >>= 1
print("nilai z >>= 1 :",z,' bytes:',format(z,"04b"))

# SHIFTING KIRI
print("==========SHIFTING LIGHT=========")
z = 10
print("nila z =",z ,"bytes = ",format(z,"04b"))
z <<= 1
print("nilai z <<= 1 :",z,' bytes:',format(z,"04b"))



