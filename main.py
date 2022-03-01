import textmons
import funcoes

print('Bem vindo ao mundo TextMon')
nome_jogador = input('Qual o seu nome?\n')
print("\n")

print("Temos essas opções:")
for i in range(0,len(textmons.conhecidos)):
    print(textmons.conhecidos[i].nome)
textmon_inicial = input("Escolha seu textmon: ")
print("\n")    

for i in range(0, len(textmons.conhecidos)):
    if (textmon_inicial == textmons.conhecidos[i].nome):
        textmon_inicial = textmons.conhecidos[i]

jogador = textmons.jogador(nome_jogador, textmon_inicial)

#funcoes.sleep(2)
#funcoes.clear()

print("Seja bem vindo " + jogador.nome + ". Seu textmon inicial é: " + jogador.inicial.nome + "\n")

print("Os ataques do seu textmon são:")
print(textmon_inicial.p1.nome + " e " + textmon_inicial.p2.nome)
print(" ")

print("Batalha")
print("Quem você quer enfrentar?")
for i in range(0,4):
    print(textmons.conhecidos[i].nome)
textmon_inimigo = input("Escolha seu adversário: ")
print("\n") 

for i in range(0, len(textmons.conhecidos)):
    if (textmon_inimigo == textmons.conhecidos[i].nome):
        textmon_inimigo = textmons.conhecidos[i]

#funcoes.sleep(2)
#funcoes.clear()
 
print('Você está enfrentando ', textmon_inimigo.nome, '\n')

funcoes.batalha(textmon_inicial, textmon_inimigo)