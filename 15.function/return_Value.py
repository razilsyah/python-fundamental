# function dengan return value

def kuadrat(argument1):
    total = argument1 ** 2
    print("nilai kuadrat dari ",argument1,"adalah",total)
    return total
kuadrat(2)
a = kuadrat(2)
# print(a) jika tidak pakai return pada fuction akan none
print(a) # ini memakai return

print("+"*50)

# fungsi dengan return value dan multiple argument

def tambah(a,b):
    total = a + b
    print(a,"+",b,"=",total)
    # return [total] bisa juga return list dll
    return total

def kali(a,b):
    total = a * b
    print(a,"X",b,"=",total)
    return total

# b = kali(3,tambah(5,6)) ~bisa seperti ini 3 * hasil dari total function tambah
b = kali(4,6)
print(b)





