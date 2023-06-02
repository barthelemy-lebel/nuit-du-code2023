import pyxel
import random

class Joueur : 

    def __init__(self):

        pyxel.init(256, 256, title="NDC23", display_scale=3)

        self.x = 16
        self.y = 16
        self.direction="up"
        self.niveau=1
        self.compteur = 0
        self.chrono_frame = 0
        self.chrono_seconde = 0
        self.liste_bonus_vie = [[random.randint(10, 110), random.randint(10, 110)]]
        self.vies = 0
        self.sortie=[16,0,48,16]
        self.entree=[16,256,48,240]
        self.niveau1=[[0,0,16,16],
                      [48,0,256,16],
                       [0,0,16,256],
                       [240,0,256,256],
                       [48,240,256,256],
                       ]
        

        pyxel.run(self.update, self.draw)

    def deplacement(self):          
        if pyxel.btn(pyxel.KEY_RIGHT) :
            self.x += 2
            self.direction="right"
            self.collision()
        if pyxel.btn(pyxel.KEY_LEFT) :
            self.x += -2
            self.direction="left"
            self.collision()
        if pyxel.btn(pyxel.KEY_DOWN) :
            self.y += 2
            self.direction="down"
            self.collision()
        if pyxel.btn(pyxel.KEY_UP) :
            self.y += -2
            self.direction="up"
            self.collision()
            
        
    def collision(self):
        if self.x+16>= 240 and self.direction=="right":
            self.x-=2
        
        elif self.x <= 16 and self.direction=="left":
            self.x+=2
            
            
            
    
            
        
    def collision(self):
        for bloc in self.niveau1 :
    
            if self.x <= bloc[0]+20 and self.y <= bloc[1]+20 and self.x + 20 >= bloc[0] and self.y + 20 >= bloc[1] and self.direction=="right":
                self.x-=2
            if self.x <= bloc[0]+20 and self.y <= bloc[1]+20 and self.x + 20 >= bloc[0] and self.y + 20 >= bloc[1] and self.direction=="left":
                self.x+=2
            if self.x <= bloc[0]+20 and self.y <= bloc[1]+20 and self.x + 20 >= bloc[0] and self.y + 20 >= bloc[1] and self.direction=="down":
                self.y-=2
            if self.x <= bloc[0]+20 and self.y <= bloc[1]+20 and self.x + 20 >= bloc[0] and self.y + 20 >= bloc[1] and self.direction=="up":
                self.y+=2
                
        
        
            
    """def combat(self):
        if self.compteur >= 600:"""
    
    def chrono(self):
        self.chrono_frame += 1
        if self.chrono_frame >= 30:
            self.chrono_frame = 0
            self.chrono_seconde += 1
            
    def bonus_vie(self):
        if self.chrono_seconde % 120 == 0:
            self.chrono_seconde += 1
            self.liste_bonus_vie.append([random.randint(10, 110), random.randint(10, 110)])
        
        for bonus_vie in self.liste_bonus_vie :

            if self.x <= bonus_vie[0]+20 and self.y <= bonus_vie[1]+20 and self.x + 20 >= bonus_vie[0] and self.y + 20 >= bonus_vie[1]:
                self.liste_bonus_vie.remove(bonus_vie)
                self.vies += 1           

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
            
        self.deplacement()
        self.chrono()
        self.bonus_vie()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 20, 20, 11)
        
        for bonus_vie in self.liste_bonus_vie:
            pyxel.rect(bonus_vie[0], bonus_vie[1], 20, 20, 4)
            
        for i in range(len(self.niveau1)):
            long=self.niveau1[i][3]-self.niveau1[i][1]
            larg=self.niveau1[i][2]-self.niveau1[i][0]
            pyxel.rect(self.niveau1[i][0],self.niveau1[i][1],larg,long,8)
        

       
j = Joueur()
