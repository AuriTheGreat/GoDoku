from pyexpat.errors import messages
import pygame
import pygame_gui
from board import Board
from solver import Solver
from views.view import View
from collections import Counter
from views.inputboardview import InputBoardView

class SolveView(View):
    def create_objects(self):
        self.solve_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((550, 10), (240, 50)),text="Solve",
                                             manager=self.manager)
        self.bruteforce_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((550, 70), (240, 50)),text="Brute Force",
                                             manager=self.manager)
        self.partialsolve_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((550, 130), (240, 50)),text="Partial Solve",
                                             manager=self.manager)
        self.check_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((550, 190), (240, 50)),text="Check",
                                             manager=self.manager)
        self.messagebox = pygame_gui.elements.UITextEntryBox(relative_rect=pygame.Rect((550, 250), (240, 230)),
                                             manager=self.manager)
        self.messagebox.disable()
        self.messagebox.html_text=""
        self.messagebox.rebuild()

        self.edit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((550, 480), (240, 50)),text="Edit Board",
                                             manager=self.manager)
        self.quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((550, 540), (240, 50)),text="Quit",
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

        self.startpuzzlestring=self.config["board"]
        self.gameboard=Board(self.startpuzzlestring)
        self.paint_board_with_puzzlestring(self.startpuzzlestring, True)

    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            self.gameboard=Board(self.get_board_puzzlestring())
            self.solver=Solver(self.gameboard)
            self.messagebox.html_text=""
            if event.ui_element == self.check_button:
                if self.gameboard.isSolved():
                    self.messagebox.html_text="Correct!"
                    self.messagebox.rebuild()
                else:
                    self.messagebox.html_text="Wrong!"
                    self.messagebox.rebuild()
            if event.ui_element == self.solve_button:
                previousstring=self.gameboard.returnPuzzleString()
                outcome=self.solver.Solve()
                if not outcome:
                    self.gameboard.insertTiles(previousstring)
                    self.messagebox.html_text="Solution was not found.\nBrute-force is recommended."
                    self.messagebox.rebuild()
                self.paint_board_with_puzzlestring(self.gameboard.returnPuzzleString())
            if event.ui_element == self.partialsolve_button:
                outcome=self.solver.HelperSolve()
                if outcome:
                    self.paint_board_with_puzzlestring(self.gameboard.returnPuzzleString())
                    self.messagebox.html_text=self.solver.helperresponse
                    self.messagebox.rebuild()
            if event.ui_element == self.bruteforce_button:
                outcome=self.solver.BruteForceSolve()
                if self.solver.solutioncount==0:
                    self.messagebox.html_text="No solution."
                elif self.solver.solutioncount>1:
                    self.messagebox.html_text="Too many solutions."
                else:
                    self.messagebox.html_text=""
                self.messagebox.rebuild()
                if outcome:
                    self.paint_board_with_puzzlestring(self.gameboard.returnPuzzleString())
            if event.ui_element == self.edit_button:
                boardstring=InputBoardView(self.screen, {"board": self.config["board"]}).mainloop()
                self.exit()
                SolveView(self.screen, {"board":boardstring}).mainloop()
            if event.ui_element == self.quit_button:
                self.exit()
            self.messagebox.rebuild()
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
