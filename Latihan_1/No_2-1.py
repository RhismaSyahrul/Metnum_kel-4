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
