from flask import Flask, render_template

app = Flask(__name__)

# Configuração das Raridades
DATA_RAW = {
    'Lendario': ['Sabugueiro', 'Pau-brasil'],
    'Epico': ['Teixo', 'Cipreste', 'Cerejeira', 'Ébano'],
    'Raro': ['Acácia', 'Figueira', 'Nogueira', 'Nogueira-preta', 'Romeira', 'Espinheiro-negro', 'Espinheiro-alvo'],
    'Incomum': ['Abeto-vermelho', 'Espinheiro', 'Freixo', 'Jacarandá', 'Lariço', 'Videira', 'Lima-prata', 'Limoeiro', 'Azevinho'],
    'Comum': ['Abeto', 'Álamo', 'Amieiro', 'Aveleira', 'Bordo', 'Carvalho', 'Carvalho-vermelho', 'Castanheiro', 'Cedro', 'Corniso', 'Faia', 'Haya', 'Loureiro', 'Macieira', 'Mogno', 'Olmo', 'Pereira', 'Pinheiro', 'Plátano', 'Salgueiro', 'Sicômoro', 'Sorveira', 'Tília', 'Ulmeiro', 'Vidoeiro', 'Zimbro']
}

# Configuração de Afinidades
AFFINITY_DATA = {
    'combat': {'label': 'Combate', 'icon': '⚔️', 'woods': ['Abeto', 'Álamo', 'Carvalho', 'Carvalho-vermelho', 'Corniso', 'Teixo', 'Freixo']},
    'defense': {'label': 'Defesa', 'icon': '🛡️', 'woods': ['Amieiro', 'Aveleira', 'Azevinho', 'Salgueiro', 'Sorveira', 'Pereira', 'Zimbro', 'Espinheiro-alvo']},
    'charms': {'label': 'Encantamentos', 'icon': '✨', 'woods': ['Bordo', 'Castanheiro', 'Cedro', 'Mogno', 'Plátano', 'Tília', 'Ulmeiro', 'Pinheiro', 'Sicômoro', 'Abeto-vermelho']},
    'complex': {'label': 'Magia Complexa', 'icon': '🔮', 'woods': ['Acácia', 'Ébano', 'Espinheiro', 'Espinheiro-negro', 'Espinheiro-alvo', 'Videira', 'Olmo', 'Nogueira', 'Nogueira-preta']},
    'healing': {'label': 'Cura', 'icon': '🌱', 'woods': ['Faia', 'Figueira', 'Haya', 'Limoeiro', 'Macieira', 'Vidoeiro', 'Loureiro']},
    'wisdom': {'label': 'Sabedoria', 'icon': '🧠', 'woods': ['Lima-prata', 'Jacarandá', 'Lariço', 'Cerejeira', 'Pau-brasil', 'Romeira', 'Videira', 'Cipreste']},
    'dark': {'label': 'Artes das Trevas', 'icon': '☠️', 'woods': ['Sabugueiro', 'Teixo', 'Espinheiro-negro']}
}

# Detalhes e Curiosidades (Lore Oficial + Adaptações)
WAND_DETAILS = {
    'Sabugueiro': {
        'desc': 'A mais rara de todas as madeiras e com fama de trazer azar. Contém magia poderosa, mas despreza donos que não sejam superiores. Difícil de dominar.',
        'skill': 'Magia extremamente poderosa, Artes das Trevas',
        'owner': 'Antioch Peverell, Albus Dumbledore, Harry Potter',
        'curiosity': 'Dizem que a Varinha das Varinhas nunca perde um duelo se seu mestre for verdadeiro.'
    },
    'Pau-brasil': {
        'desc': 'Madeira lendária da América do Sul, ardente e vibrante. Conhecida por sua "brasa" interna que responde a bruxos de espírito indomável.',
        'skill': 'Magia Elemental (Fogo), Transfiguração Avançada',
        'owner': 'Castelobruxo Grandmasters',
        'curiosity': 'Quase extinta na natureza mágica, varinhas dessa madeira são relíquias passadas de geração em geração.'
    },
    'Azevinho': {
        'desc': 'Rara e protetora, funciona melhor para quem precisa vencer a raiva e impetuosidade. Escolhe bruxos em jornadas perigosas.',
        'skill': 'Proteção contra o mal, Duelos defensivos',
        'owner': 'Harry Potter',
        'curiosity': 'Tradicionalmente considerada a antítese do Teixo. Símbolo de vida e proteção.'
    },
    'Teixo': {
        'desc': 'Varinhas de teixo são raras, associadas a duelos e maldições. Diz-se que conferem ao dono poder de vida e morte.',
        'skill': 'Artes das Trevas, Duelos letais',
        'owner': 'Tom Riddle (Lord Voldemort), Ginny Weasley',
        'curiosity': 'Costumam ser enterradas com seus donos. Se uma varinha de teixo for enterrada, dizem que ela brota em uma árvore para guardar o túmulo.'
    },
    'Carvalho': {
        'desc': 'Exige força, coragem e fidelidade. Parceira de bruxos com forte intuição e afinidade com a natureza.',
        'skill': 'Magia da Natureza, Feitiços de Defesa',
        'owner': 'Hagrid (provavelmente), Merlin',
        'curiosity': 'O Rei da Floresta do solstício de inverno ao de verão. Não deve ser colhida fora do tempo.'
    },
    'Videira': {
        'desc': 'Pertence a personalidades de profundidade oculta. Varinhas de videira parecem saber quando seu mestre ideal entra na sala.',
        'skill': 'Visão, Feitiços Complexos',
        'owner': 'Hermione Granger',
        'curiosity': 'Embora não seja tecnicamente uma "madeira" (é um caule), Ollivander a classifica como tal devido às suas propriedades únicas.'
    },
    'Cerejeira': {
        'desc': 'Muito apreciada em Mahoutokoro (Japão). Não é apenas decorativa: possui poder letal e exige autocontrole férreo.',
        'skill': 'Magia combativa, Charme e elegância',
        'owner': 'Neville Longbottom, Gilderoy Lockhart',
        'curiosity': 'Nosso preconceito ocidental muitas vezes subestima essa madeira por suas flores rosas, um erro fatal em duelo.'
    },
    'Freixo': {
        'desc': 'Teimosa e leal. Se dada ou herdada, perde poder. O dono ideal é firme em suas crenças e nunca grosseiro.',
        'skill': 'Feitiços focados, Transfiguração',
        'owner': 'Cedric Diggory, Ron Weasley (primeira varinha)',
        'curiosity': 'Existe um ditado antigo: "Freixo teimoso, castanheiro ranzinza..." que alerta sobre sua lealdade fixa.'
    },
    'Olmo': {
        'desc': 'Prefere donos com presença, dignidade e destreza mágica. Produz o menor número de acidentes e erros tolos.',
        'skill': 'Magias elegantes, Feitiços de Puro-Sangue (tradicionalmente)',
        'owner': 'Lucius Malfoy',
        'curiosity': 'Havia um boato de que apenas sangue-puros poderiam usar Olmo, o que Ollivander provou ser falso.'
    },
    'Espinheiro-negro': {
        'desc': 'Uma madeira de guerreiro. Surpreendentemente adequada tanto para Aurores quanto para Comensais da Morte. Precisa passar por perigo para se unir ao dono.',
        'skill': 'Maldições, Magia de Combate',
        'owner': 'Sir Cadogan',
        'curiosity': 'Seu arbusto tem espinhos cruéis e frutos amargos, refletindo a natureza dura de sua magia.'
    },
     'Salgueiro': {
        'desc': 'Incomum e com poder de cura. O salgueiro busca donos com inseguranças ocultas, mas grande potencial. Dizem que quem tem muito a viajar vai mais rápido com Salgueiro.',
        'skill': 'Cura, Feitiços não-verbais',
        'owner': 'Ron Weasley (segunda varinha), Lily Potter',
        'curiosity': 'Ideal para feitiços não-verbais, o que atrai bruxos avançados.'
    },
    'Nogueira': {
        'desc': 'Para bruxos de inteligência superior. Versátil e adaptável, mas se o dono perder a confiança, ela perde o poder. Uma arma letal nas mãos de quem não tem conflitos internos.',
        'skill': 'Versatilidade total, Invencionice mágica',
        'owner': 'Bellatrix Lestrange',
        'curiosity': 'Diferente de outras, uma vez subjugada, ela fará qualquer coisa que o dono pedir, por mais vil que seja.'
    },
     'Acácia': {
        'desc': 'Muito incomum. Recusa-se a fazer magia para qualquer um que não seja seu dono. Não serve para "feitiços de exibição".',
        'skill': 'Magia sutil e poderosa',
        'owner': 'Membros selecionados da nobreza bruxa',
        'curiosity': 'Ollivander parou de estocá-las pois é difícil encontrar o dono certo, mas quando encontra, é formidável.'
    },
    'Cipreste': {
        'desc': 'Associada à nobreza. Dizem que o dono de uma varinha dessas terá uma morte heróica. Almas bravas e auto-sacrificantes.',
        'skill': 'Magia de proteção, Feitiços de coragem',
        'owner': 'Remus Lupin (em algumas versões)',
        'curiosity': 'Grandes heróis da história bruxa e mártires frequentemente portavam cipreste.'
    },
    'Ébano': {
        'desc': 'Preto azeviche, impressionante. Para aqueles que têm a coragem de ser eles mesmos. Combina com donos não-conformistas.',
        'skill': 'Combate e Transfiguração',
        'owner': 'Membros da Ordem da Fênix e Comensais',
        'curiosity': 'Não perde poder com o tempo, pelo contrário, enrijece em sua lealdade.'
    }
}

