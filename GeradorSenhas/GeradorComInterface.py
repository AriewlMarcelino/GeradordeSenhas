import random
import string
from tkinter import *
import pyperclip


class GeradorDeSenhasGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Gerador de Senhas")

        # Rótulos e caixas de entrada
        self.label_comprimento = Label(self.root, text="Comprimento da senha:")
        self.entry_comprimento = Entry(self.root)
        self.label_numero_senhas = Label(self.root, text="Número de senhas:")
        self.entry_numero_senhas = Entry(self.root)
        self.label_resultado = Label(self.root, text="")

        # Botões
        self.button_gerar = Button(self.root, text="Gerar Senhas", command=self.gerar_senhas, padx=5, pady=5 )
        self.button_limpar = Button(self.root, text="Limpar", command=self.limpar_tela)
        self.button_copiar = Button(self.root, text="Copiar", command=self.copiar_senhas)

        # Posicionando os elementos na janela
        self.label_comprimento.pack()
        self.entry_comprimento.pack()
        self.label_numero_senhas.pack()
        self.entry_numero_senhas.pack()
        self.button_gerar.pack()
        self.button_limpar.pack()
        self.button_copiar.pack()
        self.label_resultado.pack()

        self.root.mainloop()

    def gerar_senhas(self):
        try:
            comprimento = int(self.entry_comprimento.get())
            numero_senhas = int(self.entry_numero_senhas.get())

            senhas = []
            for _ in range(numero_senhas):
                senha = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(comprimento))
                senhas.append(senha)

            self.label_resultado.config(text="\n".join(senhas))
        except ValueError:
            self.label_resultado.config(text="Digite apenas números para o comprimento e quantidade de senhas.")

    def limpar_tela(self):
        self.label_resultado.config(text="")
        self.entry_comprimento.delete(0, END)
        self.entry_numero_senhas.delete(0, END)

    def copiar_senhas(self):
        senhas = self.label_resultado.cget("text")
        pyperclip.copy(senhas)

if __name__ == "__main__":
    app = GeradorDeSenhasGUI()