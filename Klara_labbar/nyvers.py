from Labb_10.linkedQFile import LinkedQ
import string

atomsträng = """H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr
Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd
In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf
Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm
Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv"""

atomLista = atomsträng.split()

storaLista = list(string.ascii_uppercase)

class Syntaxfel(Exception):
    pass

def stor(q):
    temp = q.peek()
    if temp in storaLista:
        check = q.dequeue()
        return check
    
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + q.__str__())

def finns(q, check):
    if check in atomLista:
        return 
    else:
        raise Syntaxfel("Okänd atom vid radslutet " + q.__str__())
    
def nummer(q):
    temp = q.peek()
    if temp == "0":
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet " + q.__str__())
    else:
        ints = str()
        while temp.isdigit() and q.size() != 0:
            ints += temp
            q.dequeue()
            if q.size() == 0:
                pass
            else:
                temp = q.peek()
        if int(ints) > 1:
            return
        else:
            raise Syntaxfel("För litet tal vid radslutet " + q.__str__())

def readatom(q):
    temp = q.peek()
    if temp == ")":
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + q.__str__())
    elif temp.isdigit():
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + q.__str__())
    else:
        check = stor(q)
        if q.size() == 0:
            finns(q, check)
        else:
            temp = q.peek()
            if temp.islower():
                check += q.dequeue()
                finns(q, check)
            else:
                finns(q, check)
        
def readgroup(q):
    temp = q.peek()
    if temp == "(":
        q.dequeue()
        readmol(q, 2) #skicka in parantesen här antar jag
        #kolla om det finns en högerparantes
    else:
        readatom(q)
        if q.size() == 0:
            return
        else:
            temp = q.peek()
            if temp.isdigit():
                nummer(q)
            else:
                pass

def readmol(q, status):
    if status == 1:
        while q.size() != 0:
            readgroup(q)
    
    elif status == 2:
        while not q.isEmpty():
            temp = q.peek()
            if temp == ")":
                break
                
            else:
                readgroup(q)

        if q.isEmpty():
            raise Syntaxfel("Saknad högerparentes vid radslutet " + q.__str__())
        q.dequeue()
        if q.isEmpty():
            raise Syntaxfel("Saknad siffra vid radslutet " + q.__str__())
        else:
            temp = q.peek()
            if temp.isdigit():
                nummer(q) 
            else:
                raise Syntaxfel("Saknad siffra vid radslutet "+ q.__str__())
        

def store(mol):
    temp = list(mol)
    q = LinkedQ()
    for x in range(len(temp)):
        q.enqueue(temp[x])
    return q


def readformel(formel):
    q = store(formel)

    readmol(q,1)
    return "Formeln är syntaktiskt korrekt"    


if __name__ == '__main__':
    inp = str()
    while True:  
        inp = input()
        if inp == "#":
            break
        try:
            x = readformel(inp)
            print(x)
        except Syntaxfel as e:
            print(e)
