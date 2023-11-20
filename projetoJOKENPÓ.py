#Bibliotecas/libraries
from time import sleep
from random import choice

#Variáveis/variables
ia = choice([1,2,3])
pe = 'Pedra'
pa = 'Papel'
te = 'Tesoura'
lista = 1,2,3

#Design
print('\033[1;33m=-' * 7), print('\033[1;31mJ-O-K-E-N-P-Ô\033[m'), print('\033[1;33m=-\033[m' * 7)

#Escolha/Choice
print('\033[1;32mEscolha sua jogada \n [1] PEDRA\n [2] PAPEL \n [3] TESOURA\033[m') #PEDRA=ROCK, PAPEL=PAPER, TESOURA=SCISSORS
sleep(1)
esc = int(input('\033[4;36mQUAL A SUA ESCOLHA: \033[m')) #choice a number [1,2,3]

#Condições pedra/conditions rock
if esc == 1 and ia == 1:
    print('\033[1;34mVocê escolheu {}\033[m \n\033[1;36mO computador escolheu {}\033[m \n\033[1;33m\nVOCÊS EMPATARAM\033[m'.format(pe,pe))
elif esc == 1 and ia == 2:
    print('\033[1;34mVocê escolheu {}\033[m \n\033[1;36mO computador escolheu {}\033[m \n\033[1;31mVOCÊ PERDEU\033[m'.format(pe,pa))
elif esc == 1 and ia == 3:
    print('\033[1;34mVocê escolheu {}\033[m \n\033[1;36mO computador escolheu {}\033[m \n\033[1;32mVOCÊ GANHOU!!!\033[m'.format(pe,te))

#Condições papel/conditions paper
if esc == 2 and ia == 1:
    print('\033[1;34mVocê escolheu {}\033[m \n\033[1;36mO computador escolheu {}\033[m \n\033[1;32mVOCÊ GANHOU!!!\033[m'.format(pa,pe))
elif esc == 2 and ia == 2:
    print('\033[1;34mVocê escolheu {}\033[m \n\033[1;36mO computador escolheu {}\033[m \n\033[1;33mVOCÊS EMPATARAM\033[m'.format(pa,pa))
elif esc == 2 and ia == 3:
    print('\033[1;34mVocê escolheu {}\033[m \n\033[1;36mO computador escolheu {}\033[m \n\033[1;31mVOCÊ PERDEU\033[m'.format(pa,te))


#Condições Tesoura/conditions scissors
if esc == 3 and ia == 1:
    print('\033[1;34mVocê escolheu {}\033[m \n\033[1;36mO computador escolheu {}\033[m \n\033[1;31mVOCÊ PERDEU\033[m'.format(te,pe))
elif esc == 3 and ia == 2:
    print('\033[1;34mVocê escolheu {}\033[m \n\033[1;36mO computador escolheu {}\033[m \n\033[1;32mVOCÊ GANHOU!!!\033[m'.format(te,pa))
elif esc == 3 and ia == 3:
    print('\033[1;34mVocê escolheu {}\033[m \n\033[1;36mO computador escolheu {}\033[m \n\033[1;33mVOCÊS EMPATARAM\033[m'.format(te,te))