# Fallback para madeiras sem lore específica ainda, para não quebrar o modal
GENERIC_DESC = "Uma madeira nobre e cheia de personalidade. Reage bem a bruxos que demonstram respeito por sua origem."

def get_rarity_info(wood_name):
    if wood_name in DATA_RAW['Lendario']: return {'slug': 'legendary', 'label': 'L', 'name_pt': 'Lendário', 'rank': 5}
    if wood_name in DATA_RAW['Epico']: return {'slug': 'epic', 'label': 'E', 'name_pt': 'Épico', 'rank': 4}
    if wood_name in DATA_RAW['Raro']: return {'slug': 'rare', 'label': 'R', 'name_pt': 'Raro', 'rank': 3}
    if wood_name in DATA_RAW['Incomum']: return {'slug': 'uncommon', 'label': 'I', 'name_pt': 'Incomum', 'rank': 2}
    return {'slug': 'common', 'label': 'C', 'name_pt': 'Comum', 'rank': 1}

def get_affinity_info(wood_name):
    affinities = []
    found = False
    for slug, data in AFFINITY_DATA.items():
        if wood_name in data['woods']:
            affinities.append({'slug': slug, 'icon': data['icon'], 'label': data['label']})
            found = True
    if not found:
        return [{'slug': 'charms', 'icon': '✨', 'label': 'Encantamentos (Versátil)'}]
    return affinities

WAND_WOODS = []
all_woods_names = set()
for category in DATA_RAW.values():
    all_woods_names.update(category)

for name in sorted(list(all_woods_names)):
    info = get_rarity_info(name)
    aff_info = get_affinity_info(name)
    details = WAND_DETAILS.get(name, {
        'desc': GENERIC_DESC,
        'skill': 'Magia Geral',
        'owner': 'Desconhecido',
        'curiosity': 'Ainda há muito a ser descoberto sobre esta madeira.'
    })
    
    aff_slugs = " ".join([a['slug'] for a in aff_info])
    aff_icons = " ".join([a['icon'] for a in aff_info])
    
    WAND_WOODS.append({
        'name': name,
        'rarity': info['slug'],
        'badge': info['label'],
        'rarity_name': info['name_pt'],
        'rank': info['rank'],
        'affinities_slugs': aff_slugs,
        'affinities_icons': aff_icons,
        'affinities_list': aff_info,
        'details': details 
    })

# Dados de Núcleos de Varinha
WAND_CORES = [
    # Supremos (Ollivander)
    {
        'name': 'Pena de Fênix',
        'type': 'Supremo',
        'rarity': 'supreme',
        'badge': 'S', 
        'rank': 6,
        'icon': '🔥',
        'desc': 'O tipo de núcleo mais raro. Penas de fênix são capazes da maior variedade de magias, embora possam demorar mais do que as outras para revelar isso. Elas mostram mais iniciativa e são exigentes.',
        'skill': 'Maior gama mágica, Iniciativa própria',
        'owner': 'Harry Potter, Lord Voldemort, Silvano Kettleburn',
        'curiosity': 'É o núcleo mais difícil de dominar e escolher seu dono. Sua lealdade é duramente conquistada.'
    },
    {
        'name': 'Fibra de Coração de Dragão',
        'type': 'Supremo',
        'rarity': 'supreme',
        'badge': 'S',
        'rank': 6,
        'icon': '🐉',
        'desc': 'Fibras de coração de dragão produzem as varinhas mais poderosas. Elas aprendem mais rápido que outros tipos. Podem mudar de lealdade se tomadas de seu mestre original.',
        'skill': 'Poder bruto, Feitiços extravagantes',
        'owner': 'Hermione Granger, Bellatrix Lestrange, Viktor Krum, McGonagall',
        'curiosity': 'É o núcleo mais fácil de se voltar para as Artes das Trevas, embora não se incline a isso por natureza.'
    },
    {
        'name': 'Pelo de Unicórnio',
        'type': 'Supremo',
        'rarity': 'supreme',
        'badge': 'S',
        'rank': 6,
        'icon': '🦄',
        'desc': 'Produz a magia mais consistente e é o menos sujeito a flutuações. Varinhas com este núcleo são as mais fiéis e difíceis de corromper.',
        'skill': 'Magia consistente, Lealdade extrema',
        'owner': 'Ron Weasley, Neville Longbottom, Draco Malfoy',
        'curiosity': 'Não produz as varinhas mais poderosas (embora a madeira possa compensar) e podem "morrer" se maltratadas.'
    },
    
    # Lendários e Únicos
    {
        'name': 'Pelo de Testrálio',
        'type': 'Lendário',
        'rarity': 'legendary',
        'badge': 'L',
        'rank': 5,
        'icon': '💀',
        'desc': 'Uma substância instável e complicada, que só pode ser dominada por um bruxo capaz de encarar a morte.',
        'skill': 'Poder Supremo, Morte',
        'owner': 'A Varinha das Varinhas (Dumbledore, Harry)',
        'curiosity': 'O núcleo da varinha mais poderosa já criada (A Varinha das Varinhas).'
    },
    {
        'name': 'Chifre de Basilisco',
        'type': 'Lendário',
        'rarity': 'legendary',
        'badge': 'L',
        'rank': 5,
        'icon': '🐍',
        'desc': 'Um núcleo único e perigoso, impregnado com a magia de uma das criaturas mais letais do mundo mágico.',
        'skill': 'Ofidioglossia, Artes das Trevas',
        'owner': 'Salazar Slytherin',
        'curiosity': 'Varinhas com este núcleo podem ser "adormecidas" ou "despertadas" por comandos em Ofidioglossia.'
    },

    # Escola de Ilvermorny (América do Norte)
    {
        'name': 'Serpente Chifruda',
        'type': 'Épico',
        'rarity': 'epic', 
        'badge': 'E', 
        'rank': 4,
        'icon': '💎',
        'desc': 'Núcleo considerado o mais poderoso da América do Norte. Sensível ao perigo, emite um som grave de alerta.',
        'skill': 'Magia Cerebral, Alerta de Perigo',
        'owner': 'Isolt Sayre e muitos estudantes da Casa Serpente Chifruda',
        'curiosity': 'Excepcionalmente leal aos bruxos estudiosos e inteligentes.'
    },
    {
        'name': 'Pelo de Gato Wampus',
        'type': 'Épico',
        'rarity': 'epic',
        'badge': 'E',
        'rank': 4,
        'icon': '😼',
        'desc': 'Núcleo favorito dos guerreiros Cherokee. Produz varinhas de grande força, difíceis de controlar e manejar.',
        'skill': 'Magia de Combate, Força',
        'owner': 'Guerreiros Wampus',
        'curiosity': 'Dizem que apenas bruxos de grande coragem conseguem domar uma varinha de Wampus.'
    },
    {
        'name': 'Pena de Pássaro-Trovão',
        'type': 'Épico',
        'rarity': 'epic',
        'badge': 'E',
        'rank': 4,
        'icon': '🌩️',
        'desc': 'Poderoso, mas difícil de dominar. Varinhas com este núcleo são supremas em Transfiguração e podem sentir perigo sobrenatural.',
        'skill': 'Transfiguração, Magia Elemental',
        'owner': 'Shikoba Wolfe',
        'curiosity': 'Muitas vezes dispara maldições preventivamente quando sente perigo, agindo por conta própria.'
    },
    {
        'name': 'Fibra de Snallygaster',
        'type': 'Raro',
        'rarity': 'rare',
        'badge': 'R',
        'rank': 3,
        'icon': '🦎',
        'desc': 'Extraído de uma criatura dragão-pássaro nativa dos EUA. Um núcleo sólido, usado pelos primeiros fundadores.',
        'skill': 'Magia Robusta',
        'owner': 'Isolt Sayre, James Steward',
        'curiosity': 'Menos famoso que a Serpente Chifruda, mas extremamente confiável.'
    },
    {
        'name': 'Pelo de Rougarou',
        'type': 'Épico',
        'rarity': 'epic',
        'badge': 'E',
        'rank': 4,
        'icon': '🐺',
        'desc': 'Núcleo perigoso associado à magia negra na Louisiana. Atraído por bruxos que flertam com o mal.',
        'skill': 'Artes das Trevas, Sedução',
        'owner': 'Violetta Beauvais (Varinheira)',
        'curiosity': 'Dizem que varinhas de Rougarou são "vampíricas" por natureza, atraídas por sangue.'
    },

    # Exóticos e Raros
    {
        'name': 'Cabelo de Veela',
        'type': 'Épico',
        'rarity': 'epic',
        'badge': 'E',
        'rank': 4,
        'icon': '💃',
        'desc': 'Núcleo de natureza muito temperamental e volátil. Ollivander evita usá-lo pois considera as varinhas muito sensíveis.',
        'skill': 'Charme, Temperamento forte',
        'owner': 'Fleur Delacour',
        'curiosity': 'A avó de Fleur era uma Veela e doou o fio de cabelo. Funciona magnificamente para seu dono, falha para outros.'
    },
    {
        'name': 'Espinha de Monstro do Rio',
        'type': 'Raro',
        'rarity': 'rare',
        'badge': 'R',
        'rank': 3,
        'icon': '🐟',
        'desc': 'Extraído do Monstro do Rio White pelo varinheiro Thiago Quintana. Produzia varinhas longas e elegantes, de grande poder.',
        'skill': 'Feitiços de Força e Elegância',
        'owner': 'Thiago Quintana',
        'curiosity': 'O segredo de como extrair a espinha morreu com Quintana, tornando essas varinhas extintas.'
    },
    {
        'name': 'Coral',
        'type': 'Raro',
        'rarity': 'rare',
        'badge': 'R',
        'rank': 3,
        'icon': '🪸',
        'desc': 'Material marinho usado pelo famoso varinheiro Gregorovitch. Combina com bruxos ligados à água e adaptabilidade.',
        'skill': 'Magia Elemental (Água)',
        'owner': 'Gregorovitch',
        'curiosity': 'Reage mal em ambientes muito secos ou longe do mar.'
    },
    {
        'name': 'Bigode de Trasgo',
        'type': 'Comum',
        'rarity': 'common',
        'badge': 'C',
        'rank': 1,
        'icon': '🧟',
        'desc': 'Considerado um material inferior e de pouca sutileza. Produz magia bruta, barulhenta e pouco confiável.',
        'skill': 'Força bruta',
        'owner': 'Sir Cadogan',
        'curiosity': 'Diz a lenda que a varinha de Sir Cadogan explodiu.'
    },
    {
        'name': 'Chifre de Jackalope',
        'type': 'Incomum',
        'rarity': 'uncommon',
        'badge': 'I',
        'rank': 2,
        'icon': '🐰',
        'desc': 'Núcleo usado por varinheiros americanos. Jackalopes são coelhos com chifres, criaturas ágeis.',
        'skill': 'Feitiços rápidos',
        'owner': 'Desconhecido',
        'curiosity': 'Não produz muita força bruta, mas é excelente para feitiços de velocidade.'
    }
]

