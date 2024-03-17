from random import randint
#from time import sleep
computador = randint(0, 20)#sotear o número

print('Sou seu computador... acabei de pensar em um munero entre 0 e 10. ')
print('Sera que você conseque adivinhar qual foi? ')
acertou = False #vc não acertou ainda
palpites = 0 # não teve palpite
chute = []
while not acertou:#qual não acertou
    jogador = int(input('Qual é seu palpite? '))#Jogador tenta adidinha
    palpites += 1 #Palpite recebi + 1 palpite
    if jogador == computador: #pensa o mesmo nº q o PC
        acertou = True # acertou
        #chute.append(jogador)
    else:
        if jogador < computador:
            print('MAIS... tente mais uma vez')
            chute.append(jogador)
        elif jogador > computador:
            print('MENOS... tente mais uma vez')
            chute.append(jogador)
print('Acertou com {} palpites'.format(palpites))
print('Os seus chutes foram: {}'.format(chute))