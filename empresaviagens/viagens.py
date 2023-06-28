print("----------- FRM VIAGENS ---------")

nome = input("Qual é o seu nome? ")
while nome.strip() == "" or nome.isnumeric():
    print("Seleção inválida. Por favor, digite um nome válido.")
    nome = input("Qual é o seu nome? ")

print(f"Falaaa, {nome}! Você deve estar muito cansado do seu trabalho atual e quer tirar umas férias. Está no lugar certo!")
print("")

print("Responda as demais perguntas sobre os seus gostos")

print("Para onde deseja viajar?:")
print("1 - México")
print("2 - Praia")
print("3 - New York")
print("4 - Europa")

resposta1 = input("Escolha uma opção (1/2/3/4): ")
while not resposta1.isdigit() or int(resposta1) not in range(1, 5):
    print("Seleção inválida. Por favor, escolha um número de item de menu válido.")
    resposta1 = input("Informe o número do local que deseja ir: ")

print("")

print("Segunda parte: ")
print("Tipo de locomoção:")
print("1 - Avião")
print("2 - Trem")
print("3 - Carro")
print("4 - Ônibus")

resposta2 = input("Escolha uma opção (1/2/3/4): ")
while not resposta2.isdigit() or int(resposta2) not in range(1, 5):
    print("Seleção inválida. Por favor, escolha um número de item de menu válido.")
    resposta2 = input("Informe o número do transporte: ")

print("")

print("Terceira parte: ")
print("Tipo de atividades:")
print("Quais são as atividades que você quer fazer no local?")
print("1 - Andar de brinquedos")
print("2 - Passear pela cidade")
print("3 - Parque aquático")
print("4 - Andar de ski")

resposta3 = input("Escolha uma opção (1/2/3/4): ")
while not resposta3.isdigit() or int(resposta3) not in range(1, 5):
    print("Seleção inválida. Por favor, escolha um número de item de menu válido.")
    resposta3 = input("Informe o número do código da atração: ")

print("")

print("Analisando suas respostas...")

destino = ""

if resposta1 == "1" and resposta2 == "1" and resposta3 == "1":
    destino = "Cancun, México"
elif resposta1 == "1" and resposta2 == "1" and resposta3 == "2":
    destino = "Rio de Janeiro, Brasil"
elif resposta1 == "2" and resposta2 == "4" and resposta3 == "1":
    destino = "Chamonix, França"
elif resposta1 == "2" and resposta2 == "4" and resposta3 == "4":
    destino = "Aspen, Estados Unidos"

if destino != "":
    resposta4 = input("Por quantos dias você pretende viajar? ")
    while not resposta4.isdigit() or int(resposta4) <= 1 or int(resposta4) > 30:
        print("Duração inválida. Por favor, escolha um número válido de dias (entre 2 e 30 dias).")
        resposta4 = input("Por quantos dias você pretende viajar? ")

    print(f"{nome}, eu sugiro que você vá para {destino} por {resposta4} dias!")
    print("")

    agendamento = input("Você deseja agendar sua viagem? (s/n) ")

    while agendamento.lower() not in ['s', 'sim', 'n', 'não']:
        print("Seleção inválida. Por favor, responda com 's', 'sim', 'n' ou 'não'.")
        agendamento = input("Você deseja agendar sua viagem? (s/n) ")

    if agendamento.lower() in ['s', 'sim']:
        print("Ok! vamos agendar...")
        print("")

        meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        mes = input("De qual mês você prefere viajar? ")

        while mes.lower() not in meses:
            print("Mês inválido. Por favor, escolha um mês válido.")
            mes = input("De qual mês você prefere viajar? ")

        dia = input("Qual dia é melhor para você? ")

        while not dia.isdigit() or int(dia) < 2 or int(dia) > 31:
            print("Dia inválido. Por favor, escolha um dia válido (entre 2 e 31).")
            dia = input("Qual dia é melhor para você? ")

        print("")
        print(f"Está marcado então para o dia {int(dia):02d} de {mes}!")  # Formatação para exibir o dia com dois dígitos

    else:
        print("Está perdendo uma grande oportunidade... Volte sempre!")

else:
    print("Desculpe, não foi possível encontrar um destino adequado com base nas suas respostas.")
    print("")
    print("Muito obrigado, mas se estiver interessado, volte e tente refazer o questionário....")
