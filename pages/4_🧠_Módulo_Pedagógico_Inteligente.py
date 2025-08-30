import streamlit as st
# Importando os dados dos arquivos BNCC
import bncc_infantil
import bncc_fundamental
import bncc_medio

# --- Configuração da Página ---
st.set_page_config(page_title="Módulo Pedagógico Inteligente", page_icon="🧠", layout="wide")

st.title("🧠 Módulo Pedagógico Inteligente")
st.markdown("Gere atividades e planos de aula combinando a BNCC, o perfil do aluno e suas observações.")

# --- Inicialização e Verificação do Banco de Dados Temporário ---
if 'students' not in st.session_state or not st.session_state.students:
    st.warning("⚠️ Nenhum aluno cadastrado. Por favor, vá ao 'Módulo do Aluno' e cadastre pelo menos um aluno para usar este módulo.")
    st.stop()
    
# Importando o CONTEXTO_BASE do app principal (se ele estiver rodando como uma página)
# Para simplificar, vamos redefinir o CONTEXTO_BASE aqui. Em uma aplicação real, ele seria importado de um local central.
CONTEXTO_BASE = """
**PARTE 1: FUNDAMENTOS DA INTERVENÇÃO PSICOPEDAGÓGICA**
A intervenção psicopedagógica visa levar o aprendiz a construir sua aprendizagem de forma autônoma e prazerosa, resgatando o "poder aprender" e fortalecendo o autoconceito. A abordagem se baseia na Epistemologia Convergente (Piaget, Psicanálise, Psicologia Social), usando conceitos como VÍNCULO, TAREFA, e PROJETO. O terapeuta é um MEDIADOR que utiliza o LÚDICO como ferramenta principal, partindo sempre do SIGNIFICATIVO para o aprendiz, em um ambiente de ACOLHIMENTO e sem patologizar questões contextuais.

**PARTE 2: DIRETRIZES DA BASE NACIONAL COMUM CURRICULAR (BNCC)**
A IA deve utilizar as diretrizes da BNCC para contextualizar as atividades.
- **Educação Infantil:** Direitos (Conviver, Brincar, etc.) e Campos de Experiências (O eu, o outro e o nós, etc.).
- **Ensino Fundamental:** 10 Competências Gerais e Áreas do Conhecimento (Linguagens, Matemática, etc.).
- **Ensino Médio:** As mesmas competências e Áreas, incluindo Itinerários Formativos.
"""

# --- 1. Seleção do Aluno ---
st.header("1. Selecione o Aluno")
student_list = [s['name'] for s in st.session_state.students]
selected_student_name = st.selectbox("Escolha um aluno para iniciar o planejamento:", options=student_list)

selected_student = None
for student in st.session_state.students:
    if student['name'] == selected_student_name:
        selected_student = student
        break

if selected_student:
    st.info(f"**Perfil do Aluno Selecionado:**\n- **Diagnóstico/Observações:** {selected_student['diagnosis']}\n- **Série/Ano:** {selected_student['grade']}")
else:
    st.stop()

# --- 2. Busca e Seleção de Habilidades da BNCC ---
st.header("2. Busque e Selecione Habilidades da BNCC")
with st.expander("Clique para pesquisar na BNCC"):
    etapa = st.selectbox("Etapa de Ensino", ["Educação Infantil", "Ensino Fundamental"])

    habilidades_selecionadas = []

    if etapa == "Educação Infantil":
        campos = list(bncc_infantil.bncc_infantil.keys())
        campo_selecionado = st.selectbox("Campo de Experiência", campos)
        
        objetivos = bncc_infantil.bncc_infantil[campo_selecionado]
        habilidades_selecionadas = st.multiselect("Selecione os Objetivos de Aprendizagem e Desenvolvimento:", options=objetivos)

    elif etapa == "Ensino Fundamental":
        areas = list(bncc_fundamental.bncc_fundamental.keys())
        area_selecionada = st.selectbox("Área do Conhecimento", areas)

        componentes = list(bncc_fundamental.bncc_fundamental[area_selecionada].keys())
        componente_selecionado = st.selectbox("Componente Curricular", componentes)

        anos = list(bncc_fundamental.bncc_fundamental[area_selecionada][componente_selecionado].keys())
        ano_selecionado = st.selectbox("Ano", anos)
        
        habilidades = bncc_fundamental.bncc_fundamental[area_selecionada][componente_selecionado][ano_selecionado]
        habilidades_selecionadas = st.multiselect("Selecione as Habilidades:", options=habilidades)

