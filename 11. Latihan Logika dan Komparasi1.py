# Episode 12
# Latihan Logika dan Komparasi

"""
    ----TRUE----3----FALSE----10----TRUE----
    Buat program untuk aturan logika di atas
"""
inputUser = float(input("Masukkan angka <3 atau >10: "))
isKurangDari3 = inputUser < 3
print("isKurangDari3:", isKurangDari3)
isLebihDari10 = inputUser > 10
print("isLebihDari10:", isLebihDari10)
isHasil = isKurangDari3 or isLebihDari10
print("Angka yang anda masukkan: ", isHasil)

"""
    ----FALSE----3----TRUE----10----FALSE----
    Buat program untuk aturan logika di atas
"""
print("========================================\n")
inputUser = float(input("Masukkan angka 4 sampai 9: "))
isLebihDari3 = inputUser > 3
print("isLebihDari3:", isLebihDari3)
isKurangDari10 = inputUser < 10
print("isKurangDari10:", isKurangDari10)
isHasil = isLebihDari3 and isKurangDari10
print("Angka yang anda masukkan: ", isHasil)