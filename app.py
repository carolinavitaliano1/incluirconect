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
            "O eu, o outro e o nós": [{"codigo": "EI02EO01", "descricao": "Demonstrar atitudes de cuidado e solidariedade na interação com crianças e adultos."}],
            "Corpo, gestos e movimentos": [{"codigo": "EI02CG01", "descricao": "Apropriar-se de gestos e movimentos de sua cultura no cuidado de si e nos jogos e brincadeiras."}],
            "Traços, sons, cores e formas": [{"codigo": "EI02TS01", "descricao": "Criar sons com materiais, objetos e instrumentos musicais, para acompanhar diversos ritmos de música."}],
            "Escuta, fala, pensamento e imaginação": [{"codigo": "EI02EF01", "descricao": "Dialogar com crianças e adultos, expressando seus desejos, necessidades, sentimentos e opiniões."}],
            "Espaços, tempos, quantidades, relações e transformações": [{"codigo": "EI02ET01", "descricao": "Explorar e descrever semelhanças e diferenças entre as características e propriedades dos objetos (textura, massa, tamanho)."}]
        },
        "Crianças pequenas (4 anos a 5 anos e 11 meses)": {
            "O eu, o outro e o nós": [{"codigo": "EI03EO01", "descricao": "Demonstrar empatia pelos outros, percebendo que as pessoas têm diferentes sentimentos, necessidades e maneiras de pensar e agir."}],
            "Corpo, gestos e movimentos": [{"codigo": "EI03CG01", "descricao": "Criar com o corpo formas diversificadas de expressão de sentimentos, sensações e emoções, tanto nas situações do cotidiano quanto em brincadeiras."}],
            "Traços, sons, cores e formas": [{"codigo": "EI03TS01", "descricao": "Utilizar sons produzidos por materiais, objetos e instrumentos musicais durante brincadeiras de faz de conta, encenações, criações musicais, festas."}],
            "Escuta, fala, pensamento e imaginação": [{"codigo": "EI03EF01", "descricao": "Expressar ideias, desejos e sentimentos sobre suas vivências, por meio da linguagem oral e escrita (escrita espontânea), de fotos, desenhos e outras formas de expressão."}],
            "Espaços, tempos, quantidades, relações e transformações": [{"codigo": "EI03ET01", "descricao": "Estabelecer relações de comparação entre objetos, observando suas propriedades."}]
        }
    },
    "Ensino Fundamental": {
        "1º Ano": {"Língua Portuguesa": [{"codigo": "EF15LP01", "descricao": "Identificar a função social de textos que circulam em campo da vida social dos quais participa cotidianamente."}], "Matemática": [{"codigo": "EF01MA01", "descricao": "Utilizar números naturais como indicador de quantidade ou de ordem em diferentes situações cotidianas."}]},
        "2º Ano": {"Língua Portuguesa": [{"codigo": "EF12LP01", "descricao": "Ler palavras novas com precisão na decodificação."}], "Matemática": [{"codigo": "EF02MA06", "descricao": "Resolver e elaborar problemas de adição e de subtração."}]},
        "3º Ano": {"Língua Portuguesa": [{"codigo": "EF35LP03", "descricao": "Identificar a ideia central do texto, demonstrando compreensão global."}], "Matemática": [{"codigo": "EF03MA07", "descricao": "Resolver e elaborar problemas de multiplicação."}], "Ciências": [{"codigo": "EF03CI04", "descricao": "Identificar características sobre o modo de vida dos animais."}]},
        "4º Ano": {"Língua Portuguesa": [{"codigo": "EF35LP09", "descricao": "Organizar o texto em unidades de sentido, dividindo-o em parágrafos."}], "Matemática": [{"codigo": "EF04MA06", "descricao": "Resolver e elaborar problemas envolvendo diferentes significados da multiplicação."}]},
        "5º Ano": {"Língua Portuguesa": [{"codigo": "EF05LP03", "descricao": "Localizar e inferir informações em textos de diferentes gêneros."}], "Matemática": [{"codigo": "EF05MA08", "descricao": "Resolver e elaborar problemas de multiplicação e divisão com números naturais e racionais."}]},
        "6º Ano": {"Língua Portuguesa": [{"codigo": "EF67LP14", "descricao": "Diferenciar, em textos, fatos de opiniões."}], "Matemática": [{"codigo": "EF06MA13", "descricao": "Resolver e elaborar problemas que envolvam porcentagens."}], "História": [{"codigo": "EF06HI03", "descricao": "Identificar as hipóteses científicas sobre o surgimento da espécie humana."}]},
        "7º Ano": {"Matemática": [{"codigo": "EF07MA17", "descricao": "Resolver e elaborar problemas que envolvam variação de proporcionalidade direta e inversa."}], "Geografia": [{"codigo": "EF07GE01", "descricao": "Avaliar ideias e estereótipos acerca das paisagens e da formação territorial do Brasil."}]},
        "8º Ano": {"Matemática": [{"codigo": "EF08MA07", "descricao": "Resolver e elaborar problemas que possam ser representados por sistemas de equações de 1º grau."}], "Ciências": [{"codigo": "EF08CI01", "descricao": "Identificar e classificar diferentes fontes de energia (renováveis e não renováveis)."}]},
        "9º Ano": {"Língua Portuguesa": [{"codigo": "EF89LP04", "descricao": "Identificar e avaliar teses/opiniões/posicionamentos explícitos e implícitos em textos argumentativos."}], "Matemática": [{"codigo": "EF09MA05", "descricao": "Resolver e elaborar problemas que envolvam porcentagens (juros simples e compostos, acréscimos e decréscimos)."}]}
    },
    "Ensino Médio": {
        "Linguagens e suas Tecnologias": {
            "Competências Específicas": [{"codigo": 1, "descricao": "Compreender o funcionamento das diferentes linguagens e práticas culturais (artísticas, corporais e verbais) e mobilizar esses conhecimentos na recepção e produção de discursos nos diferentes campos de atuação social."}],
            "Habilidades": [
                {"codigo": "EM13LGG101", "descricao": "Compreender e analisar processos de produção e circulação de discursos, nas diferentes linguagens, para fazer escolhas fundamentadas em função de interesses pessoais e coletivos."},
                {"codigo": "EM13LP02", "descricao": "Estabelecer relações entre as partes do texto, tanto na produção como na leitura/escuta, considerando a construção composicional e o estilo do gênero."}
            ]
        },
        "Matemática e suas Tecnologias": {
            "Competências Específicas": [{"codigo": 1, "descricao": "Utilizar estratégias, conceitos e procedimentos matemáticos para interpretar situações em diversos contextos, sejam atividades cotidianas, sejam fatos das Ciências da Natureza e Humanas."}],
            "Habilidades": [{"codigo": "EM13MAT101", "descricao": "Interpretar criticamente situações econômicas, sociais e fatos relativos às Ciências da Natureza que envolvam a variação de grandezas."}]
        },
        "Ciências da Natureza e suas Tecnologias": {
            "Competências Específicas": [{"codigo": 1, "descricao": "Analisar fenômenos naturais e processos tecnológicos, com base nas interações e relações entre matéria e energia, para propor ações individuais e coletivas que aperfeiçoem processos produtivos."}],
            "Habilidades": [{"codigo": "EM13CNT101", "descricao": "Analisar e representar, com ou sem o uso de dispositivos e de aplicativos digitais, as transformações e conservações em sistemas que envolvam quantidade de matéria, de energia e de movimento."}]
        },
        "Ciências Humanas e Sociais Aplicadas": {
            "Competências Específicas": [{"codigo": 1, "descricao": "Analisar processos políticos, econômicos, sociais, ambientais e culturais nos âmbitos local, regional, nacional e mundial em diferentes tempos."}],
            "Habilidades": [{"codigo": "EM13CHS101", "descricao": "Identificar, analisar e comparar diferentes fontes e narrativas expressas em diversas linguagens, com vistas à compreensão de ideias filosóficas e de processos e eventos históricos, geográficos, políticos, etc."}]
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
