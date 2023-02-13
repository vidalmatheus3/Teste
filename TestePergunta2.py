
num = int(input("Insira um número para verificar se ele pertence a sequência Fibonacci: "))
numero = 1000
n1 = 0
n2 = 1
cont = 3
fibonacci = [0, 1]
# print('{} -> {}'.format(n1, n2), end='')

while cont <= numero:
    n3 = n1 + n2
    fibonacci.append(n3)
    # print(' -> {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1
# print(' FIM')

if num in fibonacci:
    print("Esse número pertence a sequência Fibonacci")
else:
    print("Esse número não pertence a sequência Fibonacci")