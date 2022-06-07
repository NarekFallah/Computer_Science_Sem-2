items = int(input("How Many Items"))
total = 0
for i in range (0, items):
    itemName = input("What Is The Item? ")
    price = float(input("How Much Is It? "))
    print("Thanks for purchasing " + itemName)
    total = total + price
    
print("Your Total Is; " + str(total))