# Lista de Bruxos para Filtro (Dropdown)
WIZARD_LIST = [
    'Harry Potter', 'Tom Riddle (Lord Voldemort)', 'Albus Dumbledore', 
    'Hermione Granger', 'Ron Weasley', 'Neville Longbottom', 'Draco Malfoy (Esp)',
    'Bellatrix Lestrange', 'Rubeus Hagrid', 'Cedric Diggory', 
    'Minerva McGonagall', 'Remus Lupin', 'Gilderoy Lockhart', 
    'Lucius Malfoy', 'Garrick Ollivander', 'Antioch Peverell'
]

# Dados do Mundo Mágico (Casas de Hogwarts por enquanto)
WORLD_DATA = [
    {
        'name': 'Grifinória',
        'id': 'gryffindor',
        'colors': ['#740001', '#AE0001', '#D3A625', '#EEBA30'],
        'traits': ['Coragem', 'Bravura', 'Determinação'],
        'symbol': '🦁',
        'founder': 'Godric Gryffindor',
        'ghost': 'Nick Quase Sem Cabeça',
        'desc': 'A casa dos corajosos e ousados. Seus membros são conhecidos por sua bravura e cavalheirismo. A Grifinória valoriza a coragem acima de tudo.',
        'common_room': 'Torre da Grifinória',
        'element': 'Fogo'
    },
    {
        'name': 'Sonserina',
        'id': 'slytherin',
        'colors': ['#1A472A', '#2A623D', '#AAAAAA', '#5D5D5D'],
        'traits': ['Ambição', 'Astúcia', 'Liderança'],
        'symbol': '🐍',
        'founder': 'Salazar Slytherin',
        'ghost': 'Barão Sangrento',
        'desc': 'O lar dos astutos e ambiciosos. Sonserinos farão o que for preciso para atingir seus objetivos. Valorizam a grandeza e a pureza de sangue (tradicionalmente).',
        'common_room': 'Masmorras',
        'element': 'Água'
    },
    {
        'name': 'Corvinal',
        'id': 'ravenclaw',
        'colors': ['#0E1A40', '#222F5B', '#946B2D', '#BEB9B9'], # Bronze nos livros, prata nos filmes - usando mix
        'traits': ['Inteligência', 'Sabedoria', 'Criatividade'],
        'symbol': '🦅',
        'founder': 'Rowena Ravenclaw',
        'ghost': 'Dama Cinzenta',
        'desc': 'Para aqueles de mente afiada e espírito sábio. A Corvinal preza o aprendizado, a sagacidade e o intelecto.',
        'common_room': 'Torre da Corvinal',
        'element': 'Ar'
    },
    {
        'name': 'Lufa-Lufa',
        'id': 'hufflepuff',
        'colors': ['#ECB939', '#F0C75E', '#372E29', '#726255'],
        'traits': ['Lealdade', 'Paciência', 'Trabalho Duro'],
        'symbol': '🦡',
        'founder': 'Helga Hufflepuff',
        'ghost': 'Frei Gorducho',
        'desc': 'Onde se encontram os leais e justos. Lufanos são verdadeiros e não temem a dor do trabalho árduo. É a casa mais inclusiva.',
        'common_room': 'Porão (perto da cozinha)',
        'element': 'Terra'
    }
]

@app.route('/')
def home():
    # Landing Page Mágica
    return render_template('world.html')

@app.route('/varinhas')
def wands_hub():
    # Redireciona para o início da jornada das varinhas (Madeiras)
    return wands_woods()

@app.route('/varinhas/origem')
def wands_origin():
    return render_template('origin.html', active_tab='origin')

@app.route('/varinhas/madeiras')
def wands_woods():
    return render_template('wands.html', woods=WAND_WOODS, active_tab='woods', wizards=sorted(WIZARD_LIST))

@app.route('/varinhas/nucleos')
def wands_cores():
    return render_template('wands.html', woods=WAND_CORES, active_tab='cores', wizards=sorted(WIZARD_LIST))

