# Episode 22
# Elif = else if

nama = input("Masukkan nama Anda : ")

if nama == "Fahrul" or nama == "fahrul" : # kondisi 1
    print(f"{nama} is one of us") # aksi true 1
elif nama == "Joan" or nama == "joan" : # kondisi 2
    print(f"{nama} is one of us") # aksi true 2
elif nama == "Pep" or nama == "Pep" : # kondisi 3
    print(f"{nama} is one of us") # aksi true 3
else :
    print(f"{nama} is not one of us") # aksi false
print(f"terimakasih {nama}")