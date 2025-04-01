nome = input("Digite seu nome: ")
idade = int (input("Digite sua idade: "))
salario = float(input("Digite seu salario: "))
percentual = int(input("Digite o valor do percentual : "))
acrescimo  =  salario * (percentual/100)
aumento = salario + acrescimo
print(f" Seu salario é: {aumento}")
print(nome,idade,salario,aumento)
