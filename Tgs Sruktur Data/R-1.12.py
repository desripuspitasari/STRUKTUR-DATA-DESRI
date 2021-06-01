# R-1.12

# Modul acak Python menyertakan pilihan fungsi (data) yang mengembalikan elemen acak
# dari urutan yang tidak kosong. Modul acak mencakup randrange fungsi yang lebih mendasar,
# dengan parameterisasi yang mirip dengan fungsi rentang bawaan, yang mengembalikan pilihan acak
# dari kisaran yang diberikan. Hanya dengan menggunakan fungsi randrange, terapkan versi Anda sendiri dari fungsi pilihan.

#JAWABAN

import random

def pilihanku(data):
    return data[random.randrange(0, len(data) - 1)]

alpha = [2, 2, 3, 4, 5, 6, 7, 8, 99]

print(pilihanku(alpha))
