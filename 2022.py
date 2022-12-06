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

#day5.1, 5.2
import re

current_input = inputs

starting_stack, instructions  = re.split(r"\n\n", current_input)

nbr_stacks = int(starting_stack.splitlines()[-1][-2])
stack_content = starting_stack.splitlines()[:-1]
stack_content.reverse()

stacks = [[] for i in range(0,nbr_stacks)]

#1,5,9
for i in stack_content:
    row = [i[1+j*4] for j in range(0,nbr_stacks)]
    
    for idx,val in enumerate(row):
        if val != " ":
            stacks[idx].append(val)
            
def move1(times_, from_, to_):

    for i in range(0,times_):
        elem = stacks[from_].pop()
        stacks[to_].append(elem)
        
def move2(times_, from_, to_):
    elems = []
    for i in range(0,times_):
        elems.append(stacks[from_].pop())
        
    elems.reverse()    
    [stacks[to_].append(i) for i in elems ]
    
for i in instructions.splitlines():
    ans = re.findall(r"move (\d+) from (\d+) to (\d+)", i)
    ans = [int(i) for i in ans[0]]
    ans[1]-= 1 #compensate for index 0 in array
    ans[2]-= 1 #compensate for index 0 in array
    move2(*ans)
    
string = ""
for i in stacks:
    string+=i[-1]
print(string)

#day 6
buffer = "" 
index = 0
for idx,char in enumerate(inputs):
    pos = buffer.find(char)
    if pos >= 0:
        buffer = buffer[pos+1:]
        buffer += char
        index = idx
    else:
        buffer += char
        
    if len(buffer) == 14: #4 for p.1, 14 for p.2
        break
print(buffer, idx+1)
