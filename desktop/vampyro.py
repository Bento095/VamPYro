import random
#import os
from conteudos import *

class Vampiro:
    def __init__(self, nome=None, cla=None):
        self.nome = nome if nome else "Indigente"
        self.cla = cla if cla and cla in lista_cla else random.choice(list(lista_cla.keys()))
        self.atributos = {
            'Físicos': {'Força': 1, 'Destreza': 1, 'Vigor': 1},
            'Sociais': {'Carisma': 1, 'Manipulação': 1, 'Aparência': 1},
            'Mentais': {'Percepção': 1, 'Inteligência': 1, 'Raciocínio': 1}
        }

        self.habilidades = {
            'talentos': {},
            'pericias': {},
            'conhecimento': {}
        }
        self.disciplinas = {}
        self.antecedentes = {}
        self.virtudes = {'consiencia': 1, 'autocontrole': 1, 'coragem': 1}
        self.qed = {}
        self.humanidade = 0
        self.forca_de_vontade = 0
        self.geracao = 13
        self.pontos_de_sangue = 0

        # Inicializa os atributos e habilidades
        self.definir_dados()

    def definir_dados(self):
        self.definir_disciplinas()
        self.definir_atributos()
        self.definir_habilidades()
        self.definir_antecedentes()
        self.definir_virtudes()
        self.definir_qed()
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
        if self.cla.lower() == 'nosferatu':
            # Aparência é fixada em 0
            self.atributos['Sociais']['Aparência'] = 0

        # Distribuir pontos nos atributos
        pontos_atributos = [7, 5, 3]
        for categoria, pontos in zip(self.atributos.keys(), pontos_atributos):
            while pontos > 0:
                atributo = random.choice(list(self.atributos[categoria].keys()))
                # Impede que pontos sejam alocados em "aparencia" para Nosferatu
                if self.cla.lower() == 'nosferatu' and categoria == 'Sociais' and atributo == 'Aparência':
                    continue
                if self.atributos[categoria][atributo] < 5:
                    self.atributos[categoria][atributo] += 1
                    pontos -= 1

    def definir_habilidades(self):
        pontos_habilidades = [13, 9, 5]
        for categoria, pontos in zip(self.habilidades.keys(), pontos_habilidades):
            while pontos > 0:
                habilidade = random.choice(list(lista_habilidades[categoria]))
                if habilidade not in self.habilidades[categoria]:
                    self.habilidades[categoria][habilidade] = 0
                if self.habilidades[categoria][habilidade] < 5:
                    self.habilidades[categoria][habilidade] += 1
                    pontos -= 1

    def definir_antecedentes(self):
        self.antecedentes = lista_vantagens["antecedentes"].copy()
        for _ in range(5):
            antecedente = random.choice(list(self.antecedentes.items()))
            if antecedente in self.antecedentes.items():
                self.antecedentes[antecedente[0]] += 1

    def definir_virtudes(self):
        for _ in range(8):
            virtude = random.choice(list(self.virtudes.items()))
            if self.virtudes[virtude[0]] < 5:
                self.virtudes[virtude[0]] += 1
        self.forca_de_vontade = self.virtudes['coragem']

    def definir_qed(self):
        self.qed = {}
        pontos_extras = 15
        for _ in range(5):
            caracteristica = random.choice(list(lista_qed.items()))
            if caracteristica[0] not in self.qed:
                self.qed[caracteristica[0]] = caracteristica[1]
        pontos_extras += sum(self.qed.values())

    def definir_humanidade(self):
        self.humanidade = self.virtudes['consiencia'] + self.virtudes['autocontrole']

    def definir_geracao(self):
        if 'geracao' in self.antecedentes:
            self.geracao -= self.antecedentes['geracao']

    def definir_pontos_de_sangue(self):
        d10 = list(range(1, 11))
        self.pontos_de_sangue = random.choice(d10)
        if self.geracao != 13:
            diferenca = 13 - self.geracao
            self.pontos_de_sangue = f"{self.pontos_de_sangue}/{diferenca + 10}"
        else:
            self.pontos_de_sangue = f"{self.pontos_de_sangue}/10"

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

        print(f"\nHumanidade: {self.humanidade}")
        print(f"Força de Vontade: {self.forca_de_vontade}")
        print(f"Pontos de Sangue: {self.pontos_de_sangue}")

def exibir_creditos(entry_widget):
    entry_widget.delete("1.0", "end")  # Limpa o conteúdo do widget
    entry_widget.insert("1.0", creditos)  # Insere o texto corretamente


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

