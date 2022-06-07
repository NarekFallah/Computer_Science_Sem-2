mynumbers = [6,9,32,28,15,22,3,18]

sum = 0

for x in range(0, len(mynumbers)):
    sum = sum + mynumbers[x]
Average = sum / len(mynumbers)
MaximumValue = mynumbers[0]
MinimumValue = mynumbers[0]

for x in mynumbers:
    if x > MaximumValue:
        MaximumValue = x
    if x < MinimumValue:
        MinimumValue = x
print(MinimumValue)
print(MaximumValue)
print(Average)
print("ILY Mr Poole")