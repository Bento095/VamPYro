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
            'Físicos': {'Força': 1, 'Destreza': 1, 'Vigor': 1},
            'Sociais': {'Carisma': 1, 'Manipulação': 1, 'Aparência': 1},
            'Mentais': {'Percepção': 1, 'Inteligência': 1, 'Raciocínio': 1}
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
