print("Hello, world!")

def ler_notas():
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Digite a {i}ª nota: "))
        notas.append(nota)
    return notas

def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_situacao(media):
    if media > 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def mostrar_resultado(nome, media, situacao):
    print(f"Aluno: {nome}")
    print(f"Media: {media:.2f}")
    print(f"Situação: {situacao}")

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