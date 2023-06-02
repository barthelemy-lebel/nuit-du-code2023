import os
os.system("pip install pyxel")

import pyxel
import random

class Joueur : 

    def __init__(self):

        pyxel.init(128, 128, title="NDC23")

        self.x = 60
        self.y = 60
        self.compteur = 0
        self.chrono_frame = 0
        self.chrono_seconde = 0
        self.liste_bonus_vie = [[random.randint(10, 110), random.randint(10, 110)]]
        self.vies = 0

        pyxel.run(self.update, self.draw)

    def deplacement(self):

        if pyxel.btn(pyxel.KEY_RIGHT) and self.x<120:
            self.x += 1
            self.compteur += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.x>0:
            self.x += -1
            self.compteur += 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.y<120:
            self.y += 1
            self.compteur += 1
        if pyxel.btn(pyxel.KEY_UP) and self.y>0:
            self.y += -1
            self.compteur += 1
        if pyxel.btn(pyxel.KEY_D) and self.x<120:
            self.x += 1
            self.compteur += 1
        if pyxel.btn(pyxel.KEY_Q) and self.x>0:
            self.x += -1
            self.compteur += 1
        if pyxel.btn(pyxel.KEY_S) and self.y<120:
            self.y += 1
            self.compteur += 1
        if pyxel.btn(pyxel.KEY_Z) and self.y>0:
            self.y += -1
            self.compteur += 1
            
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
        

        
j = Joueur()

