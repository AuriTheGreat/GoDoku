from tkinter import CURRENT
import pygame
import pygame_gui
from collections import Counter


pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((550, 350), (100, 50)),text="",
                                             manager=manager)

sudoku_buttons=[]
for i in range(9):
    for j in range(9):
        sudoku_button = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((0+60*j, 0+60*i), (60, 60)),
                                            manager=manager)
        sudoku_button.allowed_characters=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        sudoku_button.font.size=30
        sudoku_buttons.append(sudoku_button)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == hello_button:
                  print('Hello World!')
                  new_hello_button=pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((550, 350), (100, 50)),
                                            manager=manager)
                  hello_button.remove()
        if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            if event.ui_element in sudoku_buttons:
                currentbutton=event.ui_element
                c = Counter(currentbutton.text)
                output = ''.join(k for k, v in c.items() if v == 1)
                currentbutton.text=("".join(sorted(output)))
                if len(currentbutton.text)==1:
                    currentbutton.font.size=50
                    currentbutton.padding=(13,0)
                else:
                    currentbutton.padding=(0,0)
                    if len(currentbutton.text)<6:
                        currentbutton.font.size=15
                        currentbutton.padding=(0.5+(6-len(currentbutton.text))*3,0)
                    else:
                        currentbutton.font.size=9
                        currentbutton.padding=(3+(9-len(currentbutton.text))*3,0)
                currentbutton.rebuild()

                print(("+" + "-"*9)*9 + "+")
                for count, i in enumerate(sudoku_buttons):
                    print("|" + i.text.center(9), end="")
                    if (count+1)%9==0:
                        print("|")
                        print(("+" + "-"*9)*9 + "+")
                print()

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()