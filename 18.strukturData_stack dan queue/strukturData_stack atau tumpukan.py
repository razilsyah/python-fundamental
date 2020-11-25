# stack adalah tumpukan yang artinya first in last out

# contoh
gorengan = ["batagor","somay","gehu","combro"]
print(f"data sekarang = {gorengan}")
# nambah data
gorengan.append("tahu gejrott")
print(f"data masuk :""tahu gejrot")
print(f"data sekarang {gorengan}")

gorengan.append("bala-bala")
print(f"data masuk :"" bala-bala")
print(f"data sekarang {gorengan}")

keluar = gorengan.pop()
print(f"data keluar : {keluar}")
print("data sekarang :",gorengan)
