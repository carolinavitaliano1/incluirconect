import streamlit as st
import google.generativeai as genai

# --- CONTEXTO BASE (Psicopedagogia + BNCC) ---
CONTEXTO_BASE = """
**INÍCIO DO MATERIAL DE REFERÊNCIA OBRIGATÓRIO**

**PARTE 1: FUNDAMENTOS DA INTERVENÇÃO PSICOPEDAGÓGICA**

**1. FILOSOFIA E OBJETIVO CENTRAL:**
A intervenção psicopedagógica tem como objetivo principal levar o sujeito-aprendiz a construir sua aprendizagem de forma autônoma e prazerosa. O foco é resgatar o "poder aprender", o "desejo de aprender" e o "prazer em aprender", fortalecendo o autoconceito, a autoimagem e a autoestima do aprendiz. A aprendizagem é vista como um processo vital e não apenas como a superação de uma patologia.

**2. FUNDAMENTOS TEÓRICOS (EPISTEMOLOGIA CONVERGENTE):**
A abordagem se baseia na convergência da Psicanálise, da Epistemologia Genética (Jean Piaget) e da Psicologia Social (Pichon-Rivière). Conceitos-chave que devem guiar a intervenção são:
   - **VÍNCULO:** A criação de um vínculo positivo entre terapeuta, paciente e a tarefa é fundamental para o tratamento.
   - **PRÉ-TAREFA, TAREFA, PROJETO:** A intervenção visa mover o paciente de um estado de resistência (Pré-tarefa) para um engajamento ativo na aprendizagem (Tarefa), culminando em propostas autônomas (Projeto).

**3. METODOLOGIA E POSTURA DO TERAPEUTA:**
   - **FOCO NO PONTO DE URGÊNCIA:** A intervenção deve se concentrar no obstáculo principal que impede o aprendiz de integrar o conhecimento.
   - **NÃO HÁ MODELO RÍGIDO:** Cada caso é único. O terapeuta deve ser flexível, adaptando a intervenção à individualidade do paciente.
   - **PAPEL DE MEDIADOR:** O terapeuta não é um professor de reforço, mas um mediador entre o sujeito e o objeto de conhecimento.
   - **ACOLHIMENTO:** Diante de recusas ou medos, a postura deve ser de acolhimento, utilizando técnicas como "Ampliação de Modelo" ou "Alternativas Múltiplas".
   - **NÃO PATOLOGIZAR:** Ter cuidado para não transformar questões contextuais (familiares, escolares) em patologias do aluno.

**4. ESTRATÉGIAS E ATIVIDADES:**
   - **O LÚDICO É FUNDAMENTAL:** Jogos (de regras, simbólicos, de construção), brincadeiras e atividades criativas são as principais ferramentas.
   - **PARTIR DO SIGNIFICATIVO:** As atividades devem sempre partir de um contexto de interesse para o paciente.
   - **HISTORICIDADE:** Conectar passado, presente e futuro para que o paciente perceba seu progresso.
   - **GRADUAÇÃO DE DIFICULDADES:** Propor desafios adequados às reais possibilidades do paciente para construir uma sequência de sucessos.

**PARTE 2: DIRETRIZES DA BASE NACIONAL COMUM CURRICULAR (BNCC)**

A IA deve utilizar as seguintes diretrizes da BNCC para contextualizar as atividades propostas dentro do currículo escolar brasileiro.

**5. EDUCAÇÃO INFANTIL:**
   - **Direitos de Aprendizagem e Desenvolvimento:** Conviver, Brincar, Participar, Explorar, Expressar, Conhecer-se.
   - **Campos de Experiências:** O eu, o outro e o nós; Corpo, gestos e movimentos; Traços, sons, cores e formas; Escuta, fala, pensamento e imaginação; Espaços, tempos, quantidades, relações e transformações.

**6. ENSINO FUNDAMENTAL:**
   - **Competências Gerais:** As atividades devem, sempre que possível, promover as 10 competências gerais da BNCC (Conhecimento, Pensamento científico, crítico e criativo, Repertório cultural, Comunicação, Cultura digital, Trabalho e projeto de vida, Argumentação, Autoconhecimento e autocuidado, Empatia e cooperação, Responsabilidade e cidadania).
   - **Áreas do Conhecimento:** Linguagens, Matemática, Ciências da Natureza, Ciências Humanas, Ensino Religioso.

**7. ENSINO MÉDIO:**
   - **Competências Gerais:** As mesmas 10 competências do Ensino Fundamental.
   - **Áreas do Conhecimento e suas Competências Específicas:** Linguagens e suas Tecnologias, Matemática e suas Tecnologias, Ciências da Natureza e suas Tecnologias, Ciências Humanas e Sociais Aplicadas.
   - **Itinerários Formativos:** As propostas podem se conectar a eixos como Investigação Científica, Processos Criativos, Mediação e Intervenção Sociocultural, e Empreendedorismo.

**FIM DO MATERIAL DE REFERÊNCIA**
"""

