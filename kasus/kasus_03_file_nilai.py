def simpan_nilai(nama_file, nilai):
    with open(nama_file, "w") as file:
        for n in nilai:
            file.write(str(n) + "\n")


def baca_nilai(nama_file):
    with open(nama_file, "r") as file:
        for baris in file:
            print(baris.strip())


nilai_siswa = [80, 90, 75, 60]

simpan_nilai("nilai_siswa.txt", nilai_siswa)
baca_nilai("nilai_siswa.txt")