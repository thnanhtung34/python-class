def sum (A,B):
    S = A*B
    if S<= 1000:
        return S
    else:
        return A+B
A = int(input("Nhap vao so A = "))
B = int(input("Nhap vao so B = "))
thanhtung = sum (A,B)
with open(r"C:\Users\admin\Downloads\baitap\t.txt", "w", encoding='utf-8') as f:
    f.write(str(thanhtung))
    print(thanhtung)
    