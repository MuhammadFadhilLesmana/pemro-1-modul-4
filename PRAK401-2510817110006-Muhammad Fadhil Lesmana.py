data = input().split()
kelipatan = int(data[0])
simbol = data[1]

for i in range(1, 51):
    if i % kelipatan == 0:
        print(simbol, end=" ")
    else:
        print(i, end=" ")
print()
