from colorama import Fore, Style, init

def hapus_duplikat_dan_simpan(file_input, file_output):
    try:
        # Membaca isi file input
        with open(file_input, 'r') as file:
            domains = file.readlines()

        # Menghilangkan karakter newline dan duplikat
        unique_domains = set(domain.strip() for domain in domains)

        # Menulis hasilnya ke file output
        with open(file_output, 'w') as file:
            for domain in unique_domains:
                file.write(domain + '\n')

        # Menampilkan pesan dengan warna
        print(Fore.GREEN + f"Duplikat berhasil dihapus dan hasil disimpan di '{file_output}'.")
    
    except FileNotFoundError:
        print(Fore.RED + f"Error: File '{file_input}' tidak ditemukan.")
    except Exception as e:
        print(Fore.YELLOW + f"Terjadi kesalahan: {e}")

# Menginisialisasi colorama
init(autoreset=True)

# Meminta input nama file dari pengguna
file_input = input(Fore.CYAN + "Masukkan nama file input ( contoh list.txt ): ")
file_output = input(Fore.CYAN + "Masukkan nama file output ( contoh hasil.txt ): ")

# Menjalankan fungsi
hapus_duplikat_dan_simpan(file_input, file_output)
