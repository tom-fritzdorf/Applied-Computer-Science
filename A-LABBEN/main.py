import math

def Mode1(block): # Värden


    maxValue =  max(block) #max värde
    if maxValue == 0:
        bits = 0
        return bits
    else:
            
        bits  = math.log(maxValue)/math.log(2) #Beräknar antalet bits som behövs
        bits = math.ceil(bits) # Rundar alltid uppåt för att få minsta bits
        return bits



def Mode2(block, helLista): #skillnader
    diff = []

    
    if block[0] == 0: #Hanterar 0 vid x0
        diff.append(block[0])

    else: #hanterar ifall vi inte befinner oss på x0
        index = helLista.index(block[0]) #hittar indexet på första element i blocket i hela listan
        diff.append(abs(block[0]-helLista[index-1])) 

    for j in range(1, len(block)): #Går igenom resten av listan
        diff.append(block[j]-block[j-1])

    maxDiff = max(diff)
    if maxDiff == 0:
        bits = 0
        return bits
    else:
        bits  = math.log(maxDiff)/math.log(2) #Beräknar antalet bits som behövs
        bits = math.ceil(bits) + 1 # Rundar alltid uppåt för att få minsta bits
        return bits


def compareMode(block, helLista):

    mod1 = Mode1(block)
    mod2 = Mode2(block, helLista)

    return min(mod1, mod2)

def cost(block, lst, c):
    

    s = compareMode(block, lst)
    k = len(block)
    y = c + s * k
    return y
def generate_all_partitions(lst):

    if not lst:
        return [[]]  # Base case: return an empty partition

        
    # Result to hold all partitions
    result = []

    # Iterate through possible first blocks
    for i in range(1, len(lst) + 1):
        first_block = lst[:i]
        # Recursively partition the rest of the list
        for rest in generate_all_partitions(lst[i:]):
            result.append([first_block] + rest)

    return result

def process_list(lst, c):
    """
    Processes the list by generating all partitions and calculating the cost for each partition.
    """
    partitions = generate_all_partitions(lst)
    totCost = []

    for partition in partitions:
        tempCost = 0
        for sublist in partition:
            tempCost += cost(sublist, lst, c)
        totCost.append(tempCost)
    return totCost


lista1  = [1,2,3,4,5,3,1]
lista2 = [0,99,3,2,2,2,2,2]
lista3 = [0, 1, 3, 6, 10, 15, 21, 28, 1036, 0, 1035, 1, 1034, 2, 1033,1045, 1055, 1066, 1078, 1060, 1091]
testls = [0,99,3,2,2,2,2,2]

costs1 = process_list(lista1,5)
costs2 = process_list(lista2,3)
costs3 = process_list(lista3,16)
print(min(costs1))
print(min(costs2))
print(min(costs3))