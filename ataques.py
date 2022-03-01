class atk(object):
    def __init__(self, nome, tipo, dano):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano

choquinho = atk('choquinho', 'eletrico', 3)
choque_do_trovao = atk('choque_do_trovao', 'eletrico', 3)
chicote = atk('chicote', 'planta', 3)
raio_solar = atk('raio_solar', 'planta', 3)
bolhas = atk('bolhas', 'agua', 3)
canhao_de_agua = atk('canhao_de_agua', 'agua', 3)
cabecada = atk('cabecada', 'normal', 3)
arranhao = atk('arranhao', 'normal', 3)
chamas = atk('chamas', 'fogo', 3)
labareda = atk('labareda', 'fogo', 3)

efetivo = [('fogo', 'planta'), ('planta', 'agua'), ('agua', 'fogo'), ('eletrico', 'agua')]
inefetivo = [('planta', 'fogo'), ('agua', 'planta'), ('fogo', 'agua'), ('agua', 'eletrico')]

# planta -> agua
# agua -> fogo
# fogo -> planta
# eletrico -> agua
# normal