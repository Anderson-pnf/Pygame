import pygame

pygame.init()

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

screen = pygame.display.set_mode((1800, 900))
pygame.display.set_caption('Pong')

raquete = pygame.Surface((20, 300))
raquete.fill(AZUL)

bola = pygame.Surface((20, 20))
bola.fill(PRETO)

raquete1_x, raquete1_y = 1750,50 
raquete2_x, raquete2_y = 50, 1
bola_x, bola_y = 900, 450

raquete_largura, raquete_altura = raquete.get_width(), raquete.get_height()

pontos_player1 = 0
pontos_player2 = 0

fonte = pygame.font.SysFont('Arial', 30)

velocidade_raquete = 20
velocidade_bola_x = 15
velocidade_bola_y = 15

def reiniciar_bola():
    global bola_x, bola_y, velocidade_bola_x, velocidade_bola_y
    bola_x, bola_y = 900,300
    velocidade_bola_x = -velocidade_bola_x
    velocidade_bola_y = 15

def desenhar():
    screen.fill(BRANCO)
    screen.blit(raquete, (raquete1_x, raquete1_y))
    screen.blit(raquete, (raquete2_x, raquete2_y))
    screen.blit(bola, (bola_x, bola_y))

    pontos_textos = fonte.render(f'{pontos_player1} - {pontos_player2}', True, VERMELHO)
    screen.blit(pontos_textos, (900, 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_UP]:
        raquete1_y -= velocidade_raquete
    if teclas[pygame.K_DOWN]:
        raquete1_y += velocidade_raquete
    if teclas[pygame.K_w]:
        raquete2_y -= velocidade_raquete
    if teclas[pygame.K_s]:
        raquete2_y += velocidade_raquete

    bola_x += velocidade_bola_x
    bola_y -= velocidade_bola_y

    if bola_y <= 0 or bola_y >= 900 - bola.get_height():
        velocidade_bola_y = -velocidade_bola_y
    if (bola_x <= raquete1_x + raquete_largura and bola_x >= raquete1_x and bola_y + bola.get_height() > raquete1_y and bola_y < raquete1_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x
    if (bola_x <= raquete2_x + raquete_largura and bola_x >= raquete2_x and bola_y + bola.get_height() > raquete2_y and bola_y < raquete2_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x
    if raquete1_y < 0:
        raquete1_y = 0
    if raquete1_y > 900 - raquete_altura:
        raquete1_y = 900 - raquete_altura
    if raquete2_y < 0:
        raquete2_y = 0
    if raquete2_y > 900 - raquete_altura:
        raquete2_y = 900 - raquete_altura
    

    if bola_x <= 0:
        pontos_player2 += 1
        reiniciar_bola()
    elif bola_x >= 1800 - bola.get_width():
        pontos_player1 += 1
        reiniciar_bola()

    desenhar()
    pygame.display.update()
    pygame.time.Clock().tick(60)
