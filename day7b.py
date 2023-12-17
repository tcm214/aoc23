from collections import Counter

def max_duplicate_occurrences_in_string(hand):
    counter = Counter(hand)
    
    # Find the maximum count
    max_count = max(counter.values())
    
    # Find the character(s) with the maximum occurrences
    max_characters = [key for key, value in counter.items() if value == max_count]
    
    return max_count, len(max_characters)

def most_common_character(hand):
    # Use Counter to count occurrences of each character
    char_count = Counter(hand)
    
    # Find the most common character and its count
    most_common, count = char_count.most_common(1)[0]

    return most_common, count

def create_card_dict():
    card_dict = {
        '2':'02'
        ,'3':'03'
        ,'4':'04'
        ,'5':'05'
        ,'6':'06'
        ,'7':'07'
        ,'8':'08'
        ,'9':'09'
        ,'T':'10'
        ,'J':'11'
        ,'Q':'12'
        ,'K':'13'
        ,'A':'14'
    }
    return card_dict

def create_hand_dict():
    hand_dict = {
        'HC':2
        ,'1P':3
        ,'2P':4
        ,'3OAK':5
        ,'FH':6
        ,'4OAK':7
        ,'5OAK':8
    }
    return hand_dict

def get_tiebreaker(hand, card_dict):
    tiebreaker = ''
    for card in hand:
        tiebreaker += card_dict[card]
    return tiebreaker

def get_hand_type(hand):
    # count the Js
    jcount = hand.count("J")
    # return 5OAK if all J's. Otherwise it breaks stuff

    # print(hand)
    # print(jcount)

    if jcount == 5:
        return '5OAK'
    # remove the Js
    hand = ''.join([char for char in hand if char != "J"])
    # find the most common character
    most_common, _ = most_common_character(hand)
    # add more of the most common character, equal to the # of Js
    for j in range(jcount):
        hand += most_common
    # print(hand)
    diffcards = len(set(hand))
    if diffcards == 1:
        return '5OAK'
    if diffcards == 5:
        return 'HC'
    if diffcards == 4:
        return '1P'
    max_count, max_cards = max_duplicate_occurrences_in_string(hand)
    if max_count == 4:
        return '4OAK'
    if diffcards == 2:
        return 'FH'
    if max_cards == 2:
        return '2P'
    return '3OAK'

        
f = open("C:\\Users\\TylerMueller\\Documents\\day7.txt", "r")

# read input file
readings = [x for x in f]
#readings = [x.strip() for x in readings]

# create dictionaries for card values and hand scores
card_dict = create_card_dict()
hand_dict = create_hand_dict()

diclist = []
total_score = 0

for line in readings:
    dic = {}
    #get hand and bid from each line
    hand = line.split()[0]
    bid = int(line.split()[1])

    #get hand type
    hand_type = get_hand_type(hand)
    # print(hand_type)
    
    #get tiebreak score
    tiebreaker = get_tiebreaker(hand, card_dict)

    # create dictionary with compiled value which is the hand score glued to the tiebreaker
    dic['compiled'] = str(hand_dict[hand_type]) + tiebreaker
    dic['compscore'] = int(dic['compiled'])
    dic['bid'] = bid
    dic['hand'] = hand
    dic['hand_type'] = hand_type
    diclist.append(dic)

# create a list of the hands and bids sorted by compscore
sorted_list_asc = sorted(diclist, key=lambda x: x['compscore'], reverse=False)
# print(sorted_list_asc)

# write sorted list to file for troubleshooting
# with open("C:\\Users\\TylerMueller\\Documents\\7test.txt", 'w') as file:
    # Iterate over the list of dictionaries and write values to the file
    # for dic in sorted_list_asc:
        # file.write(f"hand: {dic['hand']}, compscore: {dic['compscore']}, hand type: {dic['hand_type']}\n")

# add up all the rank*bids
for i in range(len(sorted_list_asc)):
    total_score += (i+1)*sorted_list_asc[i]['bid']

print(total_score)
