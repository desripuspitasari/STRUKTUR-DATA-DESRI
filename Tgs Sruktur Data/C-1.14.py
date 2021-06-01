# C-1.14

# Tulis fungsi Python singkat yang mengambil urutan nilai integer dan menentukan
# jika ada pasangan bilangan yang berbeda dalam urutan yang hasil kalinya ganjil.

#JAWABAN

def odd_pair(data):
    count = 0
    for k in range(0, len(data) - 1):
        if k % 2 != 0:
            count += 1
    return 'benar' if count >= 2 else 'salah'

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = [2, 4, 6, 8]

print(odd_pair(my_list))
print(odd_pair(evens))
