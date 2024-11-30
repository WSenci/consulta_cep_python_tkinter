import requests
from tkinter import *

def pegar_cep():
    cep_valor = cep.get()
    requisicao = requests.get(f"https://viacep.com.br/ws/{cep_valor}/json/")

    if requisicao.status_code == 200:
        resp = requisicao.json()
        texto = f"CEP: {resp['cep']}\nLogradouro: {resp['logradouro']}\nBairro: {resp['bairro']}\nCidade: {resp['localidade']}\nEstado: {resp['estado']}"
        textoCep["text"] = texto
    else:
        textoCep["test"] = "CEP não encontrado!"

janela = Tk()
janela.title("Busca CEP - Python")
janela.geometry("400x400")

textoInicial = Label(janela, text="Coloque o cep e clique em buscar!")
textoInicial.grid(column=0, row=0, padx=10, pady=10)

cep = Entry(width=15, bg="white", font=("Comic Sans MS", 14))
cep.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text="Buscar", command=pegar_cep)
botao.grid(column=1, row=1, padx=10, pady=10)

textoCep = Label(janela, text="")
textoCep.grid(column=0, row=2, padx=10, pady=10)



janela.mainloop()