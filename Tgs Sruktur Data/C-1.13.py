# C-1.13

# Tulis deskripsi pseudo-code dari suatu fungsi yang membalik daftar n bilangan bulat,
# sehingga nomor-nomor tersebut terdaftar dalam urutan yang berlawanan dari sebelumnya, dan bandingkan
# metode ini ke fungsi Python yang setara untuk melakukan hal yang sama.

#JAWABAN

my_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def terbalik(data):
    temp = []
    n = len(data) - 1
    for thing in range(n, -1, -1):
        temp.append(data[thing])
    return temp


print(my_list)

print(terbalik(my_list))
