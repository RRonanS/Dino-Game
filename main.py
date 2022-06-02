import pygame
from pygame.locals import *
from sys import exit
from codigos.dino import Dino
from codigos.nuvens import Nuvem
from codigos.chao import Chao
from codigos.cacto import Cacto
from codigos.ptero import Ptero
from codigos.cactoduplo import Cacto2
from codigos.armazenamento import salvar, recorde
from random import choice, randint, random

pygame.init()

# Variáveis do jogo
velocidade = 10
width, height, size = 640, 480, (640, 480)
branco = 255, 255, 255
preto = 0, 0, 0
invencivel = False # Coloque True para ignorar os obstáculos
pontos = 0

tela = pygame.display.set_mode(size)
pygame.display.set_caption('Dino Game')
relogio = pygame.time.Clock()
imagens = pygame.image.load('imgs/dinoSpritesheet.png').convert_alpha()
imagem_cacto2 = pygame.image.load('imgs/catoduplo.png').convert_alpha()

fonte = pygame.font.SysFont('arial', 30, True, True)
fonte_menor = pygame.font.SysFont('arial', 23, False, False)

som_colisao = pygame.mixer.Sound('sons/death_sound.wav')
som_pulo = pygame.mixer.Sound('sons/jump_sound.wav')
som_pontos = pygame.mixer.Sound('sons/score_sound.wav')

# Instanciamento dos objetos
lis_sprites = pygame.sprite.Group()
dino = Dino(imagens)
lis_sprites.add(dino)
for i in range(4):
    lis_sprites.add(Nuvem(imagens, size))
for i in range(width*2//64):
    lis_sprites.add(Chao(imagens, i*64))

inimigos = pygame.sprite.Group()
cacto = Cacto(imagens)
inimigos.add(cacto)
lis_sprites.add(cacto)

ptero = Ptero(imagens)
inimigos.add(ptero)
lis_sprites.add(ptero)

cacto2 = Cacto2(imagens, imagem_cacto2)
add_cacto2 = False
lis_sprites.add(cacto2)
inimigos.add(cacto2)

obstaculo = choice((0, 1))
recorde = recorde()
colidiu = False

while True:
    # Laço do jogo
    relogio.tick(30)
    tela.fill(branco)
    if colidiu and not invencivel:
        # Quando ocorre colisão, mostra texto de fim na tela
        txt1 = fonte.render('GAME OVER', True, preto)
        txt2 = fonte_menor.render('Pressione r para continuar', True, preto)
        tela.blit(txt1, (210, 220))
        tela.blit(txt2, (180, 243))
    else:
        # Não houve colisão, mostra textos de pontuação
        txt = f'Pontos: {pontos}'
        txt2 = f'Recorde: {recorde}'
        formatado = fonte.render(txt, True, preto)
        formatado2 = fonte_menor.render(txt2, True, preto)
        tela.blit(formatado, (450, 60))
        tela.blit(formatado2, (452, 87))

    for event in pygame.event.get():
        # Leitura dos eventos na tela
        if event.type == QUIT:
            # Fechamento da tela
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            # Tecla pressionada
            if pygame.key.get_pressed()[K_SPACE]:
                # Apertou espaço(pula)
                if not dino.pulo:
                    som_pulo.play()
                dino.pular()
            if pygame.key.get_pressed()[K_r] and colidiu:
                # Game over e apertou r, reinicia o jogo
                pontos = 0
                colidiu = False
                for inimigo in inimigos.sprites():
                    inimigo.rect.x = 700
                    inimigo.vel = 10
                dino.rect.center = (100, 416)
                dino.pulo = False

    colisoes = pygame.sprite.spritecollide(dino, inimigos, False, pygame.sprite.collide_mask)
    if colisoes:
        # Verifica se houve alguma colisão
        if not colidiu:
            # Faz o som de colisão e salva a pontuação, caso seja maior que o recorde
            som_colisao.play()
            salvar(pontos)
            if pontos > recorde:
                recorde = pontos
            colidiu = True
        if invencivel:
            # Caso esteja configurado para ser invencível ignora a colisão e atualiza
            pontos += 1
            lis_sprites.update()
    else:
        pontos += 1
        lis_sprites.update()

    if pontos % 100 == 0 and not colidiu:
        # A cada 100 pontos aumenta a velocidade dos obstaculos e reproduz um som
        som_pontos.play()
        for inimigo in inimigos.sprites():
            if inimigo.vel < 23:
                inimigo.vel += 1
                velocidade += 1

    if obstaculo == 0 and not cacto.atualizar or obstaculo == 1 and not ptero.atualizar:
        # Decide quais obstaculos aparecerão na tela
        obstaculo = choice((0, 1))
        if obstaculo == 0:
            cacto.atualizar = True
            if pontos >= 300:
                chance = 150/pontos
                esc = random()
                if chance <= esc:
                    add_cacto2 = True
        else:
            ptero.atualizar = True

    if add_cacto2 and not ptero.atualizar:
        # Ainda no processo de selecionar obstaculos para a tela
        if 640 - cacto.rect.x >= 100:
            chance = randint(1, 10)
            if chance >= 6:
                cacto2.atualizar = True
                add_cacto2 = False

    lis_sprites.draw(tela)
    pygame.display.flip()
