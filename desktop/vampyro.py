import random
#import os
from conteudos import *

class Vampiro:
    def __init__(self, nome=None, cla=None):
        self.nome = nome if nome else "Cainita"
        self.cla = cla if cla and cla in lista_cla else random.choice(list(lista_cla.keys()))
        self.atributos = {
            'Físicos': {'Força': 1, 'Destreza': 1, 'Vigor': 1},
            'Sociais': {'Carisma': 1, 'Manipulação': 1, 'Aparência': 1},
            'Mentais': {'Percepção': 1, 'Inteligência': 1, 'Raciocínio': 1}
        }

        self.habilidades = {
            'Talentos': {},
            'Perícias': {},
            'Conhecimentos': {}
        }
        self.disciplinas = {}
        self.antecedentes = {}
        self.virtudes = {'Consciência': 1, 'Autocontrole': 1, 'Coragem': 1}
        self.qed = {}
        self.humanidade = 0
        self.forca_de_vontade = 0
        self.geracao = 13
        self.pontos_de_sangue = 0
        self.pontos_extras = 0

        # Inicializa os atributos e habilidades
        self.definir_dados()

    def definir_dados(self):
        self.definir_disciplinas()
        self.definir_qed()
        self.calcular_pontos_gastos()
        self.definir_atributos()  # Chama o método corrigido
        self.definir_habilidades()  # Garante que as habilidades sejam geradas
        self.definir_antecedentes()
        self.definir_virtudes()
        self.definir_humanidade()
        self.definir_geracao()
        self.definir_pontos_de_sangue()

    def definir_disciplinas(self):
        if self.cla == "Caitif":
            while len(lista_cla['Caitif']) < 3:
                disciplina = random.choice(list(lista_disciplinas.keys()))
                lista_cla['Caitif'][disciplina] = 0
            self.disciplinas = lista_cla['Caitif'].copy()
            lista_cla['Caitif'].clear()
        else:
            self.disciplinas = lista_cla[self.cla].copy()

        for _ in range(3):
            disciplina = random.choice(list(self.disciplinas.items()))
            if disciplina in self.disciplinas.items():
                self.disciplinas[disciplina[0]] += 1

    def definir_atributos(self):
        """
        Distribui pontos nos atributos, ajustando para Nosferatu se necessário.
        """
        # Cria a pool ponderada de atributos
        todas_opcoes_atributos = {a for b in lista_atributos.values() for a in b}
        pool_atributos = criar_pool_ponderada(self.disciplinas, testes_disciplinas, todas_opcoes_atributos)

        # Define as categorias e limites
        categorias = list(self.atributos.keys())  # ['Físicos', 'Sociais', 'Mentais']
        limites = [7, 5, 3]

        # Distribui os pontos nos atributos
        self.distribuir_pontos(pool_atributos, categorias, limites, tipo="atributos")

        # Regra especial para Nosferatu: Aparência é fixada em 0
        if self.cla.lower() == 'nosferatu':
            pontos_aparencia = self.atributos['Sociais']['Aparência']
            self.atributos['Sociais']['Aparência'] = 0
            # Redistribuir os pontos de Aparência para outras características sociais
            while pontos_aparencia > 0:
                opcoes_disponiveis = [
                    a for a in self.atributos['Sociais'].keys()
                    if a != 'Aparência' and self.atributos['Sociais'][a] < 5
                ]
                if not opcoes_disponiveis:
                    break
                escolha = random.choice(opcoes_disponiveis)
                self.atributos['Sociais'][escolha] += 1
                pontos_aparencia -= 1

    def distribuir_pontos(self, pool, categorias, limites, tipo="atributos"):
        """
        Distribui pontos de forma controlada entre categorias, respeitando os limites.
        """
        # Define o dicionário correto com base no tipo
        destino = self.atributos if tipo == "atributos" else self.habilidades

        for categoria, limite in zip(categorias, limites):
            pontos = limite
            while pontos > 0:
                # Filtra as opções disponíveis na categoria
                opcoes_disponiveis = [
                    opcao for opcao in pool
                    if opcao in destino[categoria] and destino[categoria][opcao] < 5
                ]
                if not opcoes_disponiveis:
                    break  # Sai do loop se não houver opções disponíveis

                # Escolhe uma opção aleatória da pool
                escolha = random.choice(opcoes_disponiveis)
                destino[categoria][escolha] += 1
                pontos -= 1

    def definir_habilidades(self):
        """
        Inicializa e distribui pontos nas habilidades.
        """
        # Inicializa todas as habilidades com valor 0
        for categoria, habilidades in lista_habilidades.items():
            self.habilidades[categoria] = {habilidade: 0 for habilidade in habilidades}

        # Cria a pool ponderada de habilidades
        todas_opcoes_habilidades = {h for b in lista_habilidades.values() for h in b}
        pool_habilidades = criar_pool_ponderada(self.disciplinas, testes_disciplinas, todas_opcoes_habilidades)

        # Define as categorias e limites
        categorias = list(self.habilidades.keys())  # ['Talentos', 'Perícias', 'Conhecimentos']
        limites = [13, 9, 5]
        random.shuffle(limites)  # Embaralha os limites para cada categoria

        # Distribui os pontos nas habilidades
        self.distribuir_pontos(pool_habilidades, categorias, limites, tipo="habilidades")

    def definir_antecedentes(self):
        self.antecedentes = lista_vantagens["Antecedentes"].copy()
        for _ in range(5):
            antecedente = random.choice(list(self.antecedentes.items()))
            if antecedente in self.antecedentes.items():
                self.antecedentes[antecedente[0]] += 1

    def definir_virtudes(self):
        for _ in range(8):
            virtude = random.choice(list(self.virtudes.items()))
            if self.virtudes[virtude[0]] < 5:
                self.virtudes[virtude[0]] += 1
        self.forca_de_vontade = self.virtudes['Coragem']

    def definir_qed(self):
        """
        Define as Qualidades e Defeitos (QED) do personagem e ajusta os pontos extras.
        """
        self.qed.clear()  # Limpa quaisquer valores anteriores
        for _ in range(5):
            caracteristica = random.choice(list(lista_qed.items()))
            if caracteristica[0] not in self.qed:
                self.qed[caracteristica[0]] = caracteristica[1]

        # Ajusta os pontos extras com base nas características QED
        self.pontos_extras += sum(self.qed.values())

    def definir_humanidade(self):
        self.humanidade = self.virtudes['Consciência'] + self.virtudes['Autocontrole']

    def definir_geracao(self):
        if 'Geração' in self.antecedentes:
            self.geracao -= self.antecedentes['Geração']

    def definir_pontos_de_sangue(self):
        d10 = list(range(1, 11))
        self.pontos_de_sangue = random.choice(d10)
        if self.geracao != 13:
            diferenca = 13 - self.geracao
            self.pontos_de_sangue = f"{self.pontos_de_sangue}/{diferenca + 10}"
        else:
            self.pontos_de_sangue = f"{self.pontos_de_sangue}/10"

    def calcular_pontos_gastos(self):
        """
        Calcula os pontos extras gastos com base nos atributos e habilidades do personagem.
        """
        # Calcula os pontos já gastos em cada categoria de atributos
        self.pontos_gastos_atributos = (
            sum(self.atributos['Físicos'].values()) - 3,
            sum(self.atributos['Sociais'].values()) - 3,
            sum(self.atributos['Mentais'].values()) - 3
        )

        # Calcula os pontos já gastos em cada categoria de habilidades
        self.pontos_gastos_habilidades = (
            sum(self.habilidades['Talentos'].values()),
            sum(self.habilidades['Perícias'].values()),
            sum(self.habilidades['Conhecimentos'].values())
        )


    def exibir_ficha(self):
        print(f"Nome: {self.nome}")
        print(f"Clã: {self.cla}")
        print(f"Geração: {self.geracao}")

        print("\nAtributos:")
        for categoria, atributos in self.atributos.items():
            print(f"  {categoria.capitalize()}:")
            atributos_lista = list(atributos.items())
            for i in range(0, len(atributos_lista), 3):
                linha = atributos_lista[i:i+3]
                linha_formatada = " | ".join(f"{atributo.capitalize()}: {valor}" for atributo, valor in linha)
                print(f"    {linha_formatada}")

        print("\nHabilidades:")
        for categoria, habilidades in self.habilidades.items():
            habilidades_filtradas = {k: v for k, v in habilidades.items() if v > 0}
            if habilidades_filtradas:
                print(f"  {categoria.capitalize()}:")
                habilidades_lista = list(habilidades_filtradas.items())
                for i in range(0, len(habilidades_lista), 3):
                    linha = habilidades_lista[i:i+3]
                    linha_formatada = " | ".join(f"{habilidade.capitalize()}: {valor}" for habilidade, valor in linha)
                    print(f"    {linha_formatada}")

        print("\nAntecedentes:")
        antecedentes_filtrados = {k: v for k, v in self.antecedentes.items() if v > 0}
        if antecedentes_filtrados:
            antecedentes_lista = list(antecedentes_filtrados.items())
            for i in range(0, len(antecedentes_lista), 3):
                linha = antecedentes_lista[i:i+3]
                linha_formatada = " | ".join(f"{antecedente.capitalize()}: {valor}" for antecedente, valor in linha)
                print(f"    {linha_formatada}")

        print("\nVirtudes:")
        virtudes_lista = list(self.virtudes.items())
        for i in range(0, len(virtudes_lista), 3):
            linha = virtudes_lista[i:i+3]
            linha_formatada = " | ".join(f"{virtude.capitalize()}: {valor}" for virtude, valor in linha)
            print(f"    {linha_formatada}")

        print("\nQualidades e Defeitos:")
        qed_lista = list(self.qed.items())
        for i in range(0, len(qed_lista), 3):
            linha = qed_lista[i:i+3]
            linha_formatada = " | ".join(f"{qed.capitalize()}: {valor}" for qed, valor in linha)
            print(f"    {linha_formatada}")

        print(f"\nTrilha: {self.humanidade}")
        print(f"Força de Vontade: {self.forca_de_vontade}")
        print(f"Pontos de Sangue: {self.pontos_de_sangue}")

