'''Recebendo as informações para o programa'''
estado = int(input("Digite o código do estado (1 a 5): "))
peso_ton = float(input("Digite o peso em toneladas: "))
codigo = int(input("Digite o código da carga (10 a 40): "))

'''Converter toneladas para kg'''
peso_kg = peso_ton * 1000


'''Definir preço por kg'''
if 10 <= codigo <= 20:
    preco_kg = 100
elif 21 <= codigo <= 30:
    preco_kg = 250
elif 31 <= codigo <= 40:
    preco_kg = 340

'''Calcular preço da carg'''
preco_carga = peso_kg * preco_kg

'''Definir imposto por estado'''
if estado == 1:
    imposto = 0.35
elif estado == 2:
    imposto = 0.25
elif estado == 3:
    imposto = 0.15
elif estado == 4:
    imposto = 0.05
elif estado == 5:
    imposto = 0

'''Calcular valor do imposto'''
valor_imposto = preco_carga * imposto


''' Calcular total'''
total = preco_carga + valor_imposto

'''Mostrar resultados'''
print("--------------------------------------------------")
print("Peso em kg:", peso_kg)
print("Preço da carga:", preco_carga)
print("Valor do imposto:", valor_imposto)
print("Valor total:", total)
print("--------------------------------------------------")