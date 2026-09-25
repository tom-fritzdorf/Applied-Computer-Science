from linkedQFile import LinkedQ
from molgrafik import *

atomsträng = """H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr
Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd
In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf
Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm
Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv"""

atomLista = atomsträng.split()


class Syntaxfel(Exception):
    pass


class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


    

def stor(q):
    temp = q.peek()
    if temp.isupper():
        check = q.dequeue()
        return check
    
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + q.__str__())

def finns(q, check):
    if check in atomLista:
        return 
    else:
        raise Syntaxfel("Okänd atom vid radslutet " + q.__str__())
    


def readnum(q,rutan):
    temp = q.peek()
    if temp == "0":
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet " + q.__str__())
    else:
        ints = str()
        while temp.isdigit() and not q.isEmpty():
            ints += temp
            q.dequeue()
            if q.isEmpty():
                pass
            else:
                temp = q.peek()
        if int(ints) > 1:
            rutan.num = int(ints)
            return rutan
        else:
            raise Syntaxfel("För litet tal vid radslutet " + q.__str__())
        

def readatom(q, rutan):
    temp = q.peek()
    if temp == ")":
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + q.__str__())
    elif temp.isdigit():
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + q.__str__())
    else:
        check = stor(q)
        if q.isEmpty():
            finns(q, check)
        else:
            temp = q.peek()
            if temp.islower():
                check += q.dequeue()
                finns(q, check)
            else:
                finns(q, check)
    rutan.atom = check
    return rutan
        
def readgroup(q):
    rutan = Ruta()
    temp = q.peek()
    if temp == "(":
        q.dequeue()
        rutan = readmol(q, False) #rutan.down
    else:
        readatom(q, rutan)
        if q.isEmpty():
            return rutan
        else:
            temp = q.peek()
            if temp.isdigit():
                readnum(q, rutan)
            else:
                pass
    return rutan
    


def readmol(q, status):
    if status:
        mol = readgroup(q)
        head = mol
        while not q.isEmpty():
            mol.next = readgroup(q)
            mol = mol.next
    
    else:
        tempmol = Ruta()
        tempmol.down = readgroup(q)
        head = tempmol
        mol = tempmol.down

        while not q.isEmpty():
            temp = q.peek()
            if temp == ")":
                break
                
   
            else:    
                newMol = readgroup(q)
                mol.next = newMol 
                mol = mol.next



        if q.isEmpty():
            raise Syntaxfel("Saknad högerparentes vid radslutet " + q.__str__())
        q.dequeue()
        if q.isEmpty():
            raise Syntaxfel("Saknad siffra vid radslutet " + q.__str__())
        else:
            temp = q.peek()
            if temp.isdigit():
                readnum(q, head) 
            else:
                raise Syntaxfel("Saknad siffra vid radslutet "+ q.__str__())
    return head
        

def store(mol):
    temp = list(mol)
    q = LinkedQ()
    for x in range(len(temp)):
        q.enqueue(temp[x])
    return q


def readformel(formel):
    q = store(formel)

    mol = readmol(q,True)
    return mol   


if __name__ == '__main__':
 
    inp = str()
    while True:  
        inp = input()
        
        if inp == "#":
            break
        try:
            mol = readformel(inp)
            mg = Molgrafik()
            mg.show(mol)
        except Syntaxfel as e:
             print(e)