def criar_pool_ponderada(disciplinas_personagem, testes_disciplinas, opcoes):
    """
    Cria uma pool ponderada de atributos ou habilidades com base nas disciplinas do personagem.
    """
    pool = []

    for opcao in opcoes:
        peso = 1  # Peso padrão

        # Aumenta o peso se a opção estiver associada a uma disciplina do personagem
        for disciplina, nivel in disciplinas_personagem.items():
            if nivel > 0 and disciplina in testes_disciplinas:
                if opcao in testes_disciplinas[disciplina]:
                    peso += nivel  # Aumenta o peso proporcional ao nível da disciplina

        pool.extend([opcao] * peso)

    return pool

def exibir_creditos(entry_widget):
    entry_widget.delete("1.0", "end")  # Limpa o conteúdo do widget
    entry_widget.insert("1.0", creditos)  # Insere o texto corretamente

def exibir_habilidades(entry_3, vampiro):
    entry_3.insert("end", "\nHabilidades:\n")
    for categoria, habilidades in vampiro.habilidades.items():
        habilidades_filtradas = {k: v for k, v in habilidades.items() if v > 0}
        if habilidades_filtradas:
            entry_3.insert("end", f"\n{categoria.capitalize()}:\n")
            habilidades_lista = list(habilidades_filtradas.items())
            for i in range(0, len(habilidades_lista), 3):
                linha = habilidades_lista[i:i+3]
                linha_formatada = " | ".join(f"{habilidade.capitalize()}: {valor}" for habilidade, valor in linha)
                entry_3.insert("end", f"{linha_formatada}\n")

'''def main():
    os.system('cls')
    print("Bem-vindo ao Gerador de Fichas de Vampiro!")
    nome = input("Digite o nome do personagem (ou deixe em branco para 'Indigente'): ").title()
    cla = input("Digite o clã do personagem (ou deixe em branco para aleatório): ").title()

    vampiro = Vampiro(nome, cla)
    os.system('cls')
    vampiro.exibir_ficha()

    if input("\nGerar novamente? (s/n): ").lower() == 's':
        main()
    else:
        print("Obrigado por usar o gerador!")

if __name__ == "__main__":
    main()
'''

