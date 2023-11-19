veiculos_alugar = []


def iniciar_veiculos_alugar():
    veiculos_alugar.append({
        "fabricante": "VW",
        "modelo": "Fusca 1300",
        "cor": "Laranja",
        "ano": "1975",
        "valor": 100.00
    })

    veiculos_alugar.append({
        "fabricante": "VW",
        "modelo": "Gol GTI",
        "cor": "Azul",
        "ano": "1989",
        "valor": 150.00
    })

    veiculos_alugar.append({
        "fabricante": "Chevrolet",
        "modelo": "Corsa Sedan 1.8",
        "cor": "Prata",
        "ano": "2010",
        "valor": 60.00
    })

    veiculos_alugar.append({
        "fabricante": "Toyota",
        "modelo": "Corolla Brad Pitty",
        "cor": "Branco",
        "ano": "2006",
        "valor": 120.00
    })

    veiculos_alugar.append({
        "fabricante": "Ford",
        "modelo": "Kadett Conversível 1.6",
        "cor": "Amarelo",
        "ano": "2000",
        "valor": 170.00
    })


def gestor_execucao():
    while( True ):
        encerrar = input("Deseja encerrar o programa? (S ou N) ").lower()
        if ( encerrar == "s" or encerrar == "sim" ):
            break
        o_que_deseja()


def mostrar_portifolio():
    cont = 1
    print("\n----------- PORTIFÓLIO DE VEÍCULOS DISPONÍVEIS PARA LOCAÇÃO -----------")
    for veiculo in veiculos_alugar:
        print(f" {cont} - {veiculo['fabricante']} {veiculo['modelo']} {veiculo['cor']} {veiculo['ano']} - Diária R$ {veiculo['valor']:.2f}" )
        cont += 1
    print("------------------------------------------------------------------------\n")


def o_que_deseja():
    print("\n=================================")
    print("Bem vindo à Locadora de Veículos!")
    print("=================================")
    print("O que deseja fazer?")
    print(" A - Mostrar portifólio")
    print(" B - Alugar um veículo")
    print(" C - Devolver um veículo")
    desejo = input().lower()
    if (desejo == "a"):
        mostrar_portifolio()


# ----- Execução do Programa -----
iniciar_veiculos_alugar()
gestor_execucao()


#mostrar_portifolio()
#o_que_deseja()

# print( veiculos_alugar[0]["fabricante"] )

# for veiculo in veiculos_alugar:
#     print(veiculo["fabricante"])