# --- DADOS DE CRIATURAS ---
CREATURES_DATA = [
    # --- FERAS (Beasts) ---
    {
        'name': 'Dragão',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXXX',
        'danger_level': 5,
        'icon': '🐉',
        'desc': 'A mais perigosa das criaturas. Dividida em várias raças, todas são mortíferas e impossíveis de domesticar.',
        'origin': 'Global'
    },
    {
        'name': 'Acromântula',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXXX',
        'danger_level': 5,
        'icon': '🕷️',
        'desc': 'Aranha monstruosa de oito olhos capaz de fala humana. Venenosa e altamente agressiva.',
        'origin': 'Bornéu / Floresta Proibida'
    },
    {
        'name': 'Basilisco',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXXX',
        'danger_level': 5,
        'icon': '🐍',
        'desc': 'O Rei das Serpentes. Seu olhar mata instantaneamente e seu veneno corrói quase qualquer substância.',
        'origin': 'Europa (Grécia)'
    },
    {
        'name': 'Mantícora',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXXX',
        'danger_level': 5,
        'icon': '🦁',
        'desc': 'Cabeça humana, corpo de leão e cauda de escorpião. Sua pele repele quase todos os feitiços.',
        'origin': 'Grécia / Ásia'
    },
    {
        'name': 'Quimera',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXXX',
        'danger_level': 5,
        'icon': '🐐',
        'desc': 'Incrivelmente rara e feroz. Possui cabeça de leão, corpo de bode e cauda de dragão.',
        'origin': 'Grécia'
    },
    {
        'name': 'Nundu',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXXX',
        'danger_level': 5,
        'icon': '🐆',
        'desc': 'Talvez a mais perigosa do mundo. Seu hálito tóxico é capaz de dizimar vilas inteiras.',
        'origin': 'África Oriental'
    },
    {
        'name': 'Trolls',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXX',
        'danger_level': 4,
        'icon': '👹',
        'desc': 'Humanoides imensos de força colossal e inteligência mínima. Comem carne humana.',
        'origin': 'Escandinávia'
    },
    {
        'name': 'Grifos',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXX',
        'danger_level': 4,
        'icon': '🦅',
        'desc': 'Metade leão, metade águia. São guardiões ferozes de tesouros e locais secretos.',
        'origin': 'Grécia'
    },
    {
        'name': 'Thestrais',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXX',
        'danger_level': 4,
        'icon': '💀',
        'desc': 'Cavalos alados esqueléticos visíveis apenas por quem já testemunhou a morte de perto.',
        'origin': 'Ilhas Britânicas'
    },
    {
        'name': 'Erumpent',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXX',
        'danger_level': 4,
        'icon': '🦏',
        'desc': 'Grande animal com um chifre explosivo. Sua pele dura resiste à maioria dos feitiços.',
        'origin': 'África'
    },
    {
        'name': 'Hipogrifos',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXX',
        'danger_level': 3,
        'icon': '🦅',
        'desc': 'Criatura orgulhosa que exige reverência. Metade águia gigante, metade cavalo.',
        'origin': 'Europa'
    },
    {
        'name': 'Fênix',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXX',
        'danger_level': 3,
        'icon': '🔥',
        'desc': 'Pássaro magnífico que renasce das cinzas. Suas lágrimas têm imenso poder curativo.',
        'origin': 'Global'
    },
    {
        'name': 'Unicórnios',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXX',
        'danger_level': 3,
        'icon': '🦄',
        'desc': 'Símbolo de pureza. Criaturas brancas e velozes cujo chifre e pelos são itens de alto valor.',
        'origin': 'Europa Setentrional'
    },
    {
        'name': 'Kappas',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXX',
        'danger_level': 3,
        'icon': '🐢',
        'desc': 'Demônios aquáticos nipônicos que estrangulam humanos. Perdem a força se a água em sua cabeça cair.',
        'origin': 'Japão'
    },
    {
        'name': 'Kelpie',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXX',
        'danger_level': 3,
        'icon': '🐎',
        'desc': 'Demônio aquático metamorfo. Atrai pessoas para cavalgarem sobre ele e as afoga.',
        'origin': 'Reino Unido / Irlanda'
    },
    {
        'name': 'Augurey',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XX',
        'danger_level': 2,
        'icon': '🦅',
        'desc': 'Pássaro melancólico que prevê chuva. Suas penas repelem tinta de qualquer espécie.',
        'origin': 'Irlanda'
    },
    {
        'name': 'Puffskein',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XX',
        'danger_level': 2,
        'icon': '🧶',
        'desc': 'Bola de pelos dócil e fofa. Popular animal de estimação que gosta de comer catotas.',
        'origin': 'Mundo todo'
    },
    {
        'name': 'Kneazle',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XX',
        'danger_level': 2,
        'icon': '🐱',
        'desc': 'Felino inteligente capaz de detectar pessoas suspeitas e guiar seus donos para casa.',
        'origin': 'Global'
    },
    {
        'name': 'Fwooper',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'X',
        'danger_level': 1,
        'icon': '🦜',
        'desc': 'Pássaro africano de cores berrantes. Seu canto constante pode levar o ouvinte à loucura.',
        'origin': 'África'
    },
    {
        'name': 'Chizpurfle',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'X',
        'danger_level': 1,
        'icon': '🦀',
        'desc': 'Pequenos parasitas mágicos de aparência lupina que se alimentam de resquícios mágicos.',
        'origin': 'Global'
    },
    # --- SERES (Beings) ---
    {
        'name': 'Gigantes',
        'category': 'being',
        'category_label': 'Ser',
        'danger': 'XXXX',
        'danger_level': 4,
        'icon': '🌋',
        'desc': 'Humanoides imensos de pele grossa e resistência a feitiços. Vivem em tribos montanhosas.',
        'origin': 'Montanhas Remotas'
    },
    {
        'name': 'Vampiros',
        'category': 'being',
        'category_label': 'Ser',
        'danger': 'XXXX',
        'danger_level': 4,
        'icon': '🧛',
        'desc': 'Humanos undead que dependem de sangue. Possuem grande agilidade e força noturna.',
        'origin': 'Europa Central / Transilvânia'
    },
    {
        'name': 'H. Lobo (Humano)',
        'category': 'being',
        'category_label': 'Ser',
        'danger': 'XXXX',
        'danger_level': 4,
        'icon': '👨‍💼',
        'desc': 'Vítimas de licantropia. Enquanto humanos, são cidadãos de pleno direito na sociedade bruxa.',
        'origin': 'Global'
    },
    {
        'name': 'Centauros',
        'category': 'being',
        'category_label': 'Fera-Autodeclarado',
        'danger': 'XXX',
        'danger_level': 3,
        'icon': '🏹',
        'desc': 'Criaturas inteligentes que estudam as estrelas. Recusaram a categoria de "Ser" na história.',
        'origin': 'Florestas Europeias'
    },
    {
        'name': 'Sereianos / Tritões',
        'category': 'being',
        'category_label': 'Fera-Autodeclarado',
        'danger': 'XXX',
        'danger_level': 3,
        'icon': '🧜‍♀️',
        'desc': 'Povos da água com cultura e linguagens complexas. Habitam lagos e oceanos profundos.',
        'origin': 'Lagos e Antilhas'
    },
    {
        'name': 'Goblins',
        'category': 'being',
        'category_label': 'Ser',
        'danger': 'XXX',
        'danger_level': 3,
        'icon': '💰',
        'desc': 'Mestres de finanças e ferreiros habilidosos. Criaram as defesas mágicas de Gringotes.',
        'origin': 'Reino Unido / Global'
    },
    {
        'name': 'Veelas',
        'category': 'being',
        'category_label': 'Ser',
        'danger': 'XXX',
        'danger_level': 3,
        'icon': '👱‍♀️',
        'desc': 'Belas mulheres que hipnotizam com sua dança. Transformam-se em feras se enfurecidas.',
        'origin': 'Europa Oriental'
    },
    {
        'name': 'Elfos domésticos',
        'category': 'being',
        'category_label': 'Ser',
        'danger': 'XX',
        'danger_level': 2,
        'icon': '🧹',
        'desc': 'Pequenos seres servos ligados a famílias bruxas. Possuem magia instintiva muito poderosa.',
        'origin': 'Reino Unido'
    },
    {
        'name': 'Leprechauns',
        'category': 'being',
        'category_label': 'Ser',
        'danger': 'XX',
        'danger_level': 2,
        'icon': '🍀',
        'desc': 'Pequenos seres travessos que distribuem moedas de ouro que desaparecem depois.',
        'origin': 'Irlanda'
    },
    # --- ESPÍRITOS (Spirits) ---
    {
        'name': 'Dementadores',
        'category': 'spirit',
        'category_label': 'Não-Ser',
        'danger': 'XXXXX',
        'danger_level': 5,
        'icon': '🌑',
        'desc': 'Sugam a esperança e alegria. Seu beijo pode extrair a alma de uma pessoa viva.',
        'origin': 'Azkaban'
    },
    {
        'name': 'Inferi',
        'category': 'spirit',
        'category_label': 'Não-Ser',
        'danger': 'XXXXX',
        'danger_level': 5,
        'icon': '🧟',
        'desc': 'Cadáveres reanimados por feitiços das trevas para servirem como soldados ou guardiões.',
        'origin': 'Geral'
    },
    {
        'name': 'Banshee',
        'category': 'spirit',
        'category_label': 'Espírito',
        'danger': 'XXXX',
        'danger_level': 4,
        'icon': '🗣️',
        'desc': 'Fantasma feminino melancólico cujo grito sinistro prediz desgraça ou morte iminente.',
        'origin': 'Irlanda / Escócia'
    },
    {
        'name': 'Poltergeist',
        'category': 'spirit',
        'category_label': 'Espírito',
        'danger': 'XXX',
        'danger_level': 3,
        'icon': '👻',
        'desc': 'Entidade do caos pura. Pirraça é o exemplo mais famoso residente em Hogwarts.',
        'origin': 'Hogwarts'
    },
    {
        'name': 'Fantasmas',
        'category': 'spirit',
        'category_label': 'Espírito',
        'danger': 'XX',
        'danger_level': 2,
        'icon': '💀',
        'desc': 'A marca transparente deixada por uma alma que não conseguiu seguir em frente.',
        'origin': 'Global'
    }
]

