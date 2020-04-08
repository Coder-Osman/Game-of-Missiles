import pygame, random, win32api, win32con, time, threading, os
def canuse (num) :
    mistime[num] = realtime[num]
    for for1 in range (realtime [num]) :
        time.sleep(1)
        mistime [num] -= 1
    canusemis [num] = True
def owncanuse(number, rnum, rtime):
    canuse(number)
    restricttime[rnum] = rtime
    for delll in range(rtime):
        time.sleep(1)
        restricttime[rnum] -= 1
    canusemis[number] = False
def set_font (font, color, text, pos, size) :
    my_font = pygame.font.Font(font, size)
    time_surf = my_font.render(text, 1, color)
    gor = time_surf.get_rect()
    gor.center = pos
    screen.blit(time_surf, gor)
    # screen.unlock ()
def set_font2 (font, color, text, pos, size) :
    my_font = pygame.font.Font(font, size)
    time_surf = my_font.render(text, 1, color)
    screen.blit(time_surf, pos)
    # screen.unlock ()
def set_font3 (font, color, text, pos, size) :
    my_font = pygame.font.Font(font, size)
    time_surf = my_font.render(text, 1, color)
    gor = time_surf.get_rect()
    gor.right, gor.top = pos
    screen.blit(time_surf, gor)
    # screen.unlock ()
def getmis (file, size = (0, 0), rotate = 0) :
    temp = pygame.image.load("素材\\missile" + file + ".png")
    if size != (0, 0) :
        temp = pygame.transform.scale(temp, size)
    if rotate != 0:
        temp = pygame.transform.rotate(temp, rotate)
    return temp
class Missile (pygame.sprite.Sprite) :
    def __init__(self, image):
        # lock.acquire ()
        self.image = image
        self.rect = image.get_rect ()
        # lock.release ()
class Missile1 (Missile) :
    def __init__(self):
        Missile.__init__(self, missile1)
    def attack (self, attacker, num, size) : # 攻方
        global mis, explode, luigi, mario
        if attacker : # 1 : 马里奥
            mario.start [0] = True
            # lock.acquire ()
            self.rect.top, self.rect.centerx = 0, luigi.rect.centerx
            # lock.release ()
            while not pygame.sprite.collide_rect (luigi, self) and self.rect.bottom < height:
                # lock.acquire ()
                self.rect.top += 50
                # lock.release ()
                time.sleep(0.1)
            if pygame.sprite.collide_rect(luigi, self) :
                explodeSound.play()
                cenbefore = self.rect.centerx
                # lock.acquire ()
                self.image = pygame.transform.scale(explode, (size * 2, size * 2))
                self.rect = self.image.get_rect()
                self.rect.centery, self.rect.centerx = luigi.rect.top, cenbefore
                # lock.release ()
                time.sleep(0.5)
                luigi.blood -= 5
        else : # 0 路易基
            luigi.start [0] = True
            # lock.acquire ()
            self.rect.top, self.rect.centerx = 0, mario.rect.centerx
            # lock.release ()
            while not pygame.sprite.collide_rect (mario, self) and self.rect.bottom < height:
                # lock.acquire ()
                self.rect.top += 50
                # lock.release ()
                time.sleep(0.1)
            if pygame.sprite.collide_rect(mario, self) :
                explodeSound.play()
                cenbefore = self.rect.centerx
                # lock.acquire ()
                self.image = pygame.transform.scale(explode, (size * 2, size * 2))
                self.rect = self.image.get_rect()
                self.rect.centery, self.rect.centerx = mario.rect.top, cenbefore
                # lock.release ()
                time.sleep(0.5)
                mario.blood -= 5
        mis [num] = None
class Missile2 (Missile):
    def __init__(self):
        Missile.__init__(self, missile2)

    def attack (self, attacker, num, size) : # 攻方
        global mis, explode, luigi, mario
        if attacker : # 1 : 马里奥
            mario.start[1] = True
            if luigi.rect.centerx < mario.rect.centerx :
                self.image = pygame.transform.rotate(self.image, 180)
                # lock.acquire ()
                self.rect.top, self.rect.left = luigi.rect.top, mario.rect.left
                # lock.release ()
                while not pygame.sprite.collide_rect(luigi, self) and self.rect.right > 0:
                    # lock.acquire ()
                    self.rect.right -= 10
                    # lock.release ()
                    time.sleep(0.1)
            else :
                # lock.acquire ()
                self.rect.top, self.rect.left = luigi.rect.top, mario.rect.left
                # lock.release ()
                while not pygame.sprite.collide_rect(luigi, self) and self.rect.left < width:
                    # lock.acquire ()
                    self.rect.right += 10
                    # lock.release ()
                    time.sleep(0.1)
            if pygame.sprite.collide_rect(luigi, self):
                luigi.blood -= 20
                # lock.acquire ()
                explode2Sound.play()
                self.image = pygame.transform.scale(explode, (size * 3, size * 3))
                self.rect = self.image.get_rect()
                self.rect.centerx = luigi.rect.centerx
                self.rect.centery = luigi.rect.centery
                # lock.release ()
                time.sleep(1)
        else : # 0 路易基
            luigi.start[1] = True
            if luigi.rect.centerx > mario.rect.centerx:
                self.image = pygame.transform.rotate(self.image, 180)
                # lock.acquire ()
                self.rect.top, self.rect.left = mario.rect.top, luigi.rect.left
                # lock.release ()
                while not pygame.sprite.collide_rect(mario, self) and self.rect.right > 0:
                    # lock.acquire ()
                    self.rect.right -= 10
                    # lock.release ()
                    time.sleep(0.1)
            else :
                luigi.start[1] = True
                # lock.acquire ()
                self.rect.top, self.rect.left = mario.rect.top, luigi.rect.left
                # lock.release ()
                while not pygame.sprite.collide_rect(mario, self) and self.rect.left < width:
                    # lock.acquire ()
                    self.rect.right += 10
                    # lock.release ()
                    time.sleep(0.1)
            if pygame.sprite.collide_rect(mario, self):
                mario.blood -= 20
                # lock.acquire ()
                explode2Sound.play()
                self.image = pygame.transform.scale(explode, (size * 3, size * 3))
                self.rect = self.image.get_rect()
                self.rect.centery = mario.rect.centery
                self.rect.centerx = mario.rect.centerx
                # lock.release ()
                time.sleep(1)
        mis [num] = None
