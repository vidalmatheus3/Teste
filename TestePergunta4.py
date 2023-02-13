fat = [{'Cidade': 'SP', 'faturamento': 67836.43}, 
        {'Cidade': 'RJ', 'faturamento': 36678.66},
        {'Cidade': 'MG', 'faturamento': 29229.88},
        {'Cidade': 'ES', 'faturamento': 27165.48},
        {'Cidade': 'Outros', 'faturamento': 19849.53}]

fat_cidade = []
fat_valor = []

for cidade in fat:
    fat_cidade.append(cidade['Cidade'])
    fat_valor.append(cidade['faturamento'])

fat_total = sum(fat_valor)

porcentagem_cidade = []
indice = 0

for valor in fat_valor:
    porcentagem = valor / fat_total * 100
    porcentagemfinal = "{:.2%}".format(porcentagem/100)
    # porcentagem_cidade.append(fat_cidade[indice])
    porcentagem_cidade.append(porcentagemfinal)

    indice = indice + 1

for i in range(len(fat_cidade)):
    print("A porcentagem de faturamento de {} é: {}".format(fat_cidade[i], porcentagem_cidade[i]))
