try:
    var1 = float( input("Digite um número: ") )
    var2 = float( input("Digite outro número: ") )
    div = var1 / var2
except    ZeroDivisionError:
    print ("Não é possível fazer uma divisão por 0")
