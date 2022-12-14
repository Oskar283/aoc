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


#day 7. Ugh I hate this solution
import re
split = re.split(r"\$ ", inputs)[1:]  #skip first empty


class FileNode():

    def __init__(self, du, name):
        self.du = du
        self.name = name


class DirNode():

    def __init__(self, name, parent):
        self.children = []
        self.parent = parent
        self.name = name
        self.du = 0  #Needs to be calculated
        self.last_iter = 0

    def add_child(self, node):
        self.children.append(node)


baseNode = DirNode("", None)

cwd = ""
cwNode = baseNode
print("Starting")
for i in split:
    cmd = i.splitlines()[0]
    out = i.splitlines()[1:]  #empty if cd
    #print(repr(cmd),out)

    if re.findall("cd.*", cmd):
        splitted_cmd = cmd.split(" ")
        arg = splitted_cmd[1]

        #print("Arg:", repr(arg))
        if arg == "..":
            #print("from_dir", cwd)
            pos = cwd.rfind("/")
            cwd = cwd[:pos]
            cwNode = cwNode.parent
            #print(f"moving up to dir {cwd}, new node={cwNode}, name={cwNode.name}")
        elif arg == "/":
            cwd = ""
            cwNode = baseNode
        else:
            cwd += f"/{arg}"
            children_names = [c.name for c in cwNode.children]
            wanted_child = cwNode.children[children_names.index(cwd)]
            cwNode = wanted_child
            #print(f"moving to dir {cwd}")

    if "ls" == cmd:
        for line in out:
            splitted_out = line.split(" ")
            #print(splitted_out)
            name = splitted_out[1]
            du = int(
                splitted_out[0]) if not splitted_out[0] == "dir" else None

            if du:
                cwNode.add_child(FileNode(int(du), f"{cwd}/{name}"))
            else:
                new_node = DirNode(f"{cwd}/{name}", cwNode)
                #print("New node", new_node.name)
                cwNode.add_child(new_node)

print("end of parse")
tot = 0
def calculateSizes(node):
    if isinstance(node, DirNode):
        if not len(node.children):
            print("Found it", node.name, node.parent)
        sum_list = [calculateSizes(child) for child in node.children]
        node.du = sum(sum_list)
        if node.du < 100000:
            global tot
            tot+=node.du
    return node.du

baseNodeSize = calculateSizes(baseNode)
print(tot, baseNodeSize)
baseNode.du = baseNodeSize

#day7.2
dirSizes = []
def listDirSizes(node): #always dirNodes
    dirNodes = [child for child in node.children if isinstance(child, DirNode)]
    if dirNodes:
        global dirSizes
        dirSizes += [child.du for child in dirNodes]
        [listDirSizes(child) for child in dirNodes]

listDirSizes(baseNode)
usedSize = baseNode.du
FS_SIZE = 70000000 
SPACE_NEEDED = 30000000
unused = FS_SIZE - usedSize
size_to_del = SPACE_NEEDED - unused
filtered = list(filter(lambda x: x>=size_to_del,dirSizes))
filtered.sort()
print("size_to_del", size_to_del)
print("filtered",filtered)

#day8.1
import numpy as np

trees = []
for idx, i in enumerate(test_input.splitlines()):
    js = [*i]
    js = [int(j) for j in js]
    trees.append(js)

trees = np.array(trees)
seen = np.zeros(trees.shape)

def calc_trees(trees, seen):
    for idx, i in enumerate(trees):
        max_height_of_tree = -1
        #look from left
        for jdx in range(len(i)):
            if i[jdx] > max_height_of_tree:
                max_height_of_tree = i[jdx] #new max height on tree
                seen[idx,jdx] += 1
    
        #look from right
        max_height_of_tree = -1
        for jdx in range(len(i)-1, 0, -1):
            if i[jdx] > max_height_of_tree:
                max_height_of_tree = i[jdx] #new max height on tree
                seen[idx,jdx] +=1

