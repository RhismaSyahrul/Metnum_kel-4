def integral_trapesium():
    # Input data dari pengguna
    n = int(input("Masukkan jumlah interval (n): "))
    a = float(input("Masukkan batas bawah (a): "))
    b = float(input("Masukkan batas atas (b): "))

    # Menghitung lebar interval
    h = (b - a) / n

    # Menginisialisasi nilai integral
    integral = 0

    # Menghitung integral menggunakan metode trapesium
    for i in range(n + 1):
        x = a + i * h
        if i == 0 or i == n:
            integral += f(x)
        else:
            integral += 2 * f(x)

    integral *= h / 2

    # Output hasil integral
    print(f'Hasil integral menggunakan metode trapesium: {integral:.4f}')

# Fungsi yang akan diintegrasikan (ganti dengan fungsi sesuai kebutuhan)
def f(x):
    return x**2

# Memanggil fungsi integral_trapesium
integral_trapesium()
