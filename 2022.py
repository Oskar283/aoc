#Hacky and very slof solutions for aoc2022.
#day 1
maxs = list([0])
sum = 0
for i in inputs.splitlines():
    if i:
        sum+=int(i)
    else:
        maxs += [sum]
        sum = 0
        
maxs.sort()
print(maxs[0])
print (68589 +  69893 + 71924)


#day 2.1
score = 0
for i in inputs.splitlines():
    opp = i[0]
    me = i[2]
    if opp == "A":
        if i[2] == "X":
            score += 1 + 3
        elif i[2] == "Y":
            score += 2 + 6
        elif i[2] == "Z":
            score += 3 + 0
    elif i[0] == "B":
        if i[2] == "X":
            score += 1 + 0
        elif i[2] == "Y":
            score += 2 + 3
        elif i[2] == "Z":
            score += 3 + 6
    elif i[0] == "C":
        if i[2] == "X":
            score += 1 + 6
        elif i[2] == "Y":
            score += 2 + 0 
        elif i[2] == "Z":
            score += 3 + 3

#day 2.2
score = 0
for i in inputs.splitlines():
    opp = i[0]
    me = i[2]
    if opp == "A":
        if i[2] == "X":
            score += 3 + 0
        elif i[2] == "Y":
            score += 1 + 3
        elif i[2] == "Z":
            score += 2 + 6
    elif i[0] == "B":
        if i[2] == "X":
            score += 1 + 0
        elif i[2] == "Y":
            score += 2 + 3
        elif i[2] == "Z":
            score += 3 + 6
    elif i[0] == "C":
        if i[2] == "X":
            score += 2 + 0
        elif i[2] == "Y":
            score += 3 + 3 
        elif i[2] == "Z":
            score += 1 + 6
            
#day3.1
sum = 0
for i in inputs.splitlines():
    half = len(i)//2
    first = i[:half]
    last = i[half:]
    #print(len(first), len(last), first+last==i, first, last)
    
    for i in first:
        for j in last:
            if i == j:
                if i.isupper():
                    val = ord(i) - 65 + 27
                else:
                    val = ord(i) - 97 + 1
    sum += val
    
    
print(sum)

#day3.2
sum_ = 0
iter_ = 0
for i in inputs.splitlines():
    if iter_ == 0:
        nr0 = i
        iter_+=1
        continue
    elif iter_ == 1:
        nr1 = i
        iter_ +=1
        continue
    elif iter_ == 2:
        nr2 = i
        iter_ = 0

    for i in "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper():
        ingroup = i in nr0 and i in nr1 and i in nr2
        if ingroup:
            if i.isupper():
                val = ord(i) - 65 + 27
            else:
                val = ord(i) - 97 + 1

    sum_+=val
    
print(sum_)

