from tkinter import *
from guizero import *
import sys


def exitapp():
    sys.exit()

def milhoVariaveis():
    tiposTrat = Window(app, title="Tipos de Tratamento", bg="#2d2e6f")
    tiposTrat.tk.attributes("-fullscreen", True)
    spacer2_Box = Box(tiposTrat, width="fill", height=180, border=True)



    pesoEspMilho = 0.70 #Kg/m³ - 0,0007 g/cm3
    densEspMilho = 1.277 #g/cm³ - 1277 Kg/m³
    volEspMilho = 0.0007 #g/cm³   0.000548159 #m3


#def soja():



app = App(title="Mecmaq",bg="#2d2e6f")
app.tk.attributes("-fullscreen", True)
#app.image("icone")
#picture = Picture(app, image="/home/pi/Pictures/TELA AUTOMAÇÃO FUNDO.png")

spacer_Box = Box(app, width="fill", height=180, border=True)

intro_Box = Box(app, width="fill", border=True)
intro = Text(intro_Box, text = "Selecione a cultura a ser tratada:",font="Geometria")
intro.text_size = 20
intro.text_color="white"

config_but_Box = Box(app, width="fill", align="bottom", border=True)
config_but = PushButton(config_but_Box, image="/home/pi/Pictures/engrenagem.png",align="left")
config_but.bg="#2d2e6f"

spacer1_Box = Box(app, width=100, height="fill", border=True, align="left")

buttons_Box = Box(app, width="fill", height="fill", border=True, align="left", layout="grid")
milho_but = PushButton(buttons_Box, milhoVariaveis, text="Milho", width="10", height="2", align="top", grid=[0,0])
milho_but.text_color="#2d2e6f"
milho_but.text_size=20
milho_but.bg="white"
milho_but.font="Geometria"

spacer_text = Text(buttons_Box, text="",width=20, grid=[1,0])

soja_but = PushButton(buttons_Box, text="Soja", width="10", height="2",align="right", grid=[2,0])
soja_but.text_size=20
soja_but.text_color="#2d2e6f"
soja_but.bg="white"
soja_but.font="Geometria"



app.display()