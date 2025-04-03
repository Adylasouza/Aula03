tipoCombustivel= input("Informe qual tipo de combustível foi abastecido (G para Gasolina e E para Etanol):  ")
litros = float(input("Informe o tipo de combustível abastecido: " ))
vGas = 5.8
vEta = 4.9
if tipoCombustivel == "G" or tipoCombustivel == "g":
    valor = vGas * litros
    print(f"Você pagará: {valor:.2f} ")

#elif tipoCombustivel == "e" or tipoCombustivel == "E"
else:
    if tipoCombustivel == "E" or tipoCombustivel == "e":
        valor =  vEta * litros
        print(f"Você pagará: {valor:.2f} ")
    else:
        print("Tipo de combustível inválido")

