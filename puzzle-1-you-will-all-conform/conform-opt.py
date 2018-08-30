#Programming for the Puzzled -- Srini Devadas
#You Will All Conform
#Input is a vector of F's and B's, in terms of forwards and backwards caps
#Output is a set of commands (printed out) to get either all F's or all B's
#Fewest commands are the goal
from random import choice

list_length = 20
rand_cap = []
for j in range(list_length): #Randomly generate a set of caps in a range of 20 people

  rand_cap.append(choice(['F','B','H']))

#print(" ".join(rand_cap))

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F' ]
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]
cap3 = ['H','H','H','H','H','H','H','H','H','H','H','B','F','B' ]

def pleaseConformOpt(caps):
    #Initialization
    start = 0
    forward = 0
    backward = 0
    heads = 0
    intervals = []
    print(" ".join(caps))
    caps = caps + ['END']

    #Determine intervals where caps are on in the same direction
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))

            if caps[start] == 'F':
                forward += 1
            elif caps[start] == 'B':
                backward += 1
            else:
                heads+=1
            start = i
    #print(intervals)
    print("Flipping Forward Caps:",forward, "commands")
    print("Flipping Backward Caps:", backward, "commands")
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            if t[0] == t[1]:
               print ("Person at position", t[0], "flip your cap!")
            else:
               print ('People in positions', t[0], 'through', t[1], 'flip your caps!')
#print(" ".join(cap3))
#pleaseConformOpt(cap3)

def pleaseConformOnepass(caps):
    caps = caps + [caps[0]] #Adds first element to the end of the array since our algorithm uses the next element to determine how the current element is affected
    for i in range(1, len(caps)):#starts iterating at element 2
        if caps[i] != caps[i-1]:#Checks if the 'next' index does NOT match the 'current' index (i-1)
            if caps[i] != caps[0]:#Since we are comparing people's cap to the first person, this condition checks if it matches the first person's cap
                print('People in positions', i, end='')
            else:
                print(' through', i-1, 'flip your caps')

pleaseConformOpt(rand_cap)
#pleaseConformOnepass(caps)
