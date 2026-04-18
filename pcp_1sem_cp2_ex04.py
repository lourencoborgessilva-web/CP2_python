# Definindo funções
def calcular_horas_extras(salario_base, horas):
    # 1.5% do salário base por hora
    valor_hora_extra = salario_base * 0.015
    return valor_hora_extra * horas


def calcular_descontos_faltas(salario_base, faltas):
    # 2% do salário base por falta
    desconto_por_falta = salario_base * 0.02
    return desconto_por_falta * faltas


def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus.lower() != 's':
        return 0

    if cargo == 1:  # Gerente
        return 1000
    elif cargo == 2:  # Analista
        return 500
    elif cargo == 3:  # Assistente
        return 300
    elif cargo == 4:  # Estagiário
        return 100
    else:
        return 0

# Lendo o cargo selecionado e verificando se ele existe
def ler_cargo():
    while True:
        try:
            cargo = int(input("Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
            if 1 <= cargo <= 4:
                return cargo
            else:
                print("Cargo inválido.")
        except ValueError:
            print("Digite um número válido.")


def main():
    # Entrada
    nome = input("Nome do funcionário: ")
    cargo = ler_cargo()
    salario_base = float(input("Salário base: "))
    horas_extras = float(input("Horas extras trabalhadas: "))
    faltas = int(input("Total de faltas no mês: "))
    recebeu_bonus = input("Recebeu bônus? (s/n): ")

    # Cálculos
    valor_horas_extras = calcular_horas_extras(salario_base, horas_extras)
    desconto_faltas = calcular_descontos_faltas(salario_base, faltas)
    bonus = calcular_bonus(cargo, recebeu_bonus)

    total_acrescimos = valor_horas_extras + bonus
    total_descontos = desconto_faltas

    salario_final = salario_base + total_acrescimos - total_descontos

    # Saída
    print("\nResumo do pagamento")
    print(f"Funcionário: {nome}")
    print(f"Salário base: R$ {salario_base:.2f}")
    print(f"Acréscimos: R$ {total_acrescimos:.2f}")
    print(f"Descontos: R$ {total_descontos:.2f}")
    print(f"Salário final: R$ {salario_final:.2f}")

# Chama a função com o codigo principal
main()
