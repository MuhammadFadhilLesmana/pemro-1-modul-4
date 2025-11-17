n, kelipatan = map(int, input().split())

total = 0
for i in range(1, n + 1):
    baris = []
    jumlah = 0
    for j in range(i, 0, -1):
        hasil = j * kelipatan
        jumlah += hasil
        baris.append(f"({j} * {kelipatan})")
    print(" + ".join(baris), f"= {jumlah}")
    total += jumlah
print(total)
