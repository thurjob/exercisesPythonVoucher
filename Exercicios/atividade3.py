nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
salario = float(input("Digite o sálario: "))
sexo = input("Digite o sexo F = feminino, M = maculino ou O = outros: ")
civil = input("Digite o estado civil s = solteiro(a), c = casado(a) ,v = viuvo(a), d = divorciado(a): ")
f = "F"

if nome == nome[0:3]:
    print("Nome inválido")

else:
    print("Nome válido")

if 0 <= idade <= 150:
    print("Idade válida")

else:
    print("Idade inválida")

if salario > 0:
    print("Salário válido")

else:
    print("Salário inválido")

if sexo == f or m or o:
    print("Sexo válido")

else:
    print("Sexo inválido")

if civil == "s"or "c"or "v"or "d":
    print("Estado cívil válido")

else:
    print("Estado cívil inválido")