# --- DADOS DOS SAPOS DE CHOCOLATE ---
FROGS_DATA = [
    {
        'id': 'dumbledore',
        'name': 'Alvo Dumbledore',
        'desc': 'Diretor de Hogwarts. Considerado o maior bruxo da era moderna. Famoso por derrotar Grindelwald e descobrir os doze usos do sangue de dragão.',
        'rarity': 'legendary',
        'rarity_label': 'Lendário',
        'title': 'O Grande Diretor',
        'icon': '🧙‍♂️',
        'category': 'Mestres de Hogwarts'
    },
    {
        'id': 'merlin',
        'name': 'Merlin',
        'desc': 'Bruxo medieval mais famoso de todos os tempos. Defensor dos direitos dos Trouxas e fundador da Ordem de Merlin.',
        'rarity': 'legendary',
        'rarity_label': 'Lendário',
        'title': 'Príncipe dos Magos',
        'icon': '📜',
        'category': 'Lendas Medievais'
    },
    {
        'id': 'gryffindor',
        'name': 'Godric Gryffindor',
        'desc': 'Co-fundador de Hogwarts. O maior duelista de seu tempo, deu o nome à casa dos corajosos e ousados.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'Bravo Duelista',
        'icon': '🦁',
        'category': 'Fundadores de Hogwarts'
    },
    {
        'id': 'hufflepuff',
        'name': 'Helga Hufflepuff',
        'desc': 'Co-fundadora de Hogwarts. Valorizava a lealdade e o trabalho duro above all. Famosa por seus feitiços culinários.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'Bondade Infinita',
        'icon': '🦡',
        'category': 'Fundadores de Hogwarts'
    },
    {
        'id': 'ravenclaw',
        'name': 'Rowena Ravenclaw',
        'desc': 'Co-fundadora de Hogwarts. A bruxa mais brilhante de sua época. Criou o diadema que conferia sabedoria.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'Mente Brilhante',
        'icon': '🦅',
        'category': 'Fundadores de Hogwarts'
    },
    {
        'id': 'slytherin',
        'name': 'Salazar Slytherin',
        'desc': 'Co-fundador de Hogwarts. Um dos primeiros Ofidioglotas registrados e mestre em Legilimência.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'Mestre da Ofidioglossia',
        'icon': '🐍',
        'category': 'Fundadores de Hogwarts'
    },
    {
        'id': 'flamel',
        'name': 'Nicolau Flamel',
        'desc': 'O único fabricante conhecido da Pedra Filosofal. Alquimista que viveu mais de 600 anos.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'O Imortal Alquimista',
        'icon': '💎',
        'category': 'Alquimistas e Inventores'
    },
    {
        'id': 'newt',
        'name': 'Newt Scamander',
        'desc': 'Famoso Magizoologista e autor de "Animais Fantásticos e Onde Habitam". Especialista em criaturas mágicas.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'O Magizoologista',
        'icon': '💼',
        'category': 'Magizoologistas e Videntes'
    },
    {
        'id': 'lockhart',
        'name': 'Gilderoy Lockhart',
        'desc': 'Autor de inúmeros best-sellers sobre suas "aventuras" e cinco vezes vencedor do prêmio do Sorriso Mais Charmoso.',
        'rarity': 'common',
        'rarity_label': 'Comum',
        'title': 'Mestre do Charme',
        'icon': '✨',
        'category': 'Mestres de Hogwarts'
    },
    {
        'id': 'morgana',
        'name': 'Morgana le Fay',
        'desc': 'Poderosa bruxa medieval, meia-irmã do Rei Arthur. Inimiga jurada de Merlin e mestra em artes das trevas.',
        'rarity': 'legendary',
        'rarity_label': 'Lendário',
        'title': 'Rainha das Sombras',
        'icon': '🔮',
        'category': 'Lendas Medievais'
    },
    {
        'id': 'harry_potter',
        'name': 'Harry Potter',
        'desc': 'O Menino que Sobreviveu. Famoso por derrotar Lord Voldemort e liderar a resistência na Batalha de Hogwarts.',
        'rarity': 'legendary',
        'rarity_label': 'Lendário',
        'title': 'O Eleito',
        'icon': '⚡',
        'category': 'O Trio de Ouro e Aliados'
    },
    {
        'id': 'hermione_granger',
        'name': 'Hermione Granger',
        'desc': 'A bruxa mais brilhante de sua idade. Co-fundadora da Armada de Dumbledore e peça chave na destruição das Horcruxes.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'Mente Brilhante',
        'icon': '📚',
        'category': 'O Trio de Ouro e Aliados'
    },
    {
        'id': 'ron_weasley',
        'name': 'Rony Weasley',
        'desc': 'Melhor amigo de Harry Potter. Destruiu a Horcrux do medalhão e foi goleiro de Quadribol da Grifinória.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'Leal Amigo',
        'icon': '♟️',
        'category': 'O Trio de Ouro e Aliados'
    },
    {
        'id': 'luna_lovegood',
        'name': 'Luna Lovegood',
        'desc': 'Membro da Armada de Dumbledore. Famosa por sua visão única do mundo e por encontrar criaturas que ninguém mais vê.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'A Observadora',
        'icon': '👓',
        'category': 'O Trio de Ouro e Aliados'
    },
    {
        'id': 'neville_longbottom',
        'name': 'Neville Longbottom',
        'desc': 'Líder da Armada de Dumbledore durante a ocupação de Hogwarts. Destruiu Nagini com a espada de Gryffindor.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'O Defensor',
        'icon': '🌱',
        'category': 'O Trio de Ouro e Aliados'
    },
    {
        'id': 'mcgonagall',
        'name': 'Minerva McGonagall',
        'desc': 'Diretora de Hogwarts e mestre em Transfiguração. Líder da defesa de Hogwarts contra os Comensais da Morte.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'Mestre da Transfiguração',
        'icon': '🐈',
        'category': 'Mestres de Hogwarts'
    },
    {
        'id': 'snape',
        'name': 'Severo Snape',
        'desc': 'Mestre de Poções e Príncipe Mestiço. Atuou como agente duplo em uma das missões de espionagem mais perigosas da história.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'O Príncipe Mestiço',
        'icon': '🧪',
        'category': 'Mestres de Hogwarts'
    },
    {
        'id': 'bellatrix',
        'name': 'Bellatrix Lestrange',
        'desc': 'A comensal da morte mais leal de Voldemort. Mestra em artes das trevas e duelos mortais.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'A Fanática',
        'icon': '🗡️',
        'category': 'Outros Bruxos de Destaque'
    },
    {
        'id': 'wildsmith',
        'name': 'Ignatia Wildsmith',
        'desc': 'Bruxa inventora do Pó de Flu, revolucionando o transporte mágico em todo o mundo.',
        'rarity': 'common',
        'rarity_label': 'Comum',
        'title': 'Inventora do Pó de Flu',
        'icon': '🔥',
        'category': 'Alquimistas e Inventores'
    },
    {
        'id': 'wenlock',
        'name': 'Bridget Wenlock',
        'desc': 'Famosa Aritmante que primeiro descobriu as propriedades mágicas do número sete.',
        'rarity': 'common',
        'rarity_label': 'Comum',
        'title': 'Mestra da Aritmancia',
        'icon': '🔢',
        'category': 'Alquimistas e Inventores'
    },
    {
        'id': 'vablatsky',
        'name': 'Cassandra Vablatsky',
        'desc': 'Célebre vidente e autora de "Esclarecendo o Futuro". Suas profecias ainda são estudadas.',
        'rarity': 'common',
        'rarity_label': 'Comum',
        'title': 'A Vidente',
        'icon': '🔮',
        'category': 'Magizoologistas e Videntes'
    },
    {
        'id': 'woodcroft',
        'name': 'Hengisto de Woodcroft',
        'desc': 'Fundador da aldeia de Hogsmeade. Fugiu de perseguições trouxas para criar o único refúgio bruxo da Grã-Bretanha.',
        'rarity': 'common',
        'rarity_label': 'Comum',
        'title': 'Fundador de Hogsmeade',
        'icon': '🍻',
        'category': 'Outros Bruxos de Destaque'
    },
    {
        'id': 'agripa',
        'name': 'Cornélio Agripa',
        'desc': 'Bruxo cujas figurinhas são extremamente raras. Um alquimista e místico que escreveu sobre magia natural.',
        'rarity': 'rare',
        'rarity_label': 'Raro',
        'title': 'O Alqumista Místico',
        'icon': '📖',
        'category': 'Alquimistas e Inventores'
    },
    {
        'id': 'ptolemy',
        'name': 'Ptolomeu',
        'desc': 'Bruxo cuja figurinha é celebrada por sua raridade. Astrônomo e geógrafo famoso do mundo bruxo antigo.',
        'rarity': 'common',
        'rarity_label': 'Comum',
        'title': 'O Astrônomo Antigo',
        'icon': '🪐',
        'category': 'Outros Bruxos de Destaque'
    },
    {
        'id': 'bertie_bott',
        'name': 'Bertie Bott',
        'desc': 'Criador dos Feijãozinhos de Todos os Sabores. Inventou o doce por acidente ao tentar criar um feijão normal.',
        'rarity': 'common',
        'rarity_label': 'Comum',
        'title': 'Mestre dos Doces',
        'icon': '🍬',
        'category': 'Outros Bruxos de Destaque'
    }
]
# --- DADOS DOS FEITIÇOS ---
SPELLS_DATA = [
    # UTILIDADE E DEFESA
    {
        'id': 'alohomora',
        'name': 'Alohomora',
        'incantation': 'Alohomora',
        'type': 'utility',
        'type_label': 'Utilidade',
        'effect': 'Destranca portas e fechaduras comuns',
        'description': 'Um feitiço essencial para exploração, capaz de abrir fechaduras que não foram seladas magicamente.',
        'difficulty': 'Iniciante',
        'icon': '🔑'
    },
    {
        'id': 'lumos',
        'name': 'Lumos',
        'incantation': 'Lumos',
        'type': 'utility',
        'type_label': 'Utilidade',
        'effect': 'Cria uma fonte de luz na ponta da varinha',
        'description': 'Ilumina ambientes escuros. A luz pode ser movida junto com a varinha.',
        'difficulty': 'Iniciante',
        'icon': '💡'
    },
    {
        'id': 'nox',
        'name': 'Nox',
        'incantation': 'Nox',
        'type': 'utility',
        'type_label': 'Utilidade',
        'effect': 'Extingue a luz da varinha',
        'description': 'O contra-feitiço direto para o Lumos.',
        'difficulty': 'Iniciante',
        'icon': '🌑'
    },
    {
        'id': 'wingardium-leviosa',
        'name': 'Wingardium Leviosa',
        'incantation': 'Wingardium Leviosa',
        'type': 'utility',
        'type_label': 'Utilidade',
        'effect': 'Levita objetos',
        'description': 'Exige um movimento preciso de "girar e sacudir" com a varinha.',
        'difficulty': 'Iniciante',
        'icon': '🍃'
    },
    {
        'id': 'accio',
        'name': 'Accio',
        'incantation': 'Accio',
        'type': 'utility',
        'type_label': 'Utilidade',
        'effect': 'Convoca objetos para a mão do bruxo',
        'description': 'Funciona mesmo com objetos fora do campo de visão, desde que o bruxo se concentre neles.',
        'difficulty': 'Intermediário',
        'icon': '🧲'
    },
    {
        'id': 'aguamenti',
        'name': 'Aguamenti',
        'incantation': 'Aguamenti',
        'type': 'utility',
        'type_label': 'Utilidade',
        'effect': 'Produz um jato de água pura',
        'description': 'Pode ser usado para beber ou apagar incêndios mágicos simples.',
        'difficulty': 'Intermediário',
        'icon': '💧'
    },
    {
        'id': 'riddikulus',
        'name': 'Riddikulus',
        'incantation': 'Riddikulus',
        'type': 'utility',
        'type_label': 'Utilidade',
        'effect': 'Vence um Bicho-Papão com humor',
        'description': 'Obriga a criatura a assumir uma forma que o bruxo considere engraçada.',
        'difficulty': 'Intermediário',
        'icon': '🤡'
    },
    {
        'id': 'incendio',
        'name': 'Incendio',
        'incantation': 'Incendio',
        'type': 'utility',
        'type_label': 'Utilidade / Combate',
        'effect': 'Produz chamas',
        'description': 'Pode ser usado para acender lareiras ou como um ataque ofensivo de fogo.',
        'difficulty': 'Iniciante',
        'icon': '🔥'
    },
    {
        'id': 'scourgify',
        'name': 'Scourgify',
        'incantation': 'Scourgify',
        'type': 'utility',
        'type_label': 'Utilidade',
        'effect': 'Limpa objetos',
        'description': 'Remove sujeira e manchas instantaneamente. Útil para tarefas domésticas mágicas.',
        'difficulty': 'Iniciante',
        'icon': '🧼'
    },
    {
        'id': 'finite-incantatem',
        'name': 'Finite Incantatem',
        'incantation': 'Finite Incantatem',
        'type': 'utility',
        'type_label': 'Utilidade',
        'effect': 'Cessa efeitos mágicos',
        'description': 'Finaliza o efeito de feitiços e encantamentos em uma área ou alvo específico.',
        'difficulty': 'Intermediário',
        'icon': '⏹️'
    },
    {
        'id': 'muffliato',
        'name': 'Muffliato',
        'incantation': 'Muffliato',
        'type': 'utility',
        'type_label': 'Utilidade (Privacidade)',
        'effect': 'Gera um zumbido nos ouvidos de terceiros',
        'description': 'Impede que pessoas próximas ouçam conversas privadas, criando um ruído de fundo.',
        'difficulty': 'Intermediário',
        'icon': '🤫'
    },
    {
        'id': 'obliviate',
        'name': 'Obliviate',
        'incantation': 'Obliviate',
        'type': 'utility',
        'type_label': 'Utilidade / Perigoso',
        'effect': 'Apaga memórias',
        'description': 'Usado para fazer o alvo esquecer eventos específicos ou toda a sua vida.',
        'difficulty': 'Difícil',
        'icon': '🧠'
    },
    {
        'id': 'engorgio',
        'name': 'Engorgio',
        'incantation': 'Engorgio',
        'type': 'utility',
        'type_label': 'Utilidade',
        'effect': 'Aumenta o tamanho de objetos ou criaturas',
        'description': 'Faz com que o alvo cresça rapidamente. O contra-feitiço é o Reducio.',
        'difficulty': 'Iniciante',
        'icon': '🔍'
    },
    {
        'id': 'geminio',
        'name': 'Geminio',
        'incantation': 'Geminio',
        'type': 'utility',
        'type_label': 'Utilidade',
        'effect': 'Duplica objetos',
        'description': 'Cria uma cópia exata de um objeto. Cópias criadas por este feitiço costumam ser menos valiosas.',
        'difficulty': 'Intermediário',
        'icon': '👯'
    },

    # COMBATE E DUELO
    {
        'id': 'expelliarmus',
        'name': 'Expelliarmus',
        'incantation': 'Expelliarmus',
        'type': 'combat',
        'type_label': 'Combate',
        'effect': 'Desarma o oponente',
        'description': 'Faz com que a varinha ou arma do oponente voe para longe de suas mãos.',
        'difficulty': 'Iniciante',
        'icon': '🪄'
    },
    {
        'id': 'stupefy',
        'name': 'Estupore (Stupefy)',
        'incantation': 'Stupefy',
        'type': 'combat',
        'type_label': 'Combate',
        'effect': 'Atordoa e desmaia o alvo',
        'description': 'O feitiço de combate mais comum em duelos, projeta um feixe de luz vermelha.',
        'difficulty': 'Intermediário',
        'icon': '💥'
    },
    {
        'id': 'bombarda',
        'name': 'Bombarda',
        'incantation': 'Bombarda',
        'type': 'combat',
        'type_label': 'Combate (Explosivo)',
        'effect': 'Cria uma pequena explosão',
        'description': 'Usado para destruir obstáculos como portas trancadas ou paredes finas.',
        'difficulty': 'Intermediário',
        'icon': '🧨'
    },
    {
        'id': 'reducto',
        'name': 'Reducto',
        'incantation': 'Reducto',
        'type': 'combat',
        'type_label': 'Combate',
        'effect': 'Pulveriza objetos sólidos',
        'description': 'Reduz objetos a pó ou pedaços minúsculos através de uma explosão focada.',
        'difficulty': 'Intermediário',
        'icon': '🧱'
    },
    {
        'id': 'impedimenta',
        'name': 'Impedimenta',
        'incantation': 'Impedimenta',
        'type': 'combat',
        'type_label': 'Combate / Defesa',
        'effect': 'Lentidão ou paralisia temporária',
        'description': 'Atrasa o oponente, impedindo-o de se mover em direção ao bruxo.',
        'difficulty': 'Intermediário',
        'icon': '🛑'
    },
    {
        'id': 'incarcerous',
        'name': 'Incarcerous',
        'incantation': 'Incarcerous',
        'type': 'combat',
        'type_label': 'Combate',
        'effect': 'Conjura cordas para prender o alvo',
        'description': 'Cordas grossas e resistentes surgem do nada para amarrar o oponente.',
        'difficulty': 'Intermediário',
        'icon': '🧶'
    },
    {
        'id': 'levicorpus',
        'name': 'Levicorpus',
        'incantation': 'Levicorpus',
        'type': 'combat',
        'type_label': 'Combate (Não-Verbal)',
        'effect': 'Lança o alvo no ar pelo tornozelo',
        'description': 'O alvo é içado de cabeça para baixo, como se estivesse pendurado por um fio invisível.',
        'difficulty': 'Intermediário',
        'icon': '🤸'
    },
    {
        'id': 'petrificus-totalus',
        'name': 'Petrificus Totalus',
        'incantation': 'Petrificus Totalus',
        'type': 'combat',
        'type_label': 'Combate',
        'effect': 'Paralisia total do corpo',
        'description': 'O alvo fica rígido como uma estátua, incapaz de se mover ou falar.',
        'difficulty': 'Iniciante',
        'icon': '🗿'
    },
    {
        'id': 'confundo',
        'name': 'Confundo',
        'incantation': 'Confundo',
        'type': 'combat',
        'type_label': 'Combate',
        'effect': 'Causa confusão mental temporária',
        'description': 'Faz o alvo ficar desorientado e suscetível a ordens simples ou erros de julgamento.',
        'difficulty': 'Intermediário',
        'icon': '😵‍💫'
    },
    {
        'id': 'expulso',
        'name': 'Expulso',
        'incantation': 'Expulso',
        'type': 'combat',
        'type_label': 'Combate',
        'effect': 'Empurra objetos ou pessoas com força explosiva',
        'description': 'Cria uma pequena explosão de pressão que arremessa alvos para longe.',
        'difficulty': 'Intermediário',
        'icon': '💣'
    },
    {
        'id': 'sectumsempra',
        'name': 'Sectumsempra',
        'incantation': 'Sectumsempra',
        'type': 'combat',
        'type_label': 'Combate (Trevas)',
        'effect': 'Provoca cortes profundos',
        'description': 'Um feitiço perigoso que corta o alvo como se fosse uma espada invisível.',
        'difficulty': 'Difícil',
        'icon': '⚔️'
    },
    {
        'id': 'diffindo',
        'name': 'Diffindo',
        'incantation': 'Diffindo',
        'type': 'combat',
        'type_label': 'Combate / Utilidade',
        'effect': 'Rasga ou corta objetos com precisão',
        'description': 'Muito usado para rasgar tecidos, abrir embalagens ou desamarrar cordas.',
        'difficulty': 'Iniciante',
        'icon': '✂️'
    },
    {
        'id': 'silencio',
        'name': 'Silencio',
        'incantation': 'Silencio',
        'type': 'combat',
        'type_label': 'Combate / Utilidade',
        'effect': 'Emudece o alvo',
        'description': 'Impede que o alvo emita sons ou realize feitiços verbais.',
        'difficulty': 'Intermediário',
        'icon': '🔇'
    },

    # DEFESA
    {
        'id': 'expecto-patronum',
        'name': 'Expecto Patronum',
        'incantation': 'Expecto Patronum',
        'type': 'defense',
        'type_label': 'Defesa',
        'effect': 'Conjura um Patrono protetor',
        'description': 'A única defesa conhecida contra Dementadores. Exige a lembrança mais feliz do bruxo.',
        'difficulty': 'Muito Difícil',
        'icon': '🦌'
    },
    {
        'id': 'protego',
        'name': 'Protego',
        'incantation': 'Protego',
        'type': 'defense',
        'type_label': 'Defesa',
        'effect': 'Cria um escudo mágico',
        'description': 'Reflete feitiços menores e protege contra ataques físicos leves.',
        'difficulty': 'Intermediário',
        'icon': '🛡️'
    },
    {
        'id': 'protego-totalum',
        'name': 'Protego Totalum',
        'incantation': 'Protego Totalum',
        'type': 'defense',
        'type_label': 'Defesa de Área',
        'effect': 'Protege uma área contra moradores',
        'description': 'Forma uma barreira protetora ao redor de um acampamento ou morada.',
        'difficulty': 'Difícil',
        'icon': '🏰'
    },
    {
        'id': 'salvio-hexia',
        'name': 'Salvio Hexia',
        'incantation': 'Salvio Hexia',
        'type': 'defense',
        'type_label': 'Defesa de Área',
        'effect': 'Protege contra feitiços externos',
        'description': 'Frequentemente usado com outros feitiços de proteção para ocultar e defender áreas.',
        'difficulty': 'Intermediário',
        'icon': '✨'
    },

    # MALDIÇÕES IMPERDOÁVEIS
    {
        'id': 'crucio',
        'name': 'Crucio',
        'incantation': 'Cruciatus',
        'type': 'unforgivable',
        'type_label': 'Maldição Imperdoável',
        'effect': 'Tortura física insuportável',
        'description': 'Causa uma dor agoniante. Exige que o bruxo realmente deseje causar sofrimento.',
        'difficulty': 'Difícil (Intencional)',
        'icon': '⚡'
    },
    {
        'id': 'imperio',
        'name': 'Imperio',
        'incantation': 'Imperio',
        'type': 'unforgivable',
        'type_label': 'Maldição Imperdoável',
        'effect': 'Controle total sobre a vítima',
        'description': 'A vítima entra em um estado de transe e obedece a qualquer comando do mestre.',
        'difficulty': 'Difícil (Foco)',
        'icon': '🧠'
    },
    {
        'id': 'avada-kedavra',
        'name': 'Avada Kedavra',
        'incantation': 'Avada Kedavra',
        'type': 'unforgivable',
        'type_label': 'Maldição Imperdoável',
        'effect': 'Morte instantânea',
        'description': 'A maldição final. Não possui contra-feitiço e mata instantaneamente sem deixar marcas.',
        'difficulty': 'Extrema',
        'icon': '💀'
    },

    # CURA E REPARO
    {
        'id': 'reparo',
        'name': 'Reparo',
        'incantation': 'Reparo',
        'type': 'utility',
        'type_label': 'Utilidade',
        'effect': 'Conserta objetos quebrados',
        'description': 'Restaura a forma original de itens danificados, desde que todos os pedaços estejam presentes.',
        'difficulty': 'Iniciante',
        'icon': '🛠️'
    },
    {
        'id': 'episkey',
        'name': 'Episkey',
        'incantation': 'Episkey',
        'type': 'healing',
        'type_label': 'Cura',
        'effect': 'Cura ferimentos leves',
        'description': 'Corrige ossos quebrados pequenos (como narizes) e estanca sangramentos menores.',
        'difficulty': 'Iniciante',
        'icon': '🩹'
    },
    {
        'id': 'rennervate',
        'name': 'Rennervate',
        'incantation': 'Rennervate',
        'type': 'healing',
        'type_label': 'Cura',
        'effect': 'Desperta alguém inconsciente',
        'description': 'O contra-feitiço para o Estupore. Revive pessoas que foram atordoadas.',
        'difficulty': 'Iniciante',
        'icon': '👁️'
    },
    {
        'id': 'ferula',
        'name': 'Ferula',
        'incantation': 'Ferula',
        'type': 'healing',
        'type_label': 'Cura',
        'effect': 'Conjura talas e bandagens',
        'description': 'Cria curativos físicos para imobilizar membros quebrados.',
        'difficulty': 'Iniciante',
        'icon': '🩹'
    },
    {
        'id': 'anapneo',
        'name': 'Anapneo',
        'incantation': 'Anapneo',
        'type': 'healing',
        'type_label': 'Cura',
        'effect': 'Limpa as vias respiratórias',
        'description': 'Desobstrui a garganta de alguém que esteja engasgado.',
        'difficulty': 'Intermediário',
        'icon': '🫁'
    },
    {
        'id': 'tergeo',
        'name': 'Tergeo',
        'incantation': 'Tergeo',
        'type': 'utility',
        'type_label': 'Utilidade',
        'effect': 'Limpa superfícies e estanca sangue',
        'description': 'Suga líquidos como sangue, poeira ou lama de roupas e superfícies.',
        'difficulty': 'Iniciante',
        'icon': '🧼'
    },
    {
        'id': 'vulnera-sanentur',
        'name': 'Vulnera Sanentur',
        'incantation': 'Vulnera Sanentur',
        'type': 'healing',
        'type_label': 'Cura Avançada',
        'effect': 'Cura cortes profundos de magia negra',
        'description': 'Eficaz contra o Sectumsempra. Exige um cântico específico e movimentos rítmicos.',
        'difficulty': 'Difícil',
        'icon': '🩸'
    }
]

