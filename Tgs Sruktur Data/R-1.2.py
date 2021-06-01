# R-1.2

# Tulis fungsi Python pendek, genap(k), yang mengambil nilai integer dan mengembalikan True jika k genap,
# dan False sebaliknya. Namun, fungsi Anda tidak dapat menggunakan operator perkalian, modulo, atau pembagian.

#JAWABAN

def is_even(k):
    return 'salah' if k & 1 else 'benar'

print(is_even(2))
print(is_even(3))
