# R-1.3

# Tulis fungsi Python pendek, minmax (data), yang mengambil urutan satu atau lebih angka,
# dan mengembalikan angka terkecil dan terbesar, dalam bentuk tupel dengan panjang dua.
# Jangan gunakan fungsi bawaan min atau maks dalam mengimplementasikan solusi Anda.

#JAWABAN

def minmax(data):
    largest = data[0]
    smallest = data[0]
    for item in data:
        if item > largest:
            largest = item
        elif item < smallest:
            smallest = item
    return smallest, largest


alpha = [7, 3, 4, 5, 6, 1, 2, 8, 9]

print(minmax(alpha))
