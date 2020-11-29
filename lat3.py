print ("-----------------------------------")
print ("    PROGRAM HITUNG RATA-RATA")
print ("-----------------------------------")

x= True
sum = 0
jumlah = 0
while ( x == True):
    try :
        bilbulat = int(input("Masukkan Bilangan Bulat : "))
        sum += bilbulat
        jumlah +=1

        opsi = input("Lagi ? (y/n) : ")
        if(opsi == "y"):
            x = True
        elif(opsi == "n"):
            x = False
        else :
            print ("Input Tidak Valid")
            break
    except ValueError :
        print("Bukan Bilangan Bulat")
        continue
rata2 = sum / jumlah
print("Rata-ratanya adalah : ", rata2)
        
