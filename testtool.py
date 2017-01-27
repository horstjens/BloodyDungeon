import random
class Viech(object):
    number=0
    book={}
    def __init__(self, hp= -1, att=-1, df=-1, dmg=-1, arm=-1, cri=-1, init=-1, spd=-1):
        self.number=Viech.number
        Viech.number+=1
        Viech.book[self.number]=self
        if hp == -1:
            self.hitpoints=random.randint(10,50)
        else:
            self.hitpoints=hp
        if att == -1:
            self.attack=random.randint(1,12)
        else:
            self.attack=att
        if df == -1:
            self.defense=random.randint(0,6)
        else:
            self.defense=df
        if dmg == -1:
            self.damage=random.randint(2,5)
        else:
            self.damage=dmg
        if arm == -1:
            self.armor=random.randint(0,3)
        else:
            self.armor=arm
        if cri == -1:
            self.critical=random.random()
        else:
            self.critical=cri
        if init == -1:
            self.initiative=random.randint(1,6)
        else:
            self.initiative=init
        if spd == -1:
            self.speed=random.randint(1,6)
        else:
            self.speed=spd
        
    def show(self):
        txt=""
        atts=[x for x in dir(self) if not "__" in x]
        for a in atts:
            txt+= "{}: {}\n".format(a, self.__getattribute__(a))
        print(txt)
        return txt
        
yannik=Viech(hp=66, att=12, df=3, dmg=4, arm=1)
yannik.show()
niklas=Viech(hp=33, att=24, df=6, dmg=2, arm=1)
niklas.show()


def strike(attacker, defender):
    w1=random.randint(1,6)+random.randint(1,6)
    w2=random.randint(1,6)+random.randint(1,6)
    if w1+attacker.attack>w2+defender.defense:
        print("Angriff erfolgreich!")
        damagemult=1
        if random.random()<attacker.critical:
            print("Kritischer Treffer!Dreifacher Schaden!")
            damagemult=3
        dmg=damagemult*attacker.damage-defender.armor
        if dmg>0:
            print("Schaden: {}".format(dmg))
            defender.hitpoints-=dmg
            return 
    else:
        print("Angriff misslungen!")
        

        
        
