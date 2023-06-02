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
        self.range={"+": [0, 20], "-": [-20, 20], "*": [0, 100], "/": [0, 5] }
        self.result=[]
        self.maxi=10
        self.mini=1
            
    def calcul(self):
        resultat=None
        a=random.randint(self.mini, self.maxi)
        b=random.randint(1, 10)
        operateur=random.choice(self.choix)
        ronge=self.range[operateur]
        print(ronge)
        
        print(a, operateur, b)
        resultat=round(self.operators[operateur](a, b))
        
        self.result.append(resultat)
        c=0
        while c<2:
            temp=random.randint(ronge[0], ronge[1])
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
        if self.level%2==0:
            self.niv_ennemi+=1
            self.coef+=1
        
        if self.niv_ennemi==2:
            if "-" not in self.choix:
                self.choix.append("-")
        if self.niv_ennemi==3:
            if "*" not in self.choix:
                self.choix.append("*")
        if self.niv_ennemi==4:
            if "/" not in self.choix:
                self.choix.append("/")
        if self.niv_ennemi==5:
            self.maxi=100
            self.range["+"]=[0, 200]
            self.range["-"]=[-200,200]
            self.range["*"]=[0, 1000]
            self.range["/"]=[0, 50]
        
            
            
combat=Combat()
while combat.level<20:
    combat.calcul()
    
