print("===== program pembagian ======")

def pembagian(a,b):
    return a/b
try:
    penyebut = int(input("masukan angka penyebut :"))
    pembilang = int(input("masukan angka pembilang :"))
    print ( pembagian ( penyebut, pembilang ) )
except ValueError: # cara menangkap keywordl error
    print("input yang anda msukan bukan angka!!!!")

print("di luar error")