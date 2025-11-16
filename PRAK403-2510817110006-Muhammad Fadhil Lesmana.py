a, b = map(int, input().split()) 
hasil = [] 
if a < b: 
    for i in range(a, b + 1): 
        hasil.append(f"{i} {b - (i - a)}") 
else: 
    for i in range(a, b - 1, -1): 
        hasil.append(f"{i} {b + (a - i)}") 
print(" - ".join(hasil)) 
