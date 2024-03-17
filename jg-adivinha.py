from random import randint #importando randomizer

while True: #iniciando o jogo
    numx = randint(1, 20) #pegando número x

    numr = int(input('Qual número o programa pensou? de 1 a 100: '))
    tentativas = 1
    chute = [numr] #abrindo uma lista de chutes
    while numr != numx: #Começando a repetição do jogo
        if numx > numr: #caso número x seja maior que chute
            print('-'*10)
            print('O número que o programa pensou é maior que {}'.format(numr))
            numr = int(input('Digite um outro número '))
            tentativas = tentativas + 1
            chute.append(numr) #adiciona chute à lista
        else: #Caso número x seja menor que chute
            print('-'*10)
            print('O número que o programa pensou é menor que {}!'.format(numr))
            numr = int(input('Digite um outro número '))
            tentativas = tentativas + 1
            chute.append(numr) #adiciona chute à lista
    print('-'*10)
    print('Parabéns, você acertou em {} tentativas, o número que o programa pensou era {}!'.format(tentativas, numx))
    print('Os seus chutes foram: {}'.format(chute))
    continuar = input('Deseja jogar outra partida?? (s/n) ') #valindando caso queira loopar o programa
    pergunta = ['sim', 's', 'yes']
    if continuar not in pergunta:
        break