POTIONS_DATA = [
    {
        'id': 'amortentia',
        'name': 'Amortentia',
        'effect': 'Poção do Amor mais poderosa',
        'type': 'utility',
        'type_label': 'Utilidade / Emoção',
        'difficulty': 'Avançada',
        'difficulty_level': 4,
        'description': 'Não cria amor, mas uma obsessão poderosa. Tem um brilho perolado e fumaça em espirais.',
        'ingredients': [
            'Ovos de Ashwinder',
            'Pétalas de Rosa de Inverno',
            'Espinhos de Porco-espinho',
            'Sementes de Erva-doce'
        ],
        'instructions': [
            'Adicione os ovos de Ashwinder ao caldeirão já aquecido.',
            'Mexa no sentido horário até a poção ficar vermelha.',
            'Adicione as pétalas de rosa e reduza o fogo.',
            'Deixe cozinhar por 24 horas até atingir o brilho perolado.'
        ],
        'icon': '💘'
    },
    {
        'id': 'felix-felicis',
        'name': 'Felix Felicis',
        'effect': 'Sorte Líquida',
        'type': 'utility',
        'type_label': 'Utilidade / Sorte',
        'difficulty': 'Extrema',
        'difficulty_level': 5,
        'description': 'Torna quem a bebe sortudo por um tempo. É de cor ouro derretido.',
        'ingredients': [
            'Ovos de Occamy',
            'Tentáculo de Murtisco',
            'Raiz de Mandrágora cozida',
            'Tintura de Tomilho'
        ],
        'instructions': [
            'Aqueça o caldeirão até a água ferver vigorosamente.',
            'Adicione os ovos de Occamy um a um.',
            'Mexa 3 vezes no sentido anti-horário após cada ingrediente.',
            'Aguarde 6 meses para que a mistura decante e se torne dourada.'
        ],
        'icon': '🧪'
    },
    {
        'id': 'polissuco',
        'name': 'Poção Polissuco',
        'effect': 'Transforma na aparência de outra pessoa',
        'type': 'utility',
        'type_label': 'Transformação',
        'difficulty': 'Muito Difícil',
        'difficulty_level': 4,
        'description': 'Permite que o usuário assuma a forma física de outra pessoa por uma hora.',
        'ingredients': [
            'Hemeróbios (cozidos por 21 dias)',
            'Sanguessugas',
            'Pó de chifre de Bicórnio',
            'Pele de Araramboia picada',
            'Um pedaço da pessoa (cabelo, unhas, etc.)'
        ],
        'instructions': [
            'Cozinhe os hemeróbios por exatamente 21 dias.',
            'Adicione as sanguessugas e mexa vigorosamente.',
            'Acrescente o pó de chifre de bicórnio e a pele de araramboia.',
            'Por último, adicione o "pedaço" da pessoa a ser assumida.'
        ],
        'icon': '👥'
    },
    {
        'id': 'veritaserum',
        'name': 'Veritaserum',
        'effect': 'Soro da Verdade mais poderoso',
        'type': 'influence',
        'type_label': 'Influência / Verdade',
        'difficulty': 'Extrema',
        'difficulty_level': 5,
        'description': 'Três gotas forçam o usuário a revelar seus segredos mais profundos.',
        'ingredients': [
            'Água pura de nascente',
            'Penas de Dedo-duro',
            'Raiz de Acônito',
            'Essência de Belladonna'
        ],
        'instructions': [
            'A poção deve ser preparada durante uma lua cheia.',
            'Misture os ingredientes em um caldeirão de cristal.',
            'Deixe descansar por um ciclo lunar completo.',
            'A poção final deve ser clara como água e sem cheiro.'
        ],
        'icon': '🩸'
    },
    {
        'id': 'esquelesgas',
        'name': 'Esquele-Gás',
        'effect': 'Regenera ossos perdidos',
        'type': 'healing',
        'type_label': 'Cura',
        'difficulty': 'Intermediária',
        'difficulty_level': 3,
        'description': 'Causa uma dor terrível durante o processo de crescimento ósseo.',
        'ingredients': [
            'Presas de dragão moídas',
            'Sumo de mandrágora',
            'Extrato de urtiga',
            'Escaravelhos esmagados'
        ],
        'instructions': [
            'Misture as presas de dragão com o sumo de mandrágora.',
            'Ferva até a poção adquirir uma cor cinza fumegante.',
            'Adicione os escaravelhos e mexa 7 vezes para a esquerda.',
            'Sirva quente ao paciente.'
        ],
        'icon': '🦴'
    },
    {
        'id': 'aconito',
        'name': 'Poção de Acônito',
        'effect': 'Alivia sintomas da Licantropia',
        'type': 'healing',
        'type_label': 'Cura / Controle',
        'difficulty': 'Muito Difícil',
        'difficulty_level': 4,
        'description': 'Permite que o lobisomem mantenha sua consciência humana durante a transformação.',
        'ingredients': [
            'Acônito (ou Mata-cão)',
            'Pó de Lua moído',
            'Sálvia de prata',
            'Essência de Cicuta'
        ],
        'instructions': [
            'Deve ser tomada diariamente na semana anterior à lua cheia.',
            'Misture o acônito delicadamente para não liberar toxinas excessivas.',
            'A fumaça deve ter um tom azulado constante.',
            'O preparo é extremamente sensível ao calor.'
        ],
        'icon': '🐺'
    }
]

