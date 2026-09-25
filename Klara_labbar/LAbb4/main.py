from labb4.linkedQFile import LinkedQ

svenska = list()


def makechildren(startord, svenska, q, slutord, tidigare):
    

    bokstäver = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                    'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
    

    for x in range(len(startord)):
        tempList = list(startord) #resetar allt kommer
        bokstav = True
        count = 0

        while bokstav:
            tempList[x] = bokstäver[count]
            ord = "".join(tempList)
            
            if ord in svenska and not tidigare.finns(ord):
                tidigare.enqueue(ord)
                q.enqueue(ord)


            if bokstäver[count] == "ö":
                bokstav = False
            count += 1
            
    if q.finns(slutord):
        for y in range(q.size()):
            q.dequeue()
        print("Det finns en väg till " + slutord)


with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    
    for rad in svenskfil:
        ordet = rad.strip()            
        if ordet in svenska:
            pass 
        else:
            
            svenska.append(ordet)             


startord = "söt"
slutord = "sur"

q = LinkedQ()
q.enqueue(startord)
tidigare = LinkedQ()


while not q.isEmpty():
    word = q.dequeue()
    makechildren(word ,svenska, q, slutord, tidigare)