class Missile3 (Missile):
    def __init__(self):
        Missile.__init__(self, missile3 [0])
        self.stop = False
    def attack (self, attacker, num) :
        global mis, luigi, mario, lstuck, mstuck
        if attacker:  # 1 : 马里奥
            self.rect.centerx, self.rect.centery = luigi.rect.centerx, luigi.rect.centery
            lstuck = True
            mario.start[2] = True
            while self.rect.top >= 50:
                # lock.acquire ()
                self.rect.top -= 30
                # lock.release ()
                luigi.rect.top -= 30
                time.sleep(0.1)
            time.sleep (5)
            lstuck = False
        else:  # 0 路易基
            self.rect.centerx, self.rect.centery = mario.rect.centerx, mario.rect.centery
            mstuck = True
            luigi.start[2] = True
            while self.rect.top >= 50:
                # lock.acquire ()
                self.rect.top -= 30
                # lock.release ()
                mario.rect.top -= 30
                time.sleep(0.1)
            time.sleep(5)
            mstuck = False
        self.stop = True
        mis[num] = None
    def change_img (self) :
        global mstuck, lstuck
        while not self.stop :
            for im in missile3 :
                # lock.acquire ()
                centrexbefore, centreybefore = self.rect.centerx, self.rect.centery
                self.image = im
                self.rect = self.image.get_rect ()
                self.rect.centerx, self.rect.centery = centrexbefore, centreybefore
                # lock.release ()
                time.sleep(0.1)
class Missile4 (Missile) :
    def __init__(self):
        Missile.__init__(self, missile4)
    def attack (self, attacker, num) :
        global mis, explode, luigi, mario
        if attacker :  # 1 : 马里奥
            explode4Sound.play()
            mario.start [3] = True
            tp = luigi.rect.top
            wid1 = 0.5
            mc = False
            lc = False
            while wid1 * 2 <= width :
                wid1 *= 2
                wid1 = int (wid1)
                # lock.acquire()
                self.image = pygame.transform.scale(self.image, (wid1, int(width / 9)))
                self.rect = self.image.get_rect()
                self.rect.left, self.rect.top = 0, tp
                if pygame.sprite.collide_rect (mario, self) :
                    if not mc :
                        mc = True
                        mario.blood -= 30
                if pygame.sprite.collide_rect (luigi, self) :
                    if not lc :
                        lc = True
                        luigi.blood -= 50
                # lock.release()
                time.sleep(0.05)
            # lock.acquire ()
            self.image = pygame.transform.scale(self.image, (width, int(width / 9)))
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = 0, tp
            if pygame.sprite.collide_rect(mario, self):
                if not mc:
                    mc = True
                    mario.blood -= 30
            if pygame.sprite.collide_rect(luigi, self):
                if not lc:
                    lc = True
                    luigi.blood -= 50
            # lock.release()
            time.sleep (1)
            # lock.acquire ()
            if pygame.sprite.collide_rect(mario, self):
                if not mc:
                    mc = True
                    mario.blood -= 30
            if pygame.sprite.collide_rect(luigi, self):
                if not lc:
                    lc = True
                    luigi.blood -= 50
            # lock.release ()
        else :  # 0 路易基
            explode4Sound.play()
            luigi.start[3] = True
            wid1 = 0.5
            mc = False
            lc = False
            tp = mario.rect.top
            while wid1 * 2 <= width:
                wid1 *= 2
                wid1 = int(wid1)
                # lock.acquire()
                self.image = pygame.transform.scale(self.image, (wid1, int(width / 9)))
                self.rect = self.image.get_rect()
                self.rect.left, self.rect.top = 0, tp
                if pygame.sprite.collide_rect(mario, self):
                    if not mc:
                        mc = True
                        mario.blood -= 50
                if pygame.sprite.collide_rect(luigi, self):
                    if not lc:
                        lc = True
                        luigi.blood -= 30
                # lock.release()
                time.sleep(0.05)
            # lock.acquire()
            self.image = pygame.transform.scale(self.image, (width, int(width / 9)))
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = 0, tp
            if pygame.sprite.collide_rect(mario, self):
                if not mc:
                    mc = True
                    mario.blood -= 50
            if pygame.sprite.collide_rect(luigi, self):
                if not lc:
                    lc = True
                    luigi.blood -= 30
            # lock.release()
            time.sleep(1)
            # lock.acquire ()
            if pygame.sprite.collide_rect(mario, self):
                if not mc:
                    mc = True
                    mario.blood -= 50
            if pygame.sprite.collide_rect(luigi, self):
                if not lc:
                    lc = True
                    luigi.blood -= 30
            # lock.release ()
        mis[num] = None
