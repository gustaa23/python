id = int(input("Digite sua idade: "))
alt = float(input("Digite sua altura: "))

if id >= 16 and alt >= 1.5:
  print("você pode brincar no brinquedo 1")
elif 16 > id >= 14 and 1.5 > alt >= 1.2:
  print("você pode brincar no brinquedo 2")
elif 14 > id >= 12 and 1.2 > alt >= 1.1:
  print("você pode brincar no brinquedo 3")
elif 12 > id >= 10 and 1.1 > alt >= 1.0:
  print("você pode brincar no brinquedo 4")
else:
  print("Procure a administração!")