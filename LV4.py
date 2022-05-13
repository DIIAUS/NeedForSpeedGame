import pygame

pygame.init()

w=1200
h=600
#colour
white=(250,250,250)
din=(119,88,26)

#screenr

SCREEN=pygame.display.set_mode((w,h))
pygame.display.set_caption('NEED FOR SPEED' )
back_g = pygame.image.load('lv4.png')
#image
class Wall_H(pygame.sprite.Sprite):
        normal = pygame.image.load('padlv4_H_P.png')
        def __init__(self, position):
            super(Wall_H, self).__init__()
            self.rect = pygame.Rect(self.normal.get_rect())
            self.rect.center = position
            self.image = self.normal
class Wall_W(pygame.sprite.Sprite):
        normal = pygame.image.load('padlv4_W_P.png')
        def __init__(self, position):
            super(Wall_W, self).__init__()
            self.rect = pygame.Rect(self.normal.get_rect())
            self.rect.center = position
            self.image = self.normal

pad=[
        Wall_H((151,174)),
        Wall_H((197,175)),
        Wall_W((298,130)),
        Wall_H((151,300)),
        Wall_H((194,298)),
        Wall_H((151,424)),
        Wall_H((577,172)),
        Wall_H((195,424)),
        Wall_H((615,171)),
        Wall_H((544,284)),
        Wall_H((604,290)),
        Wall_H((955,547)),
        Wall_H((1001,542)),
        Wall_H((1051,542)),
        Wall_H((752,372)),
        Wall_H((797,374)),
        Wall_H((754,241)),
        Wall_H((801,244)),
        Wall_H((757,111)),
        Wall_H((804,114)),
        Wall_H((758,-12)),
        Wall_H((798,-15)),
        Wall_H((17,100)),
        Wall_H((15,248)),
        Wall_H((17,384)),
        Wall_H((15,511)),
        Wall_H((1187,91)),
        Wall_H((1190,217)),
        Wall_H((1187,345)),
        Wall_H((1185,472)),
        Wall_H((1188,598)),

        Wall_W((70,-10)),
        Wall_W((258,-10)),
        Wall_W((438,-10)),
        Wall_W((632,-10)),
        Wall_W((921,-10)),
        Wall_W((1115,-10)),
        Wall_W((470,137)),
        Wall_W((432,204)),
        Wall_W((428,255)),
        Wall_W((427,312)),
        Wall_W((322,457)),
        Wall_W((522,458)),
        Wall_W((734,455)),
        Wall_W((994,132)),
        Wall_W((994,284)),
        Wall_W((994,337)),
        Wall_W((994,387)),
        Wall_W((994,451)),
        Wall_W((88,587)),
        Wall_W((270,591)),
        Wall_W((455,592)),
        Wall_W((641,591)),
        Wall_W((828,588)),

    ]

pad_group = pygame.sprite.RenderPlain(*pad)
while True :

    SCREEN.blit(back_g,(0,0))
    pad_group.draw(SCREEN)





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
        pygame.display.flip()

