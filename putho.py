from graphics import *
import time
import random
from pygame import mixer
def play_music(music_file, volume=0.8):


    freq = 50100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    mixer.init(freq, bitsize, channels, buffer)

    mixer.music.set_volume(volume)
    
    try:
        mixer.music.load(music_file)
        
    except error:
        
        return
    mixer.music.play(-1)

volume = 0.8
music_file = "song.mp3"

menu = GraphWin("10",500,500)
menutexto= Text(Point(250,250),"Clique para jogar")
menutexto.draw(menu)
menu.getMouse()
menutexto.setText("Clique na tela para avançar os diálogos")
menu.getMouse()
menutexto.setText("Recomendo o uso de fones\n (a musica é bem maneirinha)")
menu.getMouse()
menutexto.setText("Use as setas para se mover para os lados e espaço para atirar")
menu.getMouse()
menutexto.setText("Você só tem 3 vidas, cuidado.")
menu.getMouse()
menutexto.setText("Divirta-se :D")
menu.getMouse()
menutexto.setText("Tem teclas no teclado que \n ativam audios secretos\n tente por sua conta em risco.")
menu.getMouse()
menu.close()
menuon=False

musica = random.randint(5,8)

play_music(music_file, volume)


win=GraphWin("11",1000,1000)
win.setBackground(color_rgb(255,255,255))
mickeytriste = Image(Point(500,700),'mickeytriste.gif')
falamickey = Text(Point(500,200),"nossa nem me chamaram")
falaminnie = Text(Point(500,500),'É mesmo kkkk')
falapateta = Text(Point(700,500),"E nem chamamo o mickey kkkk")
faladonald = Text(Point(300,500),"Nossa que festa boa jjjkk")
Donald = Image(Point(300,800),"Donald.gif")
minnie = Image(Point(500,800),'Minnie.gif')
patep = Image(Point(700,800),"patetin.gif")
Donald.draw(win)
minnie.draw(win)
patep.draw(win)


win.getMouse()
faladonald.setTextColor('blue')
faladonald.draw(win)
win.getMouse()
faladonald.undraw()
falaminnie.setTextColor('red')
falaminnie.draw(win)
win.getMouse()
falaminnie.undraw()
falapateta.setTextColor('green')
falapateta.draw(win)
win.getMouse()
falapateta.undraw()
Donald.undraw()
minnie.undraw()
patep.undraw()
mickeytriste.draw(win)
win.getMouse()
falamickey.draw(win)
win.getMouse()
falamickey.setText("vo matar vocês lkkkjkjlkjlkj")
win.getMouse()
falamickey.undraw()
mickeytriste.undraw()

music_file = "track("+str(musica)+").ogg"

play_music(music_file, volume)
fundo = Image(Point(500,500),"fundo.png")

boneco = Image(Point(500,900),"mickey.png")
enemies = 1
enemy = Image(Point(150,150),"enemy("+str(enemies)+").gif")
welcome = Text(Point(300,900),"jogo do mickey")

startgame = Text(Point(900,900),"aperta ai pra começar")
winmessage = Text(Point(500,100),"PARABÉNS, VOCÊ ACABOU COM OS TRAIDORES!")
losemessage = Text(Point(500,100),"PERDEU!")



fundo.draw(win)

