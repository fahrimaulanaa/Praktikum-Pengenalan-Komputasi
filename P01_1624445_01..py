# NIM/NAMA: 16624445/FAHRI MAULANA AL GHAZALI
# TANGGAL: 15 OKTOBER 2024
# DESKRIPSI: Program untuk menghitung waktu akhir peserta berdasarkan tiga waktu input.

# Meminta input waktu dari pengguna
waktu_pertama = float(input("Masukkan Waktu Pertama (detik): "))
waktu_kedua = float(input("Masukkan Waktu Kedua (detik): "))
waktu_ketiga = float(input("Masukkan Waktu Ketiga (detik): "))

# Menentukan waktu minimum dari ketiga waktu yang dimasukkan
waktu_tercepat = min(waktu_pertama, waktu_kedua, waktu_ketiga)

# Menghitung waktu akhir dengan mengabaikan waktu tercepat dan membagi jumlah waktu sisanya
waktu_akhir = (waktu_pertama + waktu_kedua + waktu_ketiga - waktu_tercepat) / 2

# Menampilkan hasil perhitungan waktu akhir
print(f"Waktu akhir peserta adalah {waktu_akhir} detik")

#DOKUMENTASI CODE TIDAK TER-RECORD KARENA SEBELUMNYA TIDAK MEMBACA SOAL KALAU SEBAIKNYA CODE DIKASIH DOKUMENTASI CODE😔😔
