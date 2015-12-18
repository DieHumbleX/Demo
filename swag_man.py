import pygame

w = (255, 255, 255)
b = (0, 0, 0)
r = (255, 0, 0)
 
 
def draw_stick_figure(screen, x, y):
   
    pygame.draw.ellipse(screen, b, [1 + x, y, 10, 10], 0)
 
    pygame.draw.line(screen, b, [5 + x, 15 + y], [10 + x, 25 + y], 2)
    pygame.draw.line(screen, b, [5 + x, 15 + y], [x, 25 + y], 2)
    pygame.draw.line(screen, r, [5 + x,5+ y], [5 + x, 15 + y], 2)
    pygame.draw.line(screen, b, [5 + x, 7 + y], [9 + x, 15 + y], 2)
    pygame.draw.line(screen, b, [5 + x, 7 + y], [1 + x, 15 + y], 2)
 

pygame.init()
 

size = [620, 635]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("swag man")
 

done = False
 

clock = pygame.time.Clock()
 

pygame.mouse.set_visible(0)
 

x_speed = 0
y_speed = 0
 

x_coord = 10
y_coord = 10
 

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
       
           
            if event.key == pygame.K_LEFT:
                x_speed = -4
            elif event.key == pygame.K_RIGHT:
                x_speed = 4
            elif event.key == pygame.K_UP:
                y_speed = -4
            elif event.key == pygame.K_DOWN:
                y_speed = 4
 
        
        elif event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    x_coord=x_coord+x_speed
    y_coord=y_coord+y_speed
    if x_coord<10 :
        x_coord=10
    elif x_coord>600:
        x_coord=600
    if y_coord<10:
        y_coord=10
    elif y_coord>600:
        y_coord=600
        
        
 
    
  
    screen.fill(w)
    print x_coord,y_coord
    draw_stick_figure(screen, x_coord, y_coord)
    pygame.display.flip()
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()