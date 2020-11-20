# 1
for i in range(0,20):
    print(i)

# 2
number = 25
for i in range(number):
    print(i)

# 3
angka = 15
for i in range(20):
    print(i)
    if i is angka:
        print("angka di temukan",i)
        break # break akan keluar memberhentikan perulangan jika kondisi terpenuhi
else: # else tidak akan tercekan karna ada break
    print("world!!")

# 4
for i in range(1,30):
    print(i)
else:
    print("hello")