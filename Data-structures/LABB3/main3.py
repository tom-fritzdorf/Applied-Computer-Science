from bintreeFile import Bintree
svenska = Bintree()
engelska=Bintree()

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass 
        else:
            svenska.put(ordet)             # in i sökträdet

with open("engelska.txt", "r", encoding="utf-8") as engelskafil:
    
    content = engelskafil.read()
    words = content.split()        
    words = [word for word in words if word.isalpha()]

    for word in words:

        if word in engelska:
            pass

        else:
            engelska.put(word)
            if svenska.__contains__(word):
                print(word)
            else:
                pass
        



