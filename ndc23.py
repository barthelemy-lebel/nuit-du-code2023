import os
os.system("pip install pyxel")

import pyxel

class Joueur : 

    def __init__(self):

        pyxel.init(128, 128, title="NDC23")

        self.x = 60
        self.y = 60

        pyxel.run(self.update, self.draw)

    def deplacement(self):

        if pyxel.btn(pyxel.KEY_RIGHT) and self.x<120:
            self.x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.x>0:
            self.x += -1
        if pyxel.btn(pyxel.KEY_DOWN) and self.y<120:
            self.y += 1
        if pyxel.btn(pyxel.KEY_UP) and self.y>0:
            self.y += -1

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
            
        self.deplacement()
            

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 20, 20, 11)
        
j = Joueur()

