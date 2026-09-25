from ArrayQFile import ArrayQ
    
    
def trolleriLinked(indata):
    q = ArrayQ()
    bordet = ArrayQ()
    for i in range(len(indata)):
        q.enqueue(indata[i])


    while q.isEmpty() == False:
        x = q.dequeue()
        q.enqueue(x)
        
        x = q.dequeue()
        bordet.enqueue(x)


    return bordet.__str__()


def main():

    inKort = input("Vilka kort? ")
    inKort = inKort.split()
    inKort = [int(s) for s in inKort]
    inKort = trolleriLinked(inKort)
    print(inKort)
    


main()
