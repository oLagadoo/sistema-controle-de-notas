print("Hello, world!")

while True:
    nome_aluno = str(input("Digite seu nome: ")).lower()

    nota_somada = 0
    notas_digitadas = 0

    for i in range(1, 4):
        notas = float(input(f'Digite sua {i}ª nota: '))

        nota_somada += notas
        notas_digitadas += 1

    media_calculada = nota_somada / notas_digitadas
    print(f'Sua média é {media_calculada:.2f}')

    if media_calculada > 7:
        print("Aprovado")
    elif media_calculada >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

    opcao = input("Deseja calcular outro aluno? (s/n): ").lower()

    if opcao != 's':
        print("Programa encerrado!")
        break