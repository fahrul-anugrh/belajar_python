# Episode 9
# Latihan Konversi Satuan Temperatur

## Dari Temperatur Celsius
print("\n====PROGRAM KONVERSI TEMPERATUR====\n")
temperatur_celsius = float(input("Masukkan suhu dalam Celsius: "))
temperatur_reamur = (4/5) * temperatur_celsius
temperatur_fahrenheit = ((9/5) * temperatur_celsius) + 32
temperatur_kelvin = temperatur_celsius + 273
print("Suhu adalah", temperatur_celsius, "Celsius")
print("Suhu adalah", temperatur_reamur, "Reamur")
print("Suhu adalah", temperatur_fahrenheit, "Fahrenheit")
print("Suhu adalah", temperatur_kelvin, "Kelvin")