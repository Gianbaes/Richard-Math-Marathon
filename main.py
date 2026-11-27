from config import * 
from sprites import Player, Richard
import json
import random
import time

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Richard_Math_Marathon")

        self.clock = pygame.time.Clock()

        self.running = True
        self.score = 0
        self.highscore = 0
        self.clicking = False
        self.input = None
        self.questionanswered = 0
        self.delayBetweenQuest = 0
        self.loselives = False
        self.losethegame = False
        self.lives = 3

        self.buttonpressed = 0

        self.player = Player((WINDOW_WIDTH//2 - 500, WINDOW_HEIGHT//2 + 100), [])
        self.richard = Richard((WINDOW_WIDTH//2 + 500, WINDOW_HEIGHT//2 + 50), [])

        


        self.setup()



    def setup(self):
        

        if os.path.exists("score.json"):
            with open("score.json", "r") as highscore :
                  self.highscore = json.load(highscore)["HIGH_SCORE"]

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

        

        self.questions_equations = {
            "Ans7.5" : pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Equations', 'Ans7.5.png')).convert_alpha(),
            "Ans12" :pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Equations', 'Ans12.png')).convert_alpha(),
            "Ans13" :pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Equations', 'Ans13.png')).convert_alpha(),
            "Ans17" :pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Equations', 'Ans17.png')).convert_alpha(),
            "Ans17(2)" :pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Equations', 'Ans17(2).png')).convert_alpha()
        }

       

        self.questions_formulas = {
            "F-test" : pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Formulas', 'F-test.png')).convert_alpha(),
            "T-test" : pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Formulas', 'T-test.png')).convert_alpha(),
            "Mean" : pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Formulas', 'Mean.png')).convert_alpha(),
            "Median_even" : pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Formulas', 'Median_even.png')).convert_alpha(),
            "Median_odd" : pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Formulas', 'Median_odd.png')).convert_alpha(),
            "Range" : pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Formulas', 'Range.png')).convert_alpha(),
            "STD" : pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Formulas', 'STD.png')).convert_alpha(),
            "Var" : pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Formulas', 'Var.png')).convert_alpha()
        }

       

        self.questions_examples = {
            "Modeexamp" : pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Examples', 'Modeexamp.png')).convert_alpha(),
            "Medianexamp" : pygame.image.load(os.path.join(BASE_DIR, 'data', 'Questions', 'Examples', 'Medianexamp.png')).convert_alpha(),
        }

        
        
        self.options = {
            "Ans7.5" : [7.5,9,5],
            "Ans12" : [12,5,8],
            "Ans13" : [8,9,13],
            "Ans17" : [15,16,17],
            "Ans17(2)" : [15,19,17],
            "F-test" : ["F-test","Mean","T-test"],
            "T-test" : ["Range","F-test","T-test"],
            "Mean" : ["StdDeviation","Mean","F-test"],
            "Median_even" : ["Median_even","Mean","Var"],
            "Median_odd" : ["Mode","Median_even","Median_odd"],
            "Range" : ["Mean","Range","Mode"],
            "STD" : ["Variance","StdDeviation","T-test"],
            "Var" : ["Range","StdDeviation","Variance"],
            "Modeexamp" : ["Mean","Mode","Range"],
            "Medianexamp" : ["Median","Mean","Variance"]
        }

        self.answers = {
            "Ans7.5" : 7.5,
            "Ans12" : 12,
            "Ans13" : 13,
            "Ans17" : 17,
            "Ans17(2)" : 17,
            "F-test" : "F-test",
            "T-test" : "T-test",
            "Mean" : "Mean",
            "Median_even" : "Median_even",
            "Median_odd" : "Median_odd",
            "Range" : "Range",
            "STD" : "StdDeviation",
            "Var" : "Variance",
            "Modeexamp" : "Mode",
            "Medianexamp" : "Median"
        }

        self.questions = (
                    list(self.questions_equations.keys()) +
                    list(self.questions_formulas.keys()) +
                    list(self.questions_examples.keys())
        
        )

        self.thequestion = random.choice(self.questions)

        self.optionsforquest = self.options[self.thequestion]
        self.answerforquest = self.answers[self.thequestion]

        random.shuffle(self.optionsforquest)

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


            print(self.input)
            print(self.answerforquest)
            a, b, c = self.optionsforquest

            #assign self.input on button press
            
            if mouse_alligned_button1 and self.clicking and self.buttonpressed == 0:
                self.input = a
                self.buttonpressed = 1
                
            elif mouse_alligned_button2 and self.clicking and self.buttonpressed == 0:
                self.input = b
                self.buttonpressed = 2
      
            elif mouse_alligned_button3 and self.clicking and self.buttonpressed == 0:
                self.input = c
                self.buttonpressed = 3



            #button press anf if correct and incorrect chnge button image respectively
                
            if self.buttonpressed == 1:   
                if self.input == self.answerforquest :
                    print("correct")
                    
                    
                    self.showbuttons = self.buttonslist[2]
                elif self.input == None:
                    pass
                    
                else: 
                    print("inc")
                    self.showbuttons = self.buttonslist[3]
                    
            elif self.buttonpressed == 2: 
                if self.input == self.answerforquest :
                    print("correct")
                                        
                    self.showbuttons2 = self.buttonslist[2]
                elif self.input == None:
                    pass
                else: 
                    print("inc")
                    self.showbuttons2 = self.buttonslist[3]
                    
            elif self.buttonpressed == 3:
                if self.input == self.answerforquest :
                    print("correct")
                                        
                    self.showbuttons3 = self.buttonslist[2]
                elif self.input == None:
                    pass
                else: 
                    print("inc")
                    self.showbuttons3 = self.buttonslist[3]
                    
                    




            if self.input == self.answerforquest and self.delayBetweenQuest == 0 :
                self.delayBetweenQuest = pygame.time.get_ticks()
                self.questionanswered += 1
                
            elif self.input == None:
                
                pass
            
            if self.input != self.answerforquest and self.input is not None and not self.loselives  :
                
                self.delayBetweenQuest = pygame.time.get_ticks()
                self.lives -= 1

                self.loselives = True

            

            if self.delayBetweenQuest != 0 : #delayy before nect question
                    elapsed = pygame.time.get_ticks() - self.delayBetweenQuest 

                    if elapsed >= 1000 :
                            self.nextquest()
                            self.delayBetweenQuest = 0
                            elapsed = 0
            

            self.showbuttons = pygame.transform.scale(self.showbuttons, (300,200))
            self.showbuttons2 = pygame.transform.scale(self.showbuttons2, (300,200))
            self.showbuttons3 = pygame.transform.scale(self.showbuttons3, (300,200))

            self.display_surface.blit(self.showbuttons , self.showbuttons_1)
            self.display_surface.blit(self.showbuttons2 , self.showbuttons_2)
            self.display_surface.blit(self.showbuttons3 , self.showbuttons_3)

            
                

            font = pygame.font.Font(None, 40)
            a = font.render(str(a), True, "Blue")
            a_rect = a.get_rect(center = (self.showbuttons_1.centerx - 0, self.showbuttons_1.centery + 20))
            self.display_surface.blit(a, a_rect)

            font = pygame.font.Font(None, 40)
            b = font.render(str(b), True, "Blue")
            b_rect = b.get_rect(center = (self.showbuttons_2.centerx - 0, self.showbuttons_2.centery + 20))
            self.display_surface.blit(b, b_rect)

            font = pygame.font.Font(None, 40)
            c = font.render(str(c), True, "Blue")
            c_rect = c.get_rect(center = (self.showbuttons_3.centerx - 0, self.showbuttons_3.centery + 20))
            self.display_surface.blit(c, c_rect)
                      
    def questionsfunc(self):

         
        if self.thequestion in self.questions_equations:
            image = self.questions_equations[self.thequestion]
        elif self.thequestion in self.questions_formulas:
            image = self.questions_formulas[self.thequestion]
        elif self.thequestion in self.questions_examples:
            image = self.questions_examples[self.thequestion]

        image =  pygame.transform.scale(image, (250,100))

        self.display_surface.blit(image, self.richard.rect)

    def nextquest(self):
        self.setup()
        
        self.buttonpressed = 0
        self.input = None
        self.loselives = False
    
        self.questionsfunc()

    def lose(self):
            
        clicking = False
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicking = True

        LOSEdow = pygame.image.load(os.path.join(BASE_DIR,'data', 'images', 'LoseDOW.png')).convert_alpha()
        LOSEdow = pygame.transform.scale(LOSEdow, (1000, 500))

        mouse_X, mouse_Y = pygame.mouse.get_pos()


        font = pygame.font.Font(None, 100)
        retry_text = font.render(f"Retry", True, "Red")
        retry_rect = retry_text.get_rect(center =
                                        (650,510)
                                    )
            
        self.display_surface.blit( LOSEdow, (150,120))

        
        self.display_surface.blit (retry_text, retry_rect)
        
        mouse_alligned_retry = retry_rect.collidepoint((mouse_X, mouse_Y)) 
            
        

        if mouse_alligned_retry and clicking == True :
                game = Game ()
                game.run()             
            
            
                return

        pygame.display.update()
        
    def run (self):


        self.clicking = False
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                            self.clicking = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                            self.clicking = False
                

            dt = self.clock.tick() / 1000

            self.score += dt * 2

            font = pygame.font.Font(None, 50)
            timer = font.render(f"Score: {int(self.score)}", True, "Blue")

            with open("score.json", "w") as highscore :
                        json.dump({"HIGH_SCORE" : self.score}, highscore)
                       

            font = pygame.font.Font(None, 50)
            highesttimer = font.render(f"HighScore: {int(self.highscore)}", True, "Blue")

            if self.highscore <= self.score :
                 highesttimer = timer

            if self.lives <= 0 :
                self.losethegame = True

            if self.losethegame:
                self.lose()

            font = pygame.font.Font(None, 50)
            star = font.render(f"Star: {int(self.questionanswered)}", True, "Yellow")

            font = pygame.font.Font(None, 50)
            lives = font.render(f"Lives: {int(self.lives)}", True, "Red")

            self.display_surface.blit(self.bg, (0,0))
            self.display_surface.blit(self.midg, (0,0))
            self.display_surface.blit(self.foreg, (0,0))
            self.display_surface.blit(lives, ( 10,20))
            self.display_surface.blit(timer, ( 300,20))
            self.display_surface.blit(highesttimer, ( 600,20))
            self.display_surface.blit(star, ( 1000,20))

            self.player.update(dt)
            self.display_surface.blit(self.player.image, self.player.rect)
            self.display_surface.blit(self.richard.image, self.richard.rect)


            self.buttons()
            self.questionsfunc()
            
            pygame.display.update()


game = Game ()
game.run()     
pygame.quit()     