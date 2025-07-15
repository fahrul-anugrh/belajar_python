# Episode 19
# Width and Multiline

## Data
name = "Fahrul Dwi Anugrah"
age = 23
height = 163
weight = 60

## Standard String
data_string = f"Name : {name}, Age : {age} years old, Height : {height}, Weight :{weight}"
print("STRING".center(25,"="))
print(data_string)

## Multiline String (with \n)
data_string = f"Name : {name} \nAge : {age} years old \nHeight : {height} \nWeight : {weight}"
print("STRING".center(25,"="))
print(data_string)

## Multiline String (with """)
data_string = f"""Name : {name}
Age : {age} years old
Height : {height}
Weight : {weight}"""
print("STRING".center(25,"="))
print(data_string)

## Mengatur Spasi/Lebar/Width
data_string = f"""
Name    : {name:>18}
Age     : {age:>8} years old
Height  : {height:>18}
Weight  : {weight:>18}"""
print("STRING".center(25,"="))
print(data_string)