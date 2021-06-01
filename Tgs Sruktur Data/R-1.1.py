# R-1.1

# Tulis fungsi Python singkat, multipel (n, m), yang mengambil dua nilai integer dan mengembalikan
# True jika n adalah kelipatan dari m, yaitu, n = mi untuk beberapa bilangan bulat i, dan False sebaliknya.

#JAWABAN

def is_multiple(m, n):
    return 'benar' if m % n == 0 else 'nggak benar'

print(is_multiple(10, 3))
print(is_multiple(10, 2))
