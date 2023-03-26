import pygame
import views.mainmenu as mainmenu

if __name__ == "__main__":
    screen_size=(800,600)
    pygame.init()
    
    pygame.display.set_caption('Sudoku God')
    pygame.display.set_icon(pygame.image.load('icon.png'))
    screen = pygame.display.set_mode(screen_size)
    config = {}
    background = pygame.Surface(screen_size)
    background.fill(pygame.Color('#000000'))
    menu=mainmenu.MainMenu(screen, config)
    menu.mainloop()

    #005900000080000000000003007010060030900002004007800500006400800090000020300001005
    #125900000080000000000003007010060030900002004007800500006400800090000020300001005

    #easy elimination
    #000000079805074100460100038000658910006917004019432087008206040602000091000500006
    #000105000140000670080002400063070010900000003010090520007200080026000035000409000

    #hidden singles
    #000004028406000005100030600000301000087000140000709000002010003900000507670400000