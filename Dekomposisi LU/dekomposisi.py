import numpy as np

# Fungsi untuk melakukan dekomposisi LU pada matriks persegi
def dekomposisi(A):
    n = len(A)
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    
    # Langkah 1: Inisialisasi matriks L dan U
    for i in range(n):
        # Diagonal matriks L diisi dengan 1, yang menjadi langkah awal dalam dekomposisi LU.
        L[i][i] = 1
        
        # Langkah 2: Mengisi matriks U dan L
        for j in range(i, n):
            # Mengisi elemen matriks U dengan elemen matriks asli A
            U[i][j] = A[i][j]
            
            # Proses eliminasi Gauss: Mengurangkan elemen-elemen yang ada di atas diagonal utama.
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]
        
        for j in range(i + 1, n):
            # Mengisi elemen matriks L dengan elemen matriks asli A
            L[j][i] = A[j][i]
            
            # Proses eliminasi Gauss: Mengurangkan elemen-elemen yang ada di bawah diagonal utama.
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            
            # Membagi elemen matriks L dengan elemen diagonal utama matriks U.
            L[j][i] /= U[i][i]
            
    return L, U

A = np.array([[2, -1, 1], [-3, -2, 2], [-2, 1, 2]])
# Memanggil fungsi dekomposisi LU
L, U = dekomposisi(A)

# Output
# Matriks L
print("Matriks L (segitiga bawah): ")
print(L)

# Matriks U
print("Matriks U (segitiga atas): ")
print(U)