calc_trees(trees, seen)
#Transpose to repeat above
trees = trees.T
seen = seen
calc_trees(trees, seen)
            
#return to original
trees = trees.T
seen = seen.T
seen_1d = np.reshape(seen,-1)
#print(len(seen_1d[seen_1d>0]))

#day8.2 NOT FINISHEDS
def look_up(ix, iy, tree_matrix):
    treehouse_height = tree_matrix[ix,iy]
    nbr = 0

    if ix == 0:
        return 0

    for idx in range(ix-1, -1, -1):
        next_tree = tree_matrix[idx, iy]
        nbr+=1
        if next_tree >= treehouse_height:
            break

    return nbr

def look_down(ix, iy, tree_matrix):
    treehouse_height = tree_matrix[ix,iy]
    nbr = 0

    nbr_trees_tot = tree_matrix.shape[0]
    if ix == nbr_trees_tot:
        return 0

    print(ix)
    for index in range(ix, nbr_trees_tot+1, 1):
        print(ix, index, nbr_trees_tot)
        next_tree = tree_matrix[index, iy]
        nbr+=1
        if next_tree >= treehouse_height:
            break

    return nbr

loc = np.zeros(seen.shape)
test_tree = np.zeros(seen.shape)
test_tree[0,0] = 1
test_tree[3,0] = 2

for iy, ix in np.ndindex(test_tree.shape):
    loc[ix,iy] = look_up(ix,iy, test_tree)
    loc[ix,iy] = look_down(ix,iy, test_tree)

print(test_tree)
print(loc)

#day14
import numpy as np
with open(inputs) as fh:
    inputs = fh.read().splitlines()

parsed_coords = []
max_row = -1

for line in inputs:
    coords = line.split(" -> ")
    parsed_coords.append([]) #prepare for next coord list
    for coord in coords:
        col,row = coord.split(",")
        parsed_coords[-1].append((int(row),int(col)))

        #find max y
        if int(row) > max_row:
            max_row = int(row)

print(parsed_coords)
playarea = np.zeros((900,1000))

# 0 open
# 1 rock
# 2 sand

# occupy rocks
for line in parsed_coords:
    last_pos = line[0]
    for row,col in line[1:]:
        if col == last_pos[1]: # move vertical
            if last_pos[0] < row:
                points = np.arange(last_pos[0], row+1, 1)
            else:
                points = np.arange(row, last_pos[0]+1)

            # fill
            for p in points:
                playarea[p,col] = 1

        else: #move horz
            if last_pos[1] < col:
                points = np.arange(last_pos[1], col+1)
            else:
                points = np.arange(col, last_pos[1]+1)

            # fill
            for p in points:
                playarea[row,p] = 1

        last_pos = (row,col)

def print_playarea():
    global playarea
    print(playarea[0:10, 494:505])

print_playarea()

def drop_sand(sand_pos_row, sand_pos_col, playarea):
    if not playarea[sand_pos_row+1, sand_pos_col] > 0:
        drop_sand(sand_pos_row+1, sand_pos_col, playarea)
    elif not playarea[sand_pos_row+1, sand_pos_col-1] > 0:
        drop_sand(sand_pos_row+1, sand_pos_col-1, playarea)
    elif not playarea[sand_pos_row+1, sand_pos_col+1] > 0:
        drop_sand(sand_pos_row+1, sand_pos_col+1, playarea)
    else:
        playarea[sand_pos_row, sand_pos_col] = 2
        return None
def part1():
    try: #try until outside of area
        while(True):
            drop_sand(0, 500, playarea)

    except Exception as e:
        print(e)
        print("Done!")

    print_playarea()
    print(len(playarea[playarea == 2]))
#part1()

#part2
playarea[max_row + 2,:] = 1
print(playarea[max_row + 2,:])
def part2():
    while(playarea[0, 500] != 2):
        drop_sand(0, 500, playarea)


    print(len(playarea[playarea ==2]))

part2()
