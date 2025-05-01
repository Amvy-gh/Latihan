# Generate tabel mahasiswa
with open('mahasiswa.sql', 'w') as file:
    for i in range(50000):
        nim = f'122140{i:05}'
        nama = f'Nama_{i}'
        kampus_val = random.choice(kampus)
        jurusan_val = random.choice(jurusan)
        angkatan = random.randint(2019, 2023)
        file.write(
            f"INSERT INTO mahasiswa VALUES ('{nim}', '{nama}', '{kampus_val}', '{jurusan_val}', {angkatan});\n"
        )

# Generate tabel kelas (1 mahasiswa bisa punya 1-3 kelas)
with open('kelas.sql', 'w') as file:
    for i in range(50000):
        nim = f'122140{i:05}'
        for _ in range(random.randint(1, 3)):
            matkul_val = random.choice(matkul)
            ruang_val = random.choice(ruang)
            kelas_val = random.choice(kelas)
            hari_val = random.choice(hari)
            jam_val = random.choice(jam)
            file.write(
                f"INSERT INTO kelas VALUES ('{nim}', '{matkul_val}', '{ruang_val}', '{kelas_val}', '{hari_val}', '{jam_val}');\n"
            )