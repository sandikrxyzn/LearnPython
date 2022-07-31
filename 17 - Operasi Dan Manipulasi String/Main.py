# Minggu, 31 Jul 12:51
# SandiKrxyzn

# Operator dalam bentuk Methods

# Merubah case dari sting

# merubah semua ke uper case

salam = "bro!"
print("normal = "+ salam)
salam = salam.upper()
print("normal = "+ salam)


# Merubah Semua ke lower case
alay = "aKu KeCe AbieeeezzZZZzzzZzz"
print("bormal = "+ alay)
alay = alay.lower()
print("lower = " + alay)

## Pengecekan dengan isX method

# contoh untuk pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + "is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + "is lower = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata di mulai dengan huruf besar

# isalpha()
nama = "sand1" 
apakah_aplha = nama.isalpha() # hasilnya false apabila ada angka
print(nama + "is alpha = "+ str(apakah_aplha))

nama = "sandi" # hasilnya true karena tidak ada angka
apakah_aplha = nama.isalpha() 
print(nama + "is alpha = "+ str(apakah_aplha))

# isalnum()
saha = "duk2;" 
apakah_alnum = saha.isalnum() 
print(saha + "is alnum = "+ str(apakah_alnum))

# IsTittle()
judul = "You Cry My Happines" # Harus Besar Semua Bru true
cek_judul = judul.istitle()
print(judul + "is title = "+ str(cek_judul))

## ngecek komponen startswith() endswith() <-- Keren
# Mengecek apakah huruf sama, bila sama maka true
cek_start = "SandiMaulanaFauzan Keren".startswith("SandiMaulanaFauzan")
print("start = "+ str(cek_start))

cek_end = "SandiMaulanaFauzan Keren".endswith("Keren")
print("end = "+ str(cek_end))

## penggabungan komponen join() split()
# Join > Menggabungkan
# split > Memisahkan
pisah = ['aku','saya','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

# bila ingin gabungan tanpa koma
gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehem '.join(pisah)
print(gabungan)

#  menghilangkan kata / atau ehem
gabungan = "akuehemsayangehemkamu"
print(gabungan.split('ehem'))

## alokasi karakter rjust(), ljust(), center()
# rjust() > RideJustify > Rata Kanan

# total dalam string sesuai rjust(#)
# kanan
kanan = "kanan".rjust(10)
print("'"+ kanan + "'")

# kiri
kiri = "kiri".ljust(10)
print("'"+ kiri + "'")

# Tengah
tengah = "tengah".center(20,"-")
print("'"+ tengah + "'")

# kebalikannya -> strip()
tengah = tengah.strip("-")# Menghilangkan Tada - 
print("'"+ tengah + "'")
