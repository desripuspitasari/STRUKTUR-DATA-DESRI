# R-1.7

# berikan satu perintah yang menghitung jumlah dari r-1.6, mengandalkan sintaks pemahaman python dan fungsi penjumlahan bawaan

#JAWABAN

def sum_of_squares_odd2(n):
    return sum([k * k for k in range(0, n) if k % 2 != 0])


print(sum_of_squares_odd2(4))
