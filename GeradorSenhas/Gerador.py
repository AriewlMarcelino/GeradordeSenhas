import secrets
import string

class GeradorDeSenhas():
    def __init__(self):
        while True:
            try:
                self.gerador_de_caracteres = string.ascii_letters + string.digits
                self.comprimento_da_senha = int(input('Qual o comprimento da senha: '))
                self.numero_de_senhas = int(input('Quantas senhas você quer gerar? '))
                for i in range(self.numero_de_senhas):
                    self.gerador_de_senhas =  ''.join(secrets.choice(self.gerador_de_caracteres) for i in range(self.comprimento_da_senha))
                    print(f'\nSenhas Geradas: {self.gerador_de_senhas}')
                break
            except ValueError:
                print(f'Só é permitido numeros !')

    




    





# while True:
#   try:
#     gerador_de_caracteres = string.ascii_letters + string.digits
#     comprimento_da_senha = int(input('Qual o comprimento da senha: '))
#     numero_de_senhas = int(input('Quantas senhas você quer gerar? '))
#     for i in range(numero_de_senhas):
#       gerador_de_senhas =  ''.join(secrets.choice(gerador_de_caracteres) for i in range(comprimento_da_senha))
#       print(f'\nSenhas Geradas: {gerador_de_senhas}')
#     break
#   except ValueError:
#     print(f'Só é permitido numeros !')