from config import * 


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Richard_Math_Marathon")

        self.clock = pygame.time.Clock()

        self.running = True

        self.setup()


    def setup(self):

        self.bg = pygame.image.load(os.path.join(BASE_DIR, 'data', 'images', 'Background.png')).convert_alpha()
        self.bg = pygame.transform.scale(self.bg,(WINDOW_WIDTH, WINDOW_HEIGHT))

        self.midg = pygame.image.load(os.path.join(BASE_DIR, 'data', 'images', 'Midground.png')).convert_alpha()
        self.midg = pygame.transform.scale(self.midg,(WINDOW_WIDTH, WINDOW_HEIGHT - 100))

        self.foreg = pygame.image.load(os.path.join(BASE_DIR, 'data', 'images', 'Foreground.png')).convert_alpha()
        self.foreg = pygame.transform.scale(self.foreg,(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run (self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.display_surface.blit(self.bg, (0,0))
            self.display_surface.blit(self.midg, (0,0))
            self.display_surface.blit(self.foreg, (0,0))

            pygame.display.update()


game = Game ()
game.run()     
pygame.quit()     