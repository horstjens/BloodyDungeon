# -*- coding: utf-8 -*-
"""
author: Horst JENS
email: horstjens@gmail.com
contact: see http://spielend-programmieren.at/de:kontakt
license: gpl, see http://www.gnu.org/licenses/gpl-3.0.de.html
idea: template to show how to move surfaces (not pygames Sprite class!)
around
"""


import pygame 
import math
import random
import os


level1= [
"######.#.########",
"#@..#....w#######",
"#...#...fww######",
"#...#....w#######",
"#........#.#.#...",
"#.f.#..#.......#.",
"#fff#.####.######",
"#ff##############",
"##f##############",
"#################"
]


class Player(object):
    def __init__(self, x, y, imagename="player.png"):
        self.x=x
        self.y=y
        self.X = self.x
        self.Y = self.y
        self.hitpoints = 100
        self.image=pygame.image.load(os.path.join("data", imagename))
        self.rect = self.image.get_rect()
    
    def update(self, seconds):
        pass
                
    def blit(self, background):
        """blit the Ball on the given background surface"""
        background.blit(self.image, ( self.x, self.y))
   
class FlyingObject(pygame.sprite.Sprite):
    number = 0
    numbers = {}
    
    def __init__(self, bild, x, y, dx, dy, damage = 0):
        self._layer = 5  # self.layer = layer
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.number = FlyingObject.number
        FlyingObject.number += 1
        FlyingObject.numbers[self.number] = self
        self.image = bild
        self.damage = damage
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.age = 0
        self.width = self.rect.width
        self.height = self.rect.height
        
    def update(self, seconds):
        self.x += self.dx * seconds
        self.y += self.dy * seconds 
        self.age += seconds
        
        
        # kill if touching screen edge
        if self.x + self.width //2 > PygView.width:
            self.kill()
        if self.x - self.width //2 < 0:
            self.kill()
        if self.y + self.height // 2 > PygView.height:
            self.kill()
        if self.y - self.height // 2 < 0:
            self.kill()
        #movement
        self.rect.center = (round(self.x, 0), round(self.y, 0))
    
class Monster(object):
    def __init__(self, x, y, imagename="monster.png"):
        self.x=x
        self.y=y
        self.X = self.x
        self.Y = self.y
        self.image=pygame.image.load(os.path.join("data", imagename))
    
    #def move(self,mapdx,mapdy):
        
    
    def update(self, seconds):
        pass
                
    def blit(self, background):
        """blit the Ball on the given background surface"""
        background.blit(self.image, ( self.x, self.y))
    




def draw_examples(background):
    """painting on the background surface"""
    #------- try out some pygame draw functions --------
    # pygame.draw.line(Surface, color, start, end, width) 
    pygame.draw.line(background, (0,255,0), (10,10), (50,100))
    # pygame.draw.rect(Surface, color, Rect, width=0): return Rect
    pygame.draw.rect(background, (0,255,0), (50,50,100,25)) # rect: (x1, y1, width, height)
    # pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect
    pygame.draw.circle(background, (0,200,0), (200,50), 35)
    # pygame.draw.polygon(Surface, color, pointlist, width=0): return Rect
    pygame.draw.polygon(background, (0,180,0), ((250,100),(300,0),(350,50)))
    # pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1): return Rect
    pygame.draw.arc(background, (0,150,0),(400,10,150,100), 0, 3.14) # radiant instead of grad
    #return background # not necessary to return the surface, it's already in the memory

