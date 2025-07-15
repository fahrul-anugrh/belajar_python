# Episode 11
# Operasi Logika / Boolean

## Operator Logika
"""
    1. not
    2. or
    3. and
    4. xor
"""

## NOT
print("-----NOT-----")
a = True
hasil = not a
print("not", a, "=", hasil)

## OR
print("-----OR-----")
a = True
b = True
hasil = a or b
print(a, " or", b, " =", hasil)

a = True
b = False
hasil = a or b
print(a, " or", b, "=", hasil)

a = False
b = True
hasil = a or b
print(a, "or", b, " =", hasil)

a = False
b = False
hasil = a or b
print(a, "or", b, "=", hasil)

## AND
print("-----AND-----")
a = True
b = True
hasil = a and b
print(a, " and", b, " =", hasil)

a = True
b = False
hasil = a and b
print(a, " and", b, "=", hasil)

a = False
b = True
hasil = a and b
print(a, "and", b, " =", hasil)

a = False
b = False
hasil = a and b
print(a, "and", b, "=", hasil)

## XOR (true jika salah satu saja yang true)
print("-----AND-----")
a = True
b = True
hasil = a ^ b
print(a, " xor", b, " =", hasil)

a = True
b = False
hasil = a ^ b
print(a, " xor", b, "=", hasil)

a = False
b = True
hasil = a ^ b
print(a, "xor", b, " =", hasil)

a = False
b = False
hasil = a ^ b
print(a, "xor", b, "=", hasil)

a = False
b = False
hasil = a ^ b
print(a, "xor", b, "=", hasil)

a = False
b = False
c = True
hasil = a ^ b ^ c
print(a, "xor", b, "xor", c, "=", hasil)