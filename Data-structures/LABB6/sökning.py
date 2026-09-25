import timeit

class Låt:
    def __init__(self, trackid, låtid, artistnamn, låttitel):
        self.trackid = trackid
        self.låtid = låtid
        self.artistnamn = artistnamn
        self.låttitel = låttitel

    def __str__(self):
        return self.artistnamn
        
    def __lt__(self, other):
        
        return self.artistnamn < other.artistnamn


def readfile(indata):
    Lista = []
    
    with open(indata, "r", encoding="utf-8") as låtfil:
        for rad in låtfil:
            row = rad.strip()
            a,b,c,d = row.split("<SEP>")
            x = Låt(a,b,c,d)
            Lista.append(x)

    return Lista

def linsok(lista, testartist):
    count = 0
    for x in range(len(lista)):
        if lista[x] == testartist:
            count += 1
        else:
            pass

#chat-gpt
def sorted(arr, target):
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Beräkna mittpunkten
        mid = left + (right - left) // 2
        
        # Om vi hittar målet på mittenpositionen
        if arr[mid] == target:
            return target
        # Om målet är mindre än värdet på mitten, sök i vänstra delen
        elif arr[mid] > target:
            right = mid - 1
        # Om målet är större än värdet på mitten, sök i högra delen
        else:
            left = mid + 1
    
    # Om målet inte hittas
    return None

def makeHash(lista):
    hashTabell = {}
    

    for x in range(len(lista)):
       
        hashTabell[x] = lista[x].trackid
      

    return hashTabell


def hashSearch(hashTabell, nyckel):
        if nyckel in hashTabell:
            pass
        else:
            print("Ord finns ej!")


def main():

    filename = "LABB6/n250.txt"

    lista = readfile(filename)
    n = len(lista)
    print("Antal element =", n)
    
    sista = lista[n-1]
    testlåt = sista.låttitel
    
    låttitel_map = list(map(lambda Låt: Låt.låttitel, lista))
    value = int(input("vad vill du göra? "))
    if value == 1:

        linjtid = timeit.timeit(stmt = lambda: linsok(låttitel_map, testlåt), number = 10000)
        print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")
    elif value == 2:

        låttitel_map.sort()
        linjtid = timeit.timeit(stmt = lambda: sorted(låttitel_map, testlåt), number = 10000)
        print("Binärsökning tog", round(linjtid, 4) , "sekunder")

    elif value == 3:

        Hash = makeHash(lista)
        nyckel = n-1
        linjtid = timeit.timeit(stmt = lambda: hashSearch(Hash, nyckel), number = 10000)
        print("Sökning i hashtabell tog", round(linjtid, 4) , "sekunder")

main()