class Missile5 (Missile) :
    def __init__(self):
        Missile.__init__(self, missile5)
    def attack (self, attacker, num) :
        global mis, explode2, luigi, mario
        if attacker :  # 1 : 马里奥
            mario.start [4] = True
            lll2 = luigi.rect.centery
            xd1 = luigi.rect.centerx - mario.rect.centerx
            yd1 = luigi.rect.bottom - mario.rect.bottom
            incx = 100 / (1 + abs(yd1) / abs(xd1))
            incy = 100 - incx
            bottom1 = 1
            widx1 = 1
            if xd1 < 0 :
                widx1 = - 1
            if yd1 < 0 :
                bottom1 = - 1
            incx *= widx1
            incy *= bottom1
            nowx1 = mario.rect.centerx
            nowy1 = mario.rect.bottom
            # lock.acquire ()
            self.rect.centerx, self.rect.bottom = nowx1, nowy1
            # lock.release ()
            while True :
                if abs (widx1) > abs (xd1) and abs (bottom1) > abs (yd1) : # important
                    break
                widx1 += incx
                bottom1 += incy
                # lock.acquire()
                lasttimex1 = self.rect.centerx
                lasttimey1 = self.rect.bottom
                if abs (widx1) <= abs (xd1) :
                    self.rect.centerx = nowx1 + widx1
                elif abs (widx1 - incx) <= abs (xd1) :
                    self.rect.centerx = nowx1 + xd1
                else:
                    self.rect.centerx = lasttimex1
                if abs (bottom1) <= abs (yd1) :
                    self.rect.bottom = nowy1 + bottom1
                elif abs (bottom1 - incy) <= abs (yd1) :
                    self.rect.bottom = nowy1 + yd1
                else :
                    self.rect.bottom = lasttimey1
                # lock.release()
                time.sleep(0.3)
            # lock.acquire ()
            explode5Sound.play()
            time.sleep(0.3)
            lastcenterx = self.rect.centerx
            lastcentery = self.rect.centery
            self.image = pygame.transform.scale(explode2, (400, 400))
            self.rect = self.image.get_rect ()
            self.rect.centerx, self.rect.centery = lastcenterx, lastcentery
            # lock.release ()
            lc = False
            mc = False
            for delay111 in range (20) :
                if pygame.sprite.collide_rect(mario, self):
                    if not mc:
                        mc = True
                        mario.blood -= 50
                if pygame.sprite.collide_rect(luigi, self):
                    if not lc:
                        lc = True
                        luigi.blood -= 100
                pygame.time.delay(100)
        else :  # 0 路易基
            luigi.start[4] = True
            lll2 = mario.rect.centery
            xd1 = mario.rect.centerx - luigi.rect.centerx + 100
            yd1 = mario.rect.bottom - luigi.rect.bottom
            incx = 100 / (1 + abs(yd1) / abs(xd1))
            incy = 100 - incx
            bottom1 = 1
            widx1 = 1
            if xd1 < 0:
                widx1 = - 1
            if yd1 < 0:
                bottom1 = - 1
            incx *= widx1
            incy *= bottom1
            nowx1 = luigi.rect.centerx
            nowy1 = luigi.rect.bottom
            # lock.acquire ()
            self.rect.centerx, self.rect.bottom = nowx1, nowy1
            # lock.release ()
            while True:
                if abs(widx1) > abs(xd1) and abs(bottom1) > abs(yd1):  # important
                    break
                widx1 += incx
                bottom1 += incy
                # lock.acquire()
                lasttimex1 = self.rect.centerx
                lasttimey1 = self.rect.bottom
                if abs(widx1) <= abs(xd1):
                    self.rect.centerx = nowx1 + widx1
                elif abs(widx1 - incx) <= abs(xd1):
                    self.rect.centerx = nowx1 + xd1
                else:
                    self.rect.centerx = lasttimex1
                if abs(bottom1) <= abs(yd1):
                    self.rect.bottom = nowy1 + bottom1
                elif abs(bottom1 - incy) <= abs(yd1):
                    self.rect.bottom = nowy1 + yd1
                else:
                    self.rect.bottom = lasttimey1
                # lock.release()
                time.sleep(0.3)
            # lock.acquire()
            explode5Sound.play()
            time.sleep(0.3)
            lastcenterx = self.rect.centerx
            lastcentery = self.rect.centery
            self.image = pygame.transform.scale(explode2, (400, 400))
            self.rect = self.image.get_rect()
            self.rect.centerx, self.rect.centery = lastcenterx, lastcentery
            # lock.release()
            lc = False
            mc = False
            for delay111 in range(20):
                if pygame.sprite.collide_rect(mario, self):
                    if not mc:
                        mc = True
                        mario.blood -= 100
                if pygame.sprite.collide_rect(luigi, self):
                    if not lc:
                        lc = True
                        luigi.blood -= 50
                pygame.time.delay(100)
        mis[num] = None
