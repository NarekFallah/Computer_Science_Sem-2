import random
reslist = ["Taco Bell","Shake Shack","Hot Wings Cafe","Dominos"]
TacoBellMenu = ["Chalupa","Crunch Wrap Supreme","Cinnamon Twists","Doritos Locos Tacos"]
ShakeShackMenu = ["Shack Birger","Cheesy Fries","Bacon Burger","Mushroom Burger"]
HotWingsCafeMenu = ["Buffalo Wings","Fries","Barbeque Wings","Lemen Pepper Wings","Boneless Hot Wings"]
DominosMenu = ["Pepperoni Pizza","Cheese Pizza","Coke"]
pick = input("Pick a restaurant to dine at: ")
if pick == "Taco Bell":
    print(TacoBellMenu)
    print(TacoBellMenu[random.randrange(0,4)])
elif pick == "Shake Shack":
    print(ShakeShackMenu)
    print(ShakeShackMenu[random.randrange(0,4)])
elif pick == "Hot Wings Cafe":
    print(HotWingsCafeMenu)
    print(HotWingsCafeMenu[random.randrange(0,5)])
elif pick == "Dominos":
    print(DominosMenu)
    print(DominosMenu[random.randrange(0,3)])