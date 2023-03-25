import pygame
import pygame_gui
from views.view import View
from views.solveview import SolveView
from views.generatechoice import GenerateChoice

class MainMenu(View):
    def create_objects(self):
        self.play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 100), (100, 50)),text="Play",
                                             manager=self.manager)
        self.quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 160), (100, 50)),text="Quit",
                                             manager=self.manager)


    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            if event.ui_element == self.play_button:
                GenerateChoice(self.screen, self.config).mainloop()
            if event.ui_element == self.quit_button:
                self.exit()
                
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            #self.is_running = False
            self.exit()
            sv.SolveView(self.screen, self.config).mainloop()
        """