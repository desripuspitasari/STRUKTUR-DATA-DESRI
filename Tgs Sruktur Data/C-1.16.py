#C-1.16

# Dalam implementasi fungsi skala (halaman 25), badan perulangan mengeksekusi data perintah [j] = faktor.
# Kita telah membahas bahwa tipe numerik tidak dapat diubah,
# dan penggunaan operator = dalam konteks ini menyebabkan pembuatan instance baru (bukan mutasi dari instance yang ada).
# Lalu, bagaimana mungkin implementasi skala kita mengubah parameter aktual yang dikirim oleh pemanggil?

#JAWABAN

# Alasan mengapa parameter aktual yang dikirim oleh pemanggil fungsi diubah adalah karena parameternya adalah list (Array)
# dan elemen tertentu dari larik tersebut ditetapkan ke objek numerik baru.
