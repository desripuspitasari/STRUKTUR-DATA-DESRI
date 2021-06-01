#C-1.17

# Apakah kita telah mengimplementasikan fungsi skala (halaman 25) sebagai berikut,

def scale(data, factor):
    for val in data:
        val = factor
        
# apakah berfungsi dengan baik?
# Jelaskan mengapa atau mengapa tidak.

#JAWABAN

# Ini tidak akan berhasil.
# val adalah alias ke elemen aktual dalam data
# dan menugaskan objek baru ke dalamnya hanya akan mengubah nilai val.
