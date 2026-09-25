import csv

class Drama:
    def __init__(self, kdata):
        self.dramaName = kdata[0]
        self.rating = kdata[1]
        self.actor = kdata[2]
        self.viewership = kdata[3]
        self.genre = kdata[4]
        self.director = kdata[5]
        self.writer = kdata[6]
        self.year = int(kdata[7])
        self.NoE = kdata[8]
        self.network = kdata[9]


    def __str__(self):
        return ("Utgivet år " + str(self.year))
    
    def __lt__(self,otherDrama):
        
        return("Har mera viewers: " + str( self.viewership > otherDrama.viewership))
    

    def amountActors(self):
        
        actorList = self.actor.split(", ") # Delar upp skådespelar strängen till en lista

        return(len(actorList))    # Returnerar antal skådespelare
    
    def Comedy(self):
        genreList = self.genre.split(", ")
        
        if "Comedy" in genreList:
            return("Filmen är av genren Comedy")
        
        else:
            return("Filmen innehåller inte Comedy")
    
def objMaker(indata):
    kdramaLista = []
    
    with open(indata, newline = "") as csvfile: #öppnar csv filen
        kdramaReader = csv.reader(csvfile, delimiter=",") #Läser in csv filen och delar upp den vid varje ,
        next(kdramaReader) #hoppar över första raden
        for line in kdramaReader:
            
            kdramaLista.append(Drama(line)) #Skapar ett objekt av class Drama och stoppar in den i kdramalista

    return(kdramaLista)


def yearSearch(inputList):
    year =  int(input("vilket år vill du söka efter? "))
    count = 0 #räknare
    for i in range(len(inputList)):
        if int(inputList[i].year) == year: 
            count += 1
            
    return ("Det finns " + str(count) + " stycken filmer från " + str(year) ) 


def main():
    kdramaLista = objMaker("kdrama.csv") #kallar på läsnings funktionen
    print(kdramaLista[2].amountActors()) #printar hur många skådespelar som är med i den filmen
    print(kdramaLista[1].__lt__(kdramaLista[2])) #Jämför om ett drama har mer visningar än en annan
    print(kdramaLista[5].Comedy()) #printar om filmen innehåller genren komedi
    print(yearSearch(kdramaLista))
main()