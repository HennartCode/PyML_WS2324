
import numpy as np

x = np.random.randint(0,10,(8,4))



print(x)

def slow(x):
    d1, d2 = x.shape
    r = np.zeros((2, d1))
    for i in range(d1):
        for j in range(d2):
            for k in range(2):
                r[k, i] += (x[k, j] - x[i, j]) ** 2
    return r









def fast_1(x):
    return ((x[:2] - x) ** 2).sum(-1)


#muster---------------------
def fast_2(x):
    return ((x[:2, None] - x) ** 2).sum(-1)
#---------------------------

#print(f"slow: {slow(x)}")
#print(f"fast_2: {fast_2(x)}")
#print(f"fast_1: {fast_1(x)}")
#print(x[:2].shape, x[None,:2,None].shape, x.shape)
print(x[:,None,:2].shape)
print(x[:,None,:2])
print(x[:,None,:2]-x[:,:2])

class Auto(object):
    def __init__(self,typ,ps):
        self.typ = typ
        self.ps = ps
    def __call__(self):
        if self.ps > 150:
            print("VROOOOOOOOOOM PAPAPAP")
        else:
            print("brummmmm")
    def introduce(self):
        print(f"Hello I am a {self.typ} and i have {self.ps} PS.")


amg = Auto("amg",300)
fiat = Auto("fiat",110)

#amg.introduce()
#amg()
#fiat.introduce()
#fiat()

a = np.zeros((2,6))
b = np.random.randint(2,4,(3,4))

#print(a)
#print(b)
#print(b[2,None])
#print(b[[2]])