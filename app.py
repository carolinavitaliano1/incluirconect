# app.py
# VERSÃO COMPLETA E UNIFICADA PARA GARANTIR O FUNCIONAMENTO

import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    layout="wide",
    page_title="INTERVENÇÃO IA 7.0",
    page_icon="🧠"
)

# ##############################################################################
# BANCO DE DADOS BNCC COMPLETO (TUDO EM UM SÓ LUGAR)
# ##############################################################################
BNCC_DATABASE = {
    "Educação Infantil": {
        "Bebês (zero a 1 ano e 6 meses)": {
            "O eu, o outro e o nós": [
                {"codigo": "EI01EO01", "descricao": "Perceber que suas ações têm efeitos nas outras crianças e nos adultos."},
                {"codigo": "EI01EO02", "descricao": "Perceber as possibilidades e os limites de seu corpo nas brincadeiras e interações das quais participa."},
                {"codigo": "EI01EO03", "descricao": "Interagir com crianças da mesma faixa etária e adultos ao explorar espaços, materiais, objetos, brinquedos."},
                {"codigo": "EI01EO04", "descricao": "Comunicar necessidades, desejos e emoções, utilizando gestos, balbucios, palavras."},
                {"codigo": "EI01EO05", "descricao": "Reconhecer seu corpo e expressar suas sensações em momentos de alimentação, higiene, brincadeira e descanso."},
                {"codigo": "EI01EO06", "descricao": "Interagir com outras crianças da mesma faixa etária e adultos, adaptando-se ao convívio social."}
            ],
            "Corpo, gestos e movimentos": [
                {"codigo": "EI01CG01", "descricao": "Movimentar as partes do corpo para exprimir corporalmente emoções, necessidades e desejos."},
                {"codigo": "EI01CG02", "descricao": "Experimentar as possibilidades corporais nas brincadeiras e interações em ambientes acolhedores e desafiantes."},
                {"codigo": "EI01CG03", "descricao": "Imitar gestos e movimentos de outras crianças, adultos e animais."},
                {"codigo": "EI01CG04", "descricao": "Participar do cuidado do seu corpo e da promoção do seu bem-estar."},
                {"codigo": "EI01CG05", "descricao": "Utilizar os movimentos de preensão, encaixe e lançamento, ampliando suas possibilidades de manuseio de diferentes materiais e objetos."}
            ],
            "Traços, sons, cores e formas": [
                {"codigo": "EI01TS01", "descricao": "Explorar sons produzidos com o próprio corpo e com objetos do ambiente."},
                {"codigo": "EI01TS02", "descricao": "Traçar marcas gráficas, em diferentes suportes, usando instrumentos riscantes e tintas."},
                {"codigo": "EI01TS03", "descricao": "Explorar diferentes fontes sonoras e materiais para acompanhar brincadeiras cantadas, canções, músicas e melodias."}
            ],
            "Escuta, fala, pensamento e imaginação": [
                {"codigo": "EI01EF01", "descricao": "Reconhecer quando é chamado por seu nome e reconhecer os nomes de pessoas com quem convive."},
                {"codigo": "EI01EF02", "descricao": "Demonstrar interesse ao ouvir a leitura de poemas e a apresentação de músicas."},
                {"codigo": "EI01EF03", "descricao": "Demonstrar interesse ao ouvir histórias lidas ou contadas, observando ilustrações e os movimentos de leitura do adulto-leitor."},
                {"codigo": "EI01EF04", "descricao": "Reconhecer elementos das ilustrações de histórias, apontando-os, a pedido do adulto-leitor."},
                {"codigo": "EI01EF05", "descricao": "Imitar as variações de entonação e gestos realizados pelos adultos, ao ler histórias e ao cantar."},
                {"codigo": "EI01EF06", "descricao": "Comunicar-se com outras pessoas usando movimentos, gestos, balbucios, fala e outras formas de expressão."},
                {"codigo": "EI01EF07", "descricao": "Conhecer e manipular diferentes instrumentos e suportes de escrita."},
                {"codigo": "EI01EF08", "descricao": "Participar de situações de escuta de textos em diferentes gêneros textuais (poemas, fábulas, contos, receitas, quadrinhos, anúncios etc.)."},
                {"codigo": "EI01EF09", "descricao": "Conhecer e manipular diferentes portadores de texto (livro, revista, gibi, jornal, cartaz, CD, tablet etc.)."}
            ],
            "Espaços, tempos, quantidades, relações e transformações": [
                {"codigo": "EI01ET01", "descricao": "Explorar e descobrir as propriedades de objetos e materiais (odor, cor, sabor, temperatura)."},
                {"codigo": "EI01ET02", "descricao": "Explorar relações de causa e efeito (transbordar, tingir, misturar, mover e remover etc.) na interação com o mundo físico."},
                {"codigo": "EI01ET03", "descricao": "Explorar o ambiente pela ação e observação, manipulando, experimentando e fazendo descobertas."},
                {"codigo": "EI01ET04", "descricao": "Manipular, experimentar, arrumar e explorar o espaço por meio de experiências de deslocamentos de si e dos objetos."},
                {"codigo": "EI01ET05", "descricao": "Manipular materiais de diferentes texturas e pesos, bem como objetos e brinquedos de formas e tamanhos variados para desenvolver a descoberta de seus atributos."},
                {"codigo": "EI01ET06", "descricao": "Vivenciar diferentes ritmos, velocidades e fluxos nas interações e brincadeiras (em danças, balanços, escorregadores etc.)."}
            ],
        },
        "Crianças bem pequenas (1 ano e 7 meses a 3 anos e 11 meses)": {
            "O eu, o outro e o nós": [
                {"codigo": "EI02EO01", "descricao": "Demonstrar atitudes de cuidado e solidariedade na interação com crianças e adultos."},
                {"codigo": "EI02EO02", "descricao": "Demonstrar imagem positiva de si e confiança em sua capacidade para enfrentar dificuldades e desafios."},
                {"codigo": "EI02EO03", "descricao": "Compartilhar os objetos e os espaços com crianças da mesma faixa etária e adultos."},
                {"codigo": "EI02EO04", "descricao": "Comunicar-se com outras crianças e adultos, utilizando diferentes linguagens (oral, corporal, etc.)."},
                {"codigo": "EI02EO05", "descricao": "Perceber que as pessoas têm características físicas diferentes, respeitando essas diferenças."},
                {"codigo": "EI02EO06", "descricao": "Respeitar regras básicas de convívio social nas interações e brincadeiras."},
                {"codigo": "EI02EO07", "descricao": "Resolver conflitos nas interações e brincadeiras, com a orientação de um adulto."}
            ],
            "Corpo, gestos e movimentos": [
                {"codigo": "EI02CG01", "descricao": "Apropriar-se de gestos e movimentos de sua cultura no cuidado de si e nos jogos e brincadeiras."},
                {"codigo": "EI02CG02", "descricao": "Deslocar seu corpo no espaço, orientando-se por noções como em frente, atrás, no alto, embaixo, dentro, fora etc., ao se envolver em brincadeiras e atividades de diferentes naturezas."},
                {"codigo": "EI02CG03", "descricao": "Explorar formas de deslocamento no espaço (pular, saltar, dançar), combinando movimentos e seguindo orientações."},
                {"codigo": "EI02CG04", "descricao": "Demonstrar progressiva independência no cuidado do seu corpo."},
                {"codigo": "EI02CG05", "descricao": "Desenvolver progressivamente as habilidades manuais, adquirindo controle para desenhar, pintar, rasgar, folhear, entre outros."}
            ],
            "Traços, sons, cores e formas": [
                {"codigo": "EI02TS01", "descricao": "Criar sons com materiais, objetos e instrumentos musicais, para acompanhar diversos ritmos de música."},
                {"codigo": "EI02TS02", "descricao": "Utilizar materiais variados com possibilidades de manipulação (argila, massa de modelar), explorando cores, texturas, superfícies, planos, formas e volumes ao criar objetos tridimensionais."},
                {"codigo": "EI02TS03", "descricao": "Utilizar diferentes fontes sonoras disponíveis no ambiente em brincadeiras cantadas, canções, músicas e melodias."}
            ],
            "Escuta, fala, pensamento e imaginação": [
                {"codigo": "EI02EF01", "descricao": "Dialogar com crianças e adultos, expressando seus desejos, necessidades, sentimentos e opiniões."},
                {"codigo": "EI02EF02", "descricao": "Identificar e criar diferentes sons e reconhecer rimas e aliterações em cantigas de roda e textos poéticos."},
                {"codigo": "EI02EF03", "descricao": "Demonstrar interesse e atenção ao ouvir a leitura de histórias e outros textos, diferenciando escrita de ilustrações, e acompanhando, com orientação do adulto-leitor, a direção da leitura."},
                {"codigo": "EI02EF04", "descricao": "Formular e responder perguntas, desenvolvendo a curiosidade sobre o mundo."},
                {"codigo": "EI02EF05", "descricao": "Relatar experiências e fatos acontecidos, histórias ouvidas, filmes ou peças teatrais assistidos etc."},
                {"codigo": "EI02EF06", "descricao": "Criar e contar histórias oralmente, com base em imagens ou temas sugeridos."},
                {"codigo": "EI02EF07", "descricao": "Manusear diferentes portadores textuais, demonstrando reconhecer seus usos sociais."},
                {"codigo": "EI02EF08", "descricao": "Manipular textos e participar de situações de escuta para ampliar seu contato com diferentes gêneros textuais (parlendas, histórias de aventura, etc.)."},
                {"codigo": "EI02EF09", "descricao": "Manusear diferentes instrumentos e suportes de escrita para desenhar, traçar letras e outros sinais gráficos."}
            ],
            "Espaços, tempos, quantidades, relações e transformações": [
                {"codigo": "EI02ET01", "descricao": "Explorar e descrever semelhanças e diferenças entre as características e propriedades dos objetos (textura, massa, tamanho)."},
                {"codigo": "EI02ET02", "descricao": "Observar, relatar e descrever incidentes do cotidiano e fenômenos naturais (luz solar, vento, chuva etc.)."},
                {"codigo": "EI02ET03", "descricao": "Compartilhar, com outras crianças, situações de cuidado de plantas e animais nos espaços da instituição e fora dela."},
                {"codigo": "EI02ET04", "descricao": "Identificar relações espaciais (dentro e fora, em cima, embaixo, acima, abaixo, entre e do lado) e temporais (antes, durante e depois)."},
                {"codigo": "EI02ET05", "descricao": "Classificar objetos, considerando determinado atributo (tamanho, peso, cor, forma etc.)."},
                {"codigo": "EI02ET06", "descricao": "Utilizar conceitos básicos de tempo (agora, antes, durante, depois, ontem, hoje, amanhã, lento, rápido, de pressa, devagar)."},
                {"codigo": "EI02ET07", "descricao": "Contar oralmente objetos, pessoas, livros etc., em contextos diversos."},
                {"codigo": "EI02ET08", "descricao": "Registrar com números a quantidade de crianças (meninas e meninos, presentes e ausentes) e a quantidade de objetos da mesma natureza (bonecas, carrinhos, etc.)."}
            ]
        },
        "Crianças pequenas (4 anos a 5 anos e 11 meses)": {
            "O eu, o outro e o nós": [
                {"codigo": "EI03EO01", "descricao": "Demonstrar empatia pelos outros, percebendo que as pessoas têm diferentes sentimentos, necessidades e maneiras de pensar e agir."},
                {"codigo": "EI03EO02", "descricao": "Agir de maneira independente, com confiança em suas capacidades, e reconhecer suas conquistas e limitações."},
                {"codigo": "EI03EO03", "descricao": "Ampliar as relações interpessoais, desenvolvendo atitudes de participação e cooperação."},
                {"codigo": "EI03EO04", "descricao": "Comunicar suas ideias e sentimentos a pessoas e grupos diversos."},
                {"codigo": "EI03EO05", "descricao": "Demonstrar valorização das características de seu corpo e respeitar as características dos outros (crianças e adultos) com os quais convive."},
                {"codigo": "EI03EO06", "descricao": "Manifestar interesse e respeito por diferentes culturas e modos de vida."},
                {"codigo": "EI03EO07", "descricao": "Usar estratégias pautadas no respeito mútuo para lidar com conflitos nas interações com crianças e adultos."}
            ],
            "Corpo, gestos e movimentos": [
                {"codigo": "EI03CG01", "descricao": "Criar com o corpo formas diversificadas de expressão de sentimentos, sensações e emoções, tanto nas situações do cotidiano quanto em brincadeiras."},
                {"codigo": "EI03CG02", "descricao": "Demonstrar controle e adequação do uso de seu corpo em brincadeiras e jogos, escuta e reconto de histórias, atividades artísticas, entre outras possibilidades."},
                {"codigo": "EI03CG03", "descricao": "Criar movimentos, gestos, olhares e mímicas em brincadeiras, jogos e atividades artísticas como dança, teatro e música."},
                {"codigo": "EI03CG04", "descricao": "Adotar hábitos de autocuidado relacionados a higiene, alimentação, conforto e aparência."},
                {"codigo": "EI03CG05", "descricao": "Coordenar suas habilidades manuais no atendimento adequado a seus interesses e necessidades em situações diversas."}
            ],
            "Traços, sons, cores e formas": [
                {"codigo": "EI03TS01", "descricao": "Utilizar sons produzidos por materiais, objetos e instrumentos musicais durante brincadeiras de faz de conta, encenações, criações musicais, festas."},
                {"codigo": "EI03TS02", "descricao": "Expressar-se livremente por meio de desenho, pintura, colagem, dobradura e escultura, criando produções bidimensionais e tridimensionais."},
                {"codigo": "EI03TS03", "descricao": "Reconhecer as qualidades do som (intensidade, duração, altura e timbre), utilizando-as em suas produções sonoras e ao ouvir músicas e sons."}
            ],
            "Escuta, fala, pensamento e imaginação": [
                {"codigo": "EI03EF01", "descricao": "Expressar ideias, desejos e sentimentos sobre suas vivências, por meio da linguagem oral e escrita (escrita espontânea), de fotos, desenhos e outras formas de expressão."},
                {"codigo": "EI03EF02", "descricao": "Inventar brincadeiras cantadas, poemas e canções, criando rimas, aliterações e ritmos."},
                {"codigo": "EI03EF03", "descricao": "Escolher e folhear livros, procurando orientar-se por temas e ilustrações e tentando identificar palavras conhecidas."},
                {"codigo": "EI03EF04", "descricao": "Recontar histórias ouvidas e planejar coletivamente roteiros de vídeos e de encenações, definindo os contextos, os personagens, a estrutura da história."},
                {"codigo": "EI03EF05", "descricao": "Recontar histórias ouvidas para produção de reconto escrito, tendo o professor como escriba."},
                {"codigo": "EI03EF06", "descricao": "Produzir suas próprias histórias orais e escritas (escrita espontânea), em situações com função social significativa."},
                {"codigo": "EI03EF07", "descricao": "Levantar hipóteses sobre gêneros textuais veiculados em portadores conhecidos, recorrendo a estratégias de observação gráfica e/ou de leitura."},
                {"codigo": "EI03EF08", "descricao": "Selecionar livros e textos de gêneros conhecidos para a leitura de um adulto e/ou para sua própria leitura (partindo de seu repertório sobre esses textos, como a recuperação pela memória, pela leitura das ilustrações etc.)."},
                {"codigo": "EI03EF09", "descricao": "Levantar hipóteses em relação à linguagem escrita, realizando registros de palavras e textos, por meio de escrita espontânea."}
            ],
            "Espaços, tempos, quantidades, relações e transformações": [
                {"codigo": "EI03ET01", "descricao": "Estabelecer relações de comparação entre objetos, observando suas propriedades."},
                {"codigo": "EI03ET02", "descricao": "Observar e descrever mudanças em diferentes materiais, resultantes de ações sobre eles, em experimentos envolvendo fenômenos naturais e artificiais."},
                {"codigo": "EI03ET03", "descricao": "Identificar e selecionar fontes de informações, para responder a questões sobre a natureza, seus fenômenos, sua conservação."},
                {"codigo": "EI03ET04", "descricao": "Registrar observações, manipulações e medidas, usando múltiplas linguagens (desenho, registro por números ou escrita espontânea), em diferentes suportes."},
                {"codigo": "EI03ET05", "descricao": "Classificar objetos e figuras de acordo com suas semelhanças e diferenças."},
                {"codigo": "EI03ET06", "descricao": "Relatar fatos importantes sobre seu nascimento e desenvolvimento, a história dos seus familiares e da sua comunidade."},
                {"codigo": "EI03ET07", "descricao": "Relacionar números às suas respectivas quantidades e identificar o antes, o depois e o entre em uma sequência."},
                {"codigo": "EI03ET08", "descricao": "Expressar medidas (peso, altura etc.), construindo gráficos básicos."}
            ]
        }
    },
    "Ensino Fundamental": {
        "1º Ano": {
            "Língua Portuguesa": [{"codigo": "EF15LP01", "descricao": "Identificar a função social de textos que circulam em campo da vida social dos quais participa cotidianamente (a casa, a rua, a comunidade, a escola) e nas mídias impressa, de massa e digital, reconhecendo para que foram produzidos, onde circulam, quem os produziu e a quem se destinam."}, {"codigo": "EF01LP07", "descricao": "Identificar fonemas e sua representação por letras."}, {"codigo": "EF01LP10", "descricao": "Nomear as letras do alfabeto e recitá-lo na ordem das letras."}],
            "Arte": [{"codigo": "EF15AR01", "descricao": "Identificar e apreciar formas distintas das artes visuais tradicionais e contemporâneas, cultivando a percepção, o imaginário, a capacidade de simbolizar e o repertório imagético."}],
            "Educação Física": [{"codigo": "EF12EF01", "descricao": "Experimentar, fruir e recriar diferentes brincadeiras e jogos da cultura popular presentes no contexto comunitário e regional, reconhecendo e respeitando as diferenças individuais de desempenho dos colegas."}],
            "Matemática": [{"codigo": "EF01MA01", "descricao": "Utilizar números naturais como indicador de quantidade ou de ordem em diferentes situações cotidianas e reconhecer situações em que os números não indicam contagem nem ordem, mas sim código de identificação."}, {"codigo": "EF01MA02", "descricao": "Contar de maneira exata ou aproximada, utilizando diferentes estratégias como o pareamento e outros agrupamentos."}, {"codigo": "EF01MA04", "descricao": "Contar a quantidade de objetos de coleções até 100 unidades e apresentar o resultado por registros verbais e simbólicos, em situações de seu interesse, como jogos, brincadeiras, materiais da sala de aula, entre outros."}],
            "Ciências": [{"codigo": "EF01CI01", "descricao": "Comparar características de diferentes materiais presentes em objetos de uso cotidiano, discutindo sua origem, os modos como são descartados e como podem ser usados de forma mais consciente."}],
            "Geografia": [{"codigo": "EF01GE01", "descricao": "Descrever características observadas de seus lugares de vivência (moradia, escola etc.) e identificar semelhanças e diferenças entre esses lugares."}],
            "História": [{"codigo": "EF01HI01", "descricao": "Identificar aspectos do seu crescimento por meio do registro das lembranças particulares ou de lembranças dos membros de sua família e/ou de sua comunidade."}]
        },
        "2º Ano": {
            "Língua Portuguesa": [{"codigo": "EF12LP01", "descricao": "Ler palavras novas com precisão na decodificação, no caso de palavras de uso frequente, ler globalmente, por memorização."}, {"codigo": "EF12LP02", "descricao": "Buscar, selecionar e ler, com a mediação do professor (leitura compartilhada), textos que circulam em meios impressos ou digitais, de acordo com as necessidades e interesses."}],
            "Matemática": [{"codigo": "EF02MA06", "descricao": "Resolver e elaborar problemas de adição e de subtração, envolvendo números de até três ordens, com os significados de juntar, acrescentar, separar, retirar, utilizando estratégias pessoais ou convencionais."}],
            "Ciências": [{"codigo": "EF02CI04", "descricao": "Descrever características de plantas e animais (tamanho, forma, cor, fase da vida, local onde se desenvolvem etc.) que fazem parte de seu cotidiano e relacioná-las ao ambiente em que eles vivem."}]
        },
        "3º Ano": {
            "Língua Portuguesa": [{"codigo": "EF35LP03", "descricao": "Identificar a ideia central do texto, demonstrando compreensão global."}, {"codigo": "EF35LP05", "descricao": "Inferir o sentido de palavras ou expressões desconhecidas em textos, com base no contexto da frase ou do texto."}],
            "Matemática": [{"codigo": "EF03MA05", "descricao": "Utilizar diferentes procedimentos de cálculo para resolver problemas (mental, escrito, exato, aproximado)."}, {"codigo": "EF03MA07", "descricao": "Resolver e elaborar problemas de multiplicação (por 2, 3, 4, 5 e 10) com os significados de adição de parcelas iguais e elementos apresentados em disposição retangular, utilizando diferentes estratégias de cálculo e registros."}],
            "Ciências": [{"codigo": "EF03CI04", "descricao": "Identificar características sobre o modo de vida (o que comem, como se reproduzem, como se deslocam etc.) dos animais mais comuns no ambiente próximo."}],
            "História": [{"codigo": "EF03HI01", "descricao": "Identificar os grupos populacionais que formaram a cidade, o município e a região, as relações estabelecidas entre eles e os eventos que marcam a formação da cidade."}]
        },
        "4º Ano": {
            "Língua Portuguesa": [{"codigo": "EF04LP04", "descricao": "Usar acentuação gráfica (agudas, graves)."}, {"codigo": "EF35LP09", "descricao": "Organizar o texto em unidades de sentido, dividindo-o em parágrafos segundo as normas gráficas e de acordo com as características do gênero textual."}],
            "Matemática": [{"codigo": "EF04MA03", "descricao": "Resolver e elaborar problemas com números naturais envolvendo adição e subtração."}, {"codigo": "EF04MA06", "descricao": "Resolver e elaborar problemas envolvendo diferentes significados da multiplicação."}],
            "Geografia": [{"codigo": "EF04GE01", "descricao": "Selecionar, em seus lugares de vivência e em suas histórias familiares e/ou da comunidade, elementos de distintas culturas, valorizando o que é próprio em cada uma delas."}]
        },
        "5º Ano": {
            "Língua Portuguesa": [{"codigo": "EF05LP03", "descricao": "Localizar e inferir informações em textos de diferentes gêneros."}, {"codigo": "EF35LP15", "descricao": "Opinar e defender ponto de vista sobre tema polêmico relacionado a situações vivenciadas na escola e/ou na comunidade."}],
            "Matemática": [{"codigo": "EF05MA07", "descricao": "Resolver e elaborar problemas de adição e subtração com números naturais e com números racionais."}, {"codigo": "EF05MA08", "descricao": "Resolver e elaborar problemas de multiplicação e divisão com números naturais e com números racionais."}]
        },
        "6º Ano": {
            "Língua Portuguesa": [{"codigo": "EF67LP14", "descricao": "Diferenciar, em textos, fatos de opiniões."}],
            "Matemática": [{"codigo": "EF06MA13", "descricao": "Resolver e elaborar problemas que envolvam porcentagens, com base na ideia de proporcionalidade."}],
            "História": [{"codigo": "EF06HI03", "descricao": "Identificar as hipóteses científicas sobre o surgimento da espécie humana."}]
        },
        "7º Ano": {
            "Matemática": [{"codigo": "EF07MA17", "descricao": "Resolver e elaborar problemas que envolvam variação de proporcionalidade direta e de proporcionalidade inversa entre duas grandezas."}],
            "Geografia": [{"codigo": "EF07GE01", "descricao": "Avaliar, por meio de exemplos extraídos dos meios de comunicação, ideias e estereótipos acerca das paisagens e da formação territorial do Brasil."}]
        },
        "8º Ano": {
            "Matemática": [{"codigo": "EF08MA07", "descricao": "Resolver e elaborar problemas que possam ser representados por sistemas de equações de 1º grau com duas incógnitas e interpretá-los."}],
            "Ciências": [{"codigo": "EF08CI01", "descricao": "Identificar e classificar diferentes fontes (renováveis e não renováveis) e tipos de energia utilizados em residências, comunidades ou cidades."}]
        },
        "9º Ano": {
            "Língua Portuguesa": [{"codigo": "EF89LP04", "descricao": "Identificar e avaliar teses/opiniões/posicionamentos explícitos e implícitos, argumentos e contra-argumentos em textos argumentativos."}],
            "Matemática": [{"codigo": "EF09MA05", "descricao": "Resolver e elaborar problemas que envolvam porcentagens (juros simples e compostos, acréscimos e decréscimos)."}]}
    },
    "Ensino Médio": {
        "Linguagens e suas Tecnologias": {
            "Competências Específicas": [
                {"codigo": 1, "descricao": "Compreender o funcionamento das diferentes linguagens e práticas culturais (artísticas, corporais e verbais) e mobilizar esses conhecimentos na recepção e produção de discursos nos diferentes campos de atuação social e nas diversas mídias, para ampliar as formas de participação social, o entendimento e as possibilidades de explicação e interpretação crítica da realidade e para continuar aprendendo."},
                {"codigo": 2, "descricao": "Compreender os processos identitários, conflitos e relações de poder que permeiam as práticas sociais de linguagem, respeitando as diversidades e a pluralidade de ideias e posições, e atuar socialmente com base em princípios e valores assentados na democracia, na igualdade e nos Direitos Humanos, exercitando o autoconhecimento, a empatia, o diálogo, a resolução de conflitos e a cooperação, e combatendo preconceitos de qualquer natureza."},
                {"codigo": 3, "descricao": "Utilizar diferentes linguagens (artísticas, corporais e verbais) para exercer, com autonomia e colaboração, protagonismo e autoria na vida pessoal e coletiva, de forma crítica, criativa, ética e solidária, defendendo pontos de vista que respeitem o outro e promovam os Direitos Humanos, a consciência socioambiental e o consumo responsável, em âmbito local, regional e global."},
                {"codigo": 4, "descricao": "Compreender as línguas como fenômeno (geo)político, histórico, cultural, social, variável, heterogêneo e sensível aos contextos de uso, reconhecendo suas variedades e vivenciando-as como formas de expressões identitárias, pessoais e coletivas, bem como agindo no enfrentamento de preconceitos de qualquer natureza."},
                {"codigo": 5, "descricao": "Compreender os processos de produção e negociação de sentidos nas práticas corporais, reconhecendo-as e vivenciando-as como formas de expressão de valores e identidades, em uma perspectiva democrática e de respeito à diversidade."},
                {"codigo": 6, "descricao": "Apreciar esteticamente as mais diversas produções artísticas e culturais, considerando suas características locais, regionais e globais, e mobilizar seus conhecimentos sobre as linguagens artísticas para dar significado e (re)construir produções autorais individuais e coletivas, exercendo protagonismo de maneira crítica e criativa, com respeito à diversidade de saberes, identidades e culturas."},
                {"codigo": 7, "descricao": "Mobilizar práticas de linguagem no universo digital, considerando as dimensões técnicas, críticas, criativas, éticas e estéticas, para expandir as formas de produzir sentidos, de engajar-se em práticas autorais e coletivas, e de aprender a aprender nos campos da ciência, cultura, trabalho, informação e vida pessoal e coletiva."}
            ],
            "Habilidades": [
                {"codigo": "EM13LGG101", "descricao": "Compreender e analisar processos de produção e circulação de discursos, nas diferentes linguagens, para fazer escolhas fundamentadas em função de interesses pessoais e coletivos."},
                {"codigo": "EM13LGG102", "descricao": "Analisar visões de mundo, conflitos de interesse, preconceitos e ideologias presentes nos discursos veiculados nas diferentes mídias, ampliando suas possibilidades de explicação, interpretação e intervenção crítica da/na realidade."},
                {"codigo": "EM13LGG103", "descricao": "Analisar o funcionamento das linguagens, para interpretar e produzir criticamente discursos em textos de diversas semioses (visuais, verbais, sonoras, gestuais)."},
                {"codigo": "EM13LGG104", "descricao": "Utilizar as diferentes linguagens, levando em conta seus funcionamentos, para a compreensão e produção de textos e discursos em diversos campos de atuação social."},
                {"codigo": "EM13LGG105", "descricao": "Analisar e experimentar diversos processos de remidiação de produções multissemióticas, multimídia e transmídia, desenvolvendo diferentes modos de participação e intervenção social."},
                {"codigo": "EM13LGG201", "descricao": "Utilizar as diversas linguagens (artísticas, corporais e verbais) em diferentes contextos, valorizando-as como fenômeno social, cultural, histórico, variável, heterogêneo e sensível aos contextos de uso."},
                {"codigo": "EM13LGG202", "descricao": "Analisar interesses, relações de poder e perspectivas de mundo nos discursos das diversas práticas de linguagem (artísticas, corporais e verbais), para compreender o modo como circulam, constituem-se e (re)produzem significação e ideologias."},
                {"codigo": "EM13LGG203", "descricao": "Analisar os diálogos e os processos de disputa por legitimidade nas práticas de linguagem e em suas produções (artísticas, corporais e verbais)."},
                {"codigo": "EM13LGG204", "descricao": "Dialogar e produzir entendimento mútuo, nas diversas linguagens (artísticas, corporais e verbais), em contextos de convivência, como forma de resolver conflitos e fortalecer a cooperação."},
                {"codigo": "EM13LGG301", "descricao": "Participar de processos de produção individual e colaborativa em diferentes linguagens (artísticas, corporais e verbais), levando em conta suas formas e seus funcionamentos, para produzir sentidos em diferentes contextos."},
                {"codigo": "EM13LGG302", "descricao": "Posicionar-se criticamente diante de diversas visões de mundo presentes nos discursos em diferentes linguagens, levando em conta seus contextos de produção e de circulação."},
                {"codigo": "EM13LGG303", "descricao": "Debater questões polêmicas de relevância social, analisando diferentes argumentos e opiniões, para formular, negociar e sustentar posições, frente à análise de perspectivas distintas."},
                {"codigo": "EM13LGG304", "descricao": "Formular propostas, intervir e participar de forma crítica e criativa de práticas de linguagem (artísticas, corporais e verbais) que demandem atuação coletiva e colaborativa."},
                {"codigo": "EM13LGG305", "descricao": "Mapear e criar, por meio de práticas de linguagem, possibilidades de atuação social, política, artística e cultural para enfrentar desafios contemporâneos."},
                {"codigo": "EM13LGG401", "descricao": "Analisar criticamente textos de modo a compreender e caracterizar as línguas como fenômeno (geo)político, histórico, social, cultural, variável, heterogêneo e sensível aos contextos de uso."},
                {"codigo": "EM13LGG402", "descricao": "Empregar, nas interações sociais, a variedade e o estilo de língua adequados à situação comunicativa, ao(s) interlocutor(es) e ao gênero do discurso."},
                {"codigo": "EM13LGG403", "descricao": "Fazer uso do inglês como língua de comunicação global, levando em conta a multiplicidade e variedade de usos, usuários e funções dessa língua no mundo contemporâneo."},
                {"codigo": "EM13LGG501", "descricao": "Selecionar e utilizar movimentos corporais de forma consciente e intencional para interagir socialmente em práticas corporais, de modo a estabelecer relações construtivas, empáticas, éticas e de respeito às diferenças."},
                {"codigo": "EM13LGG502", "descricao": "Analisar criticamente preconceitos, estereótipos e relações de poder presentes nas práticas corporais, adotando posicionamento contrário a qualquer manifestação de injustiça e desrespeito a direitos humanos e valores democráticos."},
                {"codigo": "EM13LGG503", "descricao": "Vivenciar práticas corporais e significá-las em seu projeto de vida, como forma de autoconhecimento, autocuidado físico e emocional, e de lazer."},
                {"codigo": "EM13LGG601", "descricao": "Apropriar-se do patrimônio artístico de diferentes tempos e lugares, compreendendo a sua diversidade, bem como os processos de legitimação das manifestações artísticas na sociedade."},
                {"codigo": "EM13LGG602", "descricao": "Fruir e apreciar esteticamente diversas manifestações artísticas e culturais, das locais às mundiais, assim como delas participar, de modo a aguçar continuamente a sensibilidade, a imaginação e a criatividade."},
                {"codigo": "EM13LGG603", "descricao": "Expressar-se e atuar em processos de criação autorais individuais e coletivos nas diferentes linguagens artísticas e nas intersecções entre elas, recorrendo a referências estéticas e culturais, conhecimentos de naturezas diversas e experiências individuais e coletivas."},
                {"codigo": "EM13LGG604", "descricao": "Relacionar as práticas artísticas às diferentes dimensões da vida social, cultural, política e econômica e identificar o processo de construção histórica dessas práticas."},
                {"codigo": "EM13LGG701", "descricao": "Explorar tecnologias digitais da informação e comunicação (TDIC), compreendendo seus princípios e funcionalidades, e utilizá-las de modo ético, criativo, responsável e adequado a práticas de linguagem em diferentes contextos."},
                {"codigo": "EM13LGG702", "descricao": "Avaliar o impacto das tecnologias digitais da informação e comunicação (TDIC) na formação do sujeito e em suas práticas sociais, para fazer uso crítico dessa mídia em práticas de seleção, compreensão e produção de discursos em ambiente digital."},
                {"codigo": "EM13LGG703", "descricao": "Utilizar diferentes linguagens, mídias e ferramentas digitais em processos de produção coletiva, colaborativa e projetos autorais em ambientes digitais."},
                {"codigo": "EM13LGG704", "descricao": "Apropriar-se criticamente de processos de pesquisa e busca de informação, por meio de ferramentas e dos novos formatos de produção e distribuição do conhecimento na cultura de rede."},
                {"codigo": "EM13LP01", "descricao": "Relacionar o texto com suas condições de produção e seu contexto sócio-histórico de circulação, de forma a ampliar as possibilidades de construção de sentidos e de análise crítica."},
                {"codigo": "EM13LP02", "descricao": "Estabelecer relações entre as partes do texto, tanto na produção como na leitura/escuta, considerando a construção composicional e o estilo do gênero."}
            ]
        },
        "Matemática e suas Tecnologias": {
            "Competências Específicas": [
                {"codigo": 1, "descricao": "Utilizar estratégias, conceitos e procedimentos matemáticos para interpretar situações em diversos contextos, sejam atividades cotidianas, sejam fatos das Ciências da Natureza e Humanas, das questões socioeconômicas ou tecnológicas, divulgados por diferentes meios, de modo a contribuir para uma formação geral."},
                {"codigo": 2, "descricao": "Propor ou participar de ações para investigar desafios do mundo contemporâneo e tomar decisões éticas e socialmente responsáveis, com base na análise de problemas sociais, como os voltados a situações de saúde, sustentabilidade, das implicações da tecnologia no mundo do trabalho, entre outros, mobilizando e articulando conceitos, procedimentos e linguagens próprios da Matemática."},
                {"codigo": 3, "descricao": "Utilizar estratégias, conceitos, definições e procedimentos matemáticos para interpretar, construir modelos e resolver problemas em diversos contextos, analisando a plausibilidade dos resultados e a adequação das soluções propostas, de modo a construir argumentação consistente."},
                {"codigo": 4, "descricao": "Compreender e utilizar, com flexibilidade e precisão, diferentes registros de representação matemáticos (algébrico, geométrico, estatístico, computacional etc.), na busca de solução e comunicação de resultados de problemas."},
                {"codigo": 5, "descricao": "Investigar e estabelecer conjecturas a respeito de diferentes conceitos e propriedades matemáticas, empregando estratégias e recursos, como observação de padrões, experimentações e diferentes tecnologias, identificando a necessidade, ou não, de uma demonstração cada vez mais formal na validação das referidas conjecturas."}
            ],
            "Habilidades": [
                {"codigo": "EM13MAT101", "descricao": "Interpretar criticamente situações econômicas, sociais e fatos relativos às Ciências da Natureza que envolvam a variação de grandezas."},
                {"codigo": "EM13MAT102", "descricao": "Analisar tabelas, gráficos e amostras de pesquisas estatísticas apresentadas em relatórios divulgados por diferentes meios de comunicação, identificando, quando for o caso, inadequações que possam induzir a erros de interpretação."},
                {"codigo": "EM13MAT103", "descricao": "Interpretar e compreender textos científicos ou divulgados pelas mídias, que empregam unidades de medida de diferentes grandezas e as conversões possíveis entre elas."},
                {"codigo": "EM13MAT104", "descricao": "Interpretar taxas e índices de natureza socioeconômica (índice de desenvolvimento humano, taxas de inflação, entre outros)."},
                {"codigo": "EM13MAT105", "descricao": "Utilizar as noções de transformações isométricas (translação, reflexão, rotação) e transformações homotéticas para construir figuras e analisar elementos da natureza e diferentes produções humanas."},
                {"codigo": "EM13MAT106", "descricao": "Analisar a extração de informações de diferentes representações de um mesmo conjunto de dados (tabelas, gráficos de barras, de colunas, de setores e de linhas)."},
                {"codigo": "EM13MAT201", "descricao": "Propor ou participar de ações adequadas às demandas da região, preferencialmente de sua comunidade, envolvendo medições e cálculos de perímetro, de área, de volume, de capacidade ou de massa."},
                {"codigo": "EM13MAT202", "descricao": "Analisar e comparar situações que envolvam juros simples e compostos, com o uso de planilhas eletrônicas ou aplicativos."},
                {"codigo": "EM13MAT203", "descricao": "Aplicar conceitos matemáticos no planejamento, na execução e na análise de ações envolvendo a utilização de aplicativos e a criação de planilhas."},
                {"codigo": "EM13MAT301", "descricao": "Resolver e elaborar problemas do cotidiano, da Matemática e de outras áreas do conhecimento, que envolvem equações lineares e sistemas lineares."},
                {"codigo": "EM13MAT302", "descricao": "Construir modelos em linguagem matemática, para resolver problemas em diferentes contextos, avaliando sua adequação."},
                {"codigo": "EM13MAT303", "descricao": "Interpretar e comparar cenários sobre juros simples e compostos, utilizando aplicativos de simulação."},
                {"codigo": "EM13MAT304", "descricao": "Resolver e elaborar problemas com funções logarítmicas nos quais seja necessário compreender e interpretar a variação das grandezas envolvidas."},
                {"codigo": "EM13MAT305", "descricao": "Resolver e elaborar problemas com funções exponenciais nos quais seja necessário compreender e interpretar a variação das grandezas envolvidas."},
                {"codigo": "EM13MAT306", "descricao": "Resolver e elaborar problemas em contextos que envolvem fenômenos periódicos reais e suas representações por funções seno e cosseno."},
                {"codigo": "EM13MAT307", "descricao": "Empregar diferentes métodos para a obtenção da medida da área de uma superfície (reconfigurações, aproximação por cortes etc.)."},
                {"codigo": "EM13MAT308", "descricao": "Resolver e elaborar problemas de contagem envolvendo agrupamentos ordenáveis ou não de elementos, por meio dos princípios multiplicativo e aditivo."},
                {"codigo": "EM13MAT309", "descricao": "Resolver e elaborar problemas que envolvem o cálculo de áreas totais e de volumes de prismas, pirâmides e corpos redondos em situações reais."},
                {"codigo": "EM13MAT310", "descricao": "Resolver e elaborar problemas que envolvem cálculo de probabilidade de eventos em experimentos aleatórios equiprováveis."},
                {"codigo": "EM13MAT311", "descricao": "Identificar e descrever o espaço amostral de eventos aleatórios, realizando contagem das possibilidades."},
                {"codigo": "EM13MAT312", "descricao": "Resolver e elaborar problemas que envolvem o cálculo da probabilidade da união e da intersecção de eventos em experimentos aleatórios."},
                {"codigo": "EM13MAT313", "descricao": "Aplicar conceitos de um poliedro em situações-problema, para calcular, por exemplo, o número de vértices, faces e arestas."},
                {"codigo": "EM13MAT314", "descricao": "Resolver e elaborar problemas que envolvem cálculo de volumes de figuras compostas por sólidos usuais."},
                {"codigo": "EM13MAT315", "descricao": "Investigar e registrar, por meio de um fluxograma, os passos para a resolução de um grupo de problemas."},
                {"codigo": "EM13MAT316", "descricao": "Construir e interpretar tabelas e gráficos de frequências com base em dados obtidos em pesquisas por amostras estatísticas."},
                {"codigo": "EM13MAT401", "descricao": "Converter representações algébricas de funções polinomiais de 1º e 2º graus para representações geométricas no plano cartesiano."},
                {"codigo": "EM13MAT402", "descricao": "Analisar relações de interdependência entre grandezas em um problema, representadas por funções, para avaliar o comportamento de uma delas em função da outra."},
                {"codigo": "EM13MAT403", "descricao": "Analisar e estabelecer relações, com ou sem apoio de tecnologias digitais, entre as representações de uma função (tabelas, gráficos e leis de formação)."},
                {"codigo": "EM13MAT404", "descricao": "Analisar funções definidas por uma ou mais sentenças (nas representações algébrica e gráfica) e suas propriedades."},
                {"codigo": "EM13MAT405", "descricao": "Utilizar conceitos de porcentagem e de juros simples e compostos na análise de problemas de educação financeira."},
                {"codigo": "EM13MAT406", "descricao": "Construir e interpretar gráficos de funções polinomiais de 1º e 2º graus, de funções exponenciais e logarítmicas."},
                {"codigo": "EM13MAT407", "descricao": "Identificar e associar sequências numéricas (PA e PG) a funções afins e exponenciais, respectivamente."},
                {"codigo": "EM13MAT501", "descricao": "Investigar relações entre números expressos em tabelas para representá-los no plano cartesiano, identificando padrões e criando conjecturas para generalizar e expressar algebricamente essa generalização."},
                {"codigo": "EM13MAT502", "descricao": "Investigar e discutir o uso de diferentes linguagens (gráficos, tabelas, textos, etc.) na representação de dados estatísticos."},
                {"codigo": "EM13MAT503", "descricao": "Investigar pontos de máximo ou de mínimo de funções quadráticas em contextos envolvendo superfícies, trajetórias de projéteis etc."},
                {"codigo": "EM13MAT504", "descricao": "Investigar processo de obtenção da média, da amplitude e do desvio padrão de um conjunto de dados estatísticos."},
                {"codigo": "EM13MAT505", "descricao": "Resolver problemas sobre ladrilhamento do plano, com ou sem apoio de aplicativos de geometria dinâmica."},
                {"codigo": "EM13MAT506", "descricao": "Representar graficamente a variação da área e do perímetro de um polígono regular quando os comprimentos de seus lados variam."},
                {"codigo": "EM13MAT507", "descricao": "Identificar e associar progressões aritméticas (PA) a funções afins de domínios discretos."},
                {"codigo": "EM13MAT508", "descricao": "Identificar e associar progressões geométricas (PG) a funções exponenciais de domínios discretos."},
                {"codigo": "EM13MAT509", "descricao": "Investigar a deformação de ângulos e áreas provocada pelas diferentes projeções usadas em cartografia."},
                {"codigo": "EM13MAT510", "descricao": "Investigar conjuntos de dados relativos ao comportamento de duas variáveis numéricas, usando ou não tecnologias da informação."},
                {"codigo": "EM13MAT511", "descricao": "Reconhecer a existência de diferentes tipos de espaços amostrais, discretos ou não, e de eventos, equiprováveis ou não, e investigar as implicações no cálculo de probabilidades."}
            ]
        },
        "Ciências da Natureza e suas Tecnologias": {
            "Competências Específicas": [
                {"codigo": 1, "descricao": "Analisar fenômenos naturais e processos tecnológicos, com base nas interações e relações entre matéria e energia, para propor ações individuais e coletivas que aperfeiçoem processos produtivos, minimizem impactos socioambientais e melhorem as condições de vida em âmbito local, regional e global."},
                {"codigo": 2, "descricao": "Analisar e utilizar interpretações sobre a dinâmica da Vida, da Terra e do Cosmos para elaborar argumentos, realizar previsões sobre o funcionamento e a evolução dos seres vivos e do Universo, e fundamentar e defender decisões éticas e responsáveis."},
                {"codigo": 3, "descricao": "Investigar situações-problema e avaliar aplicações do conhecimento científico e tecnológico e suas implicações no mundo, utilizando procedimentos e linguagens próprios das Ciências da Natureza, para propor soluções que considerem demandas locais, regionais e/ou globais."}
            ],
            "Habilidades": [
                {"codigo": "EM13CNT101", "descricao": "Analisar e representar, com ou sem o uso de dispositivos e de aplicativos digitais, as transformações e conservações em sistemas que envolvam quantidade de matéria, de energia e de movimento."},
                {"codigo": "EM13CNT102", "descricao": "Realizar previsões, avaliar intervenções e/ou construir protótipos de sistemas térmicos que visem à sustentabilidade."},
                {"codigo": "EM13CNT103", "descricao": "Utilizar o conhecimento sobre as radiações e suas origens para avaliar as potencialidades e os riscos de sua aplicação em equipamentos de uso cotidiano, na saúde, no ambiente, na indústria e na agricultura."},
                {"codigo": "EM13CNT104", "descricao": "Avaliar os benefícios e os riscos à saúde e ao ambiente, considerando a composição, a toxicidade e a reatividade de diferentes materiais e produtos."},
                {"codigo": "EM13CNT105", "descricao": "Analisar os ciclos biogeoquímicos e interpretar os efeitos de fenômenos e ações humanas sobre esses ciclos."},
                {"codigo": "EM13CNT106", "descricao": "Avaliar, com ou sem o uso de dispositivos e aplicativos digitais, tecnologias e possíveis soluções para as demandas que envolvem a geração, o transporte, a distribuição e o consumo de energia elétrica."},
                {"codigo": "EM13CNT107", "descricao": "Realizar previsões sobre os níveis de degradação do ambiente, para propor e implementar medidas de prevenção e remediação."},
                {"codigo": "EM13CNT108", "descricao": "Identificar e explicar as propriedades da matéria que permitem o funcionamento de equipamentos e a escolha de materiais adequados para construção de objetos."},
                {"codigo": "EM13CNT201", "descricao": "Analisar e discutir modelos, teorias e leis propostos em diferentes épocas e culturas para comparar distintas explicações sobre o surgimento e a evolução da Vida, da Terra e do Universo."},
                {"codigo": "EM13CNT202", "descricao": "Analisar as diversas formas de manifestação da vida em seus diferentes níveis de organização, bem como as condições ambientais favoráveis e os fatores limitantes a elas."},
                {"codigo": "EM13CNT203", "descricao": "Aplicar os conhecimentos da evolução biológica para analisar a história humana, considerando sua origem, diversificação, dispersão pelo planeta e diferentes formas de interação com a natureza."},
                {"codigo": "EM13CNT204", "descricao": "Elaborar explicações, previsões e cálculos a respeito dos movimentos de objetos na Terra, no Sistema Solar e no Universo com base na análise das interações gravitacionais."},
                {"codigo": "EM13CNT205", "descricao": "Interpretar resultados e realizar previsões sobre atividades experimentais, fenômenos naturais e processos tecnológicos, com base nas noções de probabilidade e incerteza."},
                {"codigo": "EM13CNT206", "descricao": "Discutir a importância da preservação e conservação da biodiversidade, considerando parâmetros qualitativos e quantitativos."},
                {"codigo": "EM13CNT207", "descricao": "Identificar, analisar e discutir vulnerabilidades vinculadas às vivências e aos desafios contemporâneos aos quais as juventudes estão expostas."},
                {"codigo": "EM13CNT208", "descricao": "Aplicar os princípios da hereditariedade e da biologia molecular para analisar e prever características fenotípicas de seres vivos."},
                {"codigo": "EM13CNT209", "descricao": "Analisar a evolução dos seres vivos e as modificações nos ambientes, e as suas inter-relações."},
                {"codigo": "EM13CNT301", "descricao": "Construir questões, elaborar hipóteses, previsões e estimativas, empregar instrumentos de medição e representar e interpretar modelos explicativos para investigar e analisar fenômenos naturais."},
                {"codigo": "EM13CNT302", "descricao": "Comunicar, para públicos variados, em diversos contextos, resultados de análises, pesquisas e/ou experimentos."},
                {"codigo": "EM13CNT303", "descricao": "Interpretar textos de divulgação científica que tratem de temáticas das Ciências da Natureza, disponíveis em diferentes mídias."},
                {"codigo": "EM13CNT304", "descricao": "Analisar e debater o papel do conhecimento científico e tecnológico no combate a preconceitos, em diferentes contextos histórico-sociais."},
                {"codigo": "EM13CNT305", "descricao": "Investigar e analisar os usos de recursos naturais da biosfera, com destaque para o Brasil, e discutir a importância da conservação, para o desenvolvimento social e econômico."},
                {"codigo": "EM13CNT306", "descricao": "Avaliar os riscos envolvidos em atividades cotidianas, aplicando conhecimentos das Ciências da Natureza, para justificar o uso de equipamentos e recursos."},
                {"codigo": "EM13CNT307", "descricao": "Analisar as propriedades dos materiais para avaliar a adequação de seu uso em diferentes aplicações."},
                {"codigo": "EM13CNT308", "descricao": "Investigar e analisar o funcionamento de equipamentos elétricos e/ou eletrônicos e sistemas de automação para compreender as tecnologias contemporâneas."},
                {"codigo": "EM13CNT309", "descricao": "Analisar questões socioambientais, políticas e econômicas relativas à dependência do mundo atual em relação aos recursos não renováveis."},
                {"codigo": "EM13CNT310", "descricao": "Investigar e analisar os efeitos de programas de infraestrutura e demais serviços básicos (saneamento, energia elétrica, transporte, etc.)."}
            ]
        },
        "Ciências Humanas e Sociais Aplicadas": {
            "Competências Específicas": [
                {"codigo": 1, "descricao": "Analisar processos políticos, econômicos, sociais, ambientais e culturais nos âmbitos local, regional, nacional e mundial em diferentes tempos, a partir da pluralidade de procedimentos epistemológicos, científicos e tecnológicos."},
                {"codigo": 2, "descricao": "Analisar a formação de territórios e fronteiras em diferentes tempos e espaços, mediante a compreensão das relações de poder que determinam as territorialidades e o papel geopolítico dos Estados-nações."},
                {"codigo": 3, "descricao": "Analisar e avaliar criticamente as relações de diferentes grupos, povos e sociedades com a natureza (produção, distribuição e consumo) e seus impactos econômicos e socioambientais."},
                {"codigo": 4, "descricao": "Analisar as relações de produção, capital e trabalho em diferentes territórios, contextos e culturas, discutindo o papel dessas relações na construção, consolidação e transformação das sociedades."},
                {"codigo": 5, "descricao": "Identificar e combater as diversas formas de injustiça, preconceito e violência, adotando princípios éticos, democráticos, inclusivos e solidários, e respeitando os Direitos Humanos."},
                {"codigo": 6, "descricao": "Participar do debate público de forma crítica, respeitando diferentes posições e fazendo escolhas alinhadas ao exercício da cidadania e ao seu projeto de vida, com liberdade, autonomia, consciência crítica e responsabilidade."}
            ],
            "Habilidades": [
                {"codigo": "EM13CHS101", "descricao": "Identificar, analisar e comparar diferentes fontes e narrativas expressas em diversas linguagens, com vistas à compreensão de ideias filosóficas e de processos e eventos históricos, geográficos, políticos, econômicos, sociais, ambientais e culturais."},
                {"codigo": "EM13CHS102", "descricao": "Identificar, analisar e discutir as circunstâncias históricas, geográficas, políticas, econômicas, sociais, ambientais e culturais de matrizes conceituais."},
                {"codigo": "EM13CHS103", "descricao": "Elaborar hipóteses, selecionar evidências e compor argumentos relativos a processos políticos, econômicos, sociais, ambientais, culturais e epistemológicos."},
                {"codigo": "EM13CHS104", "descricao": "Analisar objetos e vestígios da cultura material e imaterial de modo a identificar conhecimentos, valores, crenças e práticas que caracterizam a identidade e a diversidade cultural de diferentes sociedades."},
                {"codigo": "EM13CHS105", "descricao": "Identificar, contextualizar e criticar tipologias de organização política e social, tais como cidade-estado, império, Estado-Nação etc."},
                {"codigo": "EM13CHS106", "descricao": "Utilizar as linguagens cartográfica, gráfica e iconográfica, diferentes gêneros textuais e tecnologias digitais de informação e comunicação de forma crítica, significativa, reflexiva e ética nas diversas práticas sociais."},
                {"codigo": "EM13CHS201", "descricao": "Analisar e caracterizar as dinâmicas das populações, das mercadorias e do capital nos diversos continentes, com destaque para a mobilidade e a fixação de pessoas."},
                {"codigo": "EM13CHS202", "descricao": "Analisar e avaliar os impactos das tecnologias na estruturação e nas dinâmicas de grupos, povos e sociedades contemporâneos (fluxos populacionais, financeiros, de mercadorias, de informações, de valores éticos e culturais etc.)."},
                {"codigo": "EM13CHS203", "descricao": "Comparar os significados de território, fronteiras e vazio (espacial, temporal e cultural) em diferentes sociedades e contextos."},
                {"codigo": "EM13CHS204", "descricao": "Comparar e avaliar os processos de ocupação do espaço e a formação de territórios, territorialidades e fronteiras."},
                {"codigo": "EM13CHS205", "descricao": "Analisar a produção de diferentes territorialidades em suas dimensões culturais, econômicas, ambientais, políticas e sociais, no Brasil e no mundo contemporâneo."},
                {"codigo": "EM13CHS206", "descricao": "Analisar a ocupação humana e a produção do espaço em diferentes tempos, aplicando os princípios de localização, distribuição, ordem, extensão, conexão, arranjos, causalidade, entre outros."},
                {"codigo": "EM13CHS301", "descricao": "Elaborar hipóteses, selecionar evidências e compor argumentos relativos a processos políticos, econômicos, sociais, ambientais, culturais e epistemológicos, com base na sistematização de dados e informações de diversas naturezas."},
                {"codigo": "EM13CHS302", "descricao": "Analisar e avaliar criticamente os impactos econômicos e socioambientais de cadeias produtivas ligadas à exploração de recursos naturais e às atividades agropecuárias em diferentes ambientes e escalas de análise."},
                {"codigo": "EM13CHS303", "descricao": "Debater e avaliar o papel da indústria cultural e das culturas de massa no estímulo ao consumismo e seus impactos socioambientais."},
                {"codigo": "EM13CHS304", "descricao": "Analisar os impactos socioambientais decorrentes de práticas de instituições governamentais, de empresas e de indivíduos."},
                {"codigo": "EM13CHS305", "descricao": "Analisar e discutir o papel e as competências de organismos internacionais e ONGs na proposição de soluções para problemas ambientais."},
                {"codigo": "EM13CHS306", "descricao": "Contextualizar, comparar e avaliar os impactos de diferentes modelos socioeconômicos no uso dos recursos naturais e na promoção da sustentabilidade."},
                {"codigo": "EM13CHS401", "descricao": "Identificar e analisar as relações entre sujeitos, grupos, classes sociais e sociedades com culturas e modelos de produção, de modo a problematizar as desigualdades e as violências."},
                {"codigo": "EM13CHS402", "descricao": "Analisar e comparar indicadores de emprego, trabalho e renda em diferentes espaços, escalas e tempos, associando-os a processos de estratificação e desigualdade socioeconômica."},
                {"codigo": "EM13CHS403", "descricao": "Caracterizar e analisar os impactos das transformações tecnológicas nas relações sociais e de trabalho no mundo contemporâneo."},
                {"codigo": "EM13CHS404", "descricao": "Discutir o papel dos valores e das moedas nos sistemas econômicos e financeiros em diferentes tempos e espaços."},
                {"codigo": "EM13CHS501", "descricao": "Analisar os fundamentos da ética em diferentes culturas, tempos e espaços, identificando processos que contribuem para a formação de sujeitos éticos que valorizem a liberdade, a cooperação, a autonomia, o empreendedorismo e a convivência democrática."},
                {"codigo": "EM13CHS502", "descricao": "Analisar situações da vida cotidiana, estilos de vida, valores, condutas etc., desnaturalizando e problematizando formas de desigualdade, preconceito, intolerância e discriminação."},
                {"codigo": "EM13CHS503", "descricao": "Identificar diversas formas de violência (física, simbólica, psicológica etc.), suas principais vítimas, suas causas sociais, psicológicas e afetivas."},
                {"codigo": "EM13CHS504", "descricao": "Analisar e avaliar os impasses ético-políticos decorrentes das transformações científicas e tecnológicas no mundo contemporâneo."},
                {"codigo": "EM13CHS601", "descricao": "Identificar e analisar as demandas e os protagonismos políticos, sociais e culturais dos povos indígenas e das populações afrodescendentes no Brasil contemporâneo."},
                {"codigo": "EM13CHS602", "descricao": "Identificar e caracterizar a presença do paternalismo, do autoritarismo e do populismo na política, na sociedade e nas culturas brasileira e latino-americana."},
                {"codigo": "EM13CHS603", "descricao": "Analisar a formação de diferentes países, povos e nações e de suas experiências políticas e de exercício da cidadania, aplicando conceitos políticos básicos."},
                {"codigo": "EM13CHS604", "descricao": "Discutir o papel dos organismos internacionais no contexto mundial, com vistas à elaboração de uma visão crítica sobre seus limites e suas formas de atuação nos países."},
                {"codigo": "EM13CHS605", "descricao": "Analisar os princípios da declaração dos Direitos Humanos, recorrendo às noções de justiça, igualdade e fraternidade."},
                {"codigo": "EM13CHS606", "descricao": "Analisar as características socioeconômicas da sociedade brasileira e propor medidas para enfrentar os problemas identificados e construir uma sociedade mais próspera, justa e inclusiva."}
            ]
        }
    }
}


