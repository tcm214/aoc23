def update_dic(dic, line):
    base = line.split()[0]
    left = line.split('(')[1][:3]
    right = line.split(',')[1][1:4]
    if right == 'â€‹':
        right = 'RFN'
        print('switch--------------')

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
steps = 0
root = 'AAA'
done = False

# the first line is the directions. not sure why theres a space in there but there is so I took it out
# hope my input file isnt messed up
directions = readings[0]
directions = directions.replace(' ','')
# s  ='LLRRRLRLLRLRRRLRLRRRRLLRRRLRRRLRRRLRRRLRRRLRRLRLRRLLLRRLRLRLLRLRLLLRRLRLRRLRLRLRLRRRLLRRRLRRLLLRRLLRRLLRRLLRRLLLLRLRLRRRLLRRRLRLLLRLRRLRRLRRRLRRRLRRRLLLRRRLLLRLLRRLLRRRLRRLRLRRRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRRLRRRLRRLLRRRR'
# directions = s

for line in readings[2:]:
    dic = update_dic(dic, line)

# print(dic['XFN'])
while done == False:
    for d in directions:
        if root == 'ZZZ':
            done = True
            break
        #print(root)
        root = dic[root][d]
        steps += 1

print(steps)



        
