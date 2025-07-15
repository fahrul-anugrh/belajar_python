# Episode 16 dan 17
# Operasi dan Manipulasi String

## 1. Menyambungkan string (Concatenate)
nama_depan = "Fahrul"
nama_tengah = "Dwi"
nama_belakang = "Anugrah"
nama_lengkap = nama_depan + " " + nama_tengah + " " + nama_belakang
print(nama_lengkap)

## 2. Menghitung panjang String
panjang = len(nama_lengkap)
print("Panjang dari", nama_lengkap, "=", str(panjang))

## 3. Operator untuk String

### Cek apakah ada string/char tertentu dalam variabel
huruf = "d"
nama = "Fahrul"
cek_huruf = huruf in nama_lengkap
print(huruf, "terdapat di dalam", nama_lengkap, "=", cek_huruf)
cek_nama = nama in nama_lengkap
print(nama, "terdapat di dalam", nama_lengkap, "=", cek_nama)

### Cek apakah string/char tertentu "tidak ada" dalam variabel
huruf = "d"
nama = "Fahrul"
cek_huruf = huruf not in nama_lengkap
print(huruf, "terdapat di dalam", nama_lengkap, "=", cek_huruf)
cek_nama = nama not in nama_lengkap
print(nama, "terdapat di dalam", nama_lengkap, "=", cek_nama)

### Mengulang string
print("wk"*10)
print(15*"wk")

### indexing (mengambil char/string tertentu dari variabel)
print("index ke-0 :", nama_lengkap[0]) # index pertama
print("index ke-6 :", nama_lengkap[7])
print("index ke-(-1) :", nama_lengkap[-1]) # index pertama dari belakang
print("index ke-(-2) :", nama_lengkap[-2])
print("index ke-(0:4) :", nama_lengkap[0:5]) # index 0 sampai sebelum 5
print("index ke-(0,2,4,6,8,10) :", nama_lengkap[0:10:2]) # index 0-10 dengan increment +2

### item paling kecil dan besar nilainya
print("item terkecil nilainya :", min(nama_lengkap), "dengan ASCII Code :", str(ord(min(nama_lengkap))))
print("item terbesar nilainya :", max(nama_lengkap), "dengan ASCII Code :", str(ord(max(nama_lengkap))))

ascii_code = 125
print("char dari ascii code", ascii_code, "=", chr(ascii_code))

## 4. Operator dalam bentuk method

### Count
data = "otong surotong pararotong"
jumlahO = data.count("o")
print("Jumlah o pada", data, "=", jumlahO)

### Uppercase
salam = "bro!"
salam = salam.upper()
print(salam)

### Lowercase
alay = "AkuUUU kEcE ABbbIizzz"
alay = alay.lower()
print(alay)

### Pengecakan dengan isX
#### islower() <- apakah semuanya adalah lowercase
apakah_lower = alay.islower()
print(str(apakah_lower))

#### isupper() <- apakah semuanya adalah lowercase
apakah_upper = alay.isupper()
print(str(apakah_upper))

#### isalpha() <- apakah semuanya adalah huruf
apakah_huruf = nama_depan.isalpha()
print(str(apakah_huruf))

#### isalnum() <- apakah semuanya adalah huruf dan angka (alfanumerik)
apakah_alnum = nama_depan.isalnum()
print(str(apakah_alnum))

#### isdecimal() <- apakah semuanya adalah angka
apakah_decimal = nama_depan.isdecimal()
print(str(apakah_decimal))

#### isspace() <- apakah adalah string kosong (spasi, tab, newline)
apakah_space = nama_lengkap.isspace()
print(str(apakah_space))

#### istitle() <- apakah dimulai dengan huruf kapital pada setiap kata
apakah_title = nama_lengkap.istitle()
print(str(apakah_title))


### pengecekan komponen dengan startswith dan endswith
cek_start = nama_lengkap.startswith("Fahrul")
print(str(cek_start))

cek_end = nama_lengkap.endswith("nugrah")
print(str(cek_end))

### Penggabungan dengan join() dan pemisahan dengan split()
pisah = ['aku', 'adalah', 'superman']
print(pisah)
gabung = " ".join(pisah)
print(gabung)
gabung = ",".join(pisah)
print(gabung)
gabung = " ehm ".join(pisah)
print(gabung)

pisah = gabung.split(" ehm ")
print(pisah)

### alokasi karakter ljust(), center(), rjust()
kiri = "rata kiri".ljust(20)
print("'", kiri, "'") # 15 adalah total char keseluruhan termasuk spasi

tengah = "rata tengah".center(20)
print("'", tengah, "'")

kanan = "rata kanan".rjust(20)
print("'", kanan, "'")

tengah = "rata tengah".center(20,"=")
print("'", tengah , "'")

#### Kebalikan strip()
tengah = tengah.strip("=")
print("'", tengah, "'")

kiri = kiri.strip()
print("'", kiri, "'")

### Masih banyak method built-in yang lain