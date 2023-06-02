import os
import pyxel
import random
import operator

class Combat():
    
    def __init__(self):
        self.operators={"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv }
        self.level=0
        self.niv_ennemi=1
        self.choix=["+"]
        self.coef=3
        self.range=[0,20]
        self.result=[]
            
    def calcul(self):
        resultat=None
        a=random.randint(1, 10)
        b=random.randint(1, 10)
        operateur=random.choice(self.choix)
        print(a, operateur, b)
        resultat=round(self.operators[operateur](a, b))
        
        self.result.append(resultat)
        c=0
        while c<2:
            temp=random.randint(self.range[0], self.range[1])
            if temp!=resultat:
                self.result.append(temp)
                c+=1
        
        W=self.result.pop(random.randint(0,2))
        X=self.result.pop(random.randint(0,1))
        C=self.result.pop(0)
        print(W, X, C)
        
        reponse=input("réponse : W ou X ou C")
        
        if reponse=="W" and resultat==W:
            print(True)
            self.leval()
        elif reponse=="X" and resultat==X:
            print(True)
            self.leval()
        elif reponse=="C" and resultat==C:
            print(True)
            self.leval()
        else:
            print(False)
         
    def leval(self):
        self.level+=1
        if self.level%5==0:
            self.niv_ennemi+=1
            self.coef+=1
        
        if self.niv_ennemi==2:
            if "-" not in self.choix:
                self.choix.append("-")
            self.range=[-20, 20]
        if self.niv_ennemi==3:
            if "*" not in self.choix:
                self.choix.append("*")
            self.range=[-20, 100]
        if self.niv_ennemi==4:
            if "/" not in self.choix:
                self.choix.append("/")
            self.range=[-20, 100]
            
            
combat=Combat()
while combat.level<20:
    combat.calcul()
    



