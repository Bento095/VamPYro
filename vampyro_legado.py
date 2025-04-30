import random
import time
import os
import copy
from conteudos import *

def titulo():
    os.system('cls')
    print('''
          

          Ꝟ𐌰ꡕƤ𐌸𐍂𐍈
          
          
''')
    
def creditos():
    print('Gerador de ficha de Vampire: The Masquerade - V3')
    print('Criado por: Bento')
    print('Github: https://github.com/Bento095')



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
        print(cla)
    elif cla in lista_cla:
        print(cla)
    else:
        print('Verifique a lista de clãs')
        print(list(lista_cla.keys()))
        escolher_cla()
        
cla = escolher_cla()

def definir_diciplinas():
    global cla,disciplinas
    disciplinas = {}

    if cla == "Caitif":
        while len(lista_cla['Caitif']) < 3:  # checa se 'Caitif' tem ao menos 3 disciplines
            disciplina = random.choice(list(lista_disciplinas.keys()))  # escolhe disciplinas aleatorias
            lista_cla['Caitif'][disciplina] = int(0)  # define o nivel como 0
        disciplinas_caitif = lista_cla['Caitif'].copy()  # Cria uma cópia do dicionário
        (lista_cla['Caitif']).clear()
        disciplinas = disciplinas_caitif
    else:
        disciplinas = lista_cla[cla].copy()
        

    for i in range(3):
        disciplina = random.choice(list(disciplinas.items()))
        if disciplina in disciplinas.items():
            disciplinas[disciplina[0]] += 1

    return disciplinas

def disciplinas_cla_e_definir_atributos_habilidades():
    global disciplinas,atributos,habilidades
    # Limpa as listas de atributos e habilidades de teste
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

def definir_atributos():
    global cla,atributos
    atributos = {
    'fisicos': {'forca': 1, 'destreza': 1, 'vigor': 1},
    'sociais': {'carisma': 1, 'manipulacao': 1, 'aparencia': 1},
    'mentais': {'percepcao': 1, 'inteligencia': 1, 'raciocinio': 1}
}
    for i in atributos_teste:
        if i in atributos['fisicos']:
            atributos['fisicos'][i] +=1
        elif i in atributos['sociais']:
            atributos['sociais'][i] +=1
        elif i in atributos['mentais']:
            atributos['mentais'][i] +=1     
    if cla == 'Nosferatu':
        atributos['sociais']['aparencia'] = 0

    return atributos

atributos = definir_atributos()

def definir_habilidades():
    global cla,habilidades
    habilidades = {
    'talentos': {
        'prontidao': 0, 'esportes': 0, 'briga': 0, 'esquiva': 0, 'empatia': 0,
        'expressao': 0, 'intimidacao': 0, 'lideranca': 0, 'manha': 0, 'labia': 0
    },
    'pericias': {
        'animais': 0, 'oficios': 0, 'conducao': 0, 'etiqueta': 0, 'armas_de_fogo': 0,
        'armas_brancas': 0, 'performance': 0, 'seguranca': 0, 'furtividade': 0, 'sobrevivencia': 0
    },
    'conhecimento': {
        'academicos': 0, 'computador': 0, 'financas': 0, 'investigacao': 0, 'direito': 0,
        'linguistica': 0, 'medicina': 0, 'ocultismo': 0, 'politica': 0, 'ciencia': 0
    }
}
    for i in habilidades_teste:
        if i in habilidades['talentos']:
            habilidades['talentos'][i] +=1
        elif i in habilidades['pericias']:
            habilidades['pericias'][i] +=1
        elif i in habilidades['conhecimento']:
            habilidades['conhecimento'][i] +=1

    return habilidades

atributos = definir_atributos()
habilidades = definir_habilidades()

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
    global virtudes, forca_de_vontade
    virtudes.clear() #começa limpando
    virtudes = lista_vantagens["virtudes"].copy() # {'consiencia': 1, 'autocontrole': 1, 'coragem': 1}
    ''' copia o dicionario de lista_vantagens['virtudes'] '''

    for i in range(8): # repete 8x
        virtude = random.choice(list(virtudes.items())) # declara a virtude sorteada
        if virtude in virtudes.items() and virtudes[virtude[0]] < 5: # verifica a virtude na lista
            virtudes[virtude[0]] +=1 #adiciona +1 ponto a virtude

    forca_de_vontade = virtudes['coragem']

    return virtudes #retorna o dicionario de virtudes
    return forca_de_vontade #retorna a forca de vontade

virtudes = definir_virtudes() # chama a função para definir as virtudes


