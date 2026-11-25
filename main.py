from config import * 
from sprites import Player, Richard


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Richard_Math_Marathon")

        self.clock = pygame.time.Clock()

        self.running = True

        self.player = Player((WINDOW_WIDTH//2 - 500, WINDOW_HEIGHT//2 + 100), [])
        self.richard = Richard((WINDOW_WIDTH//2 + 500, WINDOW_HEIGHT//2 + 50), [])

        self.setup()


    def setup(self):

        self.bg = pygame.image.load(os.path.join(BASE_DIR, 'data', 'images', 'Background.png')).convert_alpha()
        self.bg = pygame.transform.scale(self.bg,(WINDOW_WIDTH, WINDOW_HEIGHT))

        self.midg = pygame.image.load(os.path.join(BASE_DIR, 'data', 'images', 'Midground.png')).convert_alpha()
        self.midg = pygame.transform.scale(self.midg,(WINDOW_WIDTH, WINDOW_HEIGHT - 100))

        self.foreg = pygame.image.load(os.path.join(BASE_DIR, 'data', 'images', 'Foreground.png')).convert_alpha()
        self.foreg = pygame.transform.scale(self.foreg,(WINDOW_WIDTH, WINDOW_HEIGHT))

        self.buttonslist = [
            pygame.image.load(os.path.join(BASE_DIR, 'data', 'buttons', 'Normal.png')).convert_alpha(),
            pygame.image.load(os.path.join(BASE_DIR, 'data', 'buttons', 'Highlighted.png')).convert_alpha(),
            pygame.image.load(os.path.join(BASE_DIR, 'data', 'buttons', 'Correct.png')).convert_alpha(),
            pygame.image.load(os.path.join(BASE_DIR, 'data', 'buttons', 'Incorrect.png')).convert_alpha()
        ]

        

    def buttons (self):
        
                
            mouse_X, mouse_Y = pygame.mouse.get_pos()

            self.showbuttons = self.buttonslist[0]
            self.showbuttons2 = self.buttonslist[0]
            self.showbuttons3 = self.buttonslist[0]

            self.showbuttons_1 = self.showbuttons.get_rect(center = (180,600 ))
            self.showbuttons_2 = self.showbuttons2.get_rect(center = (580,600 ))
            self.showbuttons_3 = self.showbuttons3.get_rect(center = (980,600 ))

            
            mouse_alligned_button1 = self.showbuttons_1.collidepoint((mouse_X, mouse_Y))
            mouse_alligned_button2 = self.showbuttons_2.collidepoint((mouse_X, mouse_Y))
            mouse_alligned_button3 = self.showbuttons_3.collidepoint((mouse_X, mouse_Y))

            if mouse_alligned_button1 :
                self.showbuttons = self.buttonslist[1]
            elif mouse_alligned_button2 :
                self.showbuttons2 = self.buttonslist[1]
            elif mouse_alligned_button3 :
                self.showbuttons3 = self.buttonslist[1]
            


            self.showbuttons = pygame.transform.scale(self.showbuttons, (300,200))
            self.showbuttons2 = pygame.transform.scale(self.showbuttons2, (300,200))
            self.showbuttons3 = pygame.transform.scale(self.showbuttons3, (300,200))

            self.display_surface.blit(self.showbuttons , self.showbuttons_1)
            self.display_surface.blit(self.showbuttons2 , self.showbuttons_2)
            self.display_surface.blit(self.showbuttons3 , self.showbuttons_3)
                 



    def run (self):
        self.clicking = False
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                            self.clicking = True
                

            dt = self.clock.tick() / 1000

            self.display_surface.blit(self.bg, (0,0))
            self.display_surface.blit(self.midg, (0,0))
            self.display_surface.blit(self.foreg, (0,0))

            self.player.update(dt)
            self.display_surface.blit(self.player.image, self.player.rect)
            self.display_surface.blit(self.richard.image, self.richard.rect)

            self.buttons()

            pygame.display.update()


game = Game ()
game.run()     
pygame.quit()     