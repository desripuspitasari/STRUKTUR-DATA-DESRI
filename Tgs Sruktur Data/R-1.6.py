# R-1.6

# Tulis fungsi Python pendek yang mengambil bilangan bulat positif n dan mengembalikan jumlah kuadrat
# dari semua bilangan bulat positif ganjil yang lebih kecil dari n.

#JAWABAN

def sum_of_squares_odd(n):
    n -= 1
    total = 0
    while n > 0:
        if n % 2 != 0:
            total += n * n
        n -= 1
    return total


print('sum of squares odd')
print(sum_of_squares_odd(4))
