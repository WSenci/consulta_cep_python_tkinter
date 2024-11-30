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
        textoCep["text"] = "CEP não encontrado!"

janela = Tk()
janela.title("Busca CEP - Python")
janela.geometry("500x500")

textoInicial = Label(janela, text="Coloque o CEP e clique em buscar!", font=("Arial", 16, "bold"))
textoInicial.grid(column=0, row=0, padx=10, pady=10)

cep = Entry(width=20, bg="white", font=("Arial", 14))
cep.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text="Buscar", bg="#3b0b66", fg="white", width=8, height=2, command=pegar_cep)
botao.grid(column=1, row=1, padx=10, pady=10)

textoCep = Label(janela, text="", font=("Arial", 14))
textoCep.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()