# --- Configuração da Página e da API ---
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
except (KeyError, FileNotFoundError):
    GOOGLE_API_KEY = "SUA_API_KEY_AQUI"

st.set_page_config(
    page_title="Gerador de Roteiros Pedagógicos",
    page_icon="✨",
    layout="wide"
)

# Configurando o modelo Gemini
if GOOGLE_API_KEY and GOOGLE_API_KEY != "SUA_API_KEY_AQUI":
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
else:
    model = None

# --- Cabeçalho e Título ---
st.title("Plataforma de Intervenção Pedagógica ✨")
st.markdown("Use o menu à esquerda para navegar entre os roteiros existentes ou crie um novo com a IA personalizada.")

# --- Barra Lateral (Sidebar) ---
st.sidebar.header("Navegação")
pagina_selecionada = st.sidebar.radio(
    "Selecione uma opção:",
    ["Criar Roteiro com IA", "Ver Roteiros de Exemplo"]
)

# --- Funcionalidade Principal ---

if pagina_selecionada == "Criar Roteiro com IA":
    st.header("✨ Criar Roteiro Personalizado com IA")
    st.markdown("Preencha os campos abaixo para gerar uma atividade sob medida, fundamentada na sua metodologia e na BNCC.")

    if not model:
        st.error("ERRO: A API Key do Google AI não foi configurada corretamente. Por favor, verifique a seção 'Secrets' nas configurações do seu aplicativo no Streamlit.")
    else:
        col1, col2 = st.columns(2)
        with col1:
            nome_paciente = st.text_input("Nome do Paciente / Aluno")
        with col2:
            numero_sessao = st.number_input("Número da Sessão", min_value=1, step=1)
        
        with st.form("roteiro_form"):
            st.markdown("---")
            st.subheader("Detalhes para a Criação do Roteiro")
            
            tema_aula = st.text_input("Qual o tema da aula ou conteúdo a ser trabalhado?", "Fonema /s/")
            
            faixa_etaria = st.selectbox(
                "Qual a faixa etária do aprendiz?",
                ("Educação Infantil (0-5 anos)", "Ensino Fundamental (6-14 anos)", "Ensino Médio (15-17 anos)", "Adulto")
            )

            dificuldade = st.text_input("Qual a principal dificuldade, transtorno ou necessidade do aprendiz?", "Dislexia")
            
            ferramentas = st.multiselect(
                "Quais ferramentas digitais você gostaria de usar? (Opcional)",
                ["Wordwall", "Genially", "Padlet", "Kahoot", "Jamboard", "Pixton", "Canva", "YouTube"]
            )
            
            comandos_ia = st.text_area(
                "Informações Adicionais ou Comandos para a IA (Opcional)", 
                placeholder="Ex: O aprendiz tem hiperfoco em dinossauros. Use este tema na atividade."
            )
            
            submitted = st.form_submit_button("Gerar Roteiro")

            if submitted:
                with st.spinner("Aguarde, a IA está criando um roteiro incrível alinhado à sua metodologia..."):
                    prompt_parts = [
                        f"Você é um assistente especialista em psicopedagogia. Utilize o seguinte material de referência como base obrigatória e principal para sua resposta:\n{CONTEXTO_BASE}",
                        "---",
                        "Agora, com base nesse material, crie um roteiro de intervenção pedagógica estruturado para a seguinte solicitação:",
                        f"Tema principal: {tema_aula}.",
                        f"Nível de ensino do aprendiz: {faixa_etaria}.",
                        f"Foco da adaptação (dificuldade/transtorno): {dificuldade}.",
                        "Estruture a resposta com: Objetivo, Ferramentas Sugeridas (se aplicável) e um Passo a Passo detalhado (Acolhida, Apresentação, Desenvolvimento, Síntese, Encerramento). A resposta deve ser criativa, didática e estritamente alinhada aos princípios da base de conhecimento fornecida (tanto a parte psicopedagógica quanto a da BNCC correspondente à faixa etária)."
                    ]
                    if ferramentas:
                        prompt_parts.append(f"Incorpore o uso das seguintes ferramentas digitais: {', '.join(ferramentas)}.")
                    
                    if comandos_ia:
                        prompt_parts.append(f"Instrução adicional importante do terapeuta: {comandos_ia}")

                    prompt = "\n".join(prompt_parts)
                    
                    try:
                        response = model.generate_content(prompt)
                        st.subheader(f"📝 Roteiro Gerado para: {nome_paciente} (Sessão {numero_sessao})")
                        st.markdown(response.text)
                    except Exception as e:
                        st.error(f"Ocorreu um erro ao gerar o roteiro: {e}")


