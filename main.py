import pygame
from random import randrange

WIDTH, HEIGHT = 1000, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Assignment 1!")

#Chennai FC Goal Box Coordinates:
goalbox_top_left=(48,119)
goalbox_top_right=(195,119)
goalbox_bottom_left=(48,572)
goalbox_bottom_right=(195,572)

#Chennai FC Upper Part Coordinates:
upperpart_top_left=(198,39)
upperpart_top_right=(496,39)
upperpart_bottom_left=(198,661)
upperpart_bottom_right=(496,661)

#Draw Line Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE=(0, 0, 255)
GREEN=(0, 255, 0)




FOOTBALL_GROUND=pygame.image.load('assets\\field.png')
BLUE_PLAYER=pygame.image.load('assets\\Blue.jpg')
RED_PLAYER=pygame.image.load('assets\\Red.jpg')
FOOTBALL=pygame.image.load('assets\\Football.jpg')

FOOTBALL_GROUND=pygame.transform.scale(FOOTBALL_GROUND,(1000,700))
FOOTBALL=pygame.transform.scale(FOOTBALL,(25,25))
RED_PLAYER1=pygame.transform.scale(RED_PLAYER,(40,50))
RED_PLAYER2=pygame.transform.scale(RED_PLAYER,(40,50))
RED_PLAYER3=pygame.transform.scale(RED_PLAYER,(40,50))
BLUE_PLAYER1=pygame.transform.scale(BLUE_PLAYER,(40,50))
BLUE_PLAYER2=pygame.transform.scale(BLUE_PLAYER,(40,50))
BLUE_PLAYER3=pygame.transform.scale(BLUE_PLAYER,(40,50))
BLUE_PLAYER4=pygame.transform.scale(BLUE_PLAYER,(40,50))


def player_coods(xr1,xr2,yr1,yr2):
    return (randrange(xr1,xr2),randrange(yr1,yr2))

#Getting All the player coods
#Condition2
red_player1_coods=player_coods(goalbox_top_left[0],goalbox_top_right[0],goalbox_top_left[1],goalbox_bottom_left[1])
blue_player1_coods=player_coods(goalbox_top_left[0],goalbox_top_right[0],goalbox_top_left[1],goalbox_bottom_left[1])

#Condition3
red_player2_coods=player_coods(upperpart_top_left[0],upperpart_top_right[0],upperpart_top_left[1],upperpart_bottom_left[1])
blue_player2_coods=player_coods(upperpart_top_left[0],upperpart_top_right[0],upperpart_top_left[1],upperpart_bottom_left[1])
red_player3_coods=player_coods(upperpart_top_left[0],upperpart_top_right[0],upperpart_top_left[1],upperpart_bottom_left[1])
blue_player3_coods=player_coods(upperpart_top_left[0],upperpart_top_right[0],upperpart_top_left[1],upperpart_bottom_left[1])

def screen_initial():
    SCREEN.blit(FOOTBALL_GROUND, (0, 0))
    #Within Goal area
    SCREEN.blit(BLUE_PLAYER1, blue_player1_coods)
    SCREEN.blit(RED_PLAYER1, red_player1_coods)
    #Upper part
    SCREEN.blit(BLUE_PLAYER2, blue_player2_coods)
    SCREEN.blit(RED_PLAYER2, red_player2_coods)
    SCREEN.blit(BLUE_PLAYER3, blue_player3_coods)
    SCREEN.blit(RED_PLAYER3, red_player3_coods )
    #CONDITION1 : Bengaluru FC is performing an assisted goal shootout but from the Center Circle position
    #this player should stay put at fixed Center Circle Position
    SCREEN.blit(BLUE_PLAYER4, (500, 327))
    #Keeping football in fixed Position
    SCREEN.blit(FOOTBALL, (480, 350))
    pygame.display.update()


def show_score(x, y, stext, cost):
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 20)
    score = font.render(f"{stext} : " + cost, True, (255, 255, 255))
    SCREEN.blit(score, (x, y))
    pygame.display.update()

def calculate_cost(x1,y1,x2,y2):
    result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
    result=round(result,2)
    return result

