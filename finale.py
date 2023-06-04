import os
import pyxel
import random
import operator


class Joueur:

    def __init__(self):

        pyxel.init(256, 256, title="NDC23", display_scale=3)

        self.x = 16
        self.y = 16
        self.direction = "up"
        self.niveau = 1
        self.compteur = 0
        self.chrono_frame = 0
        self.chrono_seconde = 0
        self.liste_bonus_vie = [[random.randint(15, 200), random.randint(15, 200)]]
        self.vies = 3
        self.level=1
        self.choix = ["+"]
        self.sortie = [16, 0, 48, 16]
        self.entree = [16, 256, 48, 240]
        self.niveau1 = [[0, 0, 16, 16],
                        [48, 0, 256, 16],
                        [0, 0, 16, 256],
                        [240, 0, 256, 256],
                        [48, 240, 256, 256],
                        ]

        self.reponse = None
        self.combat = None

        pyxel.run(self.update, self.draw)

    def deplacement(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1
            self.direction = "right"

            self.collision()
            self.compteur += 1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x += -1
            self.direction = "left"
            self.collision()
            self.compteur += 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 1
            self.direction = "down"
            self.compteur += 1

            self.collision()

            self.collision()
        if pyxel.btn(pyxel.KEY_UP):
            self.y += -1
            self.direction = "up"
            if self.x >= 16 and self.x <= 48 and self.y < 16:
                self.y = 256
            else:
                self.collision()
                self.compteur += 1

    def collision(self):

        if self.x + 18 <= self.niveau1[3][0] and self.x + 18 >= self.niveau1[3][0] and self.direction == "right":
            self.x -= 1
        elif self.x <= self.niveau1[2][2] - 1 and self.x >= self.niveau1[2][0] and self.direction == "left":
            self.x += 1
        elif self.y + 18 >= self.niveau1[4][1] and self.y <= self.niveau1[4][1] and self.direction == "down":
            self.y -= 1
        elif self.y >= self.niveau1[1][1] - 18 and self.y <= self.niveau1[1][1] + 15 and self.direction == "up":
            self.y += 1

    def declanche_combat(self):
        if self.compteur >=500:
            self.compteur = 0
            self.combat = Combat()
            self.combat.calcul(self.choix)

    def reponse_check(self):

        if pyxel.btn(pyxel.KEY_W):
            self.reponse = "W"
        elif pyxel.btn(pyxel.KEY_X):
            self.reponse = "X"
        elif pyxel.btn(pyxel.KEY_C):
            self.reponse = "C"
        else:
            self.reponse = None

        if self.combat != None:

            if self.reponse != None:

                if str(self.combat.dico[self.reponse]) == str(self.combat.resultat):
                    print(True)
                    a=self.combat.leval(self.level)
                    self.level=a[0]
                    if a[1]!="" and a[1] not in self.choix:
                        self.choix.append(a[1])
                    self.combat = None

                elif str(self.combat.dico[self.reponse]) != str(self.combat.resultat):
                    print(False)
                    self.vies-=1
                    print(self.vies)
                    self.combat = None

    def chrono(self):
        self.chrono_frame += 1
        if self.chrono_frame >= 30:
            self.chrono_frame = 0
            self.chrono_seconde += 1

    def bonus_vie(self):
        if self.chrono_seconde % 60 == 0:
            self.chrono_seconde += 1
            self.liste_bonus_vie.append([random.randint(10, 110), random.randint(10, 110)])

        for bonus_vie in self.liste_bonus_vie:

            if self.x <= bonus_vie[0] + 20 and self.y <= bonus_vie[1] + 20 and self.x + 20 >= bonus_vie[
                0] and self.y + 20 >= bonus_vie[1]:
                self.liste_bonus_vie.remove(bonus_vie)
                self.vies += 1

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        self.deplacement()
        self.chrono()
        self.bonus_vie()
        self.declanche_combat()
        self.reponse_check()

    def draw(self):
        if self.combat == None:
            if self.vies>0:
                pyxel.cls(0)
                pyxel.rect(self.x, self.y, 16, 16, 5)

                for bonus_vie in self.liste_bonus_vie:
                    pyxel.rect(bonus_vie[0], bonus_vie[1], 20, 20, 4)

                for i in range(len(self.niveau1)):
                    long = self.niveau1[i][3] - self.niveau1[i][1]
                    larg = self.niveau1[i][2] - self.niveau1[i][0]
                    pyxel.rect(self.niveau1[i][0], self.niveau1[i][1], larg, long, 8)

                pyxel.text(60, 8, "Vies :", 7)
                pyxel.text(88, 8, str(self.vies), 7)

            elif self.vies<=0:
                pyxel.cls(0)
                pyxel.text(100, 100, "Game Over", 7)


        else:
            pyxel.cls(10)
            pyxel.rect(0, 170, 500, 80, 0)
            pyxel.text(120, 200, self.combat.operation, 8)
            pyxel.text(40, 230, str(self.combat.dico["W"]), 8)
            pyxel.text(120, 230, str(self.combat.dico["X"]), 8)
            pyxel.text(200, 230, str(self.combat.dico["C"]), 8)


class Combat():

    def __init__(self):
        self.operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        self.niv_ennemi = 1
        self.range = {"+": [0, 20], "-": [-20, 20], "*": [0, 100], "/": [0, 5]}
        self.result = []
        self.maxi = 10
        self.mini = 1
        self.resultat = None
        self.dico = {"W": 0,
                     "X": 0,
                     "C": 0}
        self.operation = ""

    def calcul(self, choix):

        a = random.randint(self.mini, self.maxi)
        b = random.randint(1, 10)
        operateur = random.choice(choix)
        ronge = self.range[operateur]

        self.operation = str(a) + str(operateur) + str(b)
        self.resultat = round(self.operators[operateur](a, b))

        self.result.append(self.resultat)
        c = 0
        while c < 2:
            temp = random.randint(ronge[0], ronge[1])
            if temp != self.resultat:
                self.result.append(temp)
                c += 1

        self.dico["W"] = self.result.pop(random.randint(0, 2))
        self.dico["X"] = self.result.pop(random.randint(0, 1))
        self.dico["C"] = self.result.pop(0)

    def leval(self, level):
        choix=""
        level += 1
        print("level", level)
        if level % 5 == 0:
            self.niv_ennemi += 1
            print("niv", self.niv_ennemi)
        if self.niv_ennemi == 2:
            choix="-"
        if self.niv_ennemi == 3:
            choix="*"
        if self.niv_ennemi == 4:
            choix="/"
        if self.niv_ennemi == 5:
            self.maxi = 100
            self.range["+"] = [0, 200]
            self.range["-"] = [-200, 200]
            self.range["*"] = [0, 1000]
            self.range["/"] = [0, 50]
        print("choix", choix)
        return level, choix


j = Joueur()
