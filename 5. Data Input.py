# Episode 7
# Mengambil Data Input

"""
    Data akan selalu bertipe 
"""
data = input("Masukkan Data: ")
print("Data yang dimasukkan adalah:", data, ", dengan tipe data:", type(data))

"""
    Data tipe lain : gunakan casting
"""
data_integer = int(input("Masukkan angka bulat: "))
print("Data yang dimasukkan adalah:", data_integer, ", dengan tipe data:", type(data_integer))

data_float = float(input("Masukkan angka berkoma: "))
print("Data yang dimasukkan adalah:", data_float, ", dengan tipe data:", type(data_float))

"""
    karena input selalu string, dan jika string tidak kosong maka akan selalu true
     ubah string -> integer -> 
"""
data_boolean = bool(int(input("Masukkan angka biner: ")))
print("Data yang dimasukkan adalah:", data_boolean, ", dengan tipe data:", type(data_boolean))