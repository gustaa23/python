class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return  self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def imprimir_informacoes(self):
        print(f"Retângulo da base {self.base} e altura {self.altura}")
        print(f"Área: {self.calcular_area()}")
        print(f"Perimetro: {self.calcular_perimetro()}")

retangulo1 = Retangulo(5, 3)
print(retangulo1.base)
print(retangulo1.calcular_area())
retangulo1.imprimir_informacoes()