# bitwise adalah operator binary

# bitwise or ( | )
print("=========== BITWISE OR | ===========")
a = 9
print("nilai a :",a," binary :",format(a,"08b"))
b = 5
print("nilai a :",b," binary :",format(b,"08b"))

c = a | b
print(a,"|",b ,"=",c ,"  bytes :",format(c,"08b"))



# bitwise AND ( & )
print("========== BITWISE AND & ========== ")

a = 9
print("nilai a :",a," binary :",format(a,"08b"))
b = 5
print("nilai a :",b," binary :",format(b,"08b"))

c = a & b
print(a,"&",b ,"=",c ,"  bytes :",format(c,"08b"))



# bitwise not ( ~ )
print("============ BITWISE NOT ~ ===========")

a = 9
print("nilai a :",a," binary :",format(a,"08b"))
c = ~a
print("~",a,"=",c ,"  bytes :",format(c,"08b"))
# jika ingin di balik
d = c^c
print("=",d,"  bytes :",format(d,"08b"))


b = 5
print("nilai b :",b," binary :",format(b,"08b"))
c = ~ b
print("~",b,"=",c ,"  bytes :",format(c,"08b"))

d


# bitwise XOR ( ^ )
print("\n========== BITWISE XOR ^ ========== ")

a = 9
print("nilai a :",a," binary :",format(a,"08b"))
b = 5
print("nilai a :",b," binary :",format(b,"08b"))

c = a ^ b
print(a,"^",b ,"=",c ,"  bytes :",format(c,"08b"))


# SHIFTING
# SHIFTING RIGHT
print("==========SHIFTING RIGHT============")
a = 9
print("nilai a :",a," binary :",format(a,"08b"))
b = a >> 2
print("nilai a :",b," binary :",format(b,"08b"))

# SHIFTING LIGHT
print("==========SHIFTING LIGHT============")
a = 9
print("nilai a :",a," binary :",format(a,"08b"))
b = a << 2
print("nilai a :",b," binary :",format(b,"08b"))








