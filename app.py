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
    # Redireciona para o início da jornada das varinhas (Origem)
    return wands_origin()

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
        'name': 'Acromântula',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXXX',
        'icon': '🕷️',
        'desc': 'Aranha monstruosa de oito olhos capaz de fala humana. Venenosa e impossível de treinar.',
        'origin': 'Bornéu / Floresta Proibida'
    },
    {
        'name': 'Basilisco',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXXX',
        'icon': '🐍',
        'desc': 'O Rei das Serpentes. Seu olhar mata instantaneamente e seu veneno é um dos poucos que destroem Horcruxes.',
        'origin': 'Herpo, o Sujo (Criador)'
    },
    {
        'name': 'Dragão (Barriga-de-Ferro)',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXXX',
        'icon': '🐉',
        'desc': 'A maior raça de dragão. Metálico e imenso, guardava os cofres profundos de Gringotes.',
        'origin': 'Ucrânia'
    },
    {
        'name': 'Fênix',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXXX',
        'icon': '🔥',
        'desc': 'Pássaro escarlate fiel. Renasce das cinzas, cura com lágrimas e carrega cargas imensas. Extremamente difícil de domesticar.',
        'origin': 'Egito / Índia / China'
    },
    {
        'name': 'Hipogrifo',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XXX',
        'icon': '🦅',
        'desc': 'Cabeça de águia, corpo de cavalo. Orgulhoso, exige respeito antes de permitir aproximação.',
        'origin': 'Europa'
    },
    {
        'name': 'Puffskein',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'XX',
        'icon': '🧶',
        'desc': 'Bola de pelos fofa e dócil. Popular animal de estimação bruxo. Gosta de comer catotas.',
        'origin': 'Mundo todo'
    },
    {
        'name': 'Verme-Cego (Flobberworm)',
        'category': 'beast',
        'category_label': 'Fera',
        'danger': 'X',
        'icon': '🐛',
        'desc': 'Entediante. Move-se pouco e produz muco usado em poções. Prefere alface.',
        'origin': 'Valas úmidas'
    },
    # --- SERES (Beings) ---
    {
        'name': 'Centauro',
        'category': 'being',
        'category_label': 'Ser (Classificado como Fera por pedido)',
        'danger': 'XXXX',
        'icon': '🏹',
        'desc': 'Mestre em cura, divinação e astronomia. Vivem em rebanhos e evitam humanos. Orgulhosos e misteriosos.',
        'origin': 'Florestas da Europa'
    },
    {
        'name': 'Sereiano (Selkie)',
        'category': 'being',
        'category_label': 'Ser (Classificado como Fera por pedido)',
        'danger': 'XXXX',
        'icon': '🧜‍♀️',
        'desc': 'Povo da água da Escócia e Irlanda. Beleza rústica e vozes que só soam belas embaixo d\'água.',
        'origin': 'Lago Negro (Hogwarts)'
    },
    {
        'name': 'Duende (Goblin)',
        'category': 'being',
        'category_label': 'Ser',
        'danger': 'XXX',
        'icon': '💰',
        'desc': 'Artesãos de metais habilidosos e guardiões de Gringotes. Possuem magia própria sem varinha.',
        'origin': 'Desconhecida'
    },
    # --- ESPÍRITOS (Spirits) ---
    {
        'name': 'Poltergeist',
        'category': 'spirit',
        'category_label': 'Espírito',
        'danger': 'XXX',
        'icon': '👻',
        'desc': 'Espírito do caos indestrutível. Pirraça é o exemplo mais famoso de Hogwarts.',
        'origin': 'Locais com alta emoção adolescente'
    },
    {
        'name': 'Fantasma',
        'category': 'spirit',
        'category_label': 'Espírito',
        'danger': 'XX',
        'icon': '💀',
        'desc': 'A impressão deixada por uma alma que partiu. Atravessam paredes e deixam o ar gelado.',
        'origin': 'Todo lugar onde alguém morreu infeliz'
    },
    {
        'name': 'Dementador',
        'category': 'spirit', # Classificação ambígua, mas se encaixa em não-ser/espírito maligno
        'category_label': 'Não-Ser',
        'danger': 'XXXXX',
        'icon': '🌑',
        'desc': 'Guardiões de Azkaban. Sugam a felicidade e a alma (Beijo do Dementador).',
        'origin': 'Azkaban'
    }
]

@app.route('/criaturas')
def creatures():
    return render_template('creatures.html', creatures=CREATURES_DATA, active_tab='creatures')

@app.route('/mundo')
def world():
    return render_template('world.html', houses=WORLD_DATA, active_tab='world')

if __name__ == '__main__':
    app.run(debug=True)