boneco.draw(win)
time.sleep(1)
welcome.draw(win)
time.sleep(1)
startgame.draw(win)
win.getMouse()
welcome.undraw()
startgame.undraw()
enemy.draw(win)
errorcount = 0
num1= random.randint(150,790)
num2= random.randint(150,790)
error = Image(Point(num1,num2),"tenor.png")
erros = Text(Point(100,900),"Erros:")
erros.draw(win)
direcaoinimigo=10
shot=False
shotinimigo=False
contaerros = Text(Point(130,900),str(errorcount))
direcaotiro=-40
pos = boneco.getAnchor()
enemypos = enemy.getAnchor()
tiro = Image(Point(pos.x,pos.y-100),"laser.png")
tiroinimigo = Image(Point(enemypos.x,enemypos.y+100),"laser.png")
c=0
tempo=0
vidainimigos=enemies
velocidade=1
vidastuas=2
contvida = Text(Point(900,750),'Vidas:'+str(vidastuas+1))
contvidainimigo = Text(Point(900,780),'Vidas do Inimigo:'+str(vidainimigos+1))
contvida.draw(win)
contvidainimigo.draw(win)
while True:
    if menuon==True:
        music_file = "song.mp3"
        volume = 0.8
        menu = GraphWin("10",500,500)
        menutexto= Text(Point(250,250),"Clique para recomeçar")
        menutexto.draw(menu)
        menu.getMouse()
        menu.close()
        menuon=False
        play_music(music_file, volume)
        
        win=GraphWin("11",1000,1000)
        win.setBackground(color_rgb(255,255,255))
        mickeytriste = Image(Point(500,700),'mickeytriste.gif')
        falamickey = Text(Point(500,200),"nossa nem me chamaram")
        falaminnie = Text(Point(500,500),'É mesmo kkkk')
        falapateta = Text(Point(700,500),"E nem chamamo o mickey kkkk")
        faladonald = Text(Point(300,500),"Nossa que festa boa jjjkk")
        Donald = Image(Point(300,800),"Donald.gif")
        minnie = Image(Point(500,800),'Minnie.gif')
        patep = Image(Point(700,800),"patetin.gif")
        Donald.draw(win)
        minnie.draw(win)
        patep.draw(win)


        win.getMouse()
        faladonald.setTextColor('blue')
        faladonald.draw(win)
        win.getMouse()
        faladonald.undraw()
        falaminnie.setTextColor('red')
        falaminnie.draw(win)
        win.getMouse()
        falaminnie.undraw()
        falapateta.setTextColor('green')
        falapateta.draw(win)
        win.getMouse()
        falapateta.undraw()
        Donald.undraw()
        minnie.undraw()
        patep.undraw()
        mickeytriste.draw(win)
        win.getMouse()
        falamickey.draw(win)
        win.getMouse()
        falamickey.setText("vo matar vocês lkkkjkjlkjlkj")
        win.getMouse()
        falamickey.undraw()
        mickeytriste.undraw()
        musica = random.randint(5,8)
        music_file = "track("+str(musica)+").ogg"

        play_music(music_file, volume)
        fundo = Image(Point(500,500),"fundo.png")

        boneco = Image(Point(500,900),"mickey.png")
        enemies = 1
        enemy = Image(Point(150,150),"enemy("+str(enemies)+").gif")
        welcome = Text(Point(300,900),"jogo do mickey")

        startgame = Text(Point(900,900),"aperta ai pra começar")
        winmessage = Text(Point(500,100),"PARABÉNS, VOCÊ ACABOU COM OS TRAIDORES!")
        losemessage = Text(Point(500,100),"PERDEU!")



        fundo.draw(win)

        boneco.draw(win)
        time.sleep(1)
        welcome.draw(win)
        time.sleep(1)
        startgame.draw(win)
        win.getMouse()
        welcome.undraw()
        startgame.undraw()
        enemy.draw(win)
        errorcount = 0
        num1= random.randint(150,790)
        num2= random.randint(150,790)
        error = Image(Point(num1,num2),"tenor.png")
        erros = Text(Point(100,900),"Erros:")
        erros.draw(win)
        direcaoinimigo=10
        shot=False
        shotinimigo=False
        contaerros = Text(Point(130,900),str(errorcount))
        direcaotiro=-40
        pos = boneco.getAnchor()
        enemypos = enemy.getAnchor()
        tiro = Image(Point(pos.x,pos.y-100),"laser.png")
        tiroinimigo = Image(Point(enemypos.x,enemypos.y+100),"laser.png")
        c=0
        tempo=0
        vidainimigos=enemies-1
        velocidade=1
        vidastuas=2
        contvida = Text(Point(900,750),'Vidas:'+str(vidastuas+1))
        contvidainimigo = Text(Point(900,780),'Vidas do Inimigo:'+str(vidainimigos+1))
        contvida.draw(win)
        contvidainimigo.draw(win)


    contaerros.setText(str(errorcount))



    pos = boneco.getAnchor()

    enemypos = enemy.getAnchor()
    movimento = win.checkKey()
    num1= random.randint(150,790)
    num2= random.randint(150,790)
    if enemypos.getX()<900 and enemypos.getX()>149:
        enemy.move(direcaoinimigo,0)
    else:
        direcaoinimigo*=-1
        enemy.move(direcaoinimigo,0)

    if tempo%2==0 and tempo !=0 and enemies<4:
        tiroinimigo = Image(Point(enemypos.x,enemypos.y+100),"laser.png")
        tiroinimigo.draw(win)
        shotinimigo=True
        tempo=0
        c=0
    if enemies>3 and enemies<7 and tempoquebrado%2 ==0 and tempo!=0:
        tiroinimigo = Image(Point(enemypos.x,enemypos.y+100),"laser.png")
        tiroinimigo.draw(win)
        shotinimigo=True
        tempo=0
        c=0
    if enemies==7 and tempo%1==0 and tempo!=0:
        tiroinimigo = Image(Point(enemypos.x,enemypos.y+100),"laser.png")
        tiroinimigo.draw(win)
        shotinimigo=True
        tempo=0
        c=0

    if shotinimigo==True:
        tiroinimigo.move(0,-direcaotiro/2)
    if tiroinimigo.getAnchor().getY() > 1000:
        tiroinimigo.undraw()
    if tiroinimigo.getAnchor().getX() <= pos.getX() + 78 and tiroinimigo.getAnchor().getX() >= pos.getX() -78 and tiroinimigo.getAnchor().getY() >= pos.getY() and tiroinimigo.getAnchor().getY() < 1000 and vidastuas!=0:
        tiroinimigo.undraw()
        tiroinimigo = Image(Point(enemypos.x,enemypos.y+100),"laser.png")
        vidastuas-=1
        contvida.setText("Vidas:"+str(vidastuas+1))
    if tiroinimigo.getAnchor().getX() <= pos.getX() + 78 and tiroinimigo.getAnchor().getX() >= pos.getX() -78 and tiroinimigo.getAnchor().getY() >= pos.getY() and tiroinimigo.getAnchor().getY() < 1000 and vidastuas==0 :
        boom = Image(Point(pos.x,pos.y),"boom.gif")
        boneco.undraw()
        boom.draw(win)
        losemessage.draw(win)
        pg.mixer.music.stop()
        win.getKey()
        win.close()
        music_file = "grito.mp3"
        play_music(music_file, volume)
        win2=GraphWin("12",720,600)
        fundo2 = Image(Point(250,250),"fundo2.png")
        fundo2.draw(win2)
        time.sleep(3)
        win2.close()
        pg.mixer.music.stop()
        win3= GraphWin("13",500,500)

        creditos = Text(Point(250,250),'Créditos:')
        autor  = Text(Point(250,300),'Arthur do Amaral.')
        creditos.draw(win3)
        time.sleep(1)
        autor.draw(win3)

        time.sleep(5)
        win3.close()
        menuon=True




    if movimento == 'm':
        music_file = "track(1).ogg"
        play_music(music_file, volume)
    if movimento == '0':
        music_file = "track(2).ogg"
        play_music(music_file, volume) 
    if movimento == '4':
        music_file = "track(3).ogg"
        play_music(music_file, volume)   
    if movimento == 't':
        music_file = "track(4).ogg"
        play_music(music_file, volume)      

    if movimento == "Right":
        boneco.move(10*velocidade,0)
    if movimento == "Left":
        boneco.move(-10*velocidade,0)
    if movimento == "space" and shot==False:
        tiro = Image(Point(pos.x,pos.y-100),"laser.png")
        tiro.draw(win)
        error.undraw()

        shot = True

    if shot == True:


        tiro.move(0,direcaotiro)

    if tiro.getAnchor().getX() <= enemypos.getX() + 110 and tiro.getAnchor().getX() >= enemypos.getX() - 130 and tiro.getAnchor().getY() <= enemypos.getY() and tiro.getAnchor().getY() > 0 and vidainimigos!=0:
        shot=False 
        tiro.undraw()
        tiro = Image(Point(pos.x,pos.y-100),"laser.png")
        vidainimigos-=1
        contvidainimigo.setText('Vidas do Inimigo:'+str(vidainimigos+1))

    if tiro.getAnchor().getX() <= enemypos.getX() + 110 and tiro.getAnchor().getX() >= enemypos.getX() - 130 and tiro.getAnchor().getY() <= enemypos.getY() and tiro.getAnchor().getY() > 0 and vidainimigos<=0:
        shot=False 
        tiro.undraw()
        tiro = Image(Point(pos.x,pos.y-100),"laser.png")
        contvidainimigo.setText('Vidas do Inimigo:0')
        enemy.undraw()
        tiro.undraw()
        boom = Image(Point(enemypos.x,enemypos.y),"boom.gif")
        boom.draw(win)
        error.undraw()
        win.getKey()
        winmessage.undraw()
        boom.undraw()
        enemies+=1
        vidainimigos=enemies
        contvidainimigo.setText('Vidas do Inimigo:'+str(vidainimigos+1))
        velocidade=enemies/2
        
        if enemies==8:
            contvidainimigo.undraw()
            enemies=1
            pg.mixer.music.stop()
            winmessage.draw(win)
            win.getKey()
            win.close()
            music_file = "grito.mp3"
            play_music(music_file, volume)
            win2=GraphWin("12",720,600)
            fundo2 = Image(Point(250,250),"fundo2.gif")
            fundo2.draw(win2)
            time.sleep(3)
            win2.close()
            pg.mixer.music.stop()
            win3= GraphWin("13",500,500)

            creditos = Text(Point(250,250),'Créditos:')
            autor  = Text(Point(250,300),'Arthur do Amaral.')
            creditos.draw(win3)
            time.sleep(1)
            autor.draw(win3)

            time.sleep(5)
            win3.close()
            menuon=True

        if menuon==False:
            tiro.undraw()
            boom.undraw()
            enemy = Image(Point(150,150),"enemy("+str(enemies)+").gif")
            enemy.draw(win)


    if tiro.getAnchor().getY() < 0:
        error.undraw()
        shot = False
        tiro.undraw()
        tiro = Image(Point(pos.x,1000),"laser.png")
        contaerros.undraw()
        errorcount += 1
        contaerros.setText(str(errorcount))


        error = Image(Point(num1,num2),"tenor.png")

        error.draw(win)
        contaerros.draw(win)
    

   
   
    
    c+=1
    tempo=c//60
    tempoquebrado=c//30
    time.sleep(1/60)