# Episode 18
# Format String

## Generic String
nama = "Fahrul Dwi Anugrah"
umur = 23.05
generic_str = "Hello,\n" + "I'm : " + nama + "\nUmur : " + str(umur) + " tahun"
print(generic_str)

## Format (tidak perlu casting, operasi)
### Dari String
nama = "Fahrul Dwi Anugrah"
format_str = f"String : {nama}"
print(format_str)

### Dari Boolean
boolean = True
format_str = f"Boolean : {boolean}"
print(format_str)

### Dari Angka
angka = 123
format_str = f"Angka : {angka}"
print(format_str)

### Dari Bilangan bulat
angka = 123
format_str = f"bilangan bulat : {angka:d}" #sebenarnya tidak penting
print(format_str)

### Dari Bilangan ordo ribuan
angka = 1000000
format_str = f"bilangan jutaan : {angka:,}"
print(format_str)

### Dari bilangan float
angka = 123.63664
format_str = f"Angka : {angka:.2f}"
print(format_str)

### Dari angka dengan menampilkan leading zero didepan
angka = 123.63664
format_str = f"Angka : {angka:09.2f}"
print(format_str)
format_str = f"Angka : {angka:9.2f}"
print(format_str)

### Dari angka dengan menampilkan tanda plus/minus
angka_plus = 123
angka_minus = -123.345643
format_str = f"Angka : {angka_plus:+d}"
print(format_str)
format_str = f"Angka : {angka_minus:+.2f}"
print(format_str)

### Dari angka dan memformat persen
a = 16
b = 60
c = a/b
format_str = f"persentase : {c:.2%}"
print(format_str)

### Melakukan operasi aritmatika di dalam placeholder
harga = 10000
qty = 15
format_str = f"Total belanja : Rp. {harga*qty:,}"
print(format_str)

### Melakukan format ke jenis angka lain
angka = 255
format_binary = f"binary : {bin(angka)}"
format_octal = f"octal : {oct(angka)}"
format_hex = f"hex : {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)