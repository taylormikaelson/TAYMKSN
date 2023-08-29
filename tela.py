from tkinter import *
janela = Tk()
janela.iconbitmap("c:\PROJETO\HOPE.ico")
janela.title("HOPE")
janela.geometry("500x500") # larguraXaltura + dist esquerda + dist topo
janela.wm_resizable(width=False, height=False)

texto = Label(janela,text= "login")
texto.pack()

txtlogin = Entry()
txtlogin.pack()

texto2 = Label(janela,text= "senha")
texto2.pack()

txtsenha = Entry()
txtsenha.pack()

btentrar = Button(janela, text= "entrar", command="")
btentrar.pack()

janela.mainloop()