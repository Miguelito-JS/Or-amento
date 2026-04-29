import csv

print("=== SISTEMA DE ORÇAMENTO DE ALUGUEL ===")

tipo = input("Escolha o tipo de imóvel (apartamento/casa/estudio): ").lower()

valor = 0

if tipo == "apartamento":
    valor = 700
    quartos = int(input("Quantos quartos? (1 ou 2): "))
    
    if quartos == 2:
        valor += 200
    
    garagem = input("Deseja garagem? (s/n): ").lower()
    if garagem == "s":
        valor += 300
    
    filhos = input("Possui crianças? (s/n): ").lower()
    if filhos == "n":
        valor *= 0.95

elif tipo == "casa":
    valor = 900
    quartos = int(input("Quantos quartos? (1 ou 2): "))
    
    if quartos == 2:
        valor += 250
    
    garagem = input("Deseja garagem? (s/n): ").lower()
    if garagem == "s":
        valor += 300

elif tipo == "estudio":
    valor = 1200
    vagas = int(input("Quantas vagas deseja? (mínimo 2): "))
    
    if vagas >= 2:
        valor += 250
        if vagas > 2:
            valor += (vagas - 2) * 60

else:
    print("Tipo inválido")
    exit()

print(f"\nValor do aluguel mensal: R$ {valor:.2f}")

# contrato
contrato = 2000
parcelas = int(input("Em quantas vezes deseja parcelar o contrato? (1 a 5): "))

if parcelas > 5:
    parcelas = 5

valor_parcela = contrato / parcelas

print(f"Valor do contrato: R$ {contrato:.2f}")
print(f"Parcelado em {parcelas}x de R$ {valor_parcela:.2f}")

# gerar CSV
with open("orcamento.csv", "w", newline="") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["Mes", "Valor"])

    for i in range(1, 13):
        writer.writerow([f"Mes {i}", f"{valor:.2f}"])

print("\nArquivo CSV gerado com sucesso!")