class Missile6 (Missile) :
    def __init__(self):
        rand = random.randint (0, 2)
        Missile.__init__(self, missile6 [rand])

    def attack (self, attacker, num) :
        global mis, explode, luigi, mario
        explodehere = pygame.transform.scale(explode, (100, 100))
        explode6Sound.play()
        self.rect.right = - 100
        time.sleep(0.5)
        if attacker:  # 1 : 马里奥
            mario.start[5] = True
            self.rect.right = self.rect.top = 0
            while self.rect.left < width :
                self.rect.left += 50
                willbreak = False
                if pygame.sprite.collide_rect(self, mario) :
                    explode6Sound.stop()
                    explodeSound.play()
                    lasttimerect = self.rect
                    lasttimerect.centerx = mario.rect.centerx
                    # lock.acquire ()
                    self.image = explodehere
                    self.rect = lasttimerect
                    # lock.release ()
                    mario.blood -= 5
                    time.sleep(0.2)
                    willbreak = True

                if pygame.sprite.collide_rect(self, luigi) :
                    explode6Sound.stop()
                    explodeSound.play()
                    lasttimerect = self.rect
                    lasttimerect.centerx = luigi.rect.centerx
                    # lock.acquire ()
                    self.image = explodehere
                    self.rect = lasttimerect
                    # lock.release ()
                    luigi.blood -= 5
                    time.sleep(0.2)
                    willbreak = True
                if willbreak :
                    break
                pygame.time.delay(50)
        else:  # 0 路易基
            luigi.start[5] = True
            self.rect.right = self.rect.top = 0
            while self.rect.left < width :
                self.rect.left += 50
                willbreak = False
                if pygame.sprite.collide_rect(self, mario) :
                    explode6Sound.stop()
                    explodeSound.play()
                    lasttimerect = self.rect
                    lasttimerect.centerx = mario.rect.centerx
                    # lock.acquire ()
                    self.image = explodehere
                    self.rect = lasttimerect
                    # lock.release ()
                    mario.blood -= 5
                    time.sleep(0.2)
                    willbreak = True

                if pygame.sprite.collide_rect(self, luigi) :
                    explode6Sound.stop()
                    explodeSound.play()
                    lasttimerect = self.rect
                    lasttimerect.centerx = luigi.rect.centerx
                    # lock.acquire ()
                    self.image = explodehere
                    self.rect = lasttimerect
                    # lock.release ()
                    luigi.blood -= 5
                    time.sleep(0.2)
                    willbreak = True
                if willbreak :
                    break
                pygame.time.delay(50)
        mis[num] = None
class Missile7 (Missile) :
    def __init__(self):
        Missile.__init__(self, missile7)

    def attack (self, attacker, num) :
        global mis, explode3, luigi, mario
        if attacker:  # 1 : 马里奥
            mario.start[6] = True
            if mis [10] is None :
                mis[num] = None
                return
            self.rect.top, self.rect.centerx = mis [10].rect.bottom, mis [10].rect.centerx
            mdb = False
            ldb = False
            while self.rect.bottom < height :
                if pygame.sprite.collide_mask(self, mario) and not mdb:
                    explode7Sound.play()
                    last_llleft1 = self.rect.centerx
                    self.image = explode3
                    self.rect = self.image.get_rect ()
                    self.rect.centerx = last_llleft1
                    self.rect.bottom = mario.rect.bottom
                    mario.blood -= 500
                    mdb = True
                    time.sleep(1)
                    break
                if pygame.sprite.collide_mask(self, luigi) and not ldb:
                    explode7Sound.play()
                    last_llleft1 = self.rect.centerx
                    self.image = explode3
                    self.rect = self.image.get_rect ()
                    self.rect.centerx = last_llleft1
                    self.rect.bottom = luigi.rect.bottom
                    luigi.blood -= 500
                    ldb = True
                    time.sleep(1)
                    break
                self.rect.top += 50
                time.sleep(0.1)
            else :
                explode7Sound.play()
                # lock.acquire ()
                last_llleft1 = self.rect.centerx
                self.image = explode3
                self.rect = self.image.get_rect()
                self.rect.centerx, self.rect.bottom = last_llleft1, height
                # lock.release ()
            # lock.acquire ()
            if pygame.sprite.collide_mask(self, mario) and not mdb:
                mario.blood -= 500
            if pygame.sprite.collide_mask(self, luigi) and not ldb:
                luigi.blood -= 500
            # lock.release ()
            time.sleep(1)
        else:  # 0 路易基
            luigi.start[6] = True
            if mis [11] is None :
                mis[num] = None
                return
            self.rect.top, self.rect.centerx = mis[11].rect.bottom, mis[11].rect.centerx
            mdb = False
            ldb = False
            while self.rect.bottom < height:
                if pygame.sprite.collide_mask(self, mario) and not mdb:
                    explode7Sound.play()
                    last_llleft1 = self.rect.centerx
                    self.image = explode3
                    self.rect = self.image.get_rect()
                    self.rect.centerx = last_llleft1
                    self.rect.bottom = mario.rect.bottom
                    mario.blood -= 500
                    mdb = True
                    time.sleep(1)
                    break
                if pygame.sprite.collide_mask(self, luigi) and not ldb:
                    explode7Sound.play()
                    last_llleft1 = self.rect.centerx
                    self.image = explode3
                    self.rect = self.image.get_rect()
                    self.rect.centerx = last_llleft1
                    self.rect.bottom = luigi.rect.bottom
                    luigi.blood -= 500
                    ldb = True
                    time.sleep(1)
                    break
                self.rect.top += 50
                time.sleep(0.1)
            else:
                explode7Sound.play()
                # lock.acquire ()
                last_llleft1 = self.rect.centerx
                self.image = explode3
                self.rect = self.image.get_rect()
                self.rect.centerx, self.rect.bottom = last_llleft1, height
                # lock.release ()
            # lock.acquire ()
            if pygame.sprite.collide_mask(self, mario) and not mdb:
                mario.blood -= 500
            if pygame.sprite.collide_mask(self, luigi) and not ldb:
                luigi.blood -= 500
            # lock.release ()
            time.sleep(1)
        mis[num] = None
    def wait_time (self) :
        while running :
            ttt = threading.Thread (target=owncanuse, args=(12, 0, 10))
            ttt.start()
            owncanuse(13, 1, 10)
