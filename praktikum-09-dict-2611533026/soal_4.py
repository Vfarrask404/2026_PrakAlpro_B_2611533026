siswa = input().split()
submitted = input().split()

# faras note : ini ngubah list -> set
siswa_set = set(siswa)
submitted_set = set(submitted)

# faras note : utk hitung jumlah mahasiswa yang sudah dan belum mengumpulkan
submitted_count = len(siswa_set & submitted_set)
not_submitted = siswa_set - submitted_set
not_submitted_count = len(not_submitted)

print("Submitted:", submitted_count, "students")
print("Not submitted:", not_submitted_count, "students")

# farras note : Menampilkan nomor absen yang belum mengumpulkan
for student in siswa:
    if student not in submitted_set:
        print(student)