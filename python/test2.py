x = int(input("vou adivinhar seu número, para ter certeza que você não vai tenta me enganar digite o seu numero: "))
i = 0
for x % 2 == 0:
    i = x * x
    print("EU vejo seu numero é", i)