import spritesheet #Import spritesheet
from sprite_strip_anim import SpriteStripAnim #Import sprite_strip_anim.py and SpriteStripAnim class
import math
import pygame
import random 

def shardsofstan():
 
    lstInventory = []
    chestlst = []
    blnAttack = False    
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init() #Initialize pygame
    chest = pygame.mixer.Sound('data/chest.ogg')
    stab = pygame.mixer.Sound('data/stab.ogg')
    potion = pygame.mixer.Sound('data/potion.ogg')
    rollover = pygame.mixer.Sound('data/rollover.ogg')
    pygame.mixer.music.load('data/bgmspawn.mp3')
    pygame.mixer.music.play(-1, 0.0)
    spawnpoint = "s"
    screen=pygame.display.set_mode((1280,992)) #Create game screen, size 1280 pixels by 992 pixels
    screenrect = screen.get_rect() #Get the rectangular size of the screen
    background = pygame.Surface((screen.get_size())) #Get dimension of screen
    backgroundrect = background.get_rect() #Get the rectangular area of the background
    background.fill((255,255,255)) #Fill background with white
    background = background.convert() #Convert background surface format to display format
    background0 = background.copy()
    screen.blit(background,(0,0)) #Draw background onto screen
    FPS = 4
    frames = 4
    intGlobalChestAmount = 2  
    grid = SpriteStripAnim('data/spritesheetfront.png', (0,0,19,32), 4, 1, True, frames) 
    mainChar = grid.next()     
    slime = SpriteStripAnim('data/spritesheetslime.png', (0,0,22,32), 4, 1, True, frames)
    mainCharleft = SpriteStripAnim('data/spritesheetleft.png', (0,0,14,32), 4, 1, True, frames)
    mainCharback = SpriteStripAnim('data/spritesheetback.png', (0,0,19,32), 4, 1, True, frames)
    mainCharright = SpriteStripAnim('data/spritesheetright.png', (0,0,14,32), 4, 1, True, frames)    
    maincharsurface = pygame.Rect(0, 0, 19, 32)
    hp = pygame.image.load('data/hp.png')
    signabyss = pygame.image.load('data/signabyss.png')
    signforest = pygame.image.load('data/signforest.png')
    signtundra = pygame.image.load('data/signtundra.png')
    signvalley = pygame.image.load('data/signvalley.png')
    inventoryone = pygame.image.load('data/hotbarone.png')
    inventorytwo = pygame.image.load('data/hotbartwo.png')
    inventorythree = pygame.image.load('data/hotbarthree.png')
    inventoryfour = pygame.image.load('data/hotbarfour.png')
    inventoryfive = pygame.image.load('data/hotbarfive.png')    
    inventoryoneH = pygame.image.load('data/hotbaroneactive.png')
    inventorytwoH = pygame.image.load('data/hotbartwoactive.png')
    inventorythreeH = pygame.image.load('data/hotbarthreeactive.png')
    inventoryfourH = pygame.image.load('data/hotbarfouractive.png')
    inventoryfiveH = pygame.image.load('data/hotbarfiveactive.png')
    intHealth = 100
    lstInven = [(574,967),(604,967),(634,967),(664,967),(694,967)]
    lstInvenHighlight = [(565,960),(595,960),(623,960),(653,960),(684,960)]
    lstEnemies=[]
    lstEnemyLocationX=[]
    lstEnemyLocationY=[]
    intEnemies = 0
    intEnemy2 = 0
    dx = 0 #Movement x-axis of mainchar
    dy = 0 #Movement y-axis of mainchar
 
    spawn =      ["xxxxxxxxxxxxxxxxxxxxxnxxxxxxxxxxxxxxxxxxxxx",
                  "x....................q....................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "w....................s...................qz",
                  "x.........................................x",
                  "x.........................................x",
                  "x..................ccccc..................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "xxxxxxxxxxxxxxxxxxxxxmxxxxxxxxxxxxxxxxxxxxx",
                  "hhhhhhhhhhhhhhhhhhh12345hhhhhhhhhhhhhhhhhhh"]

    forestone =  ["xxxxxxxxxxxxxxxxxxxxxnxxxxxxxxxxxxxxxxxxxxx",
                  "x....................q....................x",
                  "x.........................................x",
                  "x...................c.c...................x",
                  "x.........................................x",
                  "x...................^.^...................x",
                  "x.........................................x",
                  "x...................^.^...................x",
                  "x.........................................x",
                  "x...................^.^...................x",
                  "x.........................................x",
                  "x...................^.^...................x",
                  "x.........................................x",
                  "x...................^.^...................x",
                  "x.........................................x",
                  "x...................^.^...................x",
                  "x.........................................x",
                  "x...................^.^...................x",
                  "x.........................................x",
                  "x...................^.^...................x",
                  "x.........................................x",
                  "x...................^.^...................x",
                  "x.........................................x",
                  "x...................^.^...................x",
                  "x.........................................x",
                  "x...................^.^...................x",
                  "x.........................................x",
                  "x...................^.^...................x",
                  "x....................s....................x",
                  "xxxxxxxxxxxxxxxxxxxxxpxxxxxxxxxxxxxxxxxxxxx",
                  "hhhhhhhhhhhhhhhhhhh12345hhhhhhhhhhhhhhhhhhh"]

    foresttwo =  ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "x....................q....................x",
                  "x.........................................x",
                  "x....................c....................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x....................s....................x",
                  "xxxxxxxxxxxxxxxxxxxxxpxxxxxxxxxxxxxxxxxxxxx",
                  "hhhhhhhhhhhhhhhhhhh12345hhhhhhhhhhhhhhhhhhh"]

    snowone =    ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "nq.......................................sp",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "hhhhhhhhhhhhhhhhhhh12345hhhhhhhhhhhhhhhhhhh"]

    snowtwo =    ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.....................c..................sp",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "hhhhhhhhhhhhhhhhhhh12345hhhhhhhhhhhhhhhhhhh"]

    valleyone =  ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "ps.......................................qn",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x....................c....................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "hhhhhhhhhhhhhhhhhhh12345hhhhhhhhhhhhhhhhhhh"]

    valleytwo =  ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "ps........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "hhhhhhhhhhhhhhhhhhh12345hhhhhhhhhhhhhhhhhhh"]
    
    abysstwo    = ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "ps........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "hhhhhhhhhhhhhhhhhhh12345hhhhhhhhhhhhhhhhhhh"]

    abyssone =      ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "ps........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "x.........................................x",
                  "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "hhhhhhhhhhhhhhhhhhh12345hhhhhhhhhhhhhhhhhhh"]
    

    
    def createblock(length, height, color):
        tmpblock = pygame.Surface((length, height))
        tmpblock.fill(color)
        tmpblock.convert()
        return tmpblock
 
    def addlevel(level,spawnpoint):
        """This function read the layout of the level dictionary
           and blits it on to the screen.
           Re-calculate and return variables like block, height etc.
           usage: length, height, block, goal, maincharx, mainchary, background = addlevel(newlevel)
        """
 
        lines = len(level)
        columns = len(level[0])
 
        length = screenrect.width / columns
        height = screenrect.height / lines
        obsidian = pygame.image.load('data/obsidian.png')
        mountaintxt = pygame.image.load('data/obsidian.png')
        nextblock = createblock(length, height,(255,49,49))
        grass = pygame.image.load('data/grass.png')
        snow = pygame.image.load('data/snow.png')
        valley = pygame.image.load('data/valley.png')
        abyss = pygame.image.load('data/abyss.png')
        if level ==valleyone:
            defaulttexture = valley 
        if level ==snowone:
            defaulttexture = snow
        if level ==spawn:
            defaulttexture = grass
        if level ==valleytwo:
            defaulttexture = valley 
        if level ==snowtwo:
            defaulttexture = snow
        if level ==forestone:
            defaulttexture = grass
        if level ==foresttwo:
            defaulttexture = grass
        if level ==abyssone:
            defaulttexture = abyss
        if level ==abysstwo:
            defaulttexture = abyss   
        prevblock = createblock(length, height,(255,50,255))
        endblock  = createblock(length, height,(100,100,100))
        chest = pygame.image.load('data/chest.png')   
        tree = pygame.image.load('data/tree.png') 
        global chest
        currentsurface = pygame.Surface((32,32))
        hotbarside = pygame.image.load('data/hotbarside.png')
        background = background0.copy()
 
        for y in range(lines):
            for p in range(0,10):
                for x in range(columns):
                    if level[y][x] == "x": #Wall
                        background.blit(mountaintxt, (length * x, height * y))
                    elif level[y][x] == "n": #Next level
                        background.blit(nextblock, (length * x, height * y))
                    elif level[y][x] == "w": #Next level
                        background.blit(nextblock, (length * x, height * y))
                    elif level[y][x] == "m": #Next level
                        background.blit(nextblock, (length * x, height * y))
                    elif level[y][x] == "z": #Next level
                        background.blit(nextblock, (length * x, height * y))     
                    elif level[y][x] == "p": #Previous level
                        background.blit(prevblock, (length * x, height * y))
                    elif level[y][x] == "e": #End block
                        background.blit(endblock,  (length * x, height * y))
                    elif level[y][x] == "1": #Inventory one
                        background.blit(inventoryone,  (length * x, height * y))
                    elif level[y][x] == "2": #Inventory two
                        background.blit(inventorytwo,  (length * x, height * y))
                    elif level[y][x] == "3": #Inventory three
                        background.blit(inventorythree,  (length * x, height * y))
                    elif level[y][x] == "4": #Inventory four
                        background.blit(inventoryfour,  (length * x, height * y))
                    elif level[y][x] == "5": #Inventory five
                        background.blit(inventoryfive,  (length * x, height * y))
                    elif level[y][x] == "h": #Inventory sides
                        background.blit(hotbarside,  (length * x, height * y))                    
                    elif level[y][x] == ".": #defaulttexture
                        background.blit(defaulttexture,  (length * x, height * y))
                    elif level[y][x] == ",": #Snow
                        background.blit(defaulttexture,  (length * x, height * y))
                    elif level[y][x] == "'": #Valley
                        background.blit(defaulttexture,  (length * x, height * y)) 
                    elif level[y][x] == "c": #Chest   
                        currentsurface.blit(defaulttexture,  (0, 0))
                        currentsurface.blit(chest,  (0, 0))   
                        background.blit(currentsurface,(length * x, height * y))
                    elif level[y][x] == "^": #Tree   
                        currentsurface.blit(defaulttexture,  (0, 0))
                        currentsurface.blit(tree,  (0, 0))   
                        background.blit(currentsurface,(length * x, height * y))                    
                    elif level[y][x] == "s": #Spawn
                        if spawnpoint =="s":
                            maincharx = length * x
                            mainchary = height * y  
                        background.blit(defaulttexture, (length * x, height * y)) 
                    elif level[y][x] == "q": #Spawn
                        if spawnpoint =="q":
                            maincharx = length * x
                            mainchary = height * y  
                        background.blit(defaulttexture, (length * x, height * y))                     
                    elif level[y][x] == "t": #Spawn
                        if spawnpoint =="t":
                            maincharx = length * x
                            mainchary = height * y  
                        background.blit(defaulttexture, (length * x, height * y))    
                        
        screen.blit(background0, (0,0))               
        return length, height, maincharx, mainchary, lines, columns, background
 
    def checkchest(x1,y1,length,height,chest,intChestAmount, chestopen):
        '''Checks chests to decide which item to send to inventory function'''
        background.blit(chestopen,  (length * x1, height * y1))        
        intAmount = random.randint(1,10)
        if intChestAmount < 3 and intChestAmount > 0:
            if intAmount in range(-2,6):
                inventory("health") 
            if intAmount in range(6,11):
                inventory("attack")
        return intChestAmount
        
    def inventory(strItem):   
        intNum = 0
        attack = pygame.image.load('data/potionatk.png')  
        health = pygame.image.load('data/potion.png')
        if strItem== 'attack':
            lstInventory.append("attack")                
        if strItem== 'health':
            lstInventory.append("health")                
        while (intNum < len(lstInventory)):  
            if "attack" in lstInventory[intNum]:
                background.blit(attack, (lstInven[intNum]))            
                intNum = intNum + 1
            elif "health" in lstInventory[intNum]:
                background.blit(health, (lstInven[intNum]))         
                intNum = intNum + 1
            else:
                intNum = intNum + 1 
    
    def inventorycheck(intChoice,intTempHealth):
        intChoice = int(intChoice)
        blnTempAttack = False
        if int(intChoice) <= (len(lstInventory) - 1):
            if lstInventory[intChoice] == 'health':
                if intTempHealth != 100:
                    if intTempHealth + 20 > 100:
                        intTempHealth = 100
                        del lstInventory[intChoice]
                    else:
                        intTempHealth = intTempHealth + 20
                        pygame.mixer.Sound.play(potion)
                        del lstInventory[intChoice]
            if lstInventory[intChoice] == 'attack':
                blnTempAttack = True
                del lstInventory[intChoice]
        return intTempHealth, blnTempAttack
                
    def inventoryblit():
        '''Fix inventory (blit)'''
        background.blit(inventoryone, lstInvenHighlight[0])
        background.blit(inventorytwo, lstInvenHighlight[1])
        background.blit(inventorythree, lstInvenHighlight[2])
        background.blit(inventoryfour, lstInvenHighlight[3])
        background.blit(inventoryfive, lstInvenHighlight[4])

    def distance(pt1,pt2):
        return math.sqrt(((pt2[0]-pt1[0])**2)+((pt2[1]-pt1[1])**2))    
        
    def createenemy(blnEnemy,blnDelAll):
        if blnEnemy == True:     
            npc = pygame.image.load('data/slime.png')
            npcx = 0
            npcy = 0
            npcx = random.randint(32,950)
            npcy = random.randint(32,800)
            intHealth = 100
            intHealth = int(intHealth)
            lstTempEnem = []
            lstTempEnem.append(npc)  
            lstTempEnem.append(intHealth)  
            lstTempEnem.append(npcx)
            lstTempEnem.append(npcy)
            lstEnemies.append(lstTempEnem)

        intLoop = 0 
        while intLoop < len(lstEnemies):
            screen.blit(lstEnemies[intLoop][0],(lstEnemies[intLoop][2],lstEnemies[intLoop][3]))
            screen.blit(createblock((30 / 100 * lstEnemies[intLoop][1]), 5,(255,49,49)), (lstEnemies[intLoop][2], (lstEnemies[intLoop][3] - 10)))
            intLoop = intLoop +1
        intNewLoop = 0
        if blnDelAll ==True:
            while intNewLoop < len(lstEnemies):
                del lstEnemies[intNewLoop]
                intEnemies = 0
                intNewoop = intNewLoop +1
        
          
    #A list containing all the maps
    all_levels = [spawn, forestone, foresttwo, snowone, snowtwo, valleyone, valleytwo]  
    max_levels = len(all_levels)        
    my_game = all_levels[0] #Start with the first map
    length, height, maincharx, mainchary, lines, columns, background = addlevel(my_game,spawnpoint = "s")
 
    intVelocity = 5 #Character speed
    clock = pygame.time.Clock() #Create pygame clock
    mainloop = True
    FPS = 120 #Max frames per second
    playtime = 0
 
    while mainloop:
        milliseconds = clock.tick(FPS)  #Milliseconds passed since first frame
        seconds = milliseconds / 1000.0 #Seconds passed since last frame (float)
        playtime += seconds
        screen.blit(background, (0,0)) #Delete background                
        intHealth, blnAttack = inventorycheck('123', intHealth)             
        pygame.display.set_caption("[FPS]: %.2f dx: %i dy %i arrow keys to move" % (clock.get_fps(), dx, dy))
        background.blit(signforest,(44,400))
        background.blit(signvalley,(1200,400))
        background.blit(hp,(10,963))
        
        #Create health bar (and update):
        healthbarbg  = createblock(294, 18,(32,13,8))
        background.blit(healthbarbg, (41,967))                           
        healthbar  = createblock((290 / 100 * intHealth), 14,(255,49,49))
        background.blit(healthbar, (43,969))
        while intEnemies < 5:
            createenemy(True,False)
            intEnemies = intEnemies + 1
            intEnemy2 = intEnemy2 + 1
        
        if dx > 0:            
            pointx = maincharx + maincharsurface.width
        else:
            pointx = maincharx
        if dy > 0:     
            pointy = mainchary + maincharsurface.height
        else:
            pointy = mainchary
            
        #Determines whether character wants to exit screen
        if pointx + dx < 0:
            maincharx = 0
            pointx = 0
            dx = 0
        elif pointx + dx > screenrect.width:
            maincharx = screenrect.width - maincharsurface.width
            pointx = screenrect.width - maincharsurface.width
            dx = 0
        if pointy + dy < 0:
            mainchary = 0
            pointy = 0
            dy = 0
        elif pointy + dy > screenrect.height:
            mainchary = screenrect.height - maincharsurface.height
            pointy = screenrect.height - maincharsurface.height
            dy = 0
        intLoop = 0
        
        while intLoop < len(lstEnemies):  
            dnx = 0
            dny = 0
            if int(maincharx) in range((int(lstEnemies[intLoop][2]) - 19),(int(lstEnemies[intLoop][2]) + 19)):
                if int(mainchary) in range((int(lstEnemies[intLoop][3]) - 32),(int(lstEnemies[intLoop][3]) + 32)):            
                    if intHealth > 0:
                        intHealth = intHealth - 0.5  
            if distance((maincharx,mainchary),(lstEnemies[intLoop][2],lstEnemies[intLoop][3])) <= 200:
                (dnx, dny) = ((maincharx - lstEnemies[intLoop][2])/math.sqrt((maincharx - lstEnemies[intLoop][2]) ** 2 + (mainchary - lstEnemies[intLoop][3]) ** 2), (mainchary - lstEnemies[intLoop][3])/math.sqrt((maincharx - lstEnemies[intLoop][2]) ** 2 + (mainchary - lstEnemies[intLoop][3]) ** 2))
            if dnx < 0:
                dnx = random.randint(-2,0)
            elif dnx > 0:
                dnx = random.randint(0,2)
            if dny < 0:
                dny = random.randint(-2,0)
            elif dny > 0:
                dny = random.randint(0,2)
            lstEnemies[intLoop][2] = lstEnemies[intLoop][2] + dnx 
            lstEnemies[intLoop][3] = lstEnemies[intLoop][3] + dny   
            if lstEnemies[intLoop][1] == 0:
                del lstEnemies[intLoop]    
                intEnemy2 = intEnemy2 - 1
            intLoop = intLoop + 1            
            createenemy(False,False)
            
        y1 = int(pointy/height)
        y1 = max(0,y1) #No smaller than 0
        y1 = min(y1,lines-1) #No bigger than the lines
        x1 = int((pointx + dx)/length)
        x1 = max(0,x1) #No smaller than 0
        x1 = min(x1,columns-1) 
        y2 = int((pointy+dy)/height)
        y2 = max(0,y2)
        y2 = min(y2,lines-1)
        #Check type of tile under mainchar
        if my_game[y1][x1] == "x" :
            dx = 0
        if dx < 0:
            maincharx += dx
            mainChar = mainCharleft.next()
        if dy < 0:
            mainchary += dy
            mainChar = mainCharback.next()
        if dx > 0:
            maincharx += dx
            mainChar = mainCharright.next()
        if dy > 0:
            mainchary += dy
            mainChar = grid.next()
     
        if my_game[y2][x1] == "x":
            dy = 0
        elif my_game[y1][x1] == "c":
            pygame.mixer.Sound.play(chest)
            chestopen = pygame.image.load('data/chestopen.png')                    
            if y1 and x1 not in chestlst:       
                chestlst.append(x1)  
                chestlst.append(y1)  
                intGlobalChestAmount = checkchest(x1,y1,length,height,chest,intGlobalChestAmount, chestopen)
                dx = 0
                dy= 0
            else:
                background.blit(chestopen,  (length * x1, height * y1))        
            
        #Move enemy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #If game window is closed
                mainloop = False 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False 
                if event.key == pygame.K_UP:
                    dy = -intVelocity 
                if event.key == pygame.K_DOWN:
                    dy = intVelocity
                if event.key == pygame.K_RIGHT:
                    dx = intVelocity
                if event.key == pygame.K_LEFT:
                    dx = -intVelocity
                if event.key ==pygame.K_SPACE:
                    pygame.mixer.Sound.play(stab)
                    if mainChar ==mainCharright.next():
                        mainChar = pygame.image.load('data/swordright.png')
                    if mainChar ==grid.next():
                        mainChar = pygame.image.load('data/swordfront.png')
                    if mainChar ==mainCharleft.next():
                        mainChar = pygame.image.load('data/swordleft.png')
                    
                    if mainChar ==mainCharback.next():
                        mainChar = pygame.image.load('data/swordback.png')
                    intNLoop = 0
                    while intNLoop < len(lstEnemies):  
                        if distance((maincharx,mainchary),(lstEnemies[intNLoop][2],lstEnemies[intNLoop][3])) <= 50:
                            if blnAttack == True:
                                print('swag')                            
                            if blnAttack == False:
                                lstEnemies[intNLoop][1] = lstEnemies[intNLoop][1] - 25                           
                            if blnAttack == True:
                                lstEnemies[intNLoop][1] = lstEnemies[intNLoop][1] - 100   
                                blnAttack = False
                        intNLoop = intNLoop + 1
                        
                if event.key == pygame.K_1:
                    pygame.mixer.Sound.play(rollover)
                    inventoryblit()
                    background.blit(inventoryoneH, lstInvenHighlight[0])
                    intHealth,blnAttack = inventorycheck('0', intHealth)
                if event.key == pygame.K_2:
                    pygame.mixer.Sound.play(rollover)
                    inventoryblit()                    
                    background.blit(inventorytwoH, lstInvenHighlight[1])                    
                    intHealth,blnAttack = inventorycheck('1', intHealth)
                if event.key == pygame.K_3:
                    pygame.mixer.Sound.play(rollover)
                    inventoryblit()                    
                    background.blit(inventorythreeH, lstInvenHighlight[2])                    
                    intHealth,blnAttack = inventorycheck('2', intHealth)
                if event.key == pygame.K_4:
                    pygame.mixer.Sound.play(rollover)
                    inventoryblit()                    
                    background.blit(inventoryfourH, lstInvenHighlight[3])
                    intHealth,blnAttack = inventorycheck('3', intHealth)
                if event.key == pygame.K_5:
                    pygame.mixer.Sound.play(rollover)
                    inventoryblit()                    
                    background.blit(inventoryfiveH, lstInvenHighlight[4])
                    intHealth,blnAttack = inventorycheck('4', intHealth)
                    
            if event.type != pygame.KEYDOWN:
                dx = 0 
                dy = 0
        
        #Move surface of mainchar
        screen.blit(mainChar, (maincharx, mainchary))
        intEnemy2 = 0
        #Checks for special tiles
        if my_game[int(mainchary / height)][int(maincharx/length)] == "z":
            if intEnemy2 ==0:
                if my_game ==spawn:
                    my_game = valleyone            
                createenemy(False,True) 
                intEnemies = 0 
                intEnemy2 = 0
                length, height,  maincharx, mainchary,  lines, columns,background = addlevel(my_game, spawnpoint = "s")
            
        elif my_game[int(mainchary / height)][int(maincharx/length)] == "n":
            if intEnemy2 ==0:
                if my_game ==forestone:
                    my_game = foresttwo
                if my_game ==valleyone:
                    my_game = valleytwo            
                if my_game ==all_levels[0]:
                    my_game = forestone
                if my_game ==snowone:
                    my_game = snowtwo
                
                createenemy(False,True) 
                intEnemies = 0 
                intEnemy2 = 0
                length, height,  maincharx, mainchary,  lines, columns,background = addlevel(my_game, spawnpoint = "s")
                
        elif my_game[int(mainchary / height)][int(maincharx/length)] == "p":           
            actual = all_levels.index(my_game)
            #Cycle backwards
            if intEnemy2 ==0:
                if my_game ==valleyone:
                    my_game = all_levels[0]
                if my_game ==valleytwo:
                    my_game = all_levels[5]
                if my_game ==snowone:
                    my_game = all_levels[0]
                if my_game ==snowtwo:
                    my_game = all_levels[3]
                if my_game ==forestone:
                    my_game = all_levels[0]
                if my_game ==foresttwo:
                    my_game = all_levels[1]
                createenemy(False,True)
                intEnemies = 0
                intEnemy2 = 0
                length, height,  maincharx, mainchary,  lines, columns,background = addlevel(my_game, spawnpoint = "q")
        elif my_game[int(mainchary / height)][int(maincharx/length)] == "w":
            if intEnemy2 ==0:
                if my_game ==spawn:
                    my_game = snowone
                createenemy(False,True) 
                intEnemies = 0 
                intEnemy2 = 0
                length, height,  maincharx, mainchary,  lines, columns,background = addlevel(my_game, spawnpoint = "s")      
        elif my_game[int(mainchary / height)][int(maincharx/length)] == "m":
            if intEnemy2 ==0:
                if my_game ==spawn:
                    my_game = abyssone
                createenemy(False,True) 
                intEnemies = 0 
                intEnemy2 = 0
                length, height,  maincharx, mainchary,  lines, columns,background = addlevel(my_game, spawnpoint = "s")            
        
        elif my_game[int(mainchary / height)][int(maincharx/length)] == "e":
            #Game won > exit main loop
            mainloop = False
        pygame.display.flip()
          
    
if __name__ == "__main__":
    
    shardsofstan() #Initiate game
    
