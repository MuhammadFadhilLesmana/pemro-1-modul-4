while True: 
    print("Pilih Program") 
    print("1. Penjumlahan") 
    print("2. Pengurangan") 
    print("3. Perkalian") 
    print("4. Pembagian") 
    print("5. Exit") 
 
    try: 
        pilihan = int(input("Masukkan pilihan : ")) 
    except ValueError: 
        print("Input anda salah, silahkan coba lagi\n") 
        continue 
 
    if pilihan == 5: 
        print("Terimakasih, telah menggunakan kalkulator MUHAMMADFADHILLESMANA") 
        break 
    elif pilihan < 1 or pilihan > 5: 
        print("Input anda salah, silahkan coba lagi\n") 
        continue 
 
    try: 
        nilai1 = float(input("Masukkan nilai pertama : ")) 
        nilai2 = float(input("Masukkan nilai kedua   : ")) 
    except ValueError: 
        print("Input nilai harus berupa angka!\n") 
        continue 
 
    if pilihan == 1: 
        hasil = nilai1 + nilai2 
        print(f"Hasil Penjumlahan antara{nilai1:.2f} dengan {nilai2:.2f} adalah {hasil:.2f}") 
    elif pilihan == 2: 
        hasil = nilai1 - nilai2 
        print(f"Hasil Pengurangan antara {nilai1:.2f} dengan {nilai2:.2f} adalah {hasil:.2f}") 
    elif pilihan == 3: 
        hasil = nilai1 * nilai2 
        print(f"Hasil Perkalian antara {nilai1:.2f} dengan {nilai2:.2f} adalah {hasil:.2f}") 
    elif pilihan == 4: 
        if nilai2 == 0: 
            print("Kesalahan: Pembagian dengan nol tidak diperbolehkan.") 
        else: 
            hasil = nilai1 / nilai2 
            print(f"Hasil Pembagian antara {nilai1:.2f} dengan {nilai2:.2f} adalah {hasil:.2f}") 
print()
