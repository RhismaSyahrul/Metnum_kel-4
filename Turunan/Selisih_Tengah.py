import numpy as np

# Melakukan deklarasi fungsi turunan selisih maju, mundur, dan tengah
def hitung_turunan_selisih_maju (f, x, h):
    return (f(x + h) - f(x)) / h

def hitung_turunan_selisih_mundur(f, x, h):
    return (f(x) - f(x - h)) / h

def hitung_turunan_selisih_tengah(f, x, h):
    return (f(x + h/2) - f(x - h/2)) / h

#input untuk pengguna

# imput fungsi dalam bentuk lambda expression
input_fungsi = input("Masukkan fungsi : ")
fungsi = lambda x: eval(input_fungsi)

# input nilai x
x_evaluasi = float(input("Masukkan nilai x untuk evaluasi turunan : "))

# memilih metode turunan
metode_turunan = input("Pilih metode turunan (maju/tengah/mundur) : ").lower()

# input nilai h
h = float(input("Masukkan nilai h untuk pendekatan numerik : "))

# pilih dan hitung sesuai metode yang dipilih

if metode_turunan == 'maju':
    hasil_turunan = hitung_turunan_selisih_maju(fungsi, x_evaluasi, h)
    print(f'Turunan Maju di {x_evaluasi}: {hasil_turunan}')
elif metode_turunan == 'tengah':
    hasil_turunan = hitung_turunan_selisih_tengah(fungsi, x_evaluasi, h)
    print(f'Turunan Tengah di {x_evaluasi}: {hasil_turunan}')
elif metode_turunan == 'mundur':
    hasil_turunan = hitung_turunan_selisih_mundur(fungsi, x_evaluasi, h)
    print(f'Turunan Mundur di {x_evaluasi}: {hasil_turunan}')
else:
    print('Metode turunan tidak valid. Pilih antara "maju", "tengah", atau "mundur".')

