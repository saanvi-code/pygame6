import pygame
pygame.init()
display=pygame.display.set_mode((500,500))
font = pygame.font.Font(None,20)  
message1 = ""  
message2 = ""  
message3 = ""  



d=True
while d:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

        elif event.type==pygame.KEYDOWN:
            message1="DOWN key has been pressed"

            if event.key==pygame.K_UP:
             message2="UP key has been pressed"

            elif event.key==pygame.K_SPACE:
             message3= "space has been pressed"

        
    

    surface = font.render(message1, False, (255, 255, 255))  
    surface1 = font.render(message2, False, (255, 255, 255))  
    surface2 = font.render(message3, False, (255, 255, 255))  


    display.blit(surface, (50, 200))
    display.blit(surface1, (50, 300))
    display.blit(surface2, (50, 400))

    pygame.display.flip()
