# NIM/NAMA: 16624445/FAHRI MAULANA AL GHAZALI
# TANGGAL: 15 OKTOBER 2024
# DESKRIPSI: Program untuk menghitung waktu akhir peserta marathon dan menentukan medali yang diperoleh.

# Input jam dan menit keberangkatan
print("Masukkan Jam Keberangkatan")
keberangkatan_jam = int(input("Jam: "))         # Jam keberangkatan (0-23)
keberangkatan_menit = int(input("Menit: "))     # Menit keberangkatan (0-59)

# Input jarak antar pos dan kecepatan lari
jarak_pos1_pos2 = int(input("Masukkan jarak dari pos 1 ke pos 2 dalam M: "))  # Jarak dari pos 1 ke pos 2 dalam meter
jarak_pos2_pos3 = int(input("Masukkan jarak dari pos 2 ke pos 3 dalam M: "))  # Jarak dari pos 2 ke pos 3 dalam meter
kecepatan_lari = int(input("Masukkan kecepatan lari dalam meter/menit: "))   # Kecepatan lari awal dalam meter per menit

# Penghitungan total waktu tempuh
# Waktu untuk mencapai pos 1 ke pos 2
waktu_pos1_pos2 = jarak_pos1_pos2 / kecepatan_lari

# Kecepatan setelah melewati pos kedua (berkurang 10 meter/menit)
kecepatan_setelah_pos2 = kecepatan_lari - 10

# Memeriksa apakah kecepatan setelah pos2 valid
if kecepatan_setelah_pos2 <= 0:
    print("Kecepatan setelah pos kedua tidak valid. Nona Deb tidak bisa menyelesaikan lomba.")
    exit()  # Menghentikan program jika kecepatan tidak valid

# Waktu untuk mencapai pos 2 ke pos 3 dengan kecepatan yang berkurang
waktu_pos2_pos3 = jarak_pos2_pos3 / kecepatan_setelah_pos2

# Total waktu tempuh dalam menit
total_waktu_tempuh = waktu_pos1_pos2 + waktu_pos2_pos3

# Mengonversi waktu keberangkatan ke total menit
waktu_keberangkatan_total = (keberangkatan_jam * 60) + keberangkatan_menit

# Waktu selesai lomba dalam menit
waktu_selesai_dalam_menit = waktu_keberangkatan_total + total_waktu_tempuh

# Waktu target selesai adalah jam 09:00 (540 menit)
waktu_target = 9 * 60

# Selisih waktu antara target dan waktu selesai
selisih_waktu = waktu_target - waktu_selesai_dalam_menit

# Penentuan medali berdasarkan selisih waktu
if selisih_waktu >= 10:
    medali = "Medali Emas"      # Lebih awal 10 menit atau lebih
elif 5 <= selisih_waktu < 10:
    medali = "Medali Perak"     # Lebih awal antara 5 hingga kurang dari 10 menit
elif 0 <= selisih_waktu < 5:
    medali = "Medali Perunggu"  # Lebih awal antara 0 hingga kurang dari 5 menit
else:
    medali = "Anda Tidak Mendapatkan Medali Apapun"  # Tidak mencapai target waktu

# Menampilkan hasil perhitungan
if selisih_waktu > 0:
    # Jika selesai sebelum waktu target, tampilkan selisih waktu dan medali yang diperoleh
    print(f"Nona Deb selesai lebih awal {selisih_waktu:.0f} menit dan mendapatkan medali {medali}")
else:
    # Jika tidak selesai sebelum waktu target, tampilkan pesan kegagalan
    print("Nona Deb tidak berhasil mencapai garis finish")

#DOKUMENTASI CODE TIDAK TER-RECORD KARENA SEBELUMNYA TIDAK MEMBACA SOAL KALAU SEBAIKNYA CODE DIKASIH DOKUMENTASI CODE😔😔