# Episode 9 (Tugas)

## Konversi Fahrenheit ke Kelvin
print("\n====PROGRAM KONVERSI TEMPERATUR====\n")
temperatur_fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
temperatur_celsius = (5/9) * (temperatur_fahrenheit - 32)
temperatur_kelvin = temperatur_celsius + 273
print("Suhu adalah", temperatur_fahrenheit, "Fahrenheit")
print("Suhu adalah", temperatur_kelvin, "Kelvin")

## Konversi Temperatur Kelvin ke Fahrenheit
print("\n====PROGRAM KONVERSI TEMPERATUR====\n")
temperatur_kelvin = float(input("Masukkan suhu dalam Kelvin: "))
temperatur_celsius = temperatur_kelvin - 273
temperatur_fahrenheit = ((9/5) * temperatur_celsius) + 32
print("Suhu adalah", temperatur_kelvin, "Kelvin")
print("Suhu adalah", temperatur_fahrenheit, "Fahrenheit")