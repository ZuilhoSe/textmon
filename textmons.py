import random
import ataques
import funcoes

class textmon(object):
    
    # Constructor
    def __init__(self, nome, tipo, hp, p1, p2, ataque_base, defesa_base):
        self.nome = nome
        self.tipo = tipo   
        self.hp = hp
        self.p1 = p1
        self.p2 = p2
        self.ataque_base = ataque_base
        self.defesa_base = defesa_base
        
    def ataque(self, oponente):
        i = 0
        while i == 0:
            print("Seus ataques:")
            print(self.p1.nome)
            print(self.p2.nome)
            ataque_atual = input('Escolha seu ataque: ')

            if (ataque_atual == self.p1.nome):
                mod = funcoes.dano(self.p1.tipo, oponente.tipo)
                dano = self.p1.dano*mod+self.ataque_base-oponente.defesa_base
                oponente.hp = oponente.hp - dano
                print(self.nome, " usou ", self.p1.nome)
                print(oponente.nome, "tomou", dano, "de dano", "mod=",mod)
                print(oponente.nome, "tem apenas", oponente.hp, "de vida \n")
                i=1
            elif (ataque_atual == self.p2.nome):
                mod = funcoes.dano(self.p1.tipo, oponente.tipo)
                dano = self.p1.dano*mod+self.ataque_base-oponente.defesa_base
                oponente.hp = oponente.hp - dano
                print(self.nome, " usou ", self.p1.nome)
                print(oponente.nome, "tomou", dano, "de dano", "mod=",mod)
                print(oponente.nome, "tem apenas", oponente.hp, "de vida \n")
                i=1
            else:
                print("Ataque inexistente \n") 
                
    def ataque_aleatorio(self, oponente):
        i = random.randint(1,2)
        if (i == 1):
            mod = funcoes.dano(self.p1.tipo, oponente.tipo)
            dano = self.p1.dano*mod+self.ataque_base-oponente.defesa_base
            oponente.hp = oponente.hp - dano
            print(self.nome, " usou ", self.p1.nome)
            print(oponente.nome, "tomou", dano, "de dano", "mod=",mod)
            print(oponente.nome, "tem apenas", oponente.hp, "de vida \n")
        elif (i == 2):
            mod = funcoes.dano(self.p1.tipo, oponente.tipo)
            dano = self.p1.dano*mod+self.ataque_base-oponente.defesa_base
            oponente.hp = oponente.hp - dano
            print(self.nome, " usou ", self.p1.nome)
            print(oponente.nome, "tomou", dano, "de dano", "mod=",mod)
            print(oponente.nome, "tem apenas", oponente.hp, "de vida \n")
        
class eletrico(textmon):
    def __init__(self, nome, tipo='eletrico', hp=random.randint(8, 12), p1=ataques.choque_do_trovao, p2=ataques.choquinho, ataque_base=random.randint(1,3), defesa_base=random.randint(1,3)):
        super().__init__(nome, tipo, hp, p1, p2, ataque_base, defesa_base)
        
class planta(textmon):
    def __init__(self, nome, tipo='planta', hp=random.randint(8, 12), p1=ataques.chicote, p2=ataques.raio_solar, ataque_base=random.randint(1,3), defesa_base=random.randint(1,3)):
        super().__init__(nome, tipo, hp, p1, p2, ataque_base, defesa_base)
        
class agua(textmon):
    def __init__(self, nome, tipo='agua', hp=random.randint(8, 12), p1=ataques.bolhas, p2=ataques.canhao_de_agua, ataque_base=random.randint(1,3), defesa_base=random.randint(1,3)):
        super().__init__(nome, tipo, hp, p1, p2, ataque_base, defesa_base)
        
class normal(textmon):
    def __init__(self, nome, tipo='normal', hp=random.randint(8, 12), p1=ataques.cabecada, p2=ataques.arranhao, ataque_base=random.randint(1,3), defesa_base=random.randint(1,3)):
        super().__init__(nome, tipo, hp, p1, p2, ataque_base, defesa_base)
        
class fogo(textmon):
    def __init__(self, nome, tipo='fogo', hp=random.randint(8, 12), p1=ataques.chamas, p2=ataques.labareda, ataque_base=random.randint(1,3), defesa_base=random.randint(1,3)):
        super().__init__(nome, tipo, hp, p1, p2, ataque_base, defesa_base)
        
textchu = eletrico('textchu')
bulbatext = planta('bulbatext')
squirtext = agua('squirtext')
eeteext = normal('eeteext')              
chartext = fogo('chartext')
conhecidos = [textchu, bulbatext, squirtext, eeteext, chartext]
        
class jogador(object):
    def __init__(self, nome, inicial):
        self.nome = nome
        self.inicial = inicial
             

  