def definir_qed():
    global qed
    qed = {}
    pontos_extras = 15
    for i in range(5):
        caracteristica = random.choice(list(lista_qed.items()))
        if caracteristica not in qed.items():
            qed[caracteristica[0]] = caracteristica[1]

    pontos_extras += sum(qed.values())
    return qed

qed = definir_qed()

def definir_humanidade():
    global humanidade
    humanidade = virtudes['consiencia'] + virtudes['autocontrole']
    return humanidade


geracao = 13

def definir_geracao():
    global geracao
    geracao = 13
    if 'geracao' in antecedentes:
        geracao -= antecedentes['geracao']
    return geracao


def definir_pontos_de_sangue():
    global pontos_de_sangue
    d10 = list(range(1,11))
    pontos_de_sangue = random.choice(d10)
    if geracao != 13:
      diferenca = 13 - geracao
      pontos_de_sangue = f"{pontos_de_sangue}/{diferenca + 10}"
      return pontos_de_sangue
    else:
        pontos_de_sangue = f"{pontos_de_sangue}/{10}"
        return pontos_de_sangue

pontos_de_sangue = definir_pontos_de_sangue()

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
    
    global cla,pontos_preset_atributos  # Acessa variáveis globais
    # Cria uma lista com as categorias de atributos (físicos, sociais, mentais)
    categorias_disponiveis = list(atributos.keys())
    # Embaralha a ordem dos pontos a serem distribuídos ([7, 5, 3])
    #random.shuffle(pontos_atributos)
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
    return atributos

def pontos_gastos_habilidades():
    global pontos_extras, pontos_preset_habilidades  # Acessa variáveis globais
    pontos_preset_habilidades = sum(habilidades['talentos'].values()),sum(habilidades['pericias'].values()),sum(habilidades['conhecimento'].values())

def distribuir_pontos_habilidades():
    """
    Distribui pontos de habilidades aleatoriamente para um personagem,
    considerando limites e regras específicas.
    """
    global pontos_preset_habilidades, habilidades  # Acessa variáveis globais
    categorias_disponiveis = list(habilidades.keys())  # Cria uma lista com as categorias de habilidades
    random.shuffle(pontos_habilidades)  # Embaralha a ordem dos pontos a serem distribuídos
    pontos_habilidades_copia = pontos_habilidades.copy()

    for i in range(3):
        ponto = pontos_habilidades_copia[i]
        ponto -= pontos_preset_habilidades[i]
        if ponto <= 0:
            continue
        categoria_escolhida = categorias_disponiveis[i]
        
        while ponto > 0:
            habilidades_disponiveis = [
                habilidade for habilidade, valor in habilidades[categoria_escolhida].items()
                if valor < 5  # Limite de 5 pontos por habilidade
            ]
            if not habilidades_disponiveis:
                break  # Se não houver habilidades disponíveis para distribuir pontos, sai do loop
            habilidade_escolhida = random.choice(habilidades_disponiveis)
            habilidades[categoria_escolhida][habilidade_escolhida] += 1
            ponto -= 1

    # Remove habilidades com valor 0, mas mantém a referência global de 'habilidades'
    for tipo, hab_dict in habilidades.items():
        habilidades[tipo] = {hab: pont for hab, pont in hab_dict.items() if pont != 0}
    
    return habilidades  # Retorna a referência modificada (opcional)


def limpar_variaveis():
    global disciplinas, atributos, habilidades, antecedentes, virtudes
    global qed, humanidade, forca_de_vontade, geracao, pontos_de_sangue
    global nome, cla, pontos_extras, pontos_preset_atributos, pontos_preset_habilidades

    disciplinas = {}
    atributos = {
        'fisicos': {'forca': 1, 'destreza': 1, 'vigor': 1},
        'sociais': {'carisma': 1, 'manipulacao': 1, 'aparencia': 1},
        'mentais': {'percepcao': 1, 'inteligencia': 1, 'raciocinio': 1}
    }
    habilidades = {
        'talentos': {},
        'pericias': {},
        'conhecimento': {}
    }
    antecedentes = {}
    virtudes = {'consiencia': 1, 'autocontrole': 1, 'coragem': 1}
    qed = {}
    humanidade = None
    forca_de_vontade = None
    geracao = 13
    pontos_de_sangue = None
    nome = ""
    cla = ""
    pontos_extras = 15
    pontos_preset_atributos = (0, 0, 0)
    pontos_preset_habilidades = (0, 0, 0)


