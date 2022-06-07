import random
mylist = [1,2,3,4,5,6,7,8,9,10]
t = int(input("How many numbers do you want?: "))
for i in range(0,t):
    print(mylist[random.randrange(0,11)], end = ", ")