class Missile8 (Missile) :
    def __init__(self):
        self.rand1 = random.randint(0, 9)
        Missile.__init__(self, missile8[self.rand1][0])
        self.stop = False
    def attack (self, attacker, num) :
        global mis, explode3, luigi, mario
        if attacker:  # 1 : 马里奥
            mario.start[7] = True
            self.rect.centerx = mario.rect.centerx
            self.rect.centery = mario.rect.centery
            while True :
                xd1 = self.rect.centerx - luigi.rect.centerx
                yd1 = self.rect.centery - luigi.rect.centery
                incx = 100 / (1 + abs(yd1) / abs(xd1))
                incy = 100 - incx
                incx *= 1 if xd1 > 0 else - 1
                incy *= 1 if yd1 > 0 else - 1
                print (incx, incy)
                print (self.rect.centerx + incx, luigi.rect.centerx)
                print(self.rect.centery + incy, luigi.rect.centery)
                if self.rect.centerx + incx > luigi.rect.centerx and self.rect.centery + incy > luigi.rect.centery :
                    break
                self.rect.centerx -= incx
                self.rect.centery -= incy
                time.sleep(1)
            self.rect.centerx = luigi.rect.centerx
            self.rect.centery = luigi.rect.centery
        else:  # 0 路易基
            luigi.start[7] = True
        mis[num] = None
        self.stop = True
    def change_img (self) :
        while not self.stop :
            for img in missile8[self.rand1]:
                beforetop, beforecenterx = self.rect.top, self.rect.centerx
                self.image = img
                self.rect = self.image.get_rect()
                self.rect.top, self.rect.centerx = beforetop, beforecenterx
                time.sleep(0.1)

    def wait_time (self) :
        while running :
            ttt = threading.Thread (target=owncanuse, args=(14, 2, 10))
            ttt.start()
            owncanuse(15, 3, 10)
