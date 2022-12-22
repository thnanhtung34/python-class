print("Bảng in số")
for i in range (0,10):
    for j in range(i+1, 101, 10):
        print("{:<3}".format(j), end = ' ')
    print()