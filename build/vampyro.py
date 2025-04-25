import random
import time
import os


def titulo():
    os.system('cls')
    print('''
          

          Ꝟ𐌰ꡕƤ𐌸𐍂𐍈
          
          
''')
    
def creditos():
    print('Gerador de ficha de Vampire: The Masquerade - V3')
    print('Criado por: Bento')
    print('Github: https://github.com/Bento095')

lista_cla = {
    "Brujah":{"Rapidez":0,"Potencia":0,"Presença":0},
    "Gangrel":{"Animalismo":0,"Metamorfose":0,"Fortitude":0},
    "Malkavian":{"Demencia":0,"Auspicios":0,"Ofuscacao":0},
    "Nosferatu":{"Ofuscacao":0,"Potencia":0,"Animalismo":0},
    "Toreador":{"Auspicios":0,"Rapidez":0,"Presença":0},
    "Tremere":{"Auspicios":0,"Dominacao": 0,"Taumaturgia": 0},
    "Ventrue":{"Dominacao": 0,"Fortitude":0,"Presença":0},
    "Tzimisce":{"Vicissitude":0,"Animalismo":0,"Auspicios":0},
    "Lasombra":{"Tenebrosidade":0,"Dominacao": 0,"Potencia":0},
    "Giovanni":{"Necromancia": 0,"Dominacao": 0,"Potencia":0},
    "Assamita":{"Quietus":0,"Rapidez":0,"Ofuscacao":0},
    "Setita":{"Serpentis":0,"Ofuscacao":0,"Presença":0},
    "Ravnos":{"Quimerismo":0,"Animalismo":0,"Fortitude":0},
    "Caitif":{}
}

lista_disciplinas = {
    "Animalismo": 0,"Auspícios": 0,"Demencia": 0,"Dominacao": 0,
    "Fortitude": 0,"Metamorfose": 0,"Necromancia": 0,"Ofuscacao": 0,
    "Potencia": 0,"Presença": 0,"Quietus": 0,"Quimerismo": 0,
    "Rapidez": 0,"Serpentis": 0,"Taumaturgia": 0,"Tenebrosidade": 0,"Vicissitude": 0
}

global disciplinas_caitif
global disciplinas

lista_atributos = {
    "fisicos": {
        "forca": 1,"destreza": 1,"vigor": 1},
    "sociais": {
        "carisma": 1,"manipulacao": 1,"aparencia": 1},
    "mentais": {
        "percepcao": 1,"inteligencia": 1,"raciocinio": 1}
}

lista_habilidades = {
    "talentos": {
        'prontidao': 0,'esportes': 0,'briga': 0,'esquiva': 0,'empatia': 0,
        'expressao': 0,'intimidacao': 0,'lideranca': 0,'manha': 0,'labia': 0},
    "pericias": {
        'animais': 0,'oficios': 0,'conducao': 0,'etiqueta': 0,'armas_de_fogo': 0,
        'armas_brancas': 0,'performance': 0,'seguranca': 0,'furtividade': 0,'sobrevivencia': 0},
    "conhecimento": {
        'academicos': 0,'computador': 0,'financas': 0,'investigacao': 0,'direito': 0,
        'linguistica': 0,'medicina': 0,'ocultismo': 0,'politica': 0,'ciencia': 0}
}

lista_vantagens = {
    'antecedentes':{'aliados':0,'contatos':0,'fama':0,'geracao':0,'rebanho':0,'influencia':0,'mentor':0,'recursos':0,'lacaios':0,'status':0},
    'virtudes':{'consiencia':1,'autocontrole':1,'coragem':1}
}

