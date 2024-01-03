from os import system
lista= []

while True:
    print(f"Aperte [I]nserir")
    print(f"Aperte [A]pagar")
    print(f"Aperte [L]istar")
    opcao_validas = "ial"
    opcao = input("opcao: ")
    opcao = opcao.lower()
    if opcao in opcao_validas :
        ...
        
    else:
        print("Digite apenas I,A ou L")
        continue
    try:
        if opcao == "i":
            system("cls")
            item = input("Digite oque quer inserir na lista: ")
            lista.append(item)
            print("Adicionado")
        elif opcao == "a":
            system("cls")
            indice = int(input("escolha o indice que quer pagar: "))
            apagado =lista.pop(indice)
            print(f"{apagado} foi Apagado")
        elif opcao == "l":
            system("cls")
            for indice, item in enumerate(lista):
                print(indice,item)
            system("pause")
    except:
        print("Opcao invalida")
        continue