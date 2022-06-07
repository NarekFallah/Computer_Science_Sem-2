c = 0
with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()                    
        for i in range(0,len(sentence)):            
            if sentence[i:i+5].lower() == "whale":
                count = count + 1
print(count)
f.close()