def main():
    path_cost={}
    clock = pygame.time.Clock()
    run = True
    screen_initial()

    #path1 -->BlueCenterPlayer->BP2->BP1->Goal
    #Line Between Red_Player1 and Red_Player2
    #Adding 50 so that the line segment starts from the bottom of the player
    pygame.draw.line(SCREEN,(RED),(blue_player1_coods[0],blue_player1_coods[1]+50),(blue_player2_coods[0],blue_player2_coods[1]+50),3) 
    #Line between Red_Central_Kicker and Red_Player2
    pygame.draw.line(SCREEN,(RED),(500,377),(blue_player2_coods[0],blue_player2_coods[1]+50),3) 
    #Line between Red_Player1 and Goal Post
    pygame.draw.line(SCREEN,(RED),(blue_player1_coods[0],blue_player1_coods[1]+50),(50,357),3)
    
    path1_cost=calculate_cost(500,377,blue_player2_coods[0],blue_player2_coods[1]+50)+calculate_cost(blue_player1_coods[0],blue_player1_coods[1]+50,blue_player2_coods[0],blue_player2_coods[1]+50)+calculate_cost(blue_player1_coods[0],blue_player1_coods[1]+50,50,357)
    path_cost["BCP->BP2->BP1->G"]=path1_cost
    #Path2 -->BlueCenterPlayer->BP3-->BP1-->Goal
    #Line Between Red_Player1 and Red_Player3
    pygame.draw.line(SCREEN,(BLACK),(blue_player1_coods[0],blue_player1_coods[1]+50),(blue_player3_coods[0],blue_player3_coods[1]+50),3) 
    #Line between Red_Central_Kicker and Red_Player3
    pygame.draw.line(SCREEN,(BLACK),(500,377),(blue_player3_coods[0],blue_player3_coods[1]+50),3) 
    path2_cost=calculate_cost(500,377,blue_player3_coods[0],blue_player3_coods[1]+50)+calculate_cost(blue_player1_coods[0],blue_player1_coods[1]+50,blue_player3_coods[0],blue_player3_coods[1]+50)+calculate_cost(blue_player1_coods[0],blue_player1_coods[1]+50,50,357)
    path_cost["BCP->BP3->BP1->G"]=path2_cost
    
    #Path3 -->BlueCenterPlayer->BP1-->Goal
    pygame.draw.line(SCREEN,(YELLOW),(500,377),(blue_player1_coods[0],blue_player1_coods[1]+50),3) 
    path3_cost=calculate_cost(500,377,blue_player1_coods[0],blue_player1_coods[1]+50)+calculate_cost(blue_player1_coods[0],blue_player1_coods[1]+50,50,357)
    path_cost["BCP->BP1->G"]=path3_cost

    #path4 -->BlueCenterPlayer-BP2-->Goal
    pygame.draw.line(SCREEN,(BLUE),(blue_player2_coods[0],blue_player2_coods[1]+50),(50,357),3)
    path4_cost=calculate_cost(500,377,blue_player2_coods[0],blue_player2_coods[1]+50)+calculate_cost(blue_player2_coods[0],blue_player2_coods[1]+50,50,357)
    path_cost["BCP->BP2->G"]=path4_cost

    #path5 -->BlueCenterPlayer->BP3-->Goal
    pygame.draw.line(SCREEN,(GREEN),(blue_player3_coods[0],blue_player3_coods[1]+50),(50,357),3)
    path5_cost=calculate_cost(500,377,blue_player3_coods[0],blue_player3_coods[1]+50)+calculate_cost(blue_player3_coods[0],blue_player3_coods[1]+50,50,357)
    path_cost["BCP->BP3->G"]=path5_cost
    


    Keymin = min(zip(path_cost.values(), path_cost.keys()))[1]
    Valmin = min(zip(path_cost.values(), path_cost.keys()))[0]

    del path_cost[Keymin]
    Keymin2 = min(zip(path_cost.values(), path_cost.keys()))[1]
    Valmin2 = min(zip(path_cost.values(), path_cost.keys()))[0]



    #printing Paths
    show_score(10,10,Keymin,str(Valmin))
    show_score(10,30,Keymin2, str(Valmin2))
   
    pygame.display.update()
    while run:
        #Hardcoding the frames per second as 60 as this is then standard for games
        #This will run the while loop for 60 times per second , if this is not fesable it will run as fast as it can.
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type==pygame.MOUSEBUTTONDOWN:
                print("You pressed the left mouse button at (%d,%d)" %event.pos)
        
    pygame.quit()
    
        

if __name__ == "__main__":
    main()