lista_qed = {
    'sentidos aguçados':-1, 'ambidestro':-1, 'ingerir comida':-1, 'equilibrio perfeito':-1, 'rubror de saude':-2, 'voz encantadora':-2,
    'temerario':-3, 'digestão eficiente':-3, 'cheiro de tumulo':1, 'deficiencia auditiva':1,
    'mordida infecciosa':2, 'deficiencia visual':1, 'caolho':2, 'desfigurado':2, 'deformidade':3,
    'ferimento permanente':3, 'cura demorada':3, 'vicio':3, 'sangue fraco':4, 'portador de doença contagiosa':4,
    'pele cadavérica':5, 'bom senso':-1, 'concentração':-1, 'noção exata do tempo':-1, 'codigo de honra':-2,
    'memoria eidetica':-2, 'sono leve':-2, 'linguista nato':-2, 'temperamento calmo':-3, 'vontade de ferro':-3, 'sono pesado':1,
    'pesadelos':1, 'fobia':2, 'exclusao de presa':1, 'timidez':1, 'coração mole':1, 'dificuldade de fala':1, 'bairrismo':2, 'cabeça quente':2,
    'vingança':2, 'amnésia':1, 'lunatico':2, 'vontade fraca':3, 'consumo conspícuo':4, 'senhor de prestígio':-1, 'lider nato':-1,
    'divida de gratidão':1, 'senhor indigno':1, 'segredo sombrio':1, 'identidade trocada':1, 'ressentimento do senhor':1, 'inimigo':1, 'caçado':4,
    'membro de seita sob investigação':4, 'médium':-2, 'resistencia a magia':-2, 'habilidade oracular':-3, 'mentor espiritual':-3,
    'imunidade ao laço de sangue':-3, 'sorte':-3, 'amor verdadeiro':-4, 'nove vidas':-6, 'fé verdadeira':-7, 'toque de congelamento':1,
    'repulsa ao alho':1, 'amaldiçoado':1, 'imagem sem reflexo':1, 'presença sinistra':2, 'repulsa a cruzes':3, 'incapacidade de cruzar agua corrente':3,
    'assombrado':3, 'aperto dos amaldiçoados':4, 'futuro negro':5, 'sensibilidade a luz':5
} # Qualidades e Defeitos
# alguns foram removidos para nao impactar a limitação de narrativa, demais com multipla escolha em seu custo estao utilizando o menor, em caso de conflito, fica a escolha do mestre

removidos = {
    'corpo grande':-4, 'estatura baixa':1, 'criança':3, 'aleijado':3, 'monstruoso':3, 'mudo':4, 'surdez':4,'14 geração':2, 'cegueira':6
}

testes_disciplinas = {
    'Animalismo':{'manipulacao','carisma','animais','sobrevivencia','intimidacao'},#autocontrole
    'Auspicios':{'percepcao','empatia','inteligencia','labia','ocultismo'},#força de vontade
    'Demencia':{'carisma','empatia','manipulacao','labia','percepcao','ocultismo','intimidacao'},#pontos de sangue
    'Dominacao':{'manipulacao','intimidacao','lideranca','raciocinio','labia','carisma'},#força de vontade
    'Fortitude':{'vigor'},
    'Metamorfose':{'forca'},
    'Necromancia':{'percepcao','ocultismo','manipulacao','vigor','empatia','destreza','raciocinio','prontidao','inteligencia'},#Força de Vontade
    'Ofuscacao':{'raciocinio','furtividade','manipulacao','performance','carisma'},
    'Potencia':{'forca','destreza','esportes','briga'},
    'Presença':{'carisma','performance','intimidacao','aparencia','empatia','labia'},#força de vontade
    'Quietus':{'vigor','esportes','forca'},#pontos de sangue
    'Quimerismo':{'manipulacao','labia'},#força de vontade
    'Rapidez':{'destreza','esportes'},
    'Serpentis':{'forca','vigor'},
    'Taumaturgia':{'oficios','ciencia','vigor','esportes','raciocinio','sobrevivencia'},
    'Tenebrosidade':{'furtividade','manipulacao','ocultismo','vigor'},
    'Vicissitude':{'inteligencia','medicina','percepcao','destreza','forca','vigor'} #levando em consideração que moldar a carne seja = medicina
}

pontos_extras = 15

atributos_teste = []
habilidades_teste = []

atributos = {}

antecedentes = {}
virtudes = {}

qed = {} #qualidades e defeitos

custo_disciplinas = -7
custo_atributos = -5
custo_habilidades = -2
custo_virtudes = -2
custo_antecedentes = -1
custo_humanidade = -1
custo_forca_de_vontade = -1

pontos_atributos = [7,5,3] # pontos para atributos
pontos_habilidades = [13,9,5] # pontos para habilidades

def escolher_nome():
  print('Espaço em branco tera um nome padrão!')

  global nome

  nome = input('Nome do personagem: ').title()
  if nome == "":
      nome = "Indigente"
      print(nome)
  else:
      print(nome)

