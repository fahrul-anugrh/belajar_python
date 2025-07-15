# Episode 15
# String

## 1. Cara membuat string
"""
    1. Menggunakan single quote ('...')
    2. Menggunakan double quote ("...")
"""

data_single = 'menggunakan single quote'
print(data_single, ",", type(data_single))

data_double = "menggunakan double quote"
print(data_double, ",", type(data_double))

print('"hallo, apakabar?"')
print("'hallo, apakabar?'") 
print("ini adalah hari jum'at")

## 2. Menggunakan tanda backlash (\)

### menjadikan (') menjadi string
print('hari ini adalah hari jum\'at')
print('g\'day, isn\'t it?')

### menjadikan backlash (\) sebagai string
print('C:\\Users\\anugr')

### memberi jarak string (tab)
print("Indonesia\tnegara\t\thukum")

### menghapus (backspace)
print("Indonesia \bnegara \bhukum")
print("Indonesia\bnegara\bhukum")

### membuat baris baru (newline)
print("Baris Pertama.\nbaris kedua.") # LF : line feed (new line yg dipakai program unix, macos, linux)
print("Baris Pertama.\rbaris kedua.") # CR : carriage return (new line yg dipakai program comodore, acorn)
print("Baris Pertama.\r\nbaris kedua.") # CRLF : carriage return line feed (new line yg dipakai program windows)

## 3. String Literal atau raw

### Hati-hati, akan salah
print('C:\nUsers\anugr') 
"""
    bisa diatasi dengan mengubah backlash tsb menjadi string satu per satu
    jika banyak? gunakan cara berikut
"""

### membuat semua isinya menjadi string (raw string)
print(r'C:\nUsers\anugr\t\newfolder')

### multiline string
print("""
        NAMA : ASEP SURASEP
        KELAS : XII B
      """)

### raw string + multiline string
print(r"""
        NAMA : ASEP SURASEP
        KELAS : XII B
        Kode Nuklir : NX35MXS5566\n\t\r\HHJSJD902
      """)
