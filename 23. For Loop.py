# Episode 24
# Perulangan/Looping dengan For

## dengan List
angka_angka = [0,1,2,3,4] # ini adalah list
for i in angka_angka : # artinya i akan bernilai angka-angka tersebut setiap iterasinya
    print (i)

## dengan range
print(10*"=")
for i in range(1,11) : # berarti index 1 sampai 10 karena index 11 adalah titik stop
    print (i)

## bisa untuk string
data_str = "Fahrul Dwi Anugrah"
for huruf in data_str :
    print(huruf)