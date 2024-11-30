import requests
from tkinter import *

def mostrar():
    texto = "Texto mostrado após apertar no botão!"
    textoCotacoes["text"] = texto

janela = Tk()
janela.title("Estudando Python")
janela.geometry("400x400")

textoInicial = Label(janela, text="Clique no botão agora para ver o texto!")
textoInicial.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Mostrar", command=mostrar)
botao.grid(column=0, row=1, padx=10, pady=10)

textoCotacoes= Label(janela, text="")
textoCotacoes.grid(column=0, row=2, padx=10, pady=10)



janela.mainloop()