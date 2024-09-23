tarefas = []
lista = 0
while True:
    nvtrf = {}
    print(" MENU ")
    print ("1 - Adicionar tarefa")
    print ("2 - Mostrar tarefas")
    print ("3 - Marcar tarefa como concluída")
    print ("4 - Remover tarefa ")
    print ("5 - Sair")
    opc = int(input("Escolha a opção desejada: "))
    if  opc == 1:
        nvtrf["Descrição"] = input("Insira a descrição da sua tarefa: ")
        print ("1 - Concluída")
        print ("1 - Não concluida")
        opc2 = int(input("Escolha a opção desejada"))

        if opc2 == 1:
            nvtrf["Status"] = "Concluída"
        elif opc2 ==2:
            nvtrf["Status"] = "Não concluída"
        nvtrf["Posição"] = lista
        lista += 1
        tarefas.append(nvtrf)
    elif opc == 2 :
        print (f'Suas tarefas são:\n{tarefas}')
    elif opc == 3:
        trf = int(input("Qual a Posição da tarefa?: "))
        for i in range(len(tarefas)):
            if i == trf:
                tarefas[i]["Status"] = "Concluida"
                break
    elif opc == 4:
        trf = int(input("Qual a Posição da tarefa?: "))
        for i in range(len(tarefas)):
            if i == trf:
                tarefas.pop(trf)
                lista -= 1
                print("Tarefa removida")
                break
        for i in range(len(tarefas)):
            if tarefas[i]["Posição"] > trf:
                tarefas[i]["Posição"] -= 1
    elif opc == 5:
        print("Agradeçemos por usar o sistema!")
        print("Programa finalizado")
        break

#ARTHUR PATRIOTA#