# --- BANCOS DE DADOS ADICIONAIS ---
estrategias_por_funcao = {
    "Atenção Sustentada": ["Dividir tarefas longas em blocos menores com pausas programadas (Técnica Pomodoro).", "Usar timers visuais para marcar a duração da tarefa.", "Reduzir estímulos distratores no ambiente.", "Utilizar o 'sussurrofone' para a criança ouvir a própria voz durante a leitura."],
    "Memória de Trabalho (Operacional)": ["Fornecer instruções em etapas, uma de cada vez.", "Ensinar o uso de checklists e organizadores gráficos.", "Praticar jogos de memorização.", "Permitir o uso de tabuadas de apoio ou calculadora para focar no raciocínio."],
    "Controle Inibitório": ["Utilizar sinais de 'Pare e Pense' antes de responder.", "Praticar jogos que exigem espera e troca de turno.", "Estabelecer rotinas claras e previsíveis.", "Antecipar mudanças na rotina."],
    "Flexibilidade Cognitiva": ["Jogos que exigem mudança de regras.", "Apresentar o mesmo problema com diferentes formas de resolução.", "Criar histórias com finais alternativos.", "Incentivar o 'brainstorming' de ideias."],
    "Processamento Fonológico": ["Atividades lúdicas com rimas, aliterações e segmentação de sílabas/fonemas.", "Utilizar o método fônico multissensorial.", "Jogos de 'bingo de sons'.", "Uso de softwares focados em consciência fonológica."],
    "Processamento Visoespacial": ["Utilizar papel quadriculado para alinhar números e letras.", "Montagem de quebra-cabeças e LEGO seguindo modelos.", "Jogos de labirinto e 'encontre os 7 erros'.", "Destacar linhas ou usar réguas de leitura."]
}


