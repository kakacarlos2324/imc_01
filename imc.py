peso = float(input("digite o peso em kg:"))
altura = float(input("digite a altura em metros:"))
def calcular_imc(peso, altura):
    altura_metro = altura / 100
    imc = peso / (altura_metro **2)
    return imc
def interpretar_imc(imc) :
    if imc < 18.5:
        return "abaixo do peso"
    elif imc < 24.9:
        return "peso normal"
    elif imc < 29.9:
        return "sobrepeso"
    elif imc < 34.9:
        return "obesidade grau 1"
    elif imc < 39.9:
        return "obesidade 2"
    else:
        return "obesidade grau 3"

imc = calcular_imc(peso, altura)
categoria = interpretar_imc(imc)
print("seu imc é:", imc)
print("categoria:", categoria)


        