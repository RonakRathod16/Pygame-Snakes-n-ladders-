import pygame
import random
from LADDERS import ladders,ladders2, snakes_1,snakes_2
pygame.init()


screen_width = 1150
screen_height= 800 
# DISPLAY SETTINGS SECTION --------------------------------
ScreenSet= pygame.display.set_mode((screen_width, screen_height))
ScreenSet_1= pygame.display.set_mode((screen_width, screen_height))
name= pygame.display.set_caption("SnakeLadder")

# color filling ----------------------------


icon=pygame.image.load("resources/icon.jpeg")
pygame.display.set_icon(icon)

    
# FUNCTION FOR SHOWING TEXT ON GAME SCREEN
def show_number(number, color, x, y):
    text_screen = font.render(number,color, True)
    ScreenSet.blit(text_screen, [x,y])


# GAME VARIABLES     
turn= 'red' 
x1=10
x2=20
y1=660
y2=660
clock = pygame.time.Clock()
fps=1
button1= pygame.Rect(50,710,30,30)
exit_game = False
font = pygame.font.SysFont(None, 40)
gray=(128,128,128)


def show_players():
        one= show_number("Player-1", "Red", 910,200)
        two= show_number("Player-2", "Green",910,300)
        # three= show_number("Player-3", "yellow",910,400)
        # four= show_number("Player-4", "blue",910,500)
        return one,two
    


def roll1():
    show_number("Your turn", gray, 910,230)
    
def roll2():
    show_number("Your turn", gray, 910,330)
    
# def roll3():
#     show_number("Your turn", gray, 910,430)
    
# def roll4():
#     show_number("Your turn", gray, 910,530)


# FUNCTION OF DICE ROLLING 
def display_dice():
    dice_no=random.randint(1,6)
    
    if dice_no == 1:
        dice=pygame.image.load("resources/dice_11.png")
        
    elif dice_no == 2:
        dice=pygame.image.load("resources/dice2.png")
        
    elif dice_no == 3:
        dice=pygame.image.load("resources/dice3.png")
    elif dice_no == 4:
        dice=pygame.image.load("resources/dice_44.png")
    elif dice_no == 5:
        dice=pygame.image.load("resources/dice_55.png")
    elif dice_no == 6:
        dice=pygame.image.load("resources/dice_66.png")
    
    return dice,dice_no


# PLAYERS POINT IMAGES LOADING 
player1=pygame.image.load("resources/points11.png")
player2=pygame.image.load("resources/points22.png")


def p1(x,y):
        ScreenSet.blit(player1,(x1,y))
def p2(x,y):
        ScreenSet.blit(player2,(x2,y))

# FUNCTION OF ROLL BUTTON 
def button_fun():
    pygame.draw.rect(ScreenSet, "white", (0,701,900,100))
    pygame.draw.rect(ScreenSet, "black", (410,700,90,90))
    pygame.draw.rect(ScreenSet, "white", (50,710,30,30))
    pygame.draw.rect(ScreenSet, "black", (53,713,25,25))
    pygame.draw.rect(ScreenSet, "white", (55,715,20,20))
    
mainboards=pygame.image.load("resources/mainboard1.png")

