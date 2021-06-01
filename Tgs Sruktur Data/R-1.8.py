# R-1.8

# Python memungkinkan bilangan bulat negatif untuk digunakan sebagai indeks ke dalam urutan,
# seperti string. Jika string s memiliki panjang n, dan ekspresi s [k] digunakan
# untuk indeks -n <= k < 0, berapakah indeks ekivalen j >= 0 sehingga s[j]
# mereferensikan elemen yang sama?

#JAWABAN

s = "HELLO"
n = len(s)

for k in range(-n, 0):
    print(s[k])


for j in range(-n, 0):
    print(s[j + n])
