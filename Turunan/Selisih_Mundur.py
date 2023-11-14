def turunan_selisih_mundur(data):
    turunan = []
    
    for i in range(1, len(data)):
        turunan.append((data[i] - data[i-1]))
    
    return turunan

# Input data dari pengguna
data_input = input("Masukkan data, pisahkan dengan spasi: ")
data = [float(x) for x in data_input.split()]

# Hitung turunan selisih mundur
hasil_turunan = turunan_selisih_mundur(data)

# Tampilkan hasil
print("Data input:", data)
print("Turunan selisih mundur:", hasil_turunan)
