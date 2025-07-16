# Episode 23
# Simple Calculator using Elif

print("CALCULATOR SEDERHANA".center(30,"="), "\n")

angka_1st = float(input("Masukkan angka pertama : "))
operator = input("Masukkan operator (+, -, x, /) : ")
angka_2nd = float(input("Masukkan angka kedua : "))

if operator == "+" :
    hasil = angka_1st + angka_2nd
    print(f"{angka_1st} + {angka_2nd} = {hasil}")
elif operator == "-" :
    hasil = angka_1st - angka_2nd
    print(f"{angka_1st} - {angka_2nd} = {hasil}")
elif operator == "x" or operator == "X" :
    hasil = angka_1st * angka_2nd
    print(f"{angka_1st} * {angka_2nd} = {hasil}")
elif operator == "/" :
    hasil = angka_1st / angka_2nd
    print(f"{angka_1st} / {angka_2nd} = {hasil}")
else :
    print("Operator is not found")
