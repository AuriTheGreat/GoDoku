import pygame
import pygame_gui
import threading
from solver import Solver
from views.view import View
from views.solveview import SolveView
from views.inputboardview import InputBoardView

class GenerateChoice(View):
    def create_objects(self):
        self.generate_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 100), (100, 50)),text="Generate",
                                             manager=self.manager)

        self.input_board_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((110, 100), (150, 50)),text="Input Board",
                                             manager=self.manager)

        self.play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 540), (100, 50)),text="Play",
                                             manager=self.manager)

        self.play_button.disable()

        self.warninglabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 160), (780, 40)),text="Input the puzzle string below.",
                                             manager=self.manager)

        self.inputpuzzlestring=pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((10, 200), (780, 60)),
                                                    manager=self.manager)
        self.inputpuzzlestring.allowed_characters=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.running_generation=False

        self.waitinglabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((650, 0), (180, 40)),text="",
                                             manager=self.manager)

    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED and not self.running_generation:
            if event.ui_element == self.play_button:
                self.exit()
                SolveView(self.screen, {"board":self.inputpuzzlestring.text}).mainloop()
            if event.ui_element == self.generate_button:
                self.running_generation=True
                self.inputpuzzlestring.disable()
                t=threading.Thread(target=self.generate_board, daemon=True)
                t.start()
            if event.ui_element == self.input_board_button:
                boardstring=InputBoardView(self.screen, {"board": self.inputpuzzlestring.text}).mainloop()
                self.inputpuzzlestring.text=boardstring
                self.inputpuzzlestring.rebuild()
                self.check_length_of_input_field()
        if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            if event.ui_element==self.inputpuzzlestring:
                self.check_length_of_input_field()

    def update(self):
        if self.running_generation:
            #print(threading.main_thread())
            self.updatewaitingstatus()
            #print(self.waitinglabel.text)
        else:
            self.waitinglabel.text=""
            self.waitinglabel.rebuild()

    def check_length_of_input_field(self):
        self.play_button.disable()
        if len(self.inputpuzzlestring.text)==0:
            self.warninglabel.text="Input the puzzle string below."
        elif len(self.inputpuzzlestring.text)<81:
            self.warninglabel.text="String too short."
        elif len(self.inputpuzzlestring.text)>81:
            self.warninglabel.text="String too long."
        else:
            self.warninglabel.text=""
            self.play_button.enable()
        
        self.warninglabel.rebuild()

    def generate_board(self):
        solver=Solver()
        self.inputpuzzlestring.text=solver.board.returnPuzzleString()
        self.inputpuzzlestring.rebuild()
        self.check_length_of_input_field()
        self.running_generation=False
        self.inputpuzzlestring.enable()

    def updatewaitingstatus(self):
        text=""
        if self.waitinglabel.text=="Waiting":
            text="Waiting."
        elif self.waitinglabel.text=="Waiting.":
            text="Waiting.."
        elif self.waitinglabel.text=="Waiting..":
            text="Waiting..."
        else:
            text="Waiting"

        self.waitinglabel.text=text
        self.waitinglabel.rebuild()