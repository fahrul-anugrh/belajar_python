# Episode 12 (Tugas)

"""
    ------0++++++5------8+++++++11------
"""

inputUser = float(input("Masukkan angka (1-5 atau 8-11): "))
isZeroFive = inputUser > 0 and inputUser < 5
isEightEleven = inputUser > 8 and inputUser < 11
isHasil = isZeroFive or isEightEleven
print("Angka yang anda masukkan :", isHasil)

"""
    +++++++0------5+++++++8------11+++++++
"""

inputUser = float(input("Masukkan angka (<0 atau 6-7 atau >11): "))
isKurangDariZero = inputUser < 0
isFiveEight = inputUser > 5 and inputUser < 8
isLebihDariEleven = inputUser > 11
isHasil = isKurangDariZero or isFiveEight or isLebihDariEleven
print("Angka yang anda masukkan :", isHasil)