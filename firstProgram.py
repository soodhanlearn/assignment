spaces = 0
type = input("enter 1 for normal, 2 for inverted: ")
num = int(input("Please enter odd number :"))
lines = (num+1)/2
lines = int(lines)

if type == "2":
    for x in range (lines):
        for j in range(spaces):
            print(" ", end="")
        spaces += 1
        for i in range(num):
            print("*", end="")
        num -= 2
        print("")
#Print normal triangle
elif type == "1":
    print("entered 1")
    spaces = lines-1
    num=1
    for x in range (lines):
        for j in range(spaces):
            print(" ", end="")
        spaces -= 1
        for i in range(num):
            print("*", end="")
        num += 2
        print("")
