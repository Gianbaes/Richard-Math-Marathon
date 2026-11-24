from config import * 


class Player(pygame.sprite.Sprite):
    def __init__ (self, pos, groups):
        self.image =  pygame.image.load(os.path.join(BASE_DIR, 'data', 'Player', 'person0.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_frect(center = pos)

class Richard(pygame.sprite.Sprite):
    def __init__ (self, pos, groups):
            self.image =  pygame.image.load(os.path.join(BASE_DIR, 'data', 'Richard', 'richard0.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (300,300))
            self.rect = self.image.get_frect(center = pos)