programas = int(input("Selecione o programa\n[1]\n[2]\n[3]\n[4]\n: "))

if programas == 1:
        texto = str(input("Informe um texto: "))
        VOGAIS = "AEIOU"

        for letra in texto:
            if letra.upper() in VOGAIS:
                print(letra, end="")
        else:
            print()
            print("Executa no final do laço")

        for  numero in range(0, 51, 5):
            print(numero, end=" ")

if programas == 2:
    opcao = -1

    while opcao != 0:
        opcao = int(input("\n[1] Sacar\n[2] extrato\n[0]  Sair\n: "))

        if opcao == 1:
            print("Sacando...")
        elif opcao == 2:
            print("Exibindo o extrato...")

    else:
        print("Obrigado por usar nosso sistema bancário, até logo!")

if programas == 3: 

    while True:
        numero = int(input("Informe um numero: "))
        
        if numero == 10:
            break

        if numero % 2 == 0:
            continue

        print(numero)
    
if programas == 4:
    for numero in range(100):
        if numero % 2 == 0:
            continue

        print(numero, end=" ")