class heroiaventureiro:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def saudacao(self):
        mensagem = (
            f"Bem-vindo, {self.tipo}, {self.nome}!\n"
            f"Aos {self.idade} anos, sua jornada apenas começou.\n"
            f"Prepare-se para a aventura de sua vida!"
        )
        print("=" * 40)
        print(mensagem)

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Tipo: {self.tipo}")

    def atacar(self):
        if self.tipo == "MAGO":
            ataque = "MAGIA"
        elif self.tipo == "GUERREIRO":
            ataque = "ESPADA"
        elif self.tipo == "MONGE":
            ataque = "ARTES MARCIAISn"
        elif self.tipo == "NINJA":
            ataque = "SHURIKEN"
        else:
            ataque = "usou ataque desconhecido"
        print(f"O {self.tipo} atacou usando {ataque}.")

heroi1 = heroiaventureiro("PYTHON", 35, "MAGO")
heroi2 = heroiaventureiro("JAVA", 29, "GUERREIRO")
heroi3 = heroiaventureiro("RUBY", 34, "MONGE")
heroi4 = heroiaventureiro("JAVASCRIP", 28, "NINJA")

heroi1.saudacao()
heroi1.exibir_informacoes()
heroi1.atacar()

heroi2.saudacao()
heroi2.exibir_informacoes()
heroi2.atacar()

heroi3.saudacao()
heroi3.exibir_informacoes()
heroi3.atacar()

heroi4.saudacao()
heroi4.exibir_informacoes()
heroi4.atacar()
