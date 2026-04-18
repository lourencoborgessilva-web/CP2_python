# Definindo as funções
def pode_aprovar(idade, renda, valor):
    return idade > 18 and valor <= renda * 20


def definir_taxa(numeroParcelas):
    if numeroParcelas <= 6:
        return 0.05
    elif numeroParcelas <= 12:
        return 0.08
    else:
        return 0.10


def calcular_parcela(valor, taxa, numeroParcelas):
    i = taxa
    n = numeroParcelas
    return valor * (i * (1 + i) ** n) / ((1 + i) ** n - 1)


def calcular_total(parcela, numeroParcelas):
    return parcela * numeroParcelas


def calcular_juros(total, valor):
    return total - valor

# Verifica se o número de parcelas está corrento
def ler_numero_parcelas():
    while True:
        try:
            numeroParcelas = int(input("Número de parcelas (3 a 24): "))

            if 3 <= numeroParcelas <= 24:
                return numeroParcelas
            else:
                print("Valor inválido. Digite entre 3 e 24.\n")
        # Caso o usuario digite um numero que não seja inteiro
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.\n")

# Função principal
def main():
    # Entrada de dados
    nome = input("Nome do cliente: ")
    idade = int(input("Idade: "))
    renda = float(input("Renda mensal: "))
    valor = float(input("Valor do empréstimo: "))

    numeroParcelas = ler_numero_parcelas()

    # Verificação de aprovação
    if not pode_aprovar(idade, renda, valor):
        print("\nEmpréstimo NEGADO.")
        return

    # Processamento
    taxa = definir_taxa(numeroParcelas)
    parcela = calcular_parcela(valor, taxa, numeroParcelas)
    total = calcular_total(parcela, numeroParcelas)
    juros = calcular_juros(total, valor)

    # Saída
    print("\nEmpréstimo APROVADO")
    print(f"Cliente: {nome}")
    print(f"Valor financiado: R$ {valor:.2f}")
    print(f"Taxa de juros: {taxa * 100:.1f}% ao mês")
    print(f"Valor da parcela: R$ {parcela:.2f}")
    print(f"Total pago: R$ {total:.2f}")
    print(f"Total de juros: R$ {juros:.2f}")

# Chama a função com o codigo principal
main()
