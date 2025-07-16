# Episode 20
# Date and Time (Latihan)

import datetime as dt
print("Masukkan Tanggal, Bulan, dan Tahun Lahir Anda".center(50,"="))
tanggal = int(input("Masukkan Tanggal \t : "))
bulan = int(input("Masukkan Bulan \t\t : "))
tahun = int(input("Masukkan Tahun \t\t : "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal Lahir Anda adalah {tanggal_lahir} di Hari {tanggal_lahir:%A}")

hari_ini = dt.date.today()
umur_tahun = (hari_ini - tanggal_lahir).days // 365
umur_bulan = (hari_ini - tanggal_lahir).days % 365 // 30
print (f"Umur Anda adalah {umur_tahun} Tahun {umur_bulan} Bulan")