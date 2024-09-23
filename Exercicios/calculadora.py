
while True:
     print("1 - mult")
     print("2 - div")
     print("3 - adicao")
     print("4 - subtracao")
     print("5 - sair")

     opcao = int(input("Digite uma opcao: "))

     if opcao == 5:
          print("obrigdo por usar nosso sistema")

     elif opcao == 1:
        n1= print("Digite numero 1: ")
        n2 = print("Digite numero 2: ")
        print(f"resultado é {n1 * n2}")

     elif opcao == 2:
        n1= print("Digite numero 1: ")
        n2 = print("Digite numero 2: ")
        print(f'resultado é {n1 / n2}')
     elif opcao == 3:
        n1= print("Digite numero 1: ")
        n2 = print("Digite numero 2: ")
        print('"resultado é {n1+n2}')
     elif opcao == 4:
        n1= print("Digite numero 1: ")
        n2 = print("Digite numero 2: ")
        print(f'resultado é {n1 - n2}')


