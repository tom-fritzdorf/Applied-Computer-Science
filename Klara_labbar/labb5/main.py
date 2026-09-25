from Labb_10.linkedQFile import LinkedQ

svenska = list()


class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent


    
def writechain(slutNode):
    
    if slutNode.parent != None:
        writechain(slutNode.parent)
        print(slutNode.word)
    else:
        print(slutNode.word)
    


def makechildren(startord, svenska, q, slutord, tidigare):

    bokstäver = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                    'w', 'x', 'y', 'z', 'å', 'ä', 'ö']

    for x in range(len(startord.word)):
        tempList = list(startord.word) #reset listan så vi kommer tillbaka till startordet
        bokstav = True
        count = 0

        while bokstav:
            tempList[x] = bokstäver[count]
            ord = "".join(tempList)

            if ord in svenska and not tidigare.finns(ord):
                
                tidigare.enqueue(ord)
                lala=ParentNode(ord)
                lala.parent=startord
                q.enqueue(lala)

            if bokstäver[count] == "ö":
                bokstav = False
            count += 1
    
    


def main():
    with open("labb4/word3.txt", "r", encoding = "utf-8") as svenskfil:  
        for rad in svenskfil:
            ordet = rad.strip()            
            if ordet in svenska:
                pass 
            else:
                svenska.append(ordet)             
    startord = "ute"
    slutord = "hit"
    q = LinkedQ()
    q.enqueue(ParentNode(startord))
    tidigare = LinkedQ()
    tidigare.enqueue(startord)
    pathFound = False
    while not q.isEmpty():
        node = q.dequeue()
        if node.word == slutord:
            writechain(node)
            pathFound = True
            break
        makechildren(node ,svenska, q, slutord, tidigare)
    if not pathFound:
        print("Ingen väg hittades!")
main()