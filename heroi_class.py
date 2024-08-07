class heroiaventureiro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo


    def saudacao(self):
        print("=" * 20)
        print(f"Bem vindo jogador {self.nome} de idade {self.idade}")
        print("="*20)

    def tipo(self):
        guerreiro, mago, monge, ninja
