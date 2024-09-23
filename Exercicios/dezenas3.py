numero = int(input("Insira um número inteiro: "))

if numero <1000:
    
    centena = numero //100
    dezena = numero //10
    unidade = numero % 10


    print(f"{centena} centenas, {dezena} dezenas e {unidade} unidades")

else:
    print("digite um numero menor que 1000")