# --- MENU LATERAL DE NAVEGAÇÃO ---
with st.sidebar:
    st.title("🧠 INTERVENÇÃO IA 7.0")
    st.caption("Versão Unificada")
    pagina_selecionada = st.radio(
        "Navegue pelos Módulos:",
        ["Página Inicial", "Anamnese Aprofundada", "Plano de Ensino Individualizado (PEI)", "Gerador de Atividades Adaptadas", "Modelo RTI (Resposta à Intervenção)", "Base de Conhecimento"],
        captions=["Visão geral", "Registre informações do aluno", "Crie metas e estratégias", "Adapte materiais pedagógicos", "Planeje a intervenção em camadas", "Consulte conceitos-chave"]
    )
    st.sidebar.markdown("---")
    st.info("Uma ferramenta especialista para uma educação inclusiva e baseada em evidências.")


# --- LÓGICA DAS PÁGINAS ---

if pagina_selecionada == "Página Inicial":
    st.title("Bem-vinda à Versão 7.0 da INTERVENÇÃO IA!")
    st.subheader("Plataforma com código unificado para garantir estabilidade.")
    st.markdown("---")
    st.warning("Para resolver o problema de arquivos não encontrados, todo o código da BNCC foi consolidado em um único lugar. Esta é a versão mais estável e segura do nosso aplicativo.", icon="🛡️")
    st.markdown("""
        **Navegue pelo menu à esquerda para acessar as ferramentas:**
        - **Anamnese Aprofundada:** Um guia estruturado para coletar informações cruciais.
        - **PEI com Inteligência Clínica:** Navegue pela BNCC completa e use a busca para encontrar exatamente o que precisa.
        - **Gerador de Atividades Adaptadas:** Crie materiais acessíveis com base nos princípios do DUA.
        - **Modelo RTI:** Planeje suas intervenções de forma escalonada e sistemática.
        - **Base de Conhecimento:** Revise conceitos fundamentais a qualquer momento.
    """)

