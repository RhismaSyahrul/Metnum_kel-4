def simpson_13(f, a, b, n):
    # Memeriksa apakah jumlah subinterval genap
    if n % 2 != 0:
        raise ValueError("Jumlah subinterval harus genap untuk metode Simpson 1/3")

    # Menghitung lebar setiap subinterval
    h = (b - a) / n

    # Membuat array x yang berisi titik-titik dalam interval
    x = [a + i * h for i in range(n + 1)]

    # Menghitung nilai fungsi f(x) pada setiap titik x
    y = [f(xi) for xi in x]

    # Menggunakan rumus Simpson 1/3 untuk menghitung integral
    integral = y[0] + 4 * sum(y[i] for i in range(1, n, 2)) + 2 * sum(y[i] for i in range(2, n-1, 2)) + y[n]
    integral *= h / 3

    # Mengembalikan hasil integrasi
    return integral

def main():
    # Meminta input dari pengguna untuk fungsi f(x)
    expression = input("Masukkan fungsi f(x) (gunakan x sebagai variabel): ")
    f = lambda x: eval(expression)

    # Meminta input dari pengguna untuk batas bawah, batas atas, dan jumlah subinterval
    a = float(input("Masukkan batas bawah: "))
    b = float(input("Masukkan batas atas: "))
    n = int(input("Masukkan jumlah subinterval (harus genap): "))

    # Menghitung hasil integrasi menggunakan metode Simpson 1/3
    result = simpson_13(f, a, b, n)
    print(f"Hasil integrasi: {result}")

if __name__ == "__main__":
    main()