# --- DADOS DA ENCICLOPÉDIA DE BRUXOS ---
ENCYCLOPEDIA_WIZARDS_DATA = [
    {
        'id': 'dumbledore_full',
        'name': 'Alvo Dumbledore',
        'full_name': 'Alvo Percival Wulfrico Brian Dumbledore',
        'birth': '1881 - 1997',
        'house': 'Gryffindor',
        'house_label': 'Grifinória',
        'blood': 'Mestiço',
        'field': 'Transfiguração / Defesa',
        'achievements': [
            'Derrotou o bruxo das trevas Gerardo Grindelwald em 1945',
            'Descobriu os doze usos do sangue de dragão',
            'Criador da Ordem da Fênix',
            'Supremo Caceique da Confederação Internacional de Bruxos'
        ],
        'bio': 'Considerado por muitos o maior bruxo da era moderna, Dumbledore foi professor de Transfiguração e mais tarde Diretor de Hogwarts. Sua sabedoria e poder eram lendários, sendo o único bruxo que Lord Voldemort já temeu.',
        'icon': '🧙‍♂️'
    },
    {
        'id': 'merlin_full',
        'name': 'Merlin',
        'full_name': 'Merlin (Príncipe dos Magos)',
        'birth': 'Idade Média',
        'house': 'Slytherin',
        'house_label': 'Sonserina',
        'blood': 'Sangue-Puro',
        'field': 'Encantamentos',
        'achievements': [
            'Fundador da Ordem de Merlin',
            'Conselheiro do Rei Arthur',
            'Eminente defensor dos direitos dos trouxas',
            'Especialista em encantos de levitação e ocultação'
        ],
        'bio': 'Talvez o bruxo mais famoso da história. Merlin acreditava que os bruxos deveriam ajudar os trouxas e viver em paz com eles. Curiosamente, foi um aluno da Sonserina em Hogwarts, provando que a ambição pode ser usada para o bem maior.',
        'icon': '📜'
    },
    {
        'id': 'voldemort_full',
        'name': 'Lord Voldemort',
        'full_name': 'Tom Servolo Riddle',
        'birth': '1926 - 1998',
        'house': 'Slytherin',
        'house_label': 'Sonserina',
        'blood': 'Mestiço',
        'field': 'Artes das Trevas',
        'achievements': [
            'O bruxo das trevas mais perigoso de todos os tempos',
            'Criador de múltiplas Horcruxes',
            'Líder dos Comensais da Morte',
            'Herdeiro de Slytherin e mestre da Ofidioglossia'
        ],
        'bio': 'Aquele-Que-Não-Deve-Ser-Nomeado espalhou terror pelo mundo bruxo durante décadas. Obcecado pela imortalidade e pela pureza de sangue, ele transformou-se em uma criatura quase inumana através de magia negra proibida.',
        'icon': '🐍'
    },
    {
        'id': 'hermione_full',
        'name': 'Hermione Granger',
        'full_name': 'Hermione Jean Granger',
        'birth': '1979 - Presente',
        'house': 'Gryffindor',
        'house_label': 'Grifinória',
        'blood': 'Nascida-Trouxa',
        'field': 'Pesquisa Mágica / Lei',
        'achievements': [
            'Ministra da Magia (desde 2019)',
            'Co-fundadora da Armada de Dumbledore',
            'Responsável por destruir a Horcrux da Taça de Hufflepuff',
            'Lutou ativamente contra as injustiças sofridas por Elfos Domésticos'
        ],
        'bio': 'Conhecida como a bruxa mais brilhante de sua geração, Hermione provou que o conhecimento e a dedicação superam qualquer linhagem de sangue. Sua inteligência foi crucial para a derrota de Lord Voldemort.',
        'icon': '📚'
    },
    {
        'id': 'snape_full',
        'name': 'Severo Snape',
        'full_name': 'Severo Snape (Príncipe Mestiço)',
        'birth': '1960 - 1998',
        'house': 'Slytherin',
        'house_label': 'Sonserina',
        'blood': 'Mestiço',
        'field': 'Poções / Artes das Trevas',
        'achievements': [
            'Mestre de Poções e Diretor de Hogwarts',
            'Criador de feitiços como Sectumsempra e Muffliato',
            'Agente Duplo lendário na guerra contra Voldemort',
            'Mestre em Oclumência e Legilimência'
        ],
        'bio': 'Um homem complexo cuja lealdade foi questionada até o fim. Snape dedicou sua vida a proteger Harry Potter em memória de Lilian Evans, atuando no papel mais perigoso da Segunda Guerra Bruxa.',
        'icon': '🧪'
    },
    {
        'id': 'newt_full',
        'name': 'Newt Scamander',
        'full_name': 'Newton Artemis Fido Scamander',
        'birth': '1897 - Presente',
        'house': 'Hufflepuff',
        'house_label': 'Lufa-Lufa',
        'blood': 'Sangue-Puro',
        'field': 'Magizoologia',
        'achievements': [
            'Autor de "Animais Fantásticos e Onde Habitam"',
            'Ordem de Merlin, Segunda Classe',
            'Especialista mundial em cuidados com seres mágicos',
            'Peça chave na derrota de Grindelwald em Nova York'
        ],
        'bio': 'Um explorador incansável que viajou pelos cinco continentes para documentar criaturas mágicas. Newt ensinou ao mundo bruxo que os animais fantásticos devem ser protegidos, não apenas temidos.',
        'icon': '💼'
    },
    {
        'id': 'ravenclaw_full',
        'name': 'Rowena Ravenclaw',
        'full_name': 'Rowena Ravenclaw',
        'birth': 'Século X',
        'house': 'Ravenclaw',
        'house_label': 'Corvinal',
        'blood': 'Sangue-Puro',
        'field': 'Arquitetura Mágica',
        'achievements': [
            'Co-fundadora da Escola de Magia de Hogwarts',
            'Criadora do Diadema da Sabedoria',
            'Arquiteta das plantas mutáveis de Hogwarts',
            'Mãe da Dama Cinzenta'
        ],
        'bio': 'Famosa por sua inteligência e criatividade inigualáveis. Rowena acreditava que a mente é o maior tesouro de um bruxo. Ela selecionava alunos que demonstravam sagacidade e aprendizado rápido.',
        'icon': '🦅'
    }
]

@app.route('/bruxos')
def wizards():
    return render_template('wizards.html', wizards=ENCYCLOPEDIA_WIZARDS_DATA, active_tab='wizards')

@app.route('/pocoes')
def potions():
    return render_template('potions.html', potions=POTIONS_DATA, active_tab='potions')

@app.route('/feiticos')
def spells():
    return render_template('spells.html', spells=SPELLS_DATA, active_tab='spells')

@app.route('/sapos')
def frogs():
    return render_template('frogs.html', wizards=FROGS_DATA, active_tab='frogs')

@app.route('/criaturas')
def creatures():
    return render_template('creatures.html', creatures=CREATURES_DATA, active_tab='creatures')

@app.route('/mundo')
def world():
    return render_template('world.html', houses=WORLD_DATA, active_tab='world')

if __name__ == '__main__':
    app.run(debug=True)
