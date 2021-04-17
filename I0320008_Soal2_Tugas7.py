print("Selamat Datang di Program Menghitung Luas Persegi Panjang Maksimum")
print()

import math
a = float(input("Masukkan Panjang Persegi : "))
b = float(input("Masukkan Lebar Persegi : "))
c = float(input("Masukkan Panjang Persegi : "))
d = float(input("Masukkan Lebar Persegi : "))

#Menghitung Luas Persegi Panjang
Luas_1 = a * b
Luas_2 = c * d
print("Luas Persegi Panjang 1 adalah", Luas_1, "cm")
print("Luas Persegi Panjang dibulatkan Keatas yaitu", math.floor(Luas_1), "cm")
print("Luas Persegi Panjang 2 adalah", Luas_2, "cm")
print("Luas Persegi Panjang dibulatkan Keatas yaitu", math.floor(Luas_2), "cm")
print()

#Menentukan Luas Persegi Panjang yang Maksimum serta Pembulatannya Kebawah
print('a = ', Luas_1)
print('b = ', Luas_2)

print("Luas Persegi Panjang Maksimum adalah", max(Luas_1, Luas_2), "cm")
Maksimum = max(Luas_1, Luas_2)
print("Hasil Pembulatan Kebawah pada Luas Persegi Panjang ini adalah", math.ceil(Maksimum), "cm")
print()