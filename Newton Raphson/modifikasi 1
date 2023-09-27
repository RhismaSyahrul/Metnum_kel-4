# modifikasi Program ke-1 oleh: Rhisma Syahrul Putra
# -validasi input
# -menambahkan batas untuk iterasi


# definisi fungsi
def f(x):
    return x**2 - 2*x - 8

# Mendefinikan fungsi derivatif
def g(x):
    return 2*x - 2

# mendefinisikan fungsi metode newtonRaphson
def newtonRaphson(x0, e, N):
    
    """
    Metode Newton-Raphson untuk mencari akar dari fungsi f(x).

    Parameters:
    x0 (float): Perkiraan awal.
    e (float): Perkiraan error.
    N (int): Jumlah maksimum langkah iterasi.

    Returns:
    None
    """
    step = 1
    flag = 1
    condition = True
    
    while condition:
        if g(x0) == 0.0:
            print('Pembagian oleh nol error')
            break

        # Loop iterasi
        x1 = x0 - f(x0) / g(x0)
        print('Iterasi-%d, x1 = %0.6f dan f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step += 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nAkar yang dibutuhkan : %0.8f' % x1)
    else:
        print('\nMetode Newton-Raphson tidak konvergen setelah %d iterasi.' % N)

if __name__ == "__main__":
    try:
        x0 = float(input('Perkiraan awal: '))
        e = float(input('Perkiraan error: '))
        N = int(input('Jumlah maksimum langkah iterasi: '))
    except ValueError:
        print('Input harus berupa angka.')
        exit()

    newtonRaphson(x0, e, N)

