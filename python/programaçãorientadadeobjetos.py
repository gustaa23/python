class Contador:
    total_contadores = 0

    def __init__(self):
        Contador.total_contadores += 1

    @classmethod
    def obter_total_contadores(cls):
        return cls.total_contadores
    
contador1 = Contador()
contador2 = Contador()
contador3 = Contador()

print(Contador.obter_total_contadores())