elif pagina_selecionada == "Plano de Ensino Individualizado (PEI)":
    st.header("📝 Plano de Ensino Individualizado (PEI)")
    st.info("Utilize a base de dados completa da BNCC para fundamentar seu planejamento.")
    
    tab1, tab2 = st.tabs(["🎯 **Navegador da BNCC**", "💡 **Banco de Estratégias Clínicas**"])

    with tab1:
        etapa_ensino = st.selectbox(
            "1. Selecione a Etapa de Ensino:",
            options=list(BNCC_DATABASE.keys())
        )

        resultados = []
        keywords_input = ""
        competencias = []

        if etapa_ensino == "Educação Infantil":
            grupo_etario = st.selectbox("2. Selecione o Grupo Etário:", options=list(BNCC_DATABASE["Educação Infantil"].keys()))
            campo_exp = st.selectbox("3. Selecione o Campo de Experiência:", options=list(BNCC_DATABASE["Educação Infantil"][grupo_etario].keys()))
            keywords_input = st.text_input("Filtrar por palavras-chave (separadas por vírgula):", placeholder="Ex: corpo, gestos, sons", key="infantil_search")
            
            if st.button("Buscar Objetivos de Aprendizagem"):
                resultados = BNCC_DATABASE["Educação Infantil"][grupo_etario][campo_exp]

        elif etapa_ensino == "Ensino Fundamental":
            ano_escolar = st.selectbox("2. Selecione o Ano Escolar:", options=list(BNCC_DATABASE["Ensino Fundamental"].keys()))
            componente = st.selectbox("3. Selecione o Componente Curricular:", options=list(BNCC_DATABASE["Ensino Fundamental"][ano_escolar].keys()))
            keywords_input = st.text_input("Filtrar por palavras-chave (separadas por vírgula):", placeholder="Ex: leitura, texto, análise", key="fundamental_search")

            if st.button("Buscar Habilidades"):
                resultados = BNCC_DATABASE["Ensino Fundamental"][ano_escolar][componente]
        
        elif etapa_ensino == "Ensino Médio":
            st.selectbox("2. Selecione o Ano (para referência):", ["1º Ano", "2º Ano", "3º Ano"])
            area_conhecimento = st.selectbox("3. Selecione a Área de Conhecimento:", options=list(BNCC_DATABASE["Ensino Médio"].keys()))
            keywords_input = st.text_input("Filtrar por palavras-chave (separadas por vírgula):", placeholder="Ex: discursos, mídias, análise", key="medio_search")

            if st.button("Buscar Competências e Habilidades"):
                resultados = BNCC_DATABASE["Ensino Médio"][area_conhecimento].get("Habilidades", [])
                competencias = BNCC_DATABASE["Ensino Médio"][area_conhecimento].get("Competências Específicas", [])
                
                st.subheader(f"✅ Competências Específicas de {area_conhecimento}")
                with st.container(border=True):
                    for comp in competencias:
                        st.markdown(f"**Competência {comp['codigo']}:** {comp['descricao']}")

        # --- LÓGICA DE FILTRAGEM E EXIBIÇÃO ---
        if resultados:
            resultados_filtrados = []
            if keywords_input:
                keywords = [key.strip().lower() for key in keywords_input.split(',')]
                for item in resultados:
                    descricao = item['descricao'].lower()
                    if any(key in descricao for key in keywords):
                        resultados_filtrados.append(item)
            else:
                resultados_filtrados = resultados

            st.subheader("✅ Resultados Encontrados:")
            if not resultados_filtrados:
                st.warning("Nenhum item encontrado com as palavras-chave fornecidas.")
            else:
                for item in resultados_filtrados:
                    st.success(f"**Código:** {item['codigo']}\n\n**Descrição:** {item['descricao']}")

    with tab2:
        st.subheader("Sugestão de Estratégias por Função Cognitiva")
        funcao_selecionada = st.selectbox("Selecione a função cognitiva a ser estimulada:", options=list(estrategias_por_funcao.keys()))
        st.markdown(f"#### Estratégias para **{funcao_selecionada}**:")
        with st.container(border=True):
            for estrategia in estrategias_por_funcao[funcao_selecionada]:
                st.markdown(f"- {estrategia}")

