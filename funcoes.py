import textmons
import ataques
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def batalha(textmon_inicial, textmon_inimigo):
    while (int(textmon_inicial.hp > 0)*int(textmon_inimigo.hp > 0) == 1):
        print('seu turno \n')
        textmon_inicial.ataque(textmon_inimigo)
        if (textmon_inimigo.hp <= 0):
            print('voce ganhou')
            break
        print('')
        print('turno inimigo \n')
        textmon_inimigo.ataque_aleatorio(textmon_inicial)
        if (textmon_inicial.hp <= 0):
            print('voce perdeu')
            break
            
def dano(tipo_ataque, tipo_defesa):
    print((tipo_ataque, tipo_defesa))
    mod=1
    for i in range(0, len(ataques.efetivo)):
        if ((tipo_ataque, tipo_defesa) == ataques.efetivo[i]):
            mod = 2
            break
        elif ((tipo_ataque, tipo_defesa) == ataques.inefetivo[i]):
            mod = 0.5
            break
    return mod
    
