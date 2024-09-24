import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tree_img = pg.image.load("fig/3.png")
    tree_img =pg.transform.flip(tree_img,True,False)
    bg_img_1 =pg.transform.flip(bg_img,True,False)
    tree_img_rect=tree_img.get_rect()
    tree_img_rect.center=300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst=pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            tree_img_rect.move_ip((0,-1))
        elif key_lst[pg.K_DOWN]:
            tree_img_rect.move_ip((0,1))
        elif key_lst[pg.K_RIGHT]:
            tree_img_rect.move_ip((1,0))
        elif key_lst[pg.K_LEFT]:
            tree_img_rect.move_ip((-1,0))
        if tmr >= 3200:
            tmr=0
        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img_1, [1600-tmr, 0])
        screen.blit(bg_img, [3200-tmr, 0])
        screen.blit(bg_img_1, [4800-tmr, 0])

        screen.blit(tree_img,tree_img_rect)


        pg.display.update()
        tmr += 1
        clock.tick(1600)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()