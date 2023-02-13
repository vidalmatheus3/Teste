import json

f = open('dados.json')

data = json.load(f)

faturamento = []

num_dias = 0

for i in data:
    if i['valor'] > 0:
        faturamento.append(i['valor'])
    
media = sum(faturamento)/len(faturamento)

for i in data:
    if i['valor'] > media:
        num_dias = num_dias + 1

menor_valor = min(faturamento)
maior_valor = max(faturamento)

print("O menor faturamento em um dia é: " + str(menor_valor))
print("O maior faturamento em um dia é: " + str(maior_valor))
# print(media)
print("O faturamento de " + str(num_dias) + " dias foi superior a média mensal")