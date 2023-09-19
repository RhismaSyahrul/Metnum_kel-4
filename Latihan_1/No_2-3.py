import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

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
a = float(input("Masukkan batas bawah interval: "))
b = float(input("Masukkan batas atas interval: "))

# Input galat
tol = float(input("Masukkan galat (toleransi): "))

# Input jumlah iterasi (opsional)
n_iter = input("Masukkan jumlah iterasi (biarkan kosong jika tidak ingin membatasi iterasi): ")
if n_iter:
    n_iter = int(n_iter)
else:
    n_iter = None

# Solusi untuk fungsi
solusi = metode_bagiDua(fungsi, a, b, tol, n_iter)

# Plot fungsi
x = np.linspace(a, b, 400)
y = fungsi(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Fungsi')
plt.axhline(0, color='red', linestyle='--', alpha=0.5, label='y=0')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot Fungsi')
plt.grid(True)

# Tambahkan tanda pada akar
if solusi is not None:
    plt.scatter(solusi, 0, color='green', marker='o', label=f'Akar: x={solusi:.6f}')

plt.legend()
plt.show()
