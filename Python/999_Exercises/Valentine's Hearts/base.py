import datetime
people_list = []
comp_list = []

with open('People.txt') as f:
    for line in f:
        l = line.strip()
        people_list.append(l)

with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        comp_list.append(l)


import random
num_people = random.randrange(0,len(people_list))
num_comp = random.randrange(0,len(comp_list))

print(people_list[num_people] + " " + comp_list[num_comp])
