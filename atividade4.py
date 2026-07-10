# Define o limite de peso permitido e o valor da multa por quilo excedente
limite_peso = 50  # kg
valor_multa_por_kg = 4.00  # R$

# Solicita o peso dos peixes ao usuário
peso = float(input("Digite o peso dos peixes (em kg): "))

# Calcula o excesso de peso e a multa, se houver
excesso = max(0, peso - limite_peso)
multa = excesso * valor_multa_por_kg

# Exibe os resultados
print("\n### Relatório de Pesca ###")
print(f"Peso total dos peixes: {peso:.2f} kg")
print(f"Excesso de peso: {excesso:.2f} kg")
print(f"Multa a pagar: R$ {multa:.2f}")

# Mensagem adicional
if excesso > 0:
    print("Atenção! Você excedeu o limite de peso e deve pagar uma multa.")
else:
    print("Parabéns! Você não ultrapassou o limite de peso.")
