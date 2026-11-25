from config import * 


class Player(pygame.sprite.Sprite):
    def __init__ (self, pos, groups):
        #self.image =  pygame.image.load(os.path.join(BASE_DIR, 'data', 'Player', 'person0.png')).convert_alpha()
        self.frames_right = [
            pygame.image.load (os.path.join(BASE_DIR, 'data', 'Player', 'person0.png')).convert_alpha(),
            pygame.image.load (os.path.join(BASE_DIR, 'data', 'Player', 'person1.png')).convert_alpha(),
            pygame.image.load (os.path.join(BASE_DIR, 'data', 'Player', 'person2.png')).convert_alpha()
            ]
        
        self.moving = True

        self.clock = pygame.time.Clock
        
        self.frame_index = 0
        self.animation_speed = 8
        self.facing = 'right'
        self.image = self.frames_right[0]

        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_frect(center = pos)

        


    def animation(self, dt):
            
                    
                    frames = self.frames_right
                         

                    
                    if self.moving:
                         self.frame_index += self.animation_speed *dt 
                         self.frame_index %= len(frames)
                    else:
                         self.frame_index = 0

                    self.image = frames[int(self.frame_index)]

                    self.image = pygame.transform.scale(self.image, (100,100))

                         
    def update(self, dt):
        
        self.animation(dt)

class Richard(pygame.sprite.Sprite):
    def __init__ (self, pos, groups):
            self.image =  pygame.image.load(os.path.join(BASE_DIR, 'data', 'Richard', 'richard0.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (300,300))
            self.rect = self.image.get_frect(center = pos)