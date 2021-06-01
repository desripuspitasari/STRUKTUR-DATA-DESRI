# C-1.15

# Tulis fungsi Python yang mengambil urutan angka dan menentukan
# jika semua angka berbeda satu sama lain (yaitu, mereka berbeda).

#JAWABAN

def berbeda(data):
    count = 0
    for k in data:
        for j in range(1, len(data) - 1):
            if k == j:
                count += 1
                if count == 2:
                    return 'salah'
    return 'benar'

alpha = [2, 2, 3, 4, 5, 6, 7, 8, 99]
evens = [2, 4, 6, 8]
print(berbeda(evens))
print(berbeda(alpha))