class Vampiro:
    def __init__(self, nome, geracao, cla, atributos, habilidades, vantagens, qualidades_defeitos,
                 trilha, forca_de_vontade, pontos_de_sangue, disciplinas, antecedentes, virtudes, humanidade):
        self.nome = nome
        self.geracao = geracao
        self.cla = cla
        self.atributos = atributos
        self.habilidades = habilidades
        self.vantagens = vantagens
        self.qualidades_defeitos = qualidades_defeitos
        self.trilha = trilha
        self.forca_de_vontade = forca_de_vontade
        self.pontos_de_sangue = pontos_de_sangue
        self.disciplinas = disciplinas
        self.antecedentes = antecedentes
        self.virtudes = virtudes
        self.qed = qualidades_defeitos
        self.humanidade = humanidade



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
        
        limpar_variaveis()

    @staticmethod
    def gerar(nome=None, cla=None):
        global disciplinas, atributos, habilidades, antecedentes, virtudes, qed
        global humanidade, forca_de_vontade, geracao, pontos_de_sangue

        if not nome:
            nome = "Indigente"
        if not cla or cla not in lista_cla:
            cla = random.choice(list(lista_cla.keys()))

        # Geração real dos dados
        definir_diciplinas()
        disciplinas_cla_e_definir_atributos_habilidades()

        definir_atributos()
        definir_habilidades()
        definir_antecedentes()
        definir_virtudes()
        definir_qed()

        definir_humanidade()
        definir_geracao()
        definir_pontos_de_sangue()

        calcular_pontos_gastos()
        distribuir_pontos_atributos()
        pontos_gastos_habilidades()
        distribuir_pontos_habilidades()

        # Retorna um objeto Vampiro com os dados globais gerados
        return Vampiro(
            nome=nome,
            geracao=geracao,
            cla=cla,
            atributos=atributos,
            habilidades=habilidades,
            vantagens=lista_vantagens,
            qualidades_defeitos=qed,
            trilha=None,
            forca_de_vontade=forca_de_vontade,
            pontos_de_sangue=pontos_de_sangue,
            disciplinas=disciplinas,
            antecedentes=antecedentes,
            virtudes=virtudes,
            humanidade=humanidade
        )




def main():
    titulo()  # Função que exibe o título do jogo ou do programa
    creditos()  # Função que exibe os créditos ou informações iniciais
    
    # Passos para escolher o nome e o clã do personagem
    escolher_nome()  
    escolher_cla()
    
    # Definir disciplinas e atributos/habilidades baseados no clã
    definir_diciplinas()
    disciplinas_cla_e_definir_atributos_habilidades()

    # Definir atributos, habilidades, vantagens e qualidades/defeitos
    atributos = definir_atributos()
    habilidades = definir_habilidades()
    definir_antecedentes()
    definir_virtudes()
    definir_qed()

    # Definir humanidade, força de vontade, pontos de sangue e geração
    definir_humanidade()
    definir_geracao()
    definir_pontos_de_sangue()

    # Cálculo e distribuição de pontos extras
    calcular_pontos_gastos()
    distribuir_pontos_atributos()
    pontos_gastos_habilidades()
    distribuir_pontos_habilidades()

    # Criar o objeto Vampiro
    vampiro = Vampiro(
    nome=nome,
    geracao=geracao,
    cla=cla,
    atributos=atributos,
    habilidades=habilidades,
    vantagens=lista_vantagens,
    qualidades_defeitos=qed,
    trilha=None,
    forca_de_vontade=forca_de_vontade,
    pontos_de_sangue=pontos_de_sangue,
    disciplinas=disciplinas,
    antecedentes=antecedentes,
    virtudes=virtudes,
    humanidade=humanidade
)

    
    # Limpar o terminal
    os.system('cls')  # ou 'clear' dependendo do sistema operacional
    titulo()  # Exibe o título novamente após limpar o terminal
    vampiro.ficha()  # Exibe a ficha do personagem criado
    
    # Espera para que o usuário possa ver a ficha
    '''time.sleep(3.5)'''  # Descomente se desejar esperar antes de prosseguir
    
    limpar_variaveis()  # Limpa as variáveis globais após mostrar a ficha
    
    recomecar()  # Pergunta ao usuário se deseja gerar outro personagem

def recomecar():
    """
    Pergunta ao usuário se ele deseja gerar um novo personagem.
    """
    print('Gerar novamente? ')
    resposta = input('Digite s para sim ou n para não: ').lower()
    
    if resposta == 's':
        os.system('cls')
        main()  # Chama o main novamente para gerar um novo personagem
    elif resposta == 'n':
        os.system('cls')
        print('''
        Obrigado por testar!
        ''')
        '''time.sleep(0.68)'''  # Descomente para adicionar uma pausa
    else:
        print('Opção inválida. Tente novamente.')
        recomecar()  # Chama a função novamente em caso de resposta inválida

if __name__ == "__main__":
    main()


# esse codigo esta com problema na geracao de cla e checagem de nosferatu,
# o que faz com que o programa não funcione corretamente