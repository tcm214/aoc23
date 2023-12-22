def get_diffs(line):
    diffs = []
    for i in range(len(line)-1):
        diffs.append(line[i+1] - line[i])
    return diffs

f = open("C:\\Users\\TylerMueller\\Documents\\day9.txt", "r")

readings = [x for x in f]
readings = [x.strip() for x in readings]
scorelist = []

for line in readings:
    line_list = []
    # split line in to list of ints    
    line = line.split()
    line = [int(x) for x in line]
    # add line to list of lines 
    line_list.append(line[:])
    #print(line_list)
    while True:
        # get diffs between values           
        diffs = get_diffs(line)
        # if all values are the same, save that value and break loop
        if all(x == diffs[0] for x in diffs):
            subval = diffs[0]
            break
        # if not all the same, add diffs to line list and re-do loop with the diffs
        line_list.append(diffs)
        line = diffs[:]
    # iterate through list_list backwards and add subval to the beginning of each list
    # then thats the new subval and go up one more and do the same until the top
    for diffline in line_list[::-1]:
        subval = diffline[0] - subval
    # the final subval is what I want to keep track of
    scorelist.append(subval)

# add up the final subvals for each line
total = 0
for score in scorelist:
    total += score
print(total)
