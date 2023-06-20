sal = float(input("Digite o seu salario: "))
aum = 0
if sal <= 1000:
  aum = sal * 0.2
elif sal <= 3000:
  aum = sal * 0.15
elif sal <= 5000:
  aum = sal * 0.1
else:
  aum = sal * 0.05

print(f"O aumento de salario foi de {aum} reais e o novo salario é de {sal + aum}")