def escolher_cla():
  print('Espaço em branco tera uma cla aleatório!')
  global cla
  cla = input('Cla do personagem: ').title()

  if cla == "":
    cla = random.choice(list(lista_cla.keys()))
    cla = cla
    print(cla)
  elif cla in lista_cla:
    print(cla)
  else:
    print('Verifique a lista de clãs')
    print(list(lista_cla.keys()))
    escolher_cla()

def definir_diciplinas(cla):
    global disciplinas
    if cla == "Caitif":
        while len(lista_cla['Caitif']) < 3:  # checa se 'Caitif' tem ao menos 3 disciplines
            disciplina = random.choice(list(lista_disciplinas.keys()))  # escolhe disciplinas aleatorias
            lista_cla['Caitif'][disciplina] = int(0)  # define o nivel como 0
        print(lista_cla['Caitif'])
        disciplinas_caitif = lista_cla['Caitif'].copy()  # Cria uma cópia do dicionário
        (lista_cla['Caitif']).clear()
        disciplinas = disciplinas_caitif
    else:
        disciplinas = lista_cla[cla].copy()

    for i in range(3):
        disciplina = random.choice(list(disciplinas.items()))
        if disciplina in disciplinas.items():
            disciplinas[disciplina[0]] += 1

def disciplinas_cla_e_definir_atributos_habilidades():
    global disciplinas
    testes_do_cla = []

    # Preenche a lista testes_do_cla com base nas disciplinas
    for item in disciplinas:
        if item in testes_disciplinas:
            testes_do_cla.append(testes_disciplinas[item])

    # Limpa as listas de atributos e habilidades de teste
    atributos_teste.clear()
    habilidades_teste.clear()

    # Preenche as listas de atributos e habilidades de teste com base em testes_do_cla
    for itens_teste in testes_do_cla:
        atributos_teste.extend(list(filter(lambda x: x in [a for b in lista_atributos.values() for a in b], itens_teste)))
        habilidades_teste.extend(list(filter(lambda x: x in [a for b in lista_habilidades.values() for a in b], itens_teste)))

def definir_atributos(cla):
  global atributos
  atributos.clear()
  atributos = lista_atributos.copy()

  for i in atributos_teste:
    if i in atributos['fisicos']:
      atributos['fisicos'][i] +=1
    elif i in atributos['sociais']:
      atributos['sociais'][i] +=1
    elif i in atributos['mentais']:
      atributos['mentais'][i] +=1

  if cla == 'Nosferatu':
    atributos['sociais']['aparencia'] = 0

def definir_habilidades():
  global habilidades
  habilidades = lista_habilidades.copy()

  for i in habilidades_teste:
    if i in habilidades['talentos']:
      habilidades['talentos'][i] +=1
    elif i in habilidades['pericias']:
      habilidades['pericias'][i] +=1
    elif i in habilidades['conhecimento']:
      habilidades['conhecimento'][i] +=1

def definir_antecedentes():
  global antecedentes
  antecedentes.clear()
  antecedentes = lista_vantagens["antecedentes"].copy()
  for i in range(5):
    antecedente = random.choice(list(antecedentes.items()))
    if antecedente in antecedentes.items():
      antecedentes[antecedente[0]] += 1
    else:
      antecedentes[antecedente[0]] = 0

  for i in list(antecedentes.keys()):
    if antecedentes[i] == 0:
      del antecedentes[i]

def definir_virtudes():
  global virtudes #se n funcionar
  virtudes.clear() #começa limpando

  virtudes = lista_vantagens["virtudes"].copy() # {'consiencia': 1, 'autocontrole': 1, 'coragem': 1}
  ''' copia o dicionario de lista_vantagens['virtudes'] '''

  for i in range(8): # repete 8x
    virtude = random.choice(list(virtudes.items())) # declara a virtude sorteada
    if virtude in virtudes.items() and virtudes[virtude[0]] < 5: # verifica a virtude na lista
      virtudes[virtude[0]] +=1 #adiciona +1 ponto a virtude

def definir_qed():
  global qed
  qed.clear()
  pontos_extras = 15
  for i in range(5):
    caracteristica = random.choice(list(lista_qed.items()))
    if caracteristica not in qed.items():
      qed[caracteristica[0]] = caracteristica[1]

  pontos_extras += sum(qed.values())

def definir_humanidade():
    global humanidade
    humanidade = virtudes['consiencia'] + virtudes['autocontrole']