elif pagina_selecionada == "Ver Roteiros de Exemplo":
    st.header("📚 Banco de Roteiros de Exemplo")
    st.markdown("Estes são exemplos fixos. Os novos roteiros gerados pela IA serão sempre personalizados com base nos seus comandos e na sua metodologia.")

    st.subheader("Exemplo 1 – Gincana de Jogos Rápidos (Adaptado para TDAH)")
    st.markdown("""
    - **Objetivo:** Revisar conteúdos de forma dinâmica, mantendo a atenção através da novidade e da competição amigável.
    - **Ferramentas sugeridas:** Baamboozle, Wordwall, LearningApps.
    - **Passo a passo:**
        - **Acolhida:** Anunciar uma "gincana de jogos" com 3 rodadas rápidas para criar expectativa.
        - **Apresentação:** Explicar que cada jogo será diferente e rápido, mantendo o ritmo acelerado.
        - **Desenvolvimento:** Realizar rodadas de 5 minutos cada, alternando entre jogos do Baamboozle, Wordwall e LearningApps.
        - **Síntese:** Perguntar qual dos três jogos foi o favorito e por quê, permitindo uma breve expressão de preferência.
        - **Encerramento:** Comemorar a participação de todos na gincana, focando no esforço e na diversão.
    """)

    st.subheader("Exemplo 2 – Mapa Interativo de Sons (Adaptado para Dislexia)")
    st.markdown("""
    - **Objetivo:** Fortalecer a consciência fonológica e a associação grafema-fonema com forte suporte de áudio e visual.
    - **Ferramentas sugeridas:** ThingLink, Genially.
    - **Passo a passo:**
        - **Acolhida:** Iniciar com um som de um animal (áudio) e pedir para adivinhar qual é e qual a letra inicial do nome.
        - **Apresentação:** Apresentar uma imagem interativa (ex: uma fazenda) no ThingLink com hotspots que contêm a palavra escrita e um ícone de áudio.
        - **Desenvolvimento:** O paciente explora a imagem. Ao clicar em um hotspot, ele vê a palavra e ouve a narração. O desafio é encontrar todos os objetos que começam com um som específico.
        - **Síntese:** O paciente deve falar em voz alta outras duas palavras que também comecem com o mesmo som.
        - **Encerramento:** Parabenizar pela exploração sonora e reforçar o som aprendido.
    """)
