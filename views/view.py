import pygame
import pygame_gui

#https://stackoverflow.com/questions/59781629/how-do-i-connect-a-page-to-a-button-pygame


class View():
    def __init__(self, screen, config):
        self.screen = screen
        self.config = config

        self.screen_rect = screen.get_rect()
        self.window_surface = pygame.display.set_mode(self.screen_rect.bottomright)
        self.background = pygame.Surface(self.screen_rect.bottomright)

        self.clock = pygame.time.Clock()
        self.is_running = False

        self.widgets = []

        self.manager = pygame_gui.UIManager(self.screen_rect.bottomright)

        self.create_objects()

    def quit(self):
        pass

    def create_objects(self):
        pass

    def handle_event(self, event):
        pass

    def update(self, ):
        pass

    def draw(self, surface):
        self.screen.blit(self.background, (0, 0))
        self.manager.draw_ui(self.window_surface)   

    def exit(self):
        self.is_running = False

    def mainloop(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.is_running = False

                self.handle_event(event)
                self.manager.process_events(event)

            self.update()

            self.screen.fill((0,0,0))

            self.draw(self.screen)
            pygame.display.update()

            tickrate=25

            self.clock.tick(tickrate)
            self.manager.update(tickrate/1000)

        self.quit()