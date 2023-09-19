import numpy as np
import sympy as sp

# Memasukkan Fungsi
def input_function():
    expression = input("Masukkan ekspresi fungsi (gunakan 'x' sebagai variabel): ")
    x = sp.symbols('x')
    try:
        f = sp.sympify(expression)
        f = sp.lambdify(x, f, 'numpy')
        return f
    except:
        print("Fungsi tidak valid.")
        return None

# Input batas akar
def input_bounds():
    a = float(input("Masukkan batas bawah interval: "))
    b = float(input("Masukkan batas atas interval: "))
    return a, b

# Input galat
def input_tolerance():
    tol = float(input("Masukkan galat (toleransi): "))
    return tol

# Input jumlah iterasi (opsional)
def input_iterations():
    n_iter = input("Masukkan jumlah iterasi (biarkan kosong jika tidak ingin membatasi iterasi): ")
    if n_iter:
        n_iter = int(n_iter)
    else:
        n_iter = None
    return n_iter

# Melakukan metode bagi dua untuk mencari dan mendapatkan akar fungsi dalam interval [a, b]
def metode_bagiDua(f, a, b, tol=1e-6, n_iter=None):
    # Pengecekan "apakah ada perpotongan akar dalam interval?"
    if f(a) * f(b) >= 0:
        print("Tidak ada akar di dalam interval ini.")
        return None

    iterasi = 0
    while (b - a) / 2.0 > tol and (n_iter is None or iterasi < n_iter):
        # Hitung titik tengah pada interval
        c = (a + b) / 2.0

        # Cek "apakah akar ditemukan?"
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            # Pindahkan batas atas ke titik tengah
            b = c
        else:
            # Pindahkan batas bawah ke titik tengah
            a = c

        iterasi += 1

    # Mengembalikan perkiraan akar
    return (a + b) / 2.0

# Input fungsi
fungsi = input_function()
if fungsi is None:
    exit()

# Input batas akar
a, b = input_bounds()

# Input galat
tol = input_tolerance()

# Input jumlah iterasi (opsional)
n_iter = input_iterations()

# Solusi untuk fungsi
solusi = metode_bagiDua(fungsi, a, b, tol, n_iter)
if solusi is not None:
    print(f"Solusi fungsi adalah x = {solusi:.6f}")
else:
    print("Metode Bagi Dua tidak konvergen.")
