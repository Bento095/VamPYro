lista_cla = clãs_disciplinas = {
    "Brujah": {"Rapidez": 0, "Potência": 0, "Presença": 0},
    "Gangrel": {"Animalismo": 0, "Metamorfose": 0, "Fortitude": 0},
    "Malkavian": {"Demência": 0, "Auspícios": 0, "Ofuscação": 0},
    "Nosferatu": {"Ofuscação": 0, "Potência": 0, "Animalismo": 0},
    "Toreador": {"Auspícios": 0, "Rapidez": 0, "Presença": 0},
    "Tremere": {"Auspícios": 0, "Dominação": 0, "Taumaturgia": 0},
    "Ventrue": {"Dominação": 0, "Fortitude": 0, "Presença": 0},
    "Tzimisce": {"Vicissitude": 0, "Animalismo": 0, "Auspícios": 0},
    "Lasombra": {"Tenebrosidade": 0, "Dominação": 0, "Potência": 0},
    "Giovanni": {"Necromancia": 0, "Dominação": 0, "Potência": 0},
    "Assamita": {"Quietus": 0, "Rapidez": 0, "Ofuscação": 0},
    "Setita": {"Serpentis": 0, "Ofuscação": 0, "Presença": 0},
    "Ravnos": {"Quimerismo": 0, "Animalismo": 0, "Fortitude": 0},
    "Caitif": {}
}


lista_disciplinas = {
    "Animalismo": 0, "Auspícios": 0, "Demência": 0, "Dominação": 0,
    "Fortitude": 0, "Metamorfose": 0, "Necromancia": 0, "Ofuscação": 0,
    "Potência": 0, "Presença": 0, "Quietus": 0, "Quimerismo": 0,
    "Rapidez": 0, "Serpentis": 0, "Taumaturgia": 0, "Tenebrosidade": 0, "Vicissitude": 0
}


global disciplinas_caitif
global disciplinas

lista_atributos = {
            'Físicos': {'Força': 1, 'Destreza': 1, 'Vigor': 1},
            'Sociais': {'Carisma': 1, 'Manipulação': 1, 'Aparência': 1},
            'Mentais': {'Percepção': 1, 'Inteligência': 1, 'Raciocínio': 1}
        }

lista_habilidades = {
    "Talentos": {
        'Prontidão': 0, 'Esportes': 0, 'Briga': 0, 'Esquiva': 0, 'Empatia': 0,
        'Expressão': 0, 'Intimidação': 0, 'Liderança': 0, 'Manha': 0, 'Lábia': 0
    },
    "Perícias": {
        'Animais': 0, 'Ofícios': 0, 'Condução': 0, 'Etiqueta': 0, 'Armas de Fogo': 0,
        'Armas Brancas': 0, 'Performance': 0, 'Segurança': 0, 'Furtividade': 0, 'Sobrevivência': 0
    },
    "Conhecimentos": {
        'Acadêmicos': 0, 'Computador': 0, 'Finanças': 0, 'Investigação': 0, 'Direito': 0,
        'Linguística': 0, 'Medicina': 0, 'Ocultismo': 0, 'Política': 0, 'Ciência': 0
    }
}


lista_vantagens = {
    'Antecedentes': {
        'Aliados': 0, 'Contatos': 0, 'Fama': 0, 'Geração': 0, 'Rebanho': 0,
        'Influência': 0, 'Mentor': 0, 'Recursos': 0, 'Lacaios': 0, 'Status': 0
    },
    'Virtudes': {
        'Consciência': 1, 'Autocontrole': 1, 'Coragem': 1
    }
}


