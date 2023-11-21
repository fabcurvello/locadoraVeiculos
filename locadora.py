mostrar = "a"
alugar = "b"
devolver = "c"
veiculos_a_alugar = []  # list com dicionários de veículos a alugar
veiculos_alugados = []  # list com dicionários de veículos alugados


# Carregar base de dados de veículos no list veiculos_a_alugar
def iniciar_veiculos_alugar():
    veiculos_a_alugar.append({
        "fabricante": "VW",
        "modelo": "Fusca 1300",
        "cor": "Laranja",
        "ano": "1975",
        "valor": 100.00
    })

    veiculos_a_alugar.append({
        "fabricante": "VW",
        "modelo": "Gol GTI",
        "cor": "Azul",
        "ano": "1989",
        "valor": 150.00
    })

    veiculos_a_alugar.append({
        "fabricante": "Chevrolet",
        "modelo": "Corsa Sedan 1.8",
        "cor": "Prata",
        "ano": "2010",
        "valor": 60.00
    })

    veiculos_a_alugar.append({
        "fabricante": "Toyota",
        "modelo": "Corolla Brad Pitty",
        "cor": "Branco",
        "ano": "2006",
        "valor": 120.00
    })

    veiculos_a_alugar.append({
        "fabricante": "Ford",
        "modelo": "Kadett Conversível 1.6",
        "cor": "Amarelo",
        "ano": "2000",
        "valor": 170.00
    })


# Gerencia a execução/finalização do programa
def gestor_execucao():
    while( True ):
        o_que_deseja()
        continuar = input("Deseja continuar o programa? (S ou N) ").lower()
        if ( continuar == "n" ):
            print("-- Fim da execução do programa --")
            break



# Encaminha para a função a executar conforme escolha do usuário
def o_que_deseja():
    print("\n=================================")
    print("Bem vindo à Locadora de Veículos!")
    print("=================================")
    print("O que deseja fazer?")
    print(" A - Mostrar portifólio")
    print(" B - Alugar um veículo")
    print(" C - Devolver um veículo")
    desejo = input().lower()
    if (desejo == mostrar):
        mostrar_portifolio()
    elif (desejo == alugar):
        alugar_um_veiculo()
    elif (desejo == devolver):
        devolver_um_veiculo()
    else:
        print("Opção inválida...")


# Exibe o portifólio de veículos a alugar
def mostrar_portifolio():
    cont = 1
    print("\n----------- PORTIFÓLIO DE VEÍCULOS DISPONÍVEIS PARA LOCAÇÃO -----------")
    for veiculo in veiculos_a_alugar:
        print(f" {cont} - {veiculo['fabricante']} {veiculo['modelo']} {veiculo['cor']} {veiculo['ano']} - Diária R$ {veiculo['valor']:.2f}" )
        cont += 1
    print("------------------------------------------------------------------------\n")


# Realiza o aluguel de veículo (retirando o veículo escolhido de veiculos_a_alugar e inserindo em veiculos_alugados
def alugar_um_veiculo():
    mostrar_portifolio()
    codigo = int(input("Informe o código de veículo desejado: "))

    if ((codigo >= 1) and (codigo <= len(veiculos_a_alugar))):
        print(f"Veículo selecionado: "
              f"{veiculos_a_alugar[codigo - 1]['fabricante']} "
              f"{veiculos_a_alugar[codigo - 1]['modelo']} "
              f"{veiculos_a_alugar[codigo - 1]['cor']} "
              f"{veiculos_a_alugar[codigo - 1]['ano']}"
              f" - Diária R$ {veiculos_a_alugar[codigo - 1]['valor']:.2f}")
        confirma = input("Você confirma a sua escolha? (S ou N) ").lower()
        if ( confirma == "s" ):
            print(f"Valor da diária: R$ {veiculos_a_alugar[codigo - 1]['valor']:.2f}. ")
            total_dias = int(input("Deseja quantos dias de locação? "))
            valor_total = veiculos_a_alugar[codigo - 1]['valor'] * total_dias
            print(f"Valor total da locação será de R$ {valor_total:.2f}.")
            de_acordo = input(f"Você confirma a locação do veículo: "
                              f"{veiculos_a_alugar[codigo - 1]['modelo']} "
                              f"por {total_dias} dias "
                              f"no valor de R$ {valor_total:.2f}? (S ou N) ").lower()
            if ( de_acordo == "s"):
                veiculos_alugados.append(veiculos_a_alugar[codigo - 1])
                del veiculos_a_alugar[codigo - 1]
                print("Parabéns! Você alugou um excelente veículo.")
            else:
                print("Tentativa de locação CANCELADA.")
        else:
            print("Tentativa de locação CANCELADA.")
    else:
        print("Opção inválida...")


# Realiza a devolução de veículo (retirando o veículo escolhido de veiculos_alugados e inserindo em veiculos_a_alugar
def devolver_um_veiculo():
    cont = 1
    print("\n----------- SELECIONE O VEÍCULO PARA DEVOLUÇÃO DE LOCAÇÃO -----------")
    for veiculo in veiculos_alugados:
        print(f" {cont} - {veiculo['fabricante']} {veiculo['modelo']} {veiculo['cor']} {veiculo['ano']}")
        cont += 1
    print("-----------------------------------------------------------------------\n")

    codigo = int(input("Informe o código: "))

    if ((codigo >= 1) and (codigo <= len(veiculos_alugados))):
        print(f"Veículo selecionado: "
              f"{veiculos_alugados[codigo - 1]['fabricante']} "
              f"{veiculos_alugados[codigo - 1]['modelo']} "
              f"{veiculos_alugados[codigo - 1]['cor']} "
              f"{veiculos_alugados[codigo - 1]['ano']}")
        confirma = input("Você confirma a devolução? (S ou N) ").lower()
        if (confirma == "s"):
            veiculos_a_alugar.append(veiculos_alugados[codigo - 1])
            del veiculos_alugados[codigo - 1]
            print("Devolução de veículo concluída com êxito. Esperamos lhe ver novamente em breve!")
        else:
            print("Tentativa de devolução CANCELADA.")
    else:
        print("Opção inválida...")


# ----- Execução do Programa -----
iniciar_veiculos_alugar()
gestor_execucao()


