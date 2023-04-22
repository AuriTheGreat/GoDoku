import pygame
import pygame_gui
from board import Board
from solver import Solver
from views.view import View
from collections import Counter

class InputBoardView(View):
    def create_objects(self):
        self.save_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((550, 540), (240, 50)),text="Save",
                                             manager=self.manager)

        self.sudoku_buttons=[]
        for i in range(9):
            for j in range(9):
                newmanager=pygame_gui.UIManager(self.screen_rect.bottomright)
                self.managers.append(newmanager)
                sudoku_button = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((10+60*j, 10+60*i), (60, 60)),
                                                    manager=newmanager)
                sudoku_button.allowed_characters=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                sudoku_button.hidden_text_char=[i,j]
                self.sudoku_buttons.append(sudoku_button)

        if not self.config["board"]:
            self.config["board"]="0"*81
        elif len(self.config["board"])>81:
            self.config["board"]=self.config["board"][:81]
        elif len(self.config["board"])<81:
            self.config["board"]=self.config["board"] + "0" * len(self.config["board"])

        self.paint_board_with_puzzlestring(self.config["board"])

    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.save_button:
                self.exit()
        if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            if event.ui_element in self.sudoku_buttons:
                self.adjust_button_theme(event.ui_element)

    def paint_board_with_puzzlestring(self, puzzlestring):
        for i in range(9):
            for j in range(9):
                sudoku_button=self.sudoku_buttons[i*9+j]
                newvalue=puzzlestring[i*9+j]
                if newvalue!="0":
                    sudoku_button.text=newvalue
                self.adjust_button_theme(sudoku_button)

    def get_board_puzzlestring(self):
        puzzlestring=""

        for i in self.sudoku_buttons:
            if len(i.text)==1:
                puzzlestring+=i.text
            else:
                puzzlestring+="0"

        return puzzlestring


    def adjust_button_theme(self, button):
        if len(button.text)==1:
            button.font.size=50
            button.padding=(13,0)
        button.rebuild()

    def mainloop(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    pygame.quit()
                    sys.exit()
                #elif event.type == pygame.KEYDOWN:
                #    if event.key == pygame.K_ESCAPE:
                #        self.is_running = False

                self.handle_event(event)
                for manager in self.managers:
                    manager.process_events(event)

            self.update()

            self.screen.fill((0,0,0))

            self.draw(self.screen)
            pygame.display.update()

            tickrate=25

            self.clock.tick(tickrate)
            for manager in self.managers:
                manager.update(tickrate/1000)

        self.quit()

        return self.get_board_puzzlestring()