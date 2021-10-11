from tkinter import *
from guizero import *
import sys

volAleta = 1922223.16 #mm³

#def exitapp():
#    sys.exit()

def milhoVariaveis():
    tiposTrat = Window(app, title="Tipos de Tratamento", bg="#2d2e6f")
    tiposTrat.tk.attributes("-fullscreen", True)
    spacer2_Box = Box(tiposTrat, width="fill", height=100, border=True)

    tituloTrat_Box = Box(tiposTrat,width="fill", border=True)
    tituloTrat = Text(tituloTrat_Box, text="Selecione o tipo de Tratamento:",font="Geometria")
    tiposTrat.text_size = 20
    tiposTrat.text_color = "White"

    config_but_Box1 = Box(tiposTrat, width="fill", align="bottom", border=True)
    config_but = PushButton(config_but_Box1, image="/home/pi/Pictures/engrenagem.png",align="left")
    config_but.bg="#2d2e6f"

    spacer2_Box = Box(tiposTrat, width=100, height="fill", border=True, align="left")
    spacer3_Box = Box(tiposTrat, width=98, height="fill", border=True, align="right")

    buttons_Box1 = Box(tiposTrat, width="fill", height="fill", border=True, align="left", layout="grid")
    liq1po1_but = PushButton(buttons_Box1, espProd, text="1 Líquido 1 Pó", width="10", height="2", align="top", grid=[0,0])
    liq1po1_but.text_color="Black"
    liq1po1_but.text_size=20
    liq1po1_but.bg="white"
    liq1po1_but.font="Geometria"

    spacer2_Tex = Text(buttons_Box1, text="", width=11,grid=[1,0])

    liq1po2_but = PushButton(buttons_Box1, command=None, text="1 Líquido 2 Pós",grid=[2,0], width=10, height=2, enabled=False)
    liq1po2_but.text_color="Black"
    liq1po2_but.text_size=20
    liq1po2_but.bg="white"
    liq1po2_but.font="Geometria"

    spacer3_Tex = Text(buttons_Box1, text="", width=11,grid=[0,1])

    liq2po1_but = PushButton(buttons_Box1, command=None, text="2 Líquidos 1 Pó",grid=[0,2], width=10, height=2, enabled=False)
    liq2po1_but.text_color="Black"
    liq2po1_but.text_size=20
    liq2po1_but.bg="white"
    liq2po1_but.font="Geometria"

    liq2po2_but = PushButton(buttons_Box1, command=None, text="2 Líquidos 2 Pós",grid=[2,2], width=10, height=2, enabled=False)
    liq2po2_but.text_color="Black"
    liq2po2_but.text_size=20
    liq2po2_but.bg="white"
    liq2po2_but.font="Geometria"


    pesoEspMilho = 0.70 #Kg/m³ - 0,0007 g/cm3
    densEspMilho = 1.277 #g/cm³ - 1277 Kg/m³
    volEspMilho = 0.0007 #kg/cm³   0.000548159 #m3

#------------------------------------------------------------------------------#

#def soja():

#---------------------------------------------------------------#

def espProd():
    especificProd = Window(app, title="Tipos de Tratamento", bg="#2d2e6f")
    especificProd.tk.attributes("-fullscreen", True)

    spacer4_Box = Box(especificProd, width="fill", height=25, border=True)

    especificProd_Box = Box(especificProd, width="fill", border=True)
    especificProd_Text = Text(especificProd_Box, text="Insira as especificaões dos Produtos", font="Geometria")
    especificProd_Text.text_color = "White"
    especificProd_Text.text_size = 20

    spacer5_Box = Box(especificProd, width="fill", height=20, border=True)

    spacer6_Box = Box(especificProd, width=50, height="fill", align="left", border=True)

    formsBox = Box(especificProd, width="fill", height="fill", layout="grid",border=True)

    calda1_Box = Box(formsBox, width="fill", border=True, layout="grid", grid=[0,0])
    densidadecalda1_Text = Text(calda1_Box, text="Densidade da Calda 1     ", font="Geometria", grid=[0,0])
    densidadecalda1_Text.text_color = "White"
    densidadecalda1_Text.text_size = 15
    densidadecalda1_TextBox = TextBox(calda1_Box, grid=[1,0])
    ## densidadecalda1_TextBox.append("kg/m³")
    densidadecalda1_TextBox.bg = "White"
    densidadecalda1Final_Text = Text(calda1_Box, text="ml/Kg", font="Geometria", grid=[2,0])
    densidadecalda1Final_Text.text_color = "White"
    densidadecalda1Final_Text.text_size = 15

    spacer7_Box = Box(calda1_Box, width="fill", height=5, grid=[0,1], align="left", border=True)

    densidadecalda2_Text = Text(calda1_Box, text="Densidade da Calda 2     ", font="Geometria", grid=[0,2])
    densidadecalda2_Text.text_color = "White"
    densidadecalda2_Text.text_size = 15
    densidadecalda2_TextBox = TextBox(calda1_Box, grid=[1,2])
    ## densidadecalda2_TextBox.append("kg/m³")
    densidadecalda2_TextBox.bg = "White"
    densidadecalda2Final_Text = Text(calda1_Box, text="ml/Kg", font="Geometria", grid=[2,2])
    densidadecalda2Final_Text.text_color = "White"
    densidadecalda2Final_Text.text_size = 15

#----------------------------------------------------------#

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
milho_but.text_color="Black"
milho_but.text_size=20
milho_but.bg="white"
milho_but.font="Geometria"

spacer_text = Text(buttons_Box, text="",width=20, grid=[1,0])

soja_but = PushButton(buttons_Box, text="Soja", width="10", height="2",align="right", grid=[2,0])
soja_but.text_size=20
soja_but.text_color="Black"
soja_but.bg="white"
soja_but.font="Geometria"
#-------------------------------------------------------------------------#


app.display()