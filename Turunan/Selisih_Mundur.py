def hitung_turunan_selisih_mundur(data, h):
    turunan = []

    for i in range(1, len(data)):
        f_x_h = data[i]
        f_x = data[i - 1]
        turunan_h = (f_x_h - f_x) / h
        turunan.append(turunan_h)

    return turunan

def main():
    # Input data dari pengguna
    data_input = input("Masukkan data yang dipisahkan oleh spasi: ")
    data = [float(x) for x in data_input.split()]

    # Input nilai h dari pengguna
    h = float(input("Masukkan nilai h: "))

    # Hitung turunan selisih mundur
    turunan_selisih_mundur = hitung_turunan_selisih_mundur(data, h)

    # Tampilkan hasil
    print("Hasil Turunan Selisih Mundur:")
    for i in range(len(turunan_selisih_mundur)):
        print(f"f'({data[i+1]}) = {turunan_selisih_mundur[i]}")

if __name__ == "__main__":
    main()
