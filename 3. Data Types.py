# Episode 3
# Tipe Data

## Tipe Data Umum
### Angka Bulat (Integer)
angka_bulat = 10
print("Data : ", angka_bulat, ", bertipe : ", type(angka_bulat)) 

### Angka Desimal (Float)
angka_desimal = 10.5
print("Data : ", angka_desimal, ", bertipe : ", type(angka_desimal))

### Teks (String)
teks = "Hello, World!"
print("Data : ", teks, ", bertipe : ", type(teks))

### Boolean (True/False)
boolean_true = True
boolean_false = False
print("Data : ", boolean_true, ", bertipe : ", type(boolean_true))
print("Data : ", boolean_false, ", bertipe : ", type(boolean_false))

## Tipe Data Khusus
### Bilangan Kompleks (Complex)
bilangan_kompleks1 = 3 + 4j
bilangan_kompleks2 = complex(3, 4)
print("Data : ", bilangan_kompleks1, ", bertipe : ", type(bilangan_kompleks1))
print("Data : ", bilangan_kompleks2, ", bertipe : ", type(bilangan_kompleks2))

### Tipe Data dari Bahasa C
from ctypes import c_double, c_char_p
data_double = c_double(10.5)
print("Data : ", data_double, ", bertipe : ", type(data_double))