import pygame, random, time, asyncio
# Variablesw
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Decrypting Cryptids')
critterxowl1,critteryowl1=500, 700
critterxowl2,critteryowl2=500, 700
critterxowl3,critteryowl3=500, 700
critterxbat1,critterybat1=500, 700
critterxbat2,critterybat2=500, 700
critterxbat3,critterybat3=500, 700
async def main():
    global critterymothman,critterxmothman,critterxowl1,critteryowl1,critterxowl2,critteryowl2,critterxowl3,critteryowl3,critterxbat1,critterybat1,critterxbat2,critterybat2,critterxbat3,critterybat3,MothmanSpawned
    Newspaper = pygame.image.load('Newspaper.png')
    game1backround = pygame.image.load('Game1Backround.png')
    game2cutscene = pygame.image.load('Game2Cutscene.png')
    game3cutscene = pygame.image.load('Game3Cutscene.png')
    game3cutscene2 = pygame.image.load('Game3Cutscene2.png')
    game2backround = pygame.image.load('Game2Backround.gif')
    game3backround = pygame.image.load('Game3Maze.png')
    EndFrame = pygame.image.load('EndingFrame.png')
    Dylanleft = pygame.image.load('DylanWalk1.gif')
    Dylanright = pygame.image.load('DylanWalk2.gif')
    Dylanclimb = pygame.image.load('DylanClimb.gif')
    Rope = pygame.image.load('RopeItem.gif')
    Flashlight = pygame.image.load('FlashlightItem.gif')
    Food = pygame.image.load('ChimkinLeg.gif')
    Water = pygame.image.load('WaterBottleItem.gif')
    Lighter = pygame.image.load('LighterItem.gif')
    Camera = pygame.image.load('CameraItem.gif')
    Mothmanleft = pygame.image.load('Mothmanleft.gif')
    OwlLeft = pygame.image.load('owlleft.gif')
    OwlRight = pygame.image.load('owlright.gif')
    BatLeft = pygame.image.load('BatLeft.gif')
    BatRight = pygame.image.load('BatRight.gif')
    Game2Camera = pygame.image.load('Game2Camera.png')
    YouWin = pygame.image.load('YouWin.png')
    TheVoid = pygame.image.load('Darkness.png')
    x=20
    y=411
    numbofpictures = 0
    critterxmothman,critterymothman=500, 700

    Dylanwalk = Dylanleft

    holdingitem=False
    MothmanSpawned = False
    # Player
    def Player(Dylan,x,y):
        screen.blit(game1backround,(0,0))
        screen.blit(Dylan,(x,y))
    def Player3(Dylan,x,y):
        screen.blit(game3backround,(0,0))
        screen.blit(Dylan,(x,y))
        screen.blit(TheVoid,(x-760,y-570))

    def Game2Player(x,y):
        global critterymothman,critterxmothman,critterxowl1,critteryowl1,critterxowl2,critteryowl2,critterxowl3,critteryowl3,critterxbat1,critterybat1,critterxbat2,critterybat2,critterxbat3,critterybat3,MothmanSpawned
        if MothmanSpawned == False:
            critterxmothman = random.randrange(50,600)
            critterymothman = random.randrange(150,400)
            critterxowl1 = random.randrange(50,650)
            critteryowl1 = random.randrange(50,500)
            critterxowl2 = random.randrange(50,650)
            critteryowl2 = random.randrange(50,500)
            critterxowl3 = random.randrange(50,650)
            critteryowl3 = random.randrange(50,500)
            critterxbat1 = random.randrange(50,650)
            critterybat1 = random.randrange(50,500)
            critterxbat2 = random.randrange(50,650)
            critterybat2 = random.randrange(50,500)
            critterxbat3 = random.randrange(50,650)
            critterybat3 = random.randrange(50,500)
            MothmanSpawned=True
        screen.blit(game2backround,(0,0))
        screen.blit(Mothmanleft,(critterxmothman,critterymothman))
        screen.blit(OwlLeft,(critterxowl1,critteryowl1))
        screen.blit(OwlRight,(critterxowl2,critteryowl2))
        screen.blit(OwlRight,(critterxowl3,critteryowl3))
        screen.blit(BatLeft,(critterxbat1,critterybat1))
        screen.blit(BatRight,(critterxbat2,critterybat2))
        screen.blit(BatLeft,(critterxbat3,critterybat3))
        screen.blit(Game2Camera,(x,y))

    # Game 1 List of Items 
    collecteditems = 0
    GameOneItems = [Rope, Flashlight, Food, Water, Lighter, Camera]
    random.shuffle(GameOneItems)
    ItemOne = GameOneItems.pop(0)
    ItemTwo = GameOneItems.pop(0)
    ItemThree = GameOneItems.pop(0)
    ItemFour = GameOneItems.pop(0)
    ItemFive = GameOneItems.pop(0)
    ItemSix = GameOneItems.pop(0)

    # Game
    running = True
    currentgame=0
    
    while running == True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if currentgame == 0:
                screen.blit(Newspaper,(0,0))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        currentgame = 1
            if currentgame==1:
            
                Player(Dylanwalk,x,y)
                if y > 411:
                    y-=20
                if y < 91:
                    y+=20
                if x > 725 or x < 0:
                    if x > 725:
                        x -=10
                    elif x < 0:
                        x +=10
                else:
                    # Movement
                    if event.type == pygame.KEYDOWN:
                        if x > 300 and x < 380:
                            if event.key == pygame.K_w:
                                Dylanwalk=Dylanclimb
                                y-=20
                            elif event.key == pygame.K_s:
                                Dylanwalk=Dylanclimb
                                y+=20
                        if x > 620 and x < 700:
                            if event.key == pygame.K_w:
                                Dylanwalk=Dylanclimb
                                y-=20
                            elif event.key == pygame.K_s:
                                Dylanwalk=Dylanclimb
                                y+=20
                        if event.key == pygame.K_d:
                            print(str(x) + " " + str(y))
                            Dylanwalk=Dylanright
                            x +=20
                            if x < 300 or x > 700:
                                y = 411
                            if x > 340 and x < 640:
                                if y <= 91:
                                    y = 91
                                elif y <= 211:
                                    y = 211
                                elif y <= 331:
                                    y = 331
                                else:
                                    y = 411
                        elif event.key == pygame.K_a:
                            print(str(x) + " " + str(y))
                            Dylanwalk=Dylanleft
                            x -=20
                            if x < 300 or x > 700:
                                y = 411
                            if x > 340 and x < 640:
                                if y <= 91:
                                    y = 91
                                elif y <= 211:
                                    y = 211
                                elif y <= 331:
                                    y = 331
                                else:
                                    y = 411
                        if event.key == pygame.K_SPACE:
                            if holdingitem == False:
                                if collecteditems == 0 and x >= 450 and x <=470 and y >= 330 and y <=332:
                                    screen.blit(ItemOne,(x,y-80))
                                    holdingitem=True
                                    collecteditems=1
                                elif collecteditems == 1 and x >= 530 and x <=550 and y >= 330 and y <=332:
                                    screen.blit(ItemTwo,(x,y-80))
                                    holdingitem=True
                                    collecteditems=2
                                elif collecteditems == 2 and x >= 450 and x <=470 and y >= 210 and y <=212:
                                    screen.blit(ItemThree,(x,y-80))
                                    holdingitem=True
                                    collecteditems=3
                                elif collecteditems == 3 and x >= 530 and x <=550 and y >= 210 and y <=212:
                                    screen.blit(ItemFour,(x,y-80))
                                    holdingitem=True
                                    collecteditems=4
                                elif collecteditems == 4 and x >= 450 and x <=470 and y >= 90 and y <=92:
                                    screen.blit(ItemFive,(x,y-80))
                                    holdingitem=True
                                    collecteditems=5
                                elif collecteditems == 5 and x >= 530 and x <=550 and y >= 90 and y <=92:
                                    collecteditems=6
                                    holdingitem=True
                                    screen.blit(ItemSix,(x,y-80))
                            if holdingitem == True:
                                if x <= 240 and x >= 20:
                                    holdingitem = False
                                    if collecteditems == 6:
                                        youwintimer=True
                                        holdingitem=True
                                        currentgame = 2
                                        x = 160
                                        y = 30
                if holdingitem == True:
                    if collecteditems == 1:
                        screen.blit(ItemOne,(x,y-80))
                    if collecteditems == 2:
                        screen.blit(ItemTwo,(x,y-80))
                    if collecteditems == 3:
                        screen.blit(ItemThree,(x,y-80))
                    if collecteditems == 4:
                        screen.blit(ItemFour,(x,y-80))
                    if collecteditems == 5:
                        screen.blit(ItemFive,(x,y-80))
                    if collecteditems == 6:
                        screen.blit(ItemSix,(x,y-80))

                if collecteditems == 0:
                    screen.blit(ItemOne,(20,40))
                    screen.blit(ItemOne,(460,331))
                    screen.blit(ItemTwo,(540,331))
                    screen.blit(ItemThree,(460,211))
                    screen.blit(ItemFour,(540,211))
                    screen.blit(ItemFive,(460,91))
                    screen.blit(ItemSix ,(540,91))
                elif collecteditems == 1:
                    screen.blit(ItemTwo,(20,40))
                    screen.blit(ItemTwo,(540,331))
                    screen.blit(ItemThree,(460,211))
                    screen.blit(ItemFour,(540,211))
                    screen.blit(ItemFive,(460,91))
                    screen.blit(ItemSix ,(540,91))
                elif collecteditems == 2:
                    screen.blit(ItemThree,(20,40))
                    screen.blit(ItemThree,(460,211))
                    screen.blit(ItemFour,(540,211))
                    screen.blit(ItemFive,(460,91))
                    screen.blit(ItemSix ,(540,91))
                elif collecteditems == 3:
                    screen.blit(ItemFour,(20,40))
                    screen.blit(ItemFour,(540,211))
                    screen.blit(ItemFive,(460,91))
                    screen.blit(ItemSix ,(540,91))
                elif collecteditems == 4:
                    screen.blit(ItemFive,(20,40))
                    screen.blit(ItemFive,(460,91))
                    screen.blit(ItemSix ,(540,91))
                elif collecteditems == 5:
                    screen.blit(ItemSix,(20,40))
                    screen.blit(ItemSix ,(540,91))
                    
            if currentgame == 2:
                if youwintimer == True:
                    start_ticks=pygame.time.get_ticks()
                    youwintimer = False
                screen.blit(game2cutscene,(0,0))
                seconds=(pygame.time.get_ticks()-start_ticks)/1000
                if seconds>3:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            currentgame = 3

            if currentgame == 3:
                Game2Player(x,y)
                while y > 230:
                    y-=20
                while y < -120:
                    y+=20
                if x > 340 or x < -60:
                    while x > 340:
                        x -=10
                    while x < -60:
                        x +=10
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        print(str(x) + " " + str(y))
                        x += 40
                    elif event.key == pygame.K_a:
                        print(str(x) + " " + str(y))
                        x -= 40
                    elif event.key == pygame.K_w:
                        print(str(x) + " " + str(y))
                        y -= 40
                    elif event.key == pygame.K_s:
                        print(str(x) + " " + str(y))
                        y += 40
                    elif event.key == pygame.K_SPACE:
                        if x <= critterxmothman and x +280 >= critterxmothman and y+240 >= critterymothman and y+100 <= critterymothman:
                            numbofpictures+=1
                            MothmanSpawned = False
                        else:
                            numbofpictures-=1
                            if numbofpictures <=0:
                                numbofpictures = 0
                            MothmanSpawned = False
                if numbofpictures >=4:
                    currentgame=4
                    youwintimer=True
                    Dylanwalk = pygame.image.load('MiniDylanLeft.gif')
                    x = 40
                    y = 11

            if currentgame == 4:
                if youwintimer == True:
                    start_ticks=pygame.time.get_ticks()
                    youwintimer = False
                screen.blit(game3cutscene,(0,0))
                seconds=(pygame.time.get_ticks()-start_ticks)/1000
                if seconds>3:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            currentgame = 5
                            youwintimer=True
            if currentgame == 5:
                if youwintimer == True:
                    start_ticks=pygame.time.get_ticks()
                    youwintimer = False
                screen.blit(game3cutscene2,(0,0))
                seconds=(pygame.time.get_ticks()-start_ticks)/1000
                if seconds>3:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            currentgame = 6

            if currentgame==6:
                Dylanleft = pygame.image.load('MiniDylanLeft.gif')
                Dylanright = pygame.image.load('MiniDylanRight.gif')
                Player3(Dylanwalk,x,y)
                while y > 500:
                    x = 40
                    y = 11
                while y < -120:
                    y+=20
                if x > 760 or x < 0:
                    while x > 700:
                        youwintimer=True
                        currentgame = 7
                        x -=10
                    while x < 0:
                        x = 40
                        y = 11


                if x >=600:
                    if y >=391 and y <=431:
                        PLACEHOLDeR = True
                    else:
                        x=40
                        y=11
                elif x >=420 and x <=540 and y >=251:
                    if y >=291 and y <=411:
                        if y >=371:
                            if x >=500 and x <=520:
                                x=40
                                y=11
                    if y <=291:
                        x=40
                        y=11
                elif x >=540 and x <=580:
                    if y <=71 or y >=451:
                        x=40
                        y=11
                elif x >=320 and x <=360:
                    if y <=231:
                        if y <= -9 or y >= 171:
                            x=40
                            y=11
                    elif y >=411:
                        x=40
                        y=11
                elif x > 80:
                    if x > 180:
                        if y >=411 or y <=71:
                            x=40 
                            y=11
                        if x >=240:
                            if y <= 231:
                                if y>=91 and y <= 151:
                                    PLACEHOLDeR = True
                                else:
                                    x=40
                                    y=11
                            else:
                                if y>=351 and y <= 391:
                                    PLACEHOLDeR = True
                                else:
                                    x=40
                                    y=11
                    elif y <= 221 or y >= 281:
                        x = 40
                        y = 11
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        print(str(x) + " " + str(y))
                        x += 20
                        Dylanwalk=Dylanright
                    elif event.key == pygame.K_a:
                        print(str(x) + " " + str(y))
                        x -= 20
                        Dylanwalk=Dylanleft
                    elif event.key == pygame.K_w:
                        print(str(x) + " " + str(y))
                        y -= 20
                    elif event.key == pygame.K_s:
                        print(str(x) + " " + str(y))
                        y += 20
            if currentgame == 7:
                if youwintimer == True:
                    start_ticks=pygame.time.get_ticks()
                    youwintimer = False
                screen.blit(EndFrame,(0,0))
                seconds=(pygame.time.get_ticks()-start_ticks)/1000
                if seconds>1.5:
                    screen.blit(YouWin,(0,0))
            pygame.display.flip()
            await asyncio.sleep(0)
asyncio.run(main())

# Nice