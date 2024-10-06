"""
Mengungkap Pesan Tersembunyi

Di akhir petualangan, kamu menemukan kotak harta karun. 
Namun, untuk membukanya, kamu harus menemukan pesan tersembunyi di antara serangkaian kata. 
Penduduk Pulau Python memberimu sebuah daftar kata, dan kamu harus mencari kata yang paling sering muncul.

Contoh Input:
["harta", "karun", "petualangan", "harta", "kunci", "harta", "petualangan"]

Contoh Output:
Kata yang paling sering muncul adalah "harta"
"""
arr = ["harta", "karun", "petualangan", "harta", "kunci", "harta", "petualangan", "harta"]
# lanjutkan code dibawah ini
arr = ["harta", "karun", "petualangan", "harta", "kunci", "harta", "petualangan", "harta"]

# Membuat dictionary untuk menyimpan frekuensi kata
frekuensi_kata = {}

# Menghitung frekuensi kemunculan setiap kata
for kata in arr:
    if kata in frekuensi_kata:
        frekuensi_kata[kata] += 1
    else:
        frekuensi_kata[kata] = 1

# Mencari kata dengan frekuensi tertinggi
kata_tersering = max(frekuensi_kata, key=frekuensi_kata.get)

# Menampilkan hasil
print(f'Kata yang paling sering muncul adalah "{kata_tersering}"')
