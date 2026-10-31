def hitung_total(nilai):
    total = 0

    for n in nilai:
        total = total + n

    rata_rata = total / len(nilai)

    return total, rata_rata


nilai_siswa = [80, 90, 70, 60]

total, rata_rata = hitung_total(nilai_siswa)

print("Daftar nilai:", nilai_siswa)
print("Total nilai:", total)
print("Rata-rata nilai:", rata_rata)