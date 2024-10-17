#NIM/NAMA: 16624445/FAHRI MAULANA AL GHAZALI
#TANGGAL: 15 OKTOBER 2024
#DESKRIPSI: BENTAR

# P02 NIM 03.py

# Input jumlah uang kertas yang dimiliki tukang roti
jumlah_1000 = int(input("Jumlah uang 1000: "))     # Jumlah lembar Rp1000
jumlah_5000 = int(input("Jumlah uang 5000: "))     # Jumlah lembar Rp5000
jumlah_10000 = int(input("Jumlah uang 10000: "))   # Jumlah lembar Rp10000

# Daftar nama pelanggan yang akan diproses
pelanggan = ["Tuan Leo", "Nona Deb", "Nona Sal"]

# Dictionary untuk menyimpan hutang per pelanggan
hutang = {}

# Loop melalui setiap pelanggan untuk memproses transaksi
for nama in pelanggan:
    # Input nominal pembelian roti oleh pelanggan
    pembelian = int(input(f"Pembelian {nama}: "))
    
    # Input jumlah uang yang diterima dari pelanggan
    diterima = int(input(f"Uang diterima dari {nama}: "))
    
    # Hitung kembalian yang harus diberikan
    kembalian = diterima - pembelian
    
    # Jika uang yang diterima kurang dari pembelian, catat hutang
    if kembalian < 0:
        hutang[nama] = hutang.get(nama, 0) + abs(kembalian)
        continue  # Lanjut ke pelanggan berikutnya
    
    # Inisialisasi sisa kembalian yang perlu diberikan
    sisa = kembalian
    
    # Berikan kembalian menggunakan uang kertas terbesar terlebih dahulu
    
    for denom in [10000, 5000, 1000]:

        # Tentukan jumlah uang kertas yang tersedia untuk denominasi saat ini
        if denom == 10000:
            available = jumlah_10000
        elif denom == 5000:
            available = jumlah_5000
        else:
            available = jumlah_1000
        
        # Hitung jumlah uang kertas yang akan diberikan untuk denominasi ini
        qty = min(sisa // denom, available)
        
        # Kurangi sisa kembalian dengan nilai uang kertas yang diberikan
        sisa -= qty * denom

        # Update jumlah uang kertas yang tersedia setelah pemberian
        if denom == 10000:
            jumlah_10000 -= qty
        elif denom == 5000:
            jumlah_5000 -= qty
        else:
            jumlah_1000 -= qty
    
    # Jika masih ada sisa kembalian yang tidak bisa diberikan, catat hutang
    if sisa > 0:
        hutang[nama] = hutang.get(nama, 0) + sisa

# Format dan tampilkan hasil hutang
if hutang:
    # Buat list string yang menyatakan hutang per pelanggan
    debts = [f"Rp{v} kepada {k}" for k, v in hutang.items()]
    
    # Gabungkan string hutang dengan koma dan 'dan' jika lebih dari satu hutang
    if len(debts) == 1:
        hasil = debts[0]
    else:
        hasil = ', '.join(debts[:-1]) + f" dan {debts[-1]}"
    
    # Tampilkan total hutang
    print(f"Tukang roti memiliki hutang sebesar {hasil}.")
else:
    # Jika tidak ada hutang, tampilkan pesan sesuai
    print("Tukang roti tidak memiliki hutang.")

#DOKUMENTASI CODE TIDAK TER-RECORD KARENA SEBELUMNYA TIDAK MEMBACA SOAL KALAU SEBAIKNYA CODE DIKASIH DOKUMENTASI CODE😔😔