from imc import calcular_imc, classificar_imc

def main():
    print("=== Calculadora de IMC ===")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f"\nSeu IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")

if __name__ == "__main__":
    main()