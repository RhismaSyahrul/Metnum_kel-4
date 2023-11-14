def hitung_turunan_selisih_maju(data, h):
    turunan = []
    
    for i in range(len(data) - 1):
        f_x = data[i]
        f_x_h = data[i + 1]
        turunan_h = (f_x_h - f_x) / h
        turunan.append(turunan_h)
    
    return turunan

def main():
    # Input data dari pengguna
    data_input = input("Masukkan data yang dipisahkan oleh spasi: ")
    data = [float(x) for x in data_input.split()]

    # Input nilai h dari pengguna
    h = float(input("Masukkan nilai h: "))

    # Hitung turunan selisih maju
    turunan_selisih_maju = hitung_turunan_selisih_maju(data, h)

    # Tampilkan hasil
    print("Hasil Turunan Selisih Maju:")
    for i in range(len(turunan_selisih_maju)):
        print(f"f'({data[i]}) = {turunan_selisih_maju[i]}")

if __name__ == "__main__":
    main()
