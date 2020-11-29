try:
    anyfiles = input("Masukkan Nama File : ")
    print("Isi file", anyfiles, "adalah : ")
    print(open(anyfiles, "r").read())
except FileNotFoundError:
    print("File tidak ditemukan")
except UnicodeDecodeError:
    print("Maaf, FIle yang anda maksud tidak bisa dibuka, Karena tidak berformat .txt")
    
