import math

def update_dic(dic, line):
    base = line.split()[0]
    left = line.split('(')[1][:3]
    right = line.split(',')[1][1:4]
    dic[base] = {}
    dic[base]['L'] = left
    dic[base]['R'] = right
    return dic

f = open("C:\\Users\\TylerMueller\\Documents\\day8.txt", "r")

# read input file
readings = [x for x in f]
readings = [x.strip() for x in readings]

# initiate dictionary for the lines and steps starts at 1
dic = {}

# the first line is the directions
directions = readings[0]
directions = directions.replace(' ','')

# load dictionary of every line. The base and its corresponding left and right value
for line in readings[2:]:
    dic = update_dic(dic, line)

base_list = []
for base1 in dic:
    if base1[2] == 'A':
        base_list.append(base1)

multlist = []

for base in base_list:
    step_count = 0
    new_base = base
    done = False
    while done == False:
        for d in directions:
            new_base = dic[new_base][d]
            step_count += 1
            if new_base[2] == 'Z':
                multlist.append(step_count)
                done = True
                break

# Calculate the LCM using math.lcm
lcm_result = math.lcm(*multlist)
print(lcm_result)
