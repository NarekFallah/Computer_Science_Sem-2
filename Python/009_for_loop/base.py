x = int(input("Please Enter A Line Length"))
y = input ("Do You Want A Horizontal Or Vertical Line?: ")
if y == "horizontal":
    for x in range(0,x):
        print(" ", end = "*")
if y == "verical":
    for y in range(0,x):
        print("*")