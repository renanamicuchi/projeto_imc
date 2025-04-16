# Este sistema esta sendo criado para medição de IMC através de informações inseridas pelo usuário

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    
    elif 18.5 <= imc < 25:
        return "Peso normal"
    
    elif 25 <= imc < 30:
        return "Sobrepeso"
    
    elif 30 <= imc < 35:
        return "Obesidade grau I"
    
    elif 35 <= imc < 40:
        return "Obesidade grau II"
    
    else: 
        return "Obesidade grau III"
    
def main():
    print("=== Calculadora de IMC ===")

    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"\nSua classificação é: {classificacao}")

main()