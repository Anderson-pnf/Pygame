import pygame as py

py.init()

screen = py.display.set_mode((1800,900))
branco = (255,255,255)
vermelho = (0,0,255)

largura, altura = 25,50
x,y = largura//2, altura//2
tamanho = 30
velocidade = 10


while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()

    teclas = py.key.get_pressed()

    if teclas [py.K_LEFT]:
        x-=velocidade

    if teclas [py.K_RIGHT]:
        x+=velocidade

    if teclas [py.K_UP]:
        y-=velocidade

    if teclas [py.K_DOWN]:
        y+=velocidade
    
    screen.fill(branco)
    py.draw.rect(screen,vermelho,(x,y,tamanho,largura))
    py.display.flip()
    py.time.Clock().tick(60)