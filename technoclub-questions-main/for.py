"""
Diambang Batas Pengulangan

Naila bingung kode miliknya tidak bisa berhenti ketika menggunakan while loop.
harapan dari naila adalah ketika output sudah mencapai 100, maka program akan berhenti.
tapi sepertinya kode yang dia buat tidak berjalan sesuai harapan.
bantu naila untuk menyelesaikan masalahnya.
"""
i = 0
while (True):
    print(i)
    
    i += 1
    # lanjutkan code dibawah ini

    i = 0
while True:
    print(i)
    
    # Memeriksa jika nilai i sudah mencapai 100
    if i == 100:
        break  # Menghentikan loop jika i sama dengan 100
    
    i += 1
