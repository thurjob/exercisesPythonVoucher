funcionarios = []
maior  = 0
for i in range(4):
    d = {}
    d["nome"] = input("Digite o nome: ")
    d["função"] = input("Digite a função: ")
    d["salário"] = float(input("Digite o saldo: "))

    if d["salário"] > maior:
        maior = d["salário"]
    funcionarios.append(d)

for pessoa in funcionarios:
    if pessoa["salario"] == maior:
        print(f'Pessoa com o maior salário é{pessoa["nome"]}')
    