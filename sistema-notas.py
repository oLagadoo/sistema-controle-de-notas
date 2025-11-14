from funcoes import ler_notas, calcular_media, verificar_situacao, mostrar_resultado

print("Hello, world!")

while True:
    nome = input("Digite o nome do aluno: ")

    notas = ler_notas()
    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    mostrar_resultado(nome, media, situacao)

    opcao = input("\nDeseja calcular outro aluno? (s/n): ").lower()
    if opcao != 's':
        print("Programa encerrado!")
        break