

# # membuat proram menampilkan bilangan prima
array = []
def bilangan_prima():
    for i in range(1,36):
        if i < 36:
            array.append(i)

    print(array)
bilangan_prima()




array2 = []
user = int(input("masukan batas deretan bilangan :"))
for a in range(2,user):
    mod = 1
    print(a)
    for b in range(2,a):

        print(b)
        if a % b == 0:
            mod = 0
    if mod == 1:
        array2.append(a)

print(array2)




# # program mencari bilangan prima
# angka = int(input("Masukkan angka: "))
# # mengecek bilangan prima selalu lebih besar dari 1
# if angka > 1:
#    # mengecek faktor pembagi dengan operasi modulus
#    for i in range(2,angka):
#        if (angka % i) == 0:
#            print (angka,"bukan bilangan prima")
#            print ("karena", i,"dikalikan",angka//i,"hasilnya adalah",angka)
#            break
#    else:
#        print( angka,"adalah bilangan prima")
# # keluaran jika sebuah bilangan kurang dari atau sama dengan 1
# else:
#    print (angka,"adalah bilangan prima")









