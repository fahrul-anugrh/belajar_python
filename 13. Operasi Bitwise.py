# Episode 13
# Operasi Bitwise : operasi masing-masing bit dari bilangan biner

a = 9
b = 5

## Bitwise OR (|)
c = a | b
print("nilai :", a, "binary :", format(a, '08b'))
print("nilai :", b, "binary :", format(b, '08b'))
print("----------------------------(|)")
print("nilai :", c, "binary :", format(c, '08b'), "\n")

## Bitwise AND (&)
c = a & b
print("nilai :", a, "binary :", format(a, '08b'))
print("nilai :", b, "binary :", format(b, '08b'))
print("----------------------------(&)")
print("nilai :", c, "binary :", format(c, '08b'), "\n")

## Bitwise XOR (^)
c = a ^ b
print("nilai :", a, "binary :", format(a, '08b'))
print("nilai :", b, "binary :", format(b, '08b'))
print("----------------------------(^)")
print("nilai :", c, "binary :", format(c, '08b'), "\n")

## Bitwise not (~)
c = ~a
print("nilai :", a, "binary :", format(a, '08b'))
print("----------------------------(~)")
print("nilai :", c, "binary :", format(c, '08b'), "\n")
"""
    not tidak bisa digunakan pada operasi bitwise
    karena akan menggunakan 2's complement
    example:
    a = 9
    binary: 00001001
    1's: 11110110
                1
    -------------+
    2's: 100001001
    2's = -10
"""
"""
    jika hanya ingin membalikkan setiap bit saja, maka xor dengan 0b11111111
"""
d = 0b11111111
e = a ^ d
print("nilai :", a, "binary :", format(a, '08b'))
print("nilai :", d, "binary :", format(d, '08b'))
print("----------------------------(^)")
print("nilai :", e, "binary :", format(e, '08b'), "\n")

## Bitwise Shifting
### left shifting (<<)
c = a << 2
print("nilai :", a, "binary :", format(a, '08b'))
print("----------------------------(<<)")
print("nilai :", c, "binary :", format(c, '08b'), "\n")

### right shifting (>>)
c = a >> 2
print("nilai :", a, "binary :", format(a, '08b'))
print("----------------------------(>>)")
print("nilai :", c, "binary :", format(c, '08b'), "\n")