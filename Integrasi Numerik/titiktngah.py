def midpoint(f, a, b, n):
    # Memeriksa apakah jumlah subinterval genap
    if n % 2 != 0:
        raise ValueError("Jumlah subinterval harus genap untuk metode titik tengah")

    # Menghitung lebar setiap subinterval
    h = (b - a) / n

    # Membuat array x yang berisi titik tengah setiap subinterval
    x = [a + (i + 0.5) * h for i in range(n)]

    # Menghitung nilai fungsi f(x) pada titik-titik tengah
    y = [f(xi) for xi in x]

    # Menghitung integral menggunakan metode titik tengah
    integral = sum(y) * h

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

    # Menghitung hasil integrasi menggunakan metode titik tengah
    result = midpoint(f, a, b, n)
    print(f"Hasil integrasi: {result}")

if __name__ == "__main__":
    main()