def movement(a):
    Coor=[[10, 670], [99, 670], [188, 670], [277, 670], [366, 670], [455, 670], [544, 670], [633, 670], [722, 670], [811, 670], 
 [811, 600], [722, 600], [633, 600], [544, 600], [455, 600], [366, 600], [277, 600], [188, 600], [99, 600], [10, 600], 
 [10, 530], [99, 530], [188, 530], [277, 530], [366, 530], [455, 530], [544, 530], [633, 530], [722, 530], [811, 530], 
 [811, 460], [722, 460], [633, 460], [544, 460], [455, 460], [366, 460], [277, 460], [188, 460], [99, 460], [10, 460], 
 [10, 390], [99, 390], [188, 390], [277, 390], [366, 390], [455, 390], [544, 390], [633, 390], [722, 390], [811, 390], 
 [811, 320], [722, 320], [633, 320], [544, 320], [455, 320], [366, 320], [277, 320], [188, 320], [99, 320], [10, 320], 
 [10, 250], [99, 250], [188, 250], [277, 250], [366, 250], [455, 250], [544, 250], [633, 250], [722, 250], [811, 250], 
 [811, 180], [722, 180], [633, 180], [544, 180], [455, 180], [366, 180], [277, 180], [188, 180], [99, 180], [10, 180], 
 [10, 110], [99, 110], [188, 110], [277, 110], [366, 110], [455, 110], [544, 110], [633, 110], [722, 110], [811, 110], 
 [811, 40], [722, 40], [633, 40], [544, 40], [455, 40], [366, 40], [277, 40], [188, 40], [99, 40], [10, 40]]
               
               
                
    
    iter1=Coor[a]
    x=iter1[0]
    y=iter1[1]
    return x,y   
    

def movement_2(b):
    
    Cool=[[20, 670], [109, 670], [198, 670], [287, 670], [376, 670], [465, 670], [554, 670], [643, 670], [732, 670], [821, 670], 
 [821, 600], [732, 600], [643, 600], [554, 600], [465, 600], [376, 600], [287, 600], [198, 600], [109, 600], [20, 600], 
 [20, 530], [109, 530], [198, 530], [287, 530], [376, 530], [465, 530], [554, 530], [643, 530], [732, 530], [821, 530], 
 [821, 460], [732, 460], [643, 460], [554, 460], [465, 460], [376, 460], [287, 460], [198, 460], [109, 470], [20, 460], 
 [20, 390], [109, 390], [198, 390], [287, 390], [376, 390], [465, 390], [554, 390], [643, 390], [732, 390], [821, 390], 
 [821, 320], [732, 320], [643, 320], [554, 320], [465, 320], [376, 320], [287, 320], [198, 320], [109, 320], [20, 320], 
 [20, 250], [109, 250], [198, 250], [287, 250], [376, 250], [465, 250], [554, 250], [643, 250], [732, 250], [821, 250], 
 [821, 180], [732, 180], [643, 180], [554, 180], [465, 180], [376, 180], [287, 180], [198, 180], [109, 180], [20, 180], 
 [20, 110], [109, 110], [198, 110], [287, 110], [376, 110], [465, 110], [554, 110], [643, 110], [732, 110], [821, 110], 
 [821, 40], [732, 40], [643, 40], [554, 40], [465, 40], [376, 40], [287, 40], [198, 40], [109, 40], [20, 40]]

    
    iter2=Cool[b]
    x=iter2[0]
    y=iter2[1]
    return x,y
    
    

    
                        
normal_pos_A=0                         
normal_pos_B=0


