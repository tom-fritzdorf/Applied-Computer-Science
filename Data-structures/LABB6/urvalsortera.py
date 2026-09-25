import timeit

class Låt:
    def __init__(self, trackid, låtid, artistnamn, låttitel):
        self.trackid = trackid
        self.låtid = låtid
        self.artistnamn = artistnamn
        self.låttitel = låttitel
        
def readfile(indata):
    Lista = []
    
    with open(indata, "r", encoding="utf-8") as låtfil:
        for rad in låtfil:
            row = rad.strip()
            a,b,c,d = row.split("<SEP>")
            x = Låt(a,b,c,d)
            Lista.append(x)

    return Lista


#långsam sökningsmetod som är tagen från förelsänings-PDF
def urvalssortera(data):
    n = len(data)
    for i in range(n):
        minst = i
        for j in range(i+1,n):
            if data[j] < data[minst]:
                minst = j
        data[minst],data[i] = data[i], data[minst]
    return data


def main():
    lista = readfile("LABB6/n1000.txt")
    låttitel_map = list(map(lambda Låt: Låt.låttitel, lista))
    lista10000 = låttitel_map[0:10000]
    lista100000 = låttitel_map[0:100000]
    lista1000000 = låttitel_map[0:250000]

    linjtid10000 = timeit.timeit(stmt = lambda: urvalssortera(lista10000), number = 1)
    print("Sökning för n = 10000", round(linjtid10000, 4) , "sekunder")

    linjtid100000 = timeit.timeit(stmt = lambda: urvalssortera(lista100000), number = 1)
    print("Sökning för n = 100000", round(linjtid100000, 4) , "sekunder")
    
    linjtid1000000 = timeit.timeit(stmt = lambda: urvalssortera(lista1000000), number = 1)
    print("Sökning för n = 1000000", round(linjtid1000000, 4) , "sekunder")

main()
