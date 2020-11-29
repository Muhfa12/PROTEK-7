# membuka dan mau membaca file d:/data.txt
file = open("d:/data.txt", "r")

# rumus untuk menjumlahkan semua bilangan yang ada di dalam file data.txt
# dan jika terjadi eror karena file tidak valid, bisa di atasi dengan block try-except ValueError
sum = 0
for data in file:
    try:
        sum = sum + int(data)
    except ValueError:
            continue
print(sum)
