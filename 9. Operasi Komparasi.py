# Episode 10
# Operasi Komparasi

## operator komparasi
"""
    setiap hasil operasi adalah boolean

    1. <
    2. >
    3. <=
    4. >=
    5. ==
    6. !=
    7. is
    8. is not
"""

a = 4
b = 2

## lebih besar dari (>)
print("-----lebih besar dari (>)-----")
hasil = a > 3
print(a, ">", 3, "=", hasil)
hasil = b > 3
print(b, ">", 3, "=", hasil)
hasil = b > 2
print(b, ">", 2, "=", hasil)

## lebih kecil dari (<)
print("-----lebih kecil dari (<)-----")
hasil = a < 3
print(a, "<", 3, "=", hasil)
hasil = b < 3
print(b, "<", 3, "=", hasil)
hasil = b < 2
print(b, "<", 2, "=", hasil)

## lebih besar dari sama dengan (<=)
print("-----lebih besar dari sama dengan (>=)-----")
hasil = a >= 3
print(a, ">=", 3, "=", hasil)
hasil = b >= 3
print(b, ">=", 3, "=", hasil)
hasil = b >= 2
print(b, ">=", 2, "=", hasil)

## lebih besar dari sama dengan (<=)
print("-----lebih kecil dari sama dengan (<=)-----")
hasil = a <= 3
print(a, "<=", 3, "=", hasil)
hasil = b <= 3
print(b, "<=", 3, "=", hasil)
hasil = b <= 2
print(b, "<=", 2, "=", hasil)

## sama dengan (==)
print("-----sama dengan (==)-----")
hasil = a == 4
print(a, "==", 4, "=", hasil)
hasil = b == 4
print(b, "==", 4, "=", hasil)

## tidak sama dengan (!=)
print("-----sama dengan (==)-----")
hasil = a != 4
print(a, "!=", 4, "=", hasil)
hasil = b != 4
print(b, "!=", 4, "=", hasil)

## komparasi object identity (is)
print("-----komparasi object identity (is)-----")
x = 5
y = 5
z = 6
hasil = x is y
hasil2 = x is z
print("nilai x:", x, "id:", hex(id(x)))
print("nilai y:", y, "id:", hex(id(y)))
print("nilai z:", z, "id:", hex(id(z)))
print("x is y:", hasil)
print("x is z:", hasil2)

## komparasi object identity (is)
print("-----komparasi object identity (is not)-----")

"""
    object identity adalah address nya si object
"""

x = 5
y = 5
z = 6
hasil = x is not y
hasil2 = x is not z
print("nilai x:", x, "id:", hex(id(x)))
print("nilai y:", y, "id:", hex(id(y)))
print("nilai z:", z, "id:", hex(id(z)))
print("x is not y:", hasil)
print("x is not z:", hasil2)