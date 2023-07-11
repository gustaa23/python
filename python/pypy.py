class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print("Olá, meu nome é", self.nome)
    
    def aniversario(self):
        self.idade += 1
        print("Feliz aniversário! Agora tenho", self.idade, "anos.")

pessoa = Pessoa("João", 25)
print (pessoa.nome)
pessoa.saudacao()
pessoa.aniversario()