while not exit_game:
        ScreenSet.fill("white")
        ScreenSet.blit(mainboards,(0,0))
        button_fun()
        pygame.draw.rect(ScreenSet, "white", (1000,0,150,800))
        if turn=='red':
            roll1()
        elif turn=='green':
            roll2()
            
        
        p1(x1,y1)
        p2(x2,y2)
        for events in pygame.event.get():
                if events.type == pygame.QUIT:
                        exit_game=True
                
                elif  events.type==pygame.MOUSEBUTTONDOWN:
                    mouse_pos=pygame.mouse.get_pos()
                    
                    if button1.collidepoint(mouse_pos):
                        display_dice()
                        dice,diceNo= display_dice()
                        
                        ScreenSet.blit(dice, (420,710))
                        print(diceNo)
                    
                    if normal_pos_A>100:
                        normal_pos_A-=diceNo
                    if normal_pos_B>100:
                        normal_pos_B-=diceNo
                    # PLAYER 1-----------------------------------------------------------------------------------------------------------------------------
                    if display_dice() and turn=='red':
                        turn='green'
                        if diceNo==1:
                            normal_pos_A+=diceNo
                            coors=movement(normal_pos_A)
                            x,y=coors
                            x1=x
                            y1=y                            
                        if diceNo==2:
                            
                            normal_pos_A+=diceNo
                            coors=movement(normal_pos_A)
                            x,y=coors
                            x1=x
                            y1=y                            

                            
                        if diceNo==3:
                            if normal_pos_A<98:
                                normal_pos_A+=diceNo
                                coors=movement(normal_pos_A)
                                x,y=coors
                                x1=x
                                y1=y                            
                                x1=x
                                y1=y                            
                            if normal_pos_A>=98:
                                print("Out of range")
                        if diceNo==4:
                            if normal_pos_A<97:
                                normal_pos_A+=diceNo
                                coors=movement(normal_pos_A)
                                x,y=coors
                                x1=x
                                y1=y                            
                            if normal_pos_A>=97:
                                print("Out of range")
                            
                        if diceNo==5:
                            if normal_pos_A<96:
                                normal_pos_A+=diceNo
                                coors=movement(normal_pos_A)
                                x,y=coors
                                x1=x
                                y1=y 
                            if normal_pos_A>96:
                                print("out of range")                        
                            
                            
                        if diceNo==6:
                            if  normal_pos_A<95:
                                normal_pos_A+=diceNo
                                coors=movement(normal_pos_A)
                                x,y=coors
                                x1=x
                                y1=y
                                turn='red'
                            if normal_pos_A>=95:
                                print("out of range")                    
                                
                            

                            
                             
                        

                        
                        
                    # PLAYER 2--------------------------------------------------------------------------------------------------------------------------------
        
                    elif display_dice() and turn=='green':
                        turn='red'
                        
                        if diceNo==1:
                            normal_pos_B+=diceNo
                            coors2=movement_2(normal_pos_B)
                            a,b=coors2
                            x2=a
                            y2=b
                        if diceNo==2:
                            normal_pos_B+=diceNo
                            coors2=movement_2(normal_pos_B)
                            a,b=coors2
                            x2=a
                            y2=b
                            
                        if diceNo==3:
                            if normal_pos_B<98:
                                normal_pos_B+=diceNo
                                coors2=movement_2(normal_pos_B)
                                a,b=coors2
                                x2=a
                                y2=b
                            if normal_pos_B>=98:
                                print("Out of Range")
                        if diceNo==4:
                            if normal_pos_B<97:
                                normal_pos_B+=diceNo
                                coors2=movement_2(normal_pos_B)
                                a,b=coors2
                                x2=a
                                y2=b
                            if normal_pos_B>=97:
                                print("Out of range")
                        if diceNo==5:
                            if normal_pos_B<96:
                                normal_pos_B+=diceNo
                                coors2=movement_2(normal_pos_B)
                                a,b=coors2
                                x2=a
                                y2=b
                            if normal_pos_B>=96:
                                print("Out of range")
                        if diceNo==6:
                            if  normal_pos_B<95:
                                normal_pos_B+=diceNo
                                coors2=movement_2(normal_pos_B)
                                a,b=coors2
                                x2=a
                                y2=b
                                turn='green'
                        if normal_pos_B>=95:
                                print("out of range")
                       
                
                
                x1,y1,normal_pos_A=ladders(x1,y1,normal_pos_A)
                x1,y1,normal_pos_A=snakes_1(x1,y1,normal_pos_A)
                
                
                x2,y2,normal_pos_B=ladders2(x2,y2,normal_pos_B)
                x2,y2,normal_pos_B=snakes_2(x2,y2,normal_pos_B)
        p1(x1,y1)        
        p2(x2,y2)        
                    
        if x1==10 and y1==40 :
            ScreenSet.fill("black") 
            winner_1=pygame.image.load("resources/winner-1.png")
            ScreenSet.blit(winner_1,(0,0))
        elif x2== 20 and y2==40:
            ScreenSet.fill("black") 
            winner_2=pygame.image.load("resources/winner-2.png")
            ScreenSet.blit(winner_2,(0,0))         

        
       
        
        
        show_players()
        pygame.display.update()
        # time.sleep(1)
        clock.tick(fps)

pygame.quit()




