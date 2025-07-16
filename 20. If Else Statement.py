# Episode 21
# If dan Else Statement

"""
    1. If
    2. Kondisi
    3. Statement/Aksi
"""

nama = input("Masukkan nama Anda : ")

## If in line
print("IF".center(10,"="))
if nama == "Fahrul" or nama == "fahrul" : print(f"{nama} ganteng abiezz")
print(f"terimakasih {nama} \n")

## If with indentation
print("IF".center(10,"="))
if nama == "Fahrul" or nama == "fahrul" : 
    print(f"{nama} ganteng abiezz")
print(f"terimakasih {nama} \n")

## If Else
print("IF ELSE".center(10,"="))
if nama == "Fahrul" or nama == "fahrul" : 
    print(f"{nama} ganteng abiezz")
else :
    print(f"kamu {nama} bukan Fahrul")
print(f"terimakasih {nama}")
