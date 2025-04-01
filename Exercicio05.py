nota1 = float(input("Digita a 1 nota: "))
nota2 = float(input("Digita a 2 nota: "))
nota3 = float(input("Digita a 3 nota: "))

media = (nota1+nota2+nota3)/3

if media >= 7:
    print(f"aprovado {media}")
else:
    if media <=4:
        print(f"reprovado {media}")
    else:
        print(f"recuperação {media}")