# --- O RESTANTE DO CÓDIGO PARA AS OUTRAS PÁGINAS CONTINUA O MESMO ---
elif pagina_selecionada == "Anamnese Aprofundada":
    st.header("👤 Anamnese Aprofundada")
    with st.form("form_anamnese_avancado"):
        st.text_input("Nome Completo do Aluno")
        with st.expander("Dados de Identificação e Histórico"):
            st.date_input("Data de Nascimento"); st.text_input("Escola"); st.text_input("Ano Escolar"); st.text_area("Queixa Principal (relatada pela família/escola)")
        with st.expander("Avaliação de Funções e Habilidades (Observação Clínica)"):
            st.multiselect("Atenção", ["Sustentada", "Dividida", "Seletiva"]); st.multiselect("Memória de Trabalho", ["Baixa capacidade", "Dificuldade em manipular informações"]); st.multiselect("Flexibilidade Cognitiva", ["Rigidez", "Dificuldade em mudar de estratégia"])
            st.multiselect("Habilidades Linguísticas", ["Atraso na fala", "Dificuldade de compreensão", "Vocabulário restrito", "Dificuldades na narrativa"])
            st.multiselect("Coordenação Motora", ["Fina (dificuldade em escrever/desenhar)", "Ampla (desajeitado, dificuldade em esportes)"])
        with st.expander("Potencialidades e Interesses"):
            st.text_area("Descreva os pontos fortes, talentos e áreas de grande interesse do aluno.", height=100)
        if st.form_submit_button("Salvar Anamnese"): st.success("Anamnese salva com sucesso!")

