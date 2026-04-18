a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))


if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b


if a >= b + c:
    print("Não forma triângulo")

else:
 
    if a**2 == b**2 + c**2:
        print("Triângulo Retângulo")
    elif a**2 > b**2 + c**2:
        print("Triângulo Obtusângulo")
    else:
        print("Triângulo Acutângulo")


    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")

