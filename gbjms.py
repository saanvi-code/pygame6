import pygame
pygame.init()
screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Shapes")
pink=pygame.Color("red")
white=pygame.Color("white")
purple=pygame.Color("purple")

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0,0,0))
    pygame.draw.rect(screen,white,pygame.Rect(50,50,20,20),0)
    pygame.draw.circle(screen,pink,(100,100),30,0)
    pygame.draw.rect(screen,white,pygame.Rect(140,50,20,20),0)
    pygame.draw.line(screen,white,(10,100),(190,100),10)
    points=regular_polygon((250,250),100,5)
    pygame.draw.polygon(screen,purple,(0,255,0),points)



    
    pygame.display.flip()

pygame.quit()

