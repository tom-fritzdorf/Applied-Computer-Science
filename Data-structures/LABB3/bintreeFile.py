class Node:
    def __init__(self, indata):
        self.left = None
        self.right = None
        self.value = indata

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


def putta(p,newvalue):
        if not p: 
            return Node(newvalue)
        elif p.value == newvalue:
            #print("Värdet finns redan i träden")
            return p
        else:
            if newvalue < p.value:
                p.left = putta(p.left,newvalue)
            elif newvalue > p.value:
                p.right = putta(p.right,newvalue)
        return p

def finns(p,value):
    if p is None: 
        return False
    elif p.value == value:
        return True
    elif value < p.value:
        return finns(p.left,value)
    else:
        return finns(p.right,value)
    
def skriv(p):
    if p is None:
        return
    skriv(p.left)
    print(p.value)
    skriv(p.right)
    return


#som return sätt ihop däp plus det vi byggt upp