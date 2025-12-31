# Calculadora de IMC / BMI Calculator

Script simples em Python que calcula o Índice de Massa Corporal (IMC) de uma pessoa a partir de peso (kg) e altura (m) e classifica o resultado em faixas (baixo peso, normal, sobrepeso, obesidade).

## Como usar / How to use

Instale o pacote via pip:

```
pip install calculadora-imc
```

No seu código Python:

```
from calculadora_imc import calcular_imc

imc, categoria = calcular_imc(peso=70, altura=1.75)
print(f"IMC: {imc:.2f} – {categoria}")
# Saída: IMC: 22.86 – Peso normal
```

## Funcionalidades

- Função `calcular_imc(peso, altura)` que retorna o valor do IMC e a categoria correspondente.
- Classificação baseada na tabela de IMC: baixo peso, normal, sobrepeso, obesidade.

## English

Simple Python script that calculates a person’s Body Mass Index (BMI) based on weight (kg) and height (m) and classifies the result into ranges (underweight, normal, overweight, obesity).

### How to use

Install the package from PyPI:

```
pip install calculadora-imc
```

Then call:

```
from calculadora_imc import calcular_imc

bmi, category = calcular_imc(weight=70, height=1.75)
print(f"BMI: {bmi:.2f} – {category}")
# Output: BMI: 22.86 – Normal weight
```

### Features

- `calcular_imc(weight, height)` returns the BMI value and the category.
- Classification based on BMI ranges: underweight, normal, overweight, obesity.

## Licença / License

MIT License
