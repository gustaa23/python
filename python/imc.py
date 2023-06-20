alt = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso/(alt**2)

if imc < 18.5:
  print("Você esta abaixo do peso!")
elif imc < 25:
  print("Você está com peso normal!")
elif imc < 30:
  print("Você está com sobrepeso!")
elif imc < 35:
  print("Você está com obesidade I!")
elif imc < 40:
  print("Você está com obesidade II!")
else:
  print("Você está com obesidade III!")