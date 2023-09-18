import numpy as np
import matplotlib.pyplot as plt

# Fungsi f1(x) = x^3 - 2x + 1
def f1(x):
    return x**3 - 2*x + 1

# Fungsi f2(x) = e^x - x
def f2(x):
    return np.exp(x) - x

# Melakukan metode bagi dua untuk mencari dan mendapatkan akar fungsi dalam interval [a, b]
def metode_bagiDua(f, a, b, tol=1e-6, maks_iter=100):
    iterasi = 0
    while iterasi < maks_iter:
        c = (a + b) / 2.0
        if f(c) == 0 or (b - a) / 2.0 < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterasi += 1
    return (a + b) / 2.0

# Input fungsi, batas akar, dan galat dari pengguna
fungsi_str = input("Masukkan fungsi f(x): ")
batas_bawah = float(input("Masukkan batas bawah interval: "))
batas_atas = float(input("Masukkan batas atas interval: "))
galat = float(input("Masukkan galat yang diinginkan: "))

# Konversi fungsi dari string menjadi fungsi callable
try:
    fungsi = lambda x: eval(fungsi_str)
    solusi = metode_bagiDua(fungsi, batas_bawah, batas_atas, galat)

    if solusi is not None:
        print(f"Solusi {fungsi_str} = 0 adalah x = {solusi:.6f}")
        
        # Membuat grafik fungsi dalam interval yang ditentukan
        x = np.linspace(batas_bawah, batas_atas, 400)
        y = [fungsi(xi) for xi in x]
        plt.plot(x, y, label=f'{fungsi_str}')
        plt.axhline(0, color='red', linestyle='--', linewidth=0.5)
        plt.xlabel('x')
        plt.ylabel(f'{fungsi_str}')
        plt.title(f'Grafik {fungsi_str}')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("Metode Bagi Dua tidak konvergen.")
except (SyntaxError, NameError):
    print("Masukkan fungsi yang valid (contoh: x**3 - 2*x + 1).")
except ZeroDivisionError:
    print("Tidak ada akar di dalam interval ini.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
