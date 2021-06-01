# R-1.4

# Tulis fungsi Python singkat yang mengambil bilangan bulat positif n dan mengembalikan jumlah kuadrat
# dari semua bilangan bulat positif yang lebih kecil dari n.

#JAWABAN

def sum_of_squares(n):
    n -= 1
    total = 0
    while n > 0:
        total += n * n
        n -= 1
    return total


print('sum of squares')
print(sum_of_squares(4))
