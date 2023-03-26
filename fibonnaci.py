Num = int(input("enter a nummber"))
N1 = 0
N2 = 1
Sums = 0
if Num <= 0:
    print("enter a number greater than 0")
else:
    for i in range(0, Num):
        print(Sums, end="")
        N1 = N2
        N2 = Sums
        Sums = N1 + N2
