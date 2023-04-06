import pygame
import pygame_gui
from board import Board
from solver import Solver
from views.view import View
from collections import Counter

class SolveView(View):
    def create_objects(self):
        self.solve_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 10), (140, 50)),text="Solve",
                                             manager=self.manager)
        self.check_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 70), (140, 50)),text="Check",
                                             manager=self.manager)
        self.correctnesslabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((650, 120), (140, 40)),text="",
                                             manager=self.manager)
        self.quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 540), (140, 50)),text="Quit",
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

        puzzlestring=self.config["board"]
        self.gameboard=Board(puzzlestring)
        self.paint_board_with_puzzlestring(puzzlestring, True)

    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            self.gameboard=Board(self.get_board_puzzlestring())
            self.solver=Solver(self.gameboard)
            if event.ui_element == self.check_button:
                if self.gameboard.isSolved():
                    self.correctnesslabel.text="Correct!"
                    self.correctnesslabel.rebuild()
                else:
                    self.correctnesslabel.text="Wrong!"
                    self.correctnesslabel.rebuild()
            if event.ui_element == self.solve_button:
                outcome=self.solver.Solve()
                self.paint_board_with_puzzlestring(self.gameboard.returnPuzzleString())
                if not outcome:
                    self.correctnesslabel.text="No solution."
                    self.correctnesslabel.rebuild()
            if event.ui_element == self.quit_button:
                self.exit()
        if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            if event.ui_element in self.sudoku_buttons:
                self.adjust_button_theme(event.ui_element)


    def paint_board_with_puzzlestring(self, puzzlestring, initial=False):
        for i in range(9):
            for j in range(9):
                sudoku_button=self.sudoku_buttons[i*9+j]
                newvalue=puzzlestring[i*9+j]
                if newvalue!="0":
                    sudoku_button.text=newvalue
                    if initial:
                        sudoku_button.disable()
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
        c = Counter(button.text)
        output = ''.join(k for k, v in c.items() if v == 1)
        button.text=("".join(sorted(output)))
        self.gameboard.tiles[button.hidden_text_char[0]][button.hidden_text_char[1]].value=button.text
        if len(button.text)==1:
            button.font.size=50
            button.padding=(13,0)
        else:
            button.padding=(0,0)
            if len(button.text)<6:
                button.font.size=15
                button.padding=(0.5+(6-len(button.text))*3,0)
            else:
                button.font.size=9
                button.padding=(3+(9-len(button.text))*3,0)

        if not button.is_enabled:
            button.text_colour=(255, 241, 27)
            button.text_cursor_colour=(33, 40, 45)
        button.rebuild()
