# Episode 14
# Operasi Assignment : operasi yang digabung dengan assignment

## Aritmatika Assignment
a = 5 # assignment
print("nilai a =", a)

a += 1
print("nilai a += 1 menjadi", a)

a -= 2
print("nilai a -= 2 menjadi", a)

a *= 5
print("nilai a *= 5 menjadi", a)

a /= 2
print("nilai a /= 2 menjadi", a)

a %= 3
print("nilai a %= 3 menjadi", a)

a = 10
a //= 3
print("nilai a //= 3 menjadi", a)

a = 5
a **= 3
print("nilai a **= 3 menjadi", a)

## Bitwise Assignment
a = True
print("nilai a =", a, ", dengan binary =", format(a, '04b'))
a |= False
print("nilai a |= False ", a, ", dengan binary =", format(a, '04b'))

a = True
a &= False
print("nilai a &= False", a, ", dengan binary =", format(a, '04b'))

a = True
a ^= False
print("nilai a ^= False ", a, ", dengan binary =", format(a, '04b'))

a = 0b0100
print("Nilai a =",  a, " dengan binary = ", format(a, '04b'))
a >>= 2
print("Nilai a >>= 2",  a, " dengan binary = ", format(a, '04b'))
a <<= 1
print("Nilai a <<= 1",  a, " dengan binary = ", format(a, '04b'))