from z3 import *
#the sollution to the crribage players problem
def cribbage(terms,n):
    #creating an array to contain possitive numbers.
    cells=[Int('%d' %i) for i in range(terms)]
    creating our solver
    s=Solver()
    #adding the two constraints : consecutive and summ=the number.
    for i in range(terms-1):
        s.add(cells[i]+1 == cells[i+1])
    s.add(Sum(cells)== n)
    s.add(cells[0]>0)
    if s.check()==sat :
        print(s.model())
#an example.        
cribbage(3,15)
        
        