class Mario (pygame.sprite.Sprite) :
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mariopic1
        self.blood = 1000
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect ()
        self.start = [False] * (int (kindsofmis / 2))
        self.rect.right, self.rect.bottom = width * 0.2, height

    def check (self) :
        if self.rect.left < 0  :
            self.rect.left = 0
        elif self.rect.right > width :
            self.rect.right = width
        if self.rect.top < 0 :
            self.rect.top = 0
        elif self.rect.bottom > height :
            self.rect.bottom = height
        if self.blood <= 0:
            self.die()

    def die (self) : # luigi Wins
        self.blood = 0
        set_font ("素材\\font.ttf", (0, 255, 0), "Luigi WINs", (width / 2, height / 2), 200)
        run1 = True
        pygame.display.flip()
        while run1 :
            for event2 in pygame.event.get() :
                if event2.type == pygame.KEYDOWN :
                    if event2.key == pygame.K_ESCAPE :
                        run1 = False
                    elif event2.key == pygame.K_RETURN :
                        main ()
        pygame.quit()
        os._exit(0)

    def legend (self) :
        set_font2("素材\\font.ttf", (255, 0, 0), "Mario", (10, 10), 50)
        set_font2("素材\\font.ttf", (255, 0, 0), "Blood: %d" % self.blood, (10, 60), 30)
        set_font2("素材\\font.ttf", (255, 0, 0), "Missile1 waiting: 0s", (10, 90), 20)
        if not self.start [1] :
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile2 waiting: %ds" % 0, (10, 110), 20)
        else :
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile2 waiting: %ds" % mistime[2], (10, 110), 20)
        if not self.start[2]:
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile3 waiting: %ds" % 0, (10, 130), 20)
        else:
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile3 waiting: %ds" % mistime[4], (10, 130), 20)
        if not self.start[3]:
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile4 waiting: %ds" % 0, (10, 150), 20)
        else:
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile4 waiting: %ds" % mistime[6], (10, 150), 20)
        if not self.start[4]:
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile5 waiting: %ds" % 0, (10, 170), 20)
        else:
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile5 waiting: %ds" % mistime[8], (10, 170), 20)
        if not self.start[5]:
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile6 waiting: %ds" % 0, (10, 190), 20)
        else:
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile6 waiting: %ds" % mistime[10], (10, 190), 20)
        if not restricttime [0] :
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile7 waiting: %ds" % mistime[12], (10, 210), 20)
        else :
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile7 waiting: %ds --- %ds" %
                      (mistime[12], restricttime [0]), (10, 210), 20)
        if not restricttime [2] :
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile8 waiting: %ds" % mistime[14], (10, 230), 20)
        else :
            set_font2("素材\\font.ttf", (255, 0, 0), "Missile8 waiting: %ds --- %ds" %
                      (mistime[14], restricttime [2]), (10, 230), 20)
class Luigi (pygame.sprite.Sprite) :
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = luigipic1
        self.blood = 1000
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect ()
        self.start = [False] * (int (kindsofmis / 2))
        self.start [6] = True
        self.rect.right, self.rect.bottom = width * 0.8, height

    def check (self) :
        if self.rect.left < 0  :
            self.rect.left = 0
        elif self.rect.right > width :
            self.rect.right = width
        if self.rect.top < 0 :
            self.rect.top = 0
        elif self.rect.bottom > height :
            self.rect.bottom = height
        if self.blood <= 0:
            self.die()

    def die (self) : # luigi Wins
        self.blood = 0
        set_font ("素材\\font.ttf", (255, 0, 0), "Mario WINs", (width / 2, height / 2), 200)
        run1 = True
        pygame.display.flip()
        while run1:
            for event2 in pygame.event.get():
                if event2.type == pygame.KEYDOWN:
                    if event2.key == pygame.K_ESCAPE :
                        run1 = False
                    elif event2.key == pygame.K_RETURN :
                        main ()
        pygame.quit()
        os._exit(0)

    def legend (self) :
        set_font3("素材\\font.ttf", (0, 255, 0), "Luigi", (width - 10, 10), 50)
        set_font3("素材\\font.ttf", (0, 255, 0), "Blood: %d" % self.blood, (width - 10, 60), 30)
        set_font3("素材\\font.ttf", (0, 255, 0), "Missile1 waiting: 0s", (width -10, 90), 20)
        if not self.start [1] :
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile2 waiting: %ds" % 0, (width -10, 110), 20)
        else :
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile2 waiting: %ds" % mistime[3], (width -10, 110), 20)
        if not self.start[2]:
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile3 waiting: %ds" % 0, (width - 10, 130), 20)
        else:
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile3 waiting: %ds" % mistime[5], (width - 10, 130), 20)
        if not self.start[3]:
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile4 waiting: %ds" % 0, (width - 10, 150), 20)
        else:
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile4 waiting: %ds" % mistime[7], (width - 10, 150), 20)
        if not self.start[4]:
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile5 waiting: %ds" % 0, (width - 10, 170), 20)
        else:
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile5 waiting: %ds" % mistime[9], (width - 10, 170), 20)
        if not self.start[5]:
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile6 waiting: %ds" % 0, (width - 10, 190), 20)
        else:
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile6 waiting: %ds" % mistime[11], (width - 10, 190), 20)
        if not restricttime [1] :
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile7 waiting: %ds" % mistime[13], (width - 10, 210), 20)
        else :
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile7 waiting: %ds --- %ds" %
                      (mistime[13], restricttime [1]), (width - 10, 210), 20)
        if not restricttime [3] :
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile8 waiting: %ds" % mistime[15], (width - 10, 230), 20)
        else :
            set_font3("素材\\font.ttf", (0, 255, 0), "Missile8 waiting: %ds --- %ds" %
                      (mistime[13], restricttime [2]), (width - 10, 230), 20)
def animate () :
    luigi.check()
    mario.check()
    screen.fill ([0, 187, 255])
    if not lstuck :
        luigi.rect.top += 2
    if not mstuck :
        mario.rect.top += 2
    screen.blit(mario.image, mario.rect)
    screen.blit (luigi.image, luigi.rect)
    mario.legend ()
    luigi.legend()
    for i in mis :
        if i is not None :
            if type (i) == type([]) :
                for j in i :
                    # image = j.image
                    screen.blit(j.image, j.rect)
            else :
                # image = i.image
                screen.blit(i.image, i.rect)
    pygame.display.flip()
    pygame.time.delay(20)