def write(background, text, x=50, y=150, color=(0,0,0),
          fontsize=None, center=False):
        """write text on pygame surface. """
        if fontsize is None:
            fontsize = 24
        font = pygame.font.SysFont('mono', fontsize, bold=True)
        fw, fh = font.size(text)
        surface = font.render(text, True, color)
        if center: # center text around x,y
            background.blit(surface, (x-fw//2, y-fh//2))
        else:      # topleft corner is x,y
            background.blit(surface, (x,y))


class PygView(object):
    width = 0
    height = 0
  
    def __init__(self, width=640, height=400, fps=30):
        """Initialize pygame, window, background, font,...
           default arguments 
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        PygView.width = width    # make global readable
        PygView.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()  
        self.background.fill((255,255,255)) # fill background white
        self.background=pygame.image.load(os.path.join("data","yannikbild1.png"))
        self.pfeil_nord=pygame.image.load(os.path.join("data","nord_missile-n.png"))
        self.pfeil_ost=pygame.image.load(os.path.join("data","ost_missile-n.png"))
        self.pfeil_süd=pygame.image.load(os.path.join("data","süd_missile-n.png"))
        self.pfeil_west=pygame.image.load(os.path.join("data","west_missile-n.png"))
        self.feuerpfeil_nord=pygame.image.load(os.path.join("data","nord_missile-fire-n.png"))
        self.feuerpfeil_ost=pygame.image.load(os.path.join("data","ost_missile-fire-n.png"))
        self.feuerpfeil_süd=pygame.image.load(os.path.join("data","süd_missile-fire-n.png"))
        self.feuerpfeil_west=pygame.image.load(os.path.join("data","west_missile-fire-n.png"))
        self.knochenpfeil_nord=pygame.image.load(os.path.join("data","nord_bone-n.png"))
        self.knochenpfeil_ost=pygame.image.load(os.path.join("data","ost_bone-n.png"))
        self.knochenpfeil_süd=pygame.image.load(os.path.join("data","süd_bone-n.png"))
        self.knochenpfeil_west=pygame.image.load(os.path.join("data","west_bone-n.png"))
        self.eispfeil_nord=pygame.image.load(os.path.join("data","nord_icemissile-n-3.png"))
        self.eispfeil_ost=pygame.image.load(os.path.join("data","ost_icemissile-n-3.png"))
        self.eispfeil_süd=pygame.image.load(os.path.join("data","süd_icemissile-n-3.png"))
        self.eispfeil_west=pygame.image.load(os.path.join("data","west_icemissile-n-3.png"))
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        #self.font = pygame.font.SysFont('mono', 24, bold=True)
        self.paint() 

    def paint(self):
        """painting on the surface"""
        # make an interesting background 
        # draw_examples(self.background)
        # create (non-pygame) Sprites. 
        # self.ball1 = Ball(x=100, y=100) # creating the Ball object (not a pygame Sprite)
        # self.ball2 = Ball(x=200, y=100) # create another Ball object (not a pygame Sprite)
        # self.ballgroup = [ self.ball1, self.ball2 ] # put all "Sprites" into this list
        self.player1= Player(self.width/2, self.height/2)
        self.playergroup = [self.player1, ]
        self.monster1=Monster(325,300)
        self.monster2=Monster(400,300)
        self.monstergroup=[self.monster1,self.monster2]
        self.allgroup = pygame.sprite.LayeredUpdates()
        self.flygroup = pygame.sprite.Group() 
        FlyingObject.groups = self.allgroup, self.flygroup
        Player.groups = self.allgroup
        
        # for drawing


    def movemonsters(self, dx, dy):
        for m in self.monstergroup:
                m.x += dx
                m.y += dy
              

    def run(self):
        """The mainloop"""
        self.delta = 60
        pygame.display.set_caption("Press ESC to quit. Player1 hp {}".format(self.player1.hitpoints))
        self.mapdx = 4 * self.delta  #
        self.mapdy = 1 * self.delta  #
        self.fx = 1 # field of tilemap. 0,0 is left upper corner
        self.fy = 1 
        

        delta = self.delta
        running = True
        self.lastdir = "up"
        while running and self.player1.hitpoints > 0:
            pygame.display.set_caption("Press ESC to quit. Player1 hp {}".format(self.player1.hitpoints))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                elif event.type == pygame.KEYDOWN:
                    x = PygView.width // 2+ 30
                    y =PygView.height // 2 + 30
                    if event.key == pygame.K_q:
                        if self.lastdir == "right":
                            FlyingObject(self.feuerpfeil_ost, 
                                         x-5, y-10, 200, 0, damage = 5
                                         )
                        if self.lastdir == "left":
                            FlyingObject(self.feuerpfeil_west, 
                                         x-5, y-10, -200, 0, damage = 5
                                         )
                        if self.lastdir == "down":
                            FlyingObject(self.feuerpfeil_süd, 
                                         x-5, y-10, 0, 200, damage = 5
                                         )
                        if self.lastdir == "up":
                            FlyingObject(self.feuerpfeil_nord, 
                                         x-5, y-10, 0, -200, damage = 5
                                         )
                    if event.key == pygame.K_w:
                        if self.lastdir == "right":
                            for z in (14, 7, 0, -7, -14):
                                FlyingObject(self.feuerpfeil_ost,
                                         x-5, y-10, 200, z, damage = 3
                                         )                                                 
                        if self.lastdir == "left":
                            for z in (14, 7, 0, -7, -14):          
                                FlyingObject(self.feuerpfeil_west,
                                         x-5, y-10, -200, z, damage = 3
                                         )                           
                        if self.lastdir == "down":
                            for z in (14, 7, 0, -7, -14):
                                FlyingObject(self.feuerpfeil_süd,
                                     x-5, y-10, z, 200, damage = 3
                                     )                      
                        if self.lastdir == "up":
                            for z in (14, 7, 0, -7, -14):
                                FlyingObject(self.feuerpfeil_nord,
                                     x-5, y-10, z, -200, damage = 3
                                     )                     
                                                           
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    # if event.key == pygame.K_b:
                       # self.ballgroup.append(Ball()) # add balls!
                    
                    
                    if event.key == pygame.K_UP:
                        self.lastdir = "up"
                        if self.mapdy + self.delta > 60:
                        #    delta = 60 - self.mapdy
                            pass
                        else:
                            delta = self.delta

                        tile2go= level1[self.fy-1][self.fx]

                        if tile2go in "#f":
                            print("illegal move")
                        else:
                            self.mapdy += delta

                            self.fy -= 1
                            self.movemonsters(0,delta) 
                            for f in self.flygroup:
                                f.y += delta

                        print(self.mapdx, self.mapdy)
                    if event.key == pygame.K_DOWN:
                        self.lastdir = "down"
                        if self.mapdy - self.delta < -390:
                        #    delta = -390 - self.mapdy
                            pass
                        else:
                            delta = self.delta

                        tile2go = level1[self.fy+1][self.fx]
                        if tile2go in "#f":
                            print("illegal move")
                        else:                        
                            self.fy += 1

                            self.mapdy -= delta
                            self.movemonsters(0,-delta)
                            for f in self.flygroup:
                                f.y -= delta
                        
                        print(self.mapdx, self.mapdy)
                    if event.key == pygame.K_RIGHT:
                        self.lastdir = "right"
                        if self.mapdx - self.delta < -690:
                        #    delta = -690 - self.mapdx
                            pass
                        else:
                            delta = self.delta

                        tile2go = level1[self.fy][self.fx+1]
                        if tile2go in "#f":
                            print("illegal move")
                        else:
                            self.fx += 1

                            self.mapdx -= delta
                            self.movemonsters(-delta,0)
                            for f in self.flygroup:
                                f.x -= delta
                            
                        
                        print(self.mapdx, self.mapdy)
                    if event.key == pygame.K_LEFT:
                        self.lastdir = "left"
                        if self.mapdx + self.delta > 240:
                        #    delta = 240 - self.mapdx
                            pass
                        else:
                            delta = self.delta
                        tile2go= level1[self.fy][self.fx-1]
                        if tile2go in "#fw":
                            print("illegal move")
                        else:
                            self.fx-=1

                            self.mapdx += delta
                            self.movemonsters(delta,0)
                            for f in self.flygroup:
                                f.x += delta
                        
                        print(self.mapdx, self.mapdy)
            # feuerpfeil schütze            
            if random.random() < 0.5:
                 FlyingObject(self.feuerpfeil_süd, 
                              self.monster1.x+30, self.monster1.y+30, 0, 100, damage = 2)  
            if random.random() < 0.1:
                bild = random.choice((self.eispfeil_süd, self.eispfeil_nord, self.eispfeil_ost, self.eispfeil_west))
                if bild == self.eispfeil_süd:
                    dx = random.randint(-10,10)
                    dy = random.randint(50,100)
                    FlyingObject(bild, self.monster2.x+50, self.monster2.y+30, dx, dy, damage = 3)
                if bild == self.eispfeil_nord:
                    dx = random.randint(-10,10)
                    dy = random.randint(-100,-50)
                    FlyingObject(bild, self.monster2.x+50, self.monster2.y+30, dx, dy, damage = 4)                                     
                if bild == self.eispfeil_ost:
                    dx = random.randint(50,100)
                    dy = random.randint(-10,10)
                    FlyingObject(bild, self.monster2.x+50, self.monster2.y+30, dx, dy, damage = 5)
                if bild == self.eispfeil_west:
                    dx = random.randint(-100,-50)
                    dy = random.randint(-10,10)
                    FlyingObject(bild, self.monster2.x+50, self.monster2.y+30, dx, dy, damage = 6)
            
            # end of event handler
            milliseconds = self.clock.tick(self.fps) #
            seconds = milliseconds / 1000
            self.playtime += seconds
            # delete everything on screen
            self.screen.blit(self.background, (self.mapdx, self.mapdy)) 
            # write text below sprites
            # write(self.screen, "FPS: {:6.3}  PLAYTIME: {:6.3} SECONDS".format(
            #               self.clock.get_fps(), self.playtime))
            # not-pygame-sprites
            #for myball in self.ballgroup:
            #    myball.update(seconds)
            #for myball in self.ballgroup:
            #    myball.blit(self.screen)
            #---------- collision detection-----------------
            for p in self.playergroup:
                #print(p.hitpoints)
                crashgroup = pygame.sprite.spritecollide(p, self.flygroup, False)
                for arrow in crashgroup:
                    print("arrow", arrow.damage)
                    p.hitpoints -= arrow.damage
                    arrow.kill()
            
            
            #-----------bliting------------
            for p in self.playergroup:
                p.blit(self.screen)
            for m in self.monstergroup:
                m.blit(self.screen)
            
                
            # write text over everything 
            # write(self.screen, "Press b to add another ball", x=self.width//2, y=250, center=True)
            # next frame
            self.allgroup.update(seconds)
            self.allgroup.draw(self.screen)
            pygame.display.flip()
            
        pygame.quit()


if __name__ == '__main__':
    PygView().run()

