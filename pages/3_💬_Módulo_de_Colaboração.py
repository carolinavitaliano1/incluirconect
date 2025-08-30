import streamlit as st
from datetime import datetime

# --- Configuração da Página ---
st.set_page_config(
    page_title="Módulo de Colaboração",
    page_icon="💬",
    layout="wide"
)

st.title("💬 Módulo de Colaboração Multidisciplinar")
st.markdown("A ponte entre escola, família e equipe terapêutica.")

# --- Inicialização e Verificação do Banco de Dados Temporário ---
if 'students' not in st.session_state or not st.session_state.students:
    st.warning("⚠️ Nenhum aluno cadastrado. Por favor, vá ao 'Módulo do Aluno' e cadastre pelo menos um aluno para usar este módulo.")
    st.stop()

if 'communications' not in st.session_state:
    st.session_state.communications = []

# --- Seleção do Aluno ---
st.header("1. Selecione o Aluno")
student_list = [s['name'] for s in st.session_state.students]
selected_student_name = st.selectbox("Escolha um aluno para ver ou adicionar registros de comunicação:", options=student_list)

# Encontrar o ID do aluno selecionado
selected_student_id = [s['id'] for s in st.session_state.students if s['name'] == selected_student_name][0]


# --- Formulário para Adicionar Novo Registro ---
st.header("2. Adicionar Novo Registro de Comunicação")
with st.form("new_log_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        author_name = st.text_input("Seu Nome")
    with col2:
        author_role = st.selectbox("Sua Função/Papel", 
                                   options=["Professor(a) Regente", "Professor(a) de AEE", "Coordenador(a) Pedagógico(a)", "Psicopedagogo(a)", "Família", "Terapeuta Ocupacional", "Fonoaudiólogo(a)", "Psicólogo(a)", "Médico(a)", "Outro"])

    log_entry = st.text_area("Digite aqui a sua mensagem, observação ou registro:", height=150, placeholder="Ex: Hoje o aluno demonstrou grande avanço na atividade de reconhecimento de sílabas. Compartilho o material utilizado em anexo...")

    # Adicionar um campo para upload de arquivo (ainda não salva o arquivo, apenas o nome)
    uploaded_file = st.file_uploader("Anexar um arquivo (Opcional)")

    submit_button = st.form_submit_button("Salvar Registro")

    if submit_button:
        if author_name and log_entry:
            file_info = f"Arquivo anexado: {uploaded_file.name}" if uploaded_file else None
            
            new_log = {
                "id": len(st.session_state.communications) + 1,
                "student_id": selected_student_id,
                "author_name": author_name,
                "author_role": author_role,
                "log_entry": log_entry,
                "attachment": file_info,
                "timestamp": datetime.now() 
            }
            st.session_state.communications.append(new_log)
            st.success("Registro de comunicação salvo com sucesso!")
        else:
            st.error("Por favor, preencha seu nome e a mensagem.")

# --- Exibição do Histórico de Comunicação ---
st.markdown("---")
st.header(f"3. Histórico de Comunicação de {selected_student_name}")

student_logs = [log for log in st.session_state.communications if log['student_id'] == selected_student_id]

if not student_logs:
    st.info(f"Nenhum registro de comunicação para {selected_student_name} ainda.")
else:
    # Ordenar os registros do mais novo para o mais antigo
    sorted_logs = sorted(student_logs, key=lambda x: x['timestamp'], reverse=True)
    
    for log in sorted_logs:
        with st.container(border=True):
            col1_info, col2_info = st.columns([3, 1])
            with col1_info:
                st.markdown(f"**👤 {log['author_name']}** (*{log['author_role']}*)")
            with col2_info:
                st.caption(f"🗓️ {log['timestamp'].strftime('%d/%m/%Y às %H:%M')}")
            
            st.markdown(log['log_entry'])
            if log['attachment']:
                st.info(f"📎 {log['attachment']}")