# --- 3. Personalização e Geração com IA ---
st.header("3. Personalize e Gere a Atividade")
with st.form("generation_form"):
    st.subheader("Habilidades da BNCC Selecionadas:")
    if habilidades_selecionadas:
        for habilidade in habilidades_selecionadas:
            st.success(habilidade)
    else:
        st.warning("Nenhuma habilidade selecionada. A IA irá gerar uma atividade mais genérica.")

    st.subheader("Personalização Avançada")
    observacoes = st.text_area("Observações Pontuais do Aprendiz (Preferências, dificuldades do dia, etc.)", 
                               placeholder="Ex: Hoje está mais agitado. Gosta muito de dinossauros. Apresenta boa resposta a estímulos visuais.")
    
    atividade_existente = st.text_area("Atividade Existente para Adaptar (Opcional)",
                                       placeholder="Cole aqui o texto de uma atividade que você já tem e queira adaptar.")

    acao_ia = st.selectbox("Qual ação você deseja que a IA realize?",
                           ["Criar uma atividade nova", "Adaptar a atividade existente", "Sugerir 3 abordagens diferentes para o conteúdo"])
    
    submit_button = st.form_submit_button("🧠 Gerar com IA")

# --- 4. Exibição do Resultado ---
if submit_button:
    st.header("4. Resultado Gerado pela IA")
    if not st.session_state.get('api_key_configured', True): # Simula a verificação da chave
        st.error("ERRO: A API Key do Google AI não foi configurada corretamente.")
    else:
        with st.spinner("Aguarde, a IA está combinando todo o conhecimento para criar a melhor intervenção..."):
            # Construção do Prompt Avançado
            prompt_parts = [
                f"**Contexto Obrigatório:**\n{CONTEXTO_BASE}\n",
                "---",
                "**INSTRUÇÃO:**",
                f"Você deve atuar como um especialista em psicopedagogia e educação inclusiva. Com base no contexto obrigatório e nos dados a seguir, execute a ação solicitada.",
                "\n**DADOS DO APRENDIZ:**",
                f"- Nome: {selected_student['name']}",
                f"- Perfil Clínico/Educacional: {selected_student['diagnosis']}",
                f"- Nível Escolar: {selected_student['grade']}",
                f"\n**DADOS PEDAGÓGICOS:**",
                f"- Habilidades da BNCC a serem trabalhadas: {', '.join(habilidades_selecionadas) if habilidades_selecionadas else 'Não especificada'}",
                f"- Observações do dia (altamente relevantes): {observacoes if observacoes else 'Nenhuma'}",
                f"\n**AÇÃO SOLICITADA:** {acao_ia}",
            ]
            
            if acao_ia == "Adaptar a atividade existente" and atividade_existente:
                prompt_parts.append(f"\n**ATIVIDADE ORIGINAL PARA ADAPTAR:**\n{atividade_existente}")

            prompt = "\n".join(prompt_parts)
            
            # Simulação de chamada de IA (em um app real, aqui entraria a chamada para a API do Gemini)
            # response_text = f"**Roteiro Gerado para {selected_student['name']}**\n\n**Ação:** {acao_ia}\n\n*A IA geraria aqui uma resposta completa com base no prompt super detalhado que construímos, considerando o perfil, BNCC e suas observações.*"
            # st.markdown(response_text)
            
            # --- CHAMADA REAL PARA A IA ---
            try:
                # Re-importando e configurando o modelo (garante que está disponível na página)
                import google.generativeai as genai
                GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
                genai.configure(api_key=GOOGLE_API_KEY)
                model = genai.GenerativeModel('gemini-1.5-flash-latest')

                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Ocorreu um erro ao contatar a IA: {e}")