def main () :
    global running, mstuck, lstuck, mario, luigi, mis, canusemis, mistime, misss7
    mario = Mario()
    luigi = Luigi()
    mis = [None] * kindsofmis
    mis[14] = mis[15] = []
    canusemis = [True] * kindsofmis
    canusemis[12] = canusemis[13] = False
    mistime = [0] * kindsofmis
    mistime[12] = mistime[13] = 90
    mstuck = lstuck = False
    misss7 = Missile7()
    ttd1 = threading.Thread(target=misss7.wait_time)
    ttd1.start()
    misss8 = Missile8()
    ttd2 = threading.Thread(target=misss8.wait_time)
    ttd2.start()
    while running:
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and not lstuck:
                    luigi.rect.top += 20
                if event.key == pygame.K_UP and not lstuck:
                    luigi.rect.top -= 20
                if event.key == pygame.K_LEFT and not lstuck:
                    luigi.rect.left -= 20
                    last_rect1 = luigi.rect
                    luigi.image = luigipic1
                    luigi.rect = last_rect1
                if event.key == pygame.K_RIGHT and not lstuck:
                    luigi.rect.left += 20
                    last_rect2 = luigi.rect
                    luigi.image = luigipic2
                    luigi.rect = last_rect2
                if event.key == pygame.K_s and not mstuck:
                    mario.rect.top += 20
                if event.key == pygame.K_w and not mstuck:
                    mario.rect.top -= 20
                if event.key == pygame.K_a and not mstuck:
                    mario.rect.left -= 20
                    last_rect3 = mario.rect
                    mario.image = mariopic2
                    mario.rect = last_rect3
                if event.key == pygame.K_d and not mstuck:
                    mario.rect.left += 20
                    last_rect4 = mario.rect
                    mario.image = mariopic1
                    mario.rect = last_rect4

                if event.key == pygame.K_1 and mis[0] is None:  # 马里奥
                    mis[0] = Missile1()
                    td1 = threading.Thread(target=mis[0].attack, args=(1, 0, 11))
                    td1.start()
                if event.key == pygame.K_KP1 and mis[1] is None:  # 路易基
                    mis[1] = Missile1()
                    td2 = threading.Thread(target=mis[1].attack, args=(0, 1, 11))
                    td2.start()
                if event.key == pygame.K_2 and mis[2] is None and canusemis[2]:  # 马里奥
                    mis[2] = Missile2()
                    td3 = threading.Thread(target=mis[2].attack, args=(1, 2, 46))
                    td3.start()
                    canusemis[2] = False
                    tdd1 = threading.Thread(target=canuse, args=(2,))
                    tdd1.start()
                if event.key == pygame.K_KP2 and mis[3] is None and canusemis[3]:  # 路易基
                    mis[3] = Missile2()
                    td4 = threading.Thread(target=mis[3].attack, args=(0, 3, 46))
                    td4.start()
                    canusemis[3] = False
                    tdd2 = threading.Thread(target=canuse, args=(3,))
                    tdd2.start()
                if event.key == pygame.K_3 and mis[4] is None and canusemis[4]:  # 马里奥
                    mis[4] = Missile3()
                    tddd1 = threading.Thread(target=mis[4].change_img)
                    td5 = threading.Thread(target=mis[4].attack, args=(1, 4))
                    tddd1.start()
                    td5.start()
                    canusemis[4] = False
                    tdd3 = threading.Thread(target=canuse, args=(4,))
                    tdd3.start()
                if event.key == pygame.K_KP3 and mis[5] is None and canusemis[5]:  # 路易基
                    mis[5] = Missile3()
                    tddd2 = threading.Thread(target=mis[5].change_img)
                    td6 = threading.Thread(target=mis[5].attack, args=(0, 5))
                    tddd2.start()
                    td6.start()
                    canusemis[5] = False
                    tdd4 = threading.Thread(target=canuse, args=(5,))
                    tdd4.start()
                if event.key == pygame.K_4 and mis[6] is None and canusemis[6]:  # 马里奥
                    mis[6] = Missile4()
                    td7 = threading.Thread(target=mis[6].attack, args=(1, 6))
                    td7.start()
                    canusemis[6] = False
                    tdd5 = threading.Thread(target=canuse, args=(6,))
                    tdd5.start()
                if event.key == pygame.K_KP4 and mis[7] is None and canusemis[7]:  # 路易基
                    mis[7] = Missile4()
                    td8 = threading.Thread(target=mis[7].attack, args=(0, 7))
                    td8.start()
                    canusemis[7] = False
                    tdd6 = threading.Thread(target=canuse, args=(7,))
                    tdd6.start()
                if event.key == pygame.K_5 and mis[8] is None and canusemis[8]:  # 马里奥
                    mis[8] = Missile5()
                    td9 = threading.Thread(target=mis[8].attack, args=(1, 8))
                    td9.start()
                    canusemis[8] = False
                    tdd7 = threading.Thread(target=canuse, args=(8,))
                    tdd7.start()
                if event.key == pygame.K_KP5 and mis[9] is None and canusemis[9]:  # 路易基
                    mis[9] = Missile5()
                    td10 = threading.Thread(target=mis[9].attack, args=(0, 9))
                    td10.start()
                    canusemis[9] = False
                    tdd8 = threading.Thread(target=canuse, args=(9,))
                    tdd8.start()
                if event.key == pygame.K_6 and mis[10] is None and canusemis[10]:  # 马里奥
                    mis[10] = Missile6()
                    td11 = threading.Thread(target=mis[10].attack, args=(1, 10))
                    td11.start()
                    canusemis[10] = False
                    tdd9 = threading.Thread(target=canuse, args=(10,))
                    tdd9.start()
                if event.key == pygame.K_KP6 and mis[11] is None and canusemis[11]:  # 路易基
                    mis[11] = Missile6()
                    td12 = threading.Thread(target=mis[11].attack, args=(0, 11))
                    td12.start()
                    canusemis[11] = False
                    tdd10 = threading.Thread(target=canuse, args=(11,))
                    tdd10.start()
                if event.key == pygame.K_7 and mis[12] is None and canusemis[12] and mis[10] is not None:  # 马里奥
                    mis[12] = Missile7()
                    td13 = threading.Thread(target=mis[12].attack, args=(1, 12))
                    td13.start()
                if event.key == pygame.K_KP7 and mis[13] is None and canusemis[13] and mis[11] is not None:  # 路易基
                    mis[13] = Missile7()
                    td14 = threading.Thread(target=mis[13].attack, args=(0, 13))
                    td14.start()
                """if event.key == pygame.K_8 and canusemis[14]:  # 马里奥
                    mis[14].append(Missile8())
                    tddd3 = threading.Thread(target=mis[14][-1].change_img)
                    td15 = threading.Thread(target=mis[14][-1].attack, args=(1, 14))
                    tddd3.start()
                    td15.start()
                if event.key == pygame.K_KP8 and canusemis[15]:  # 路易基
                    mis[15].append(Missile8())
                    tddd4 = threading.Thread(target=mis[15][-1].change_img)
                    td16 = threading.Thread(target=mis[15][-1].attack, args=(0, 15))
                    tddd4.start()
                    td16.start()"""
        animate()
    pygame.quit()
