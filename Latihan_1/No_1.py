# No.1
# buatlah sebuah fungsi penyelesaian yang tepat baik dengan menggunakan metode bagi Dua ketika
# a. f(x) = x^3 - 2x + 1
# b. f(x) = e^x - x

import numpy as np

#memasukan Fungsi f1(x) = x^3 - 2x + 1
def f1(x):
  return x**3 - 2*x + 1
#memasukan Fungsi f2(x) = e^x - x
def f2(x):
  return np.exp(x) - x

#Melakukan metode bagi dua untuk mencari dan mendapatkan akar fungsi dalam interval [a, b]
def metode_bagiDua(f, a, b, tol=1e-6, maks_iter=100):

  #pengecekan "apakah ada perpotongan akar dalam interval?"
  if f(a) * f(b) >= 0:
    print("Tidak ada akar di dalam interval ini.")
    return None

  iterasi = 0
  while (b - a) / 2.0 > tol and iterasi < maks_iter:
    #hitung titik tengah pada interval
    c = (a + b) / 2.0

    #cek "apakah akar ditemukan?"
    if f(c) == 0:
      return c
    elif f(a) * f(c) < 0:
      #pindahkan batas atas ke titik tengah
      b = c
    else:
      #pindahkan batas bawah ke titik tengah
      a = c
    
    iterasi += 1
  
  #mengembalikan perkiraan akar
  return (a + b) / 2.0


#solusi untuk f1(x) = 0
solusi_f1 = metode_bagiDua(f1, -2, 2)
if solusi_f1 is not None:
  print(f"Solusi f1(x) = 0 adalah x = {solusi_f1:.6f}")
else:
  print("Metode Bagi Dua tidak konvergen untuk f1(x).")



#solusi untuk f2(x) = 0
solusi_f2 = metode_bagiDua(f2, -1, 2)
if solusi_f2 is not None:
    print(f"Solusi f2(x) = 0 adalah x = {solusi_f2:.6f}")
else:
    print("Metode Bagi Dua tidak konvergen untuk f2(x).")
