prod = float(input("Qual o valor do produto: "))

venda = input("À vista ou Parcelado: V - P ")
valor = 0

if venda.upper() == "V":
  valor = prod * 0.9
  print(f"Sua compra foi {valor:.2f}") 
elif venda.upper() == "P":
  parc = int(input("Quantas parcelas: "))
  if parc <= 3:
    valor = prod * 1.05
    print(f"Sua compra foi {valor:.2f}, com parcelas de {valor/parc:.2f}")
  else:
    valor = prod * 1.1
    print(f"Sua compra foi {valor:.2f}, com parcelas de {valor/parc:.2f}") 
else:
  print("Opção invalida, inicie novamente!")