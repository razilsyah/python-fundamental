# queue adalah antrian yang artinya first in first out

# untuk antrial di dalam python tidak ada build in jadi harus import dari library
# import
from collections import deque

antrian = deque([1,2,3,4,5])
print("data sekarang :",antrian)

# menambah antrian
antrian.append(6)
print("data masuk :",6)
print("data sekarang :",antrian)

antrian.append(7)
print("data masuk :",7)
print("data sekarang :",antrian)

# mengurangi antrian
out = antrian.popleft()
print("data keluar :",out)
print("data sekarang :",antrian)

out = antrian.popleft()
print("data keluar :",out)
print("data sekarang :",antrian)

out = antrian.popleft()
print("data keluar :",out)
print("data sekarang :",antrian)

# coba di tambah lagi
antrian.append(8)
print("data masuk :",8)
print("data sekarang :",antrian)