pygame.init()
pygame.font.init()
pygame.mixer.init()
realtime = [0, 0, 15, 15, 30, 30, 40, 40, 60, 60, 35, 35, 3, 3, 20, 20]
kindsofmis = len(realtime)
mis = [None] * kindsofmis
mis [14] = mis [15] = []
# lock = threading.Lock ()
size = width, height = win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
missile1 = getmis("1", (11, 100), 180)
missile2 = getmis("2", (80, 46), 180)
missile3 = []
missile4 = getmis ("4", (1, int (width / 9)))
missile5 = getmis("5", (200, 200))
missile6 = []
missile7 = getmis("7", (100, 50), 90)
missile8 = []
explode2 = pygame.image.load ("素材\\explode2.png")
explode3 = pygame.image.load ("素材\\explode3.png")
explode3 = pygame.transform.scale(explode3, (500, 500))
explodeSound = pygame.mixer.Sound("素材\\explode.wav")
explode2Sound = pygame.mixer.Sound("素材\\explode2.wav")
explode4Sound = pygame.mixer.Sound("素材\\explode4.wav")
explode5Sound = pygame.mixer.Sound("素材\\explode5.wav")
explode6Sound = pygame.mixer.Sound("素材\\explode6.wav")
explode7Sound = pygame.mixer.Sound("素材\\explode7.wav")
mis3sizelist = [(38, 46), (50, 44), (60, 48), (46, 44)]
mis6sizelist = (100, 100)
for name in range (1, 5) :
    missile3.append(getmis("3\\missile3_%d" % name, mis3sizelist [name - 1]))
for name in range (1, 4) :
    missile6.append(getmis("6\\missile6_%d" % name, mis6sizelist))
for namei in range (1, 11) :
    temp = []
    for namej in range (1, 5) :
        temp.append(getmis("8\\missile8_%d_%d" % (namei, namej)))
    missile8.append(temp)
explode = pygame.image.load ("素材\\explode.png")
mariopic1 = pygame.image.load ("素材\\mario.png")
mariopic1 = pygame.transform.scale(mariopic1, (60, 80))
luigipic1 = pygame.image.load ("素材\\luigi.png")
luigipic1 = pygame.transform.scale(luigipic1, (56, 90))
mariopic2 = pygame.transform.flip(mariopic1, True, False)
luigipic2 = pygame.transform.flip(luigipic1, True, False)
mario = Mario ()
luigi = Luigi ()
canusemis = [True] * kindsofmis
canusemis [12] = canusemis [13] = False
mistime = [0] * kindsofmis
mistime [12] = mistime [13] = 90
mstuck = lstuck = False
screen = pygame.display.set_mode(size, flags=pygame.FULLSCREEN)
restricttime = [0, 0, 0, 0]
running = True
main()
"""
1 : explode.wav
2 : explode2.wav
4 : explode4.wav
5 : explode5.wav
7 : explode7.wav
"""