elif pagina_selecionada == "Gerador de Atividades Adaptadas":
    st.header("🎨 Gerador de Atividades Adaptadas (Avançado)")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Atividade Original"); enunciado_original = st.text_area("Enunciado Original:", "Resolva os problemas de matemática com atenção."); atividade_original = st.text_area("Conteúdo da Atividade:", "1. Maria tinha 5 maçãs e comprou mais 3. Com quantas ela ficou?\n2. João tinha 10 laranjas e deu 4 para seu amigo. Com quantas ele ficou?")
    with col2:
        st.subheader("Aplicar Adaptações"); adapt_fonte = st.checkbox("Sugerir fonte ampliada e maior espaçamento."); adapt_vocabulario = st.checkbox("Simplificar vocabulário do enunciado."); adapt_quantidade = st.checkbox("Reduzir a quantidade de questões pela metade."); adapt_passos = st.checkbox("Sugerir a quebra de problemas em etapas."); adapt_resposta = st.checkbox("Sugerir formas de resposta alternativas (oral, desenho, múltipla escolha).")
    if st.button("Gerar Pré-visualização Adaptada"):
        st.subheader("✅ Pré-visualização da Atividade Adaptada")
        with st.container(border=True):
            enunciado_adaptado = "Vamos calcular! Resolva as continhas abaixo." if adapt_vocabulario else enunciado_original
            st.markdown(f"**Enunciado:** {enunciado_adaptado}")
            questoes = atividade_original.split('\n')
            if adapt_quantidade: questoes = questoes[:len(questoes)//2] if len(questoes) > 1 else questoes
            for q in questoes: st.write(q)
            st.markdown("---"); st.markdown("**Recomendações para Aplicação:**")
            if adapt_fonte: st.write("- Imprimir com fonte 20pt e espaçamento 1.5 entre linhas.")
            if adapt_passos: st.write("- Para cada problema, oriente o aluno a seguir as etapas: ler, desenhar, montar a conta, responder.")
            if adapt_resposta: st.write("- Permita que o aluno responda oralmente ou desenhando, caso tenha dificuldades na escrita.")

elif pagina_selecionada == "Modelo RTI (Resposta à Intervenção)":
    st.header("📊 Modelo RTI (Resposta à Intervenção)"); st.text_area("Nível 1: Intervenção Universal (Toda a Turma)", key="rti1"); st.text_area("Nível 2: Intervenção em Pequeno Grupo (Alunos em Risco)", key="rti2"); st.text_area("Nível 3: Intervenção Individualizada e Intensiva", key="rti3"); st.button("Salvar Plano RTI")

elif pagina_selecionada == "Base de Conhecimento":
    st.header("📚 Base de Conhecimento")
    with st.expander("🧠 O que são Funções Executivas?"): st.markdown("São um conjunto de habilidades mentais que nos permitem controlar e autorregular nossos pensamentos, emoções e ações. Componentes: Memória de Trabalho, Controle Inibitório e Flexibilidade Cognitiva.")
    with st.expander("🗣️ O que é Consciência Fonológica?"): st.markdown("É a habilidade de perceber e manipular os sons da fala, sem envolver letras. Inclui rimas, sílabas e fonemas. Dificuldades nesta área são um forte preditor de dislexia.")
    with st.expander("🔢 O que é Senso Numérico?"): st.markdown("É uma compreensão intuitiva dos números, sua magnitude e suas relações. É a base para o aprendizado matemático. Crianças com baixo senso numérico precisam de atividades com materiais concretos.")
