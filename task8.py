a = int(input("enter the num"))
b = int(input("enter the end of the num"))
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)
