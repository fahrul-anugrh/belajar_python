# Episode 6
# Casting Tipe Data (Mengubah Tipe Data)

## Integer
print("======INTEGER=======")
data_integer = 10
print("Data = ", data_integer, ", bertipe : ", type(data_integer))
data_string = str(data_integer)
data_float = float(data_integer)
data_boolean = bool(data_integer)
print("Data = ", data_string, ", bertipe : ", type(data_string))
print("Data = ", data_float, ", bertipe : ", type(data_float))
print("Data = ", data_boolean, ", bertipe : ", type(data_boolean)) # jika 0 -> false, Selain 0 -> true

## Float
print("======FLOAT=======")
data_float = 11.9
print("Data = ", data_float, ", bertipe : ", type(data_float))
data_integer = int(data_float)
data_string = str(data_float)
data_boolean = bool(data_float)
print("Data = ", data_integer, ", bertipe : ", type(data_integer)) # akan dibulatkan ke bawah
print("Data = ", data_string, ", bertipe : ", type(data_string))
print("Data = ", data_boolean, ", bertipe : ", type(data_boolean))

## Boolean
print("======BOOLEAN=======")
data_boolean = False
print("Data = ", data_boolean, ", bertipe : ", type(data_boolean))
data_integer = int(data_boolean)
data_string = str(data_boolean)
data_float = float(data_boolean)
print("Data = ", data_integer, ", bertipe : ", type(data_integer))
print("Data = ", data_string, ", bertipe : ", type(data_string))
print("Data = ", data_float, ", bertipe : ", type(data_float))

## String
print("======STRING=======")
data_string = "FAHRUL DWI ANUGRAH"
print("Data = ", data_string, ", bertipe : ", type(data_string))
data_integer = int(data_string)
data_float = float(data_string)
data_boolean = bool(data_string)
print("Data = ", data_integer, ", bertipe : ", type(data_integer)) # error jika string bukan angka
print("Data = ", data_float, ", bertipe : ", type(data_float)) # error jika string bukan angka
print("Data = ", data_boolean, ", bertipe : ", type(data_boolean)) # jika string kosong -> false, jika berisi -> true