def definir_forca_de_vontade():
    global forca_de_vontade
    forca_de_vontade = virtudes['coragem']

def definir_geracao():
  global geracao
  geracao = 13

  if 'geracao' in antecedentes:
    geracao -= antecedentes['geracao']

def definir_pontos_de_sangue():
    global pontos_de_sangue
    d10 = list(range(1,11))
    pontos_de_sangue = random.choice(d10)
    if geracao != 13:
      diferenca = 13 - geracao
      pontos_de_sangue = f"{pontos_de_sangue}/{diferenca + 10}"
    else:
        pontos_de_sangue = f"{pontos_de_sangue}/{10}"

def calcular_pontos_gastos():
    """
    Calcula os pontos extras gastos com base nos atributos do personagem.
    """
    global pontos_extras
    global pontos_preset_atributos  # Acessa variáveis globais

    # Calcula os pontos já gastos em cada categoria de atributos
    pontos_preset_atributos = (
        sum(atributos['fisicos'].values()) - 3,
        sum(atributos['sociais'].values()) - 3,
        sum(atributos['mentais'].values()) - 3
    )

    # Verifica se há mais de 4 pontos gastos em pelo menos duas categorias
    if (
        (pontos_preset_atributos[0] >= 4 and pontos_preset_atributos[1] >= 4) or
        (pontos_preset_atributos[0] >= 4 and pontos_preset_atributos[2] >= 4) or
        (pontos_preset_atributos[1] >= 4 and pontos_preset_atributos[2] >= 4)
    ):
        pontos_extras += custo_atributos

def distribuir_pontos_atributos():
    """
    Distribui pontos de atributos aleatoriamente para um personagem,
    considerando limites e regras específicas.
    """
    global atributos, pontos_preset_atributos  # Acessa variáveis globais

    # Cria uma lista com as categorias de atributos (físicos, sociais, mentais)
    categorias_disponiveis = list(atributos.keys())

    # Embaralha a ordem dos pontos a serem distribuídos ([7, 5, 3])
    random.shuffle(pontos_atributos)

    # Cria uma cópia da lista de pontos para evitar modificá-la diretamente
    pontos_atributos_copia = pontos_atributos.copy()

    # Itera pelas 3 categorias de atributos (físicos, sociais, mentais)
    for i in range(3):
        # Define a quantidade de pontos para a categoria atual
        ponto = pontos_atributos_copia[i]

        # Subtrai os pontos já gastos na categoria
        ponto -= pontos_preset_atributos[i]

        # Se não há mais pontos para distribuir na categoria, pula para a próxima
        if ponto <= 0:
            continue

        # Define a categoria de atributo atual (físicos, sociais ou mentais)
        categoria_escolhida = list(atributos.keys())[i]

        # Distribui pontos na categoria enquanto houver pontos disponíveis
        while ponto > 0:
            # Cria uma lista de atributos disponíveis para receber pontos
            # (valor menor que 5 e respeitando a regra do Nosferatu)
            atributos_disponiveis = [
                atributo for atributo, valor in atributos[categoria_escolhida].items()
                if valor < 5 and (cla != 'Nosferatu' or atributo != 'aparencia')
            ]

            # Se não houver mais atributos disponíveis na categoria, sai do loop
            if not atributos_disponiveis:
                break

            # Escolhe aleatoriamente um atributo da lista de atributos disponíveis
            atributo_escolhido = random.choice(atributos_disponiveis)

            # Adiciona 1 ponto ao atributo escolhido
            atributos[categoria_escolhida][atributo_escolhido] += 1

            # Diminui 1 da quantidade de pontos disponíveis para a categoria
            ponto -= 1

def pontos_gastos_habilidades():
    global pontos_extras, pontos_preset_habilidades  # Acessa variáveis globais
    pontos_preset_habilidades = sum(habilidades['talentos'].values()),sum(habilidades['pericias'].values()),sum(habilidades['conhecimento'].values())