lista_qed = {
    'sentidos aguçados': -1, 'ambidestro': -1, 'ingerir comida': -1, 'equilíbrio perfeito': -1, 'rubor de saúde': -2, 'voz encantadora': -2,
    'temerário': -3, 'digestão eficiente': -3, 'cheiro de túmulo': 1, 'deficiência auditiva': 1,
    'mordida infecciosa': 2, 'deficiência visual': 1, 'caolho': 2, 'desfigurado': 2, 'deformidade': 3,
    'ferimento permanente': 3, 'cura demorada': 3, 'vício': 3, 'sangue fraco': 4, 'portador de doença contagiosa': 4,
    'pele cadavérica': 5, 'bom senso': -1, 'concentração': -1, 'noção exata do tempo': -1, 'código de honra': -2,
    'memória eidética': -2, 'sono leve': -2, 'linguista nato': -2, 'temperamento calmo': -3, 'vontade de ferro': -3, 'sono pesado': 1,
    'pesadelos': 1, 'fobia': 2, 'exclusão de presa': 1, 'timidez': 1, 'coração mole': 1, 'dificuldade de fala': 1, 'bairrismo': 2, 'cabeça quente': 2,
    'vingança': 2, 'amnésia': 1, 'lunático': 2, 'vontade fraca': 3, 'consumo conspícuo': 4, 'senhor de prestígio': -1, 'líder nato': -1,
    'dívida de gratidão': 1, 'senhor indigno': 1, 'segredo sombrio': 1, 'identidade trocada': 1, 'ressentimento do senhor': 1, 'inimigo': 1, 'caçado': 4,
    'membro de seita sob investigação': 4, 'médium': -2, 'resistência à magia': -2, 'habilidade oracular': -3, 'mentor espiritual': -3,
    'imunidade ao laço de sangue': -3, 'sorte': -3, 'amor verdadeiro': -4, 'nove vidas': -6, 'fé verdadeira': -7, 'toque de congelamento': 1,
    'repulsa ao alho': 1, 'amaldiçoado': 1, 'imagem sem reflexo': 1, 'presença sinistra': 2, 'repulsa a cruzes': 3, 'incapacidade de cruzar água corrente': 3,
    'assombrado': 3, 'aperto dos amaldiçoados': 4, 'futuro negro': 5, 'sensibilidade à luz': 5
}
 # Qualidades e Defeitos
# alguns foram removidos para nao impactar a limitação de narrativa, demais com multipla escolha em seu custo estao utilizando o menor, em caso de conflito, fica a escolha do mestre

removidos = {
    'corpo grande': -4, 'estatura baixa': 1, 'criança': 3, 'aleijado': 3, 'monstruoso': 3, 'mudo': 4,
    'surdez': 4, '14ª geração': 2, 'cegueira': 6
}


testes_disciplinas = {
    'Animalismo': {'Manipulação', 'Carisma', 'Animais', 'Sobrevivência', 'Intimidação'},  # Autocontrole
    'Auspícios': {'Percepção', 'Empatia', 'Inteligência', 'Lábia', 'Ocultismo'},  # Força de Vontade
    'Demência': {'Carisma', 'Empatia', 'Manipulação', 'Lábia', 'Percepção', 'Ocultismo', 'Intimidação'},  # Pontos de Sangue
    'Dominação': {'Manipulação', 'Intimidação', 'Liderança', 'Raciocínio', 'Lábia', 'Carisma'},  # Força de Vontade
    'Fortitude': {'Vigor'},
    'Metamorfose': {'Força'},
    'Necromancia': {'Percepção', 'Ocultismo', 'Manipulação', 'Vigor', 'Empatia', 'Destreza', 'Raciocínio', 'Prontidão', 'Inteligência'},  # Força de Vontade
    'Ofuscação': {'Raciocínio', 'Furtividade', 'Manipulação', 'Performance', 'Carisma'},
    'Potência': {'Força', 'Destreza', 'Esportes', 'Briga'},
    'Presença': {'Carisma', 'Performance', 'Intimidação', 'Aparência', 'Empatia', 'Lábia'},  # Força de Vontade
    'Quietus': {'Vigor', 'Esportes', 'Força'},  # Pontos de Sangue
    'Quimerismo': {'Manipulação', 'Lábia'},  # Força de Vontade
    'Rapidez': {'Destreza', 'Esportes'},
    'Serpentis': {'Força', 'Vigor'},
    'Taumaturgia': {'Ofícios', 'Ciência', 'Vigor', 'Esportes', 'Raciocínio', 'Sobrevivência'},
    'Tenebrosidade': {'Furtividade', 'Manipulação', 'Ocultismo', 'Vigor'},
    'Vicissitude': {'Inteligência', 'Medicina', 'Percepção', 'Destreza', 'Força', 'Vigor'}  # Moldar Carne ~ Medicina
}


pontos_extras = 15

atributos_teste = []
habilidades_teste = []

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

forca_de_vontade = 0

creditos = (
    "VamPYro - Criador de  Fichas de Vampiro: A Máscara V3 \n\n"
    "Feito por: \n"
    "Bento - GitHub: https://github.com/Bento095,\n" 
    "LinkedIn: www.linkedin.com/in/bruno-bento-a58a33321.\n "
    "\n\n" 
    " Obrigado pelo apoio e feedbacks da Coterie da Mariola:\n" 
    "Andirá, Don, Edgar, Dornelas, Sebastião, Gabriel, Jaha e Túlio.\n\n"
    " Este projeto é uma criação de fã, desenvolvido com fins\n"
    "educacionais e sem fins lucrativos.\n"
    " Não sou o detentor dos direitos sobre o sistema\n"
    "'Vampiro: A Máscara', cujos direitos pertencem aos seus\n"
    "respectivos criadores e detentores legais.\n"
    " Este programa é gratuito e feito apenas como uma homenagem e \n"
    "ferramenta de estudo."
)