def distribuir_pontos_habilidades():
    """
    Distribui pontos de habilidades aleatoriamente para um personagem,
    considerando limites e regras específicas.
    """
    global habilidades, pontos_preset_habilidades  # Acessa variáveis globais

    categorias_disponiveis = list(habilidades.keys())  # Cria uma lista com as categorias de habilidades

    random.shuffle(pontos_habilidades)  # Embaralha a ordem dos pontos a serem distribuídos

    pontos_habilidades_copia = pontos_habilidades.copy()

    for i in range(3):
        ponto = pontos_habilidades_copia[i]
        ponto -= pontos_preset_habilidades[i]

        if ponto <= 0:
            continue

        categoria_escolhida = list(habilidades.keys())[i]

        while ponto > 0:
            habilidades_disponiveis = [
                habilidade for habilidade, valor in habilidades[categoria_escolhida].items()
                if valor < 5
            ]

            if not habilidades_disponiveis:
                break

            habilidade_escolhida = random.choice(habilidades_disponiveis)
            habilidades[categoria_escolhida][habilidade_escolhida] += 1
            ponto -= 1

    habilidades = {tipo: {hab: pont for hab, pont in hab_dict.items() if pont != 0}
              for tipo, hab_dict in habilidades.items()}        
    

class Vampiro:
    def __init__(self, nome, geracao, cla, atributos, habilidades, vantagens, qualidades_defeitos, trilha, forca_de_vontade, pontos_de_sangue):
        self.nome = nome
        self.geracao = geracao
        self.cla = cla
        self.atributos = atributos
        self.habilidades = habilidades
        self.vantagens = vantagens
        self.qualidades_defeitos = qualidades_defeitos
        self.disciplinas = disciplinas
        self.antecedentes = antecedentes
        self.virtudes = virtudes
        self.qed = qualidades_defeitos
        self.humanidade = humanidade
        self.forca_de_vontade = forca_de_vontade
        self.pontos_de_sangue = pontos_de_sangue


    def ficha(self):
      print(self.nome, self.cla, self.geracao, "geração,",
        '\nAtributos',
        '\nFisicos:', self.atributos['fisicos'],
        '\nSociais:', self.atributos['sociais'],
        '\nMentais:', self.atributos['mentais'],
        '\nHabilidades:',
        '\nTalentos:', self.habilidades['talentos'],
        '\nPericias:', self.habilidades['pericias'],
        '\nConhecimentos:', self.habilidades['conhecimento'],
        '\nVantagens:',
        '\nAntecedentes', self.antecedentes,
        '\nDisciplinas', self.disciplinas,
        '\nVirtudes', self.virtudes,
        '\nQualidades e Defeitos', self.qed,
        '\nHumanidade', self.humanidade,'|', 'Força de Vontade', self.forca_de_vontade,'|', 'Pontos de Sangue', self.pontos_de_sangue)

def recomecar():
    print('Gerar novamente? ')
    resposta = input('Digite s para sim ou n para não: ').lower()
    if resposta == 's':
        os.system('cls')
        main()
    elif resposta == 'n':
        os.system('cls')
        print('''
              
              Obrigado por testar!
              
''')
        time.sleep(0.68)
    else:
        print('Opção inválida. Tente novamente.')
        recomecar()
    
   
def main():
    titulo()
    creditos()
    # Escolha do nome e clã do personagem
    escolher_nome()
    escolher_cla()

    # Definição de disciplinas e atributos/habilidades baseados no clã
    definir_diciplinas(cla)
    disciplinas_cla_e_definir_atributos_habilidades()

    # Definição de atributos, habilidades, vantagens e qualidades/defeitos
    definir_atributos(cla)
    definir_habilidades()
    definir_antecedentes()
    definir_virtudes()
    definir_qed()

    # Definição de humanidade, força de vontade, pontos de sangue e geração
    definir_humanidade()
    definir_forca_de_vontade()
    definir_geracao()
    definir_pontos_de_sangue()

    # Cálculo e distribuição de pontos extras
    calcular_pontos_gastos()
    distribuir_pontos_atributos()
    pontos_gastos_habilidades()
    distribuir_pontos_habilidades()

    # Criação do objeto Vampiro e exibição da ficha
    vampiro = Vampiro(
        nome=nome,
        geracao=geracao,
        cla=cla,
        atributos=atributos,
        habilidades=habilidades,
        vantagens=lista_vantagens,
        qualidades_defeitos=qed,
        trilha=None,  # Adicione a trilha se necessário
        forca_de_vontade=forca_de_vontade,
        pontos_de_sangue=pontos_de_sangue
    )
    os.system('cls')
    titulo()
    vampiro.ficha()
    time.sleep(3.5)
    recomecar()

if __name__ == "__main__":
    main()
