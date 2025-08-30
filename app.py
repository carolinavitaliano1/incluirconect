import streamlit as st
from datetime import datetime

# --- Configuração da Página ---
st.set_page_config(
    page_title="Módulo do Aluno",
    page_icon="👤",
    layout="wide"
)

st.title("👤 Módulo do Aluno - Prontuário Digital Único")

# --- Inicialização do "Banco de Dados Temporário" ---
# Usamos o st.session_state para guardar os dados enquanto o app está aberto.
if 'students' not in st.session_state:
    st.session_state.students = []

# --- Formulário para Cadastrar Novo Aluno ---
with st.expander("➕ Cadastrar Novo Aluno", expanded=False):
    with st.form("new_student_form", clear_on_submit=True):
        st.subheader("Informações do Aprendiz")
        
        col1, col2 = st.columns(2)
        with col1:
            student_name = st.text_input("Nome Completo do Aluno", placeholder="Insira o nome completo")
            birth_date = st.date_input("Data de Nascimento")
        with col2:
            school_name = st.text_input("Escola Atual", placeholder="Nome da escola")
            student_grade = st.text_input("Série / Ano", placeholder="Ex: 3º Ano do Ensino Fundamental")

        st.subheader("Informações Adicionais")
        diagnosis = st.text_area("Diagnósticos e Observações Relevantes", placeholder="Descreva diagnósticos, laudos, e observações importantes.")
        family_contact = st.text_area("Contato e Observações da Família", placeholder="Nome do responsável, telefone, e-mail, e outras observações.")

        submit_button = st.form_submit_button("Salvar Aluno")

        if submit_button:
            if student_name: # Verifica se o nome foi preenchido
                # Cria um dicionário para o novo aluno
                new_student = {
                    "id": len(st.session_state.students) + 1,
                    "name": student_name,
                    "birth_date": birth_date.strftime("%d/%m/%Y"),
                    "school": school_name,
                    "grade": student_grade,
                    "diagnosis": diagnosis,
                    "family_contact": family_contact,
                    "created_at": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                }
                # Adiciona o aluno à nossa lista no banco de dados temporário
                st.session_state.students.append(new_student)
                st.success(f"Aluno {student_name} salvo com sucesso!")
            else:
                st.error("O campo 'Nome Completo do Aluno' é obrigatório.")


# --- Exibição dos Alunos Cadastrados ---
st.markdown("---")
st.header("Alunos Cadastrados")

if not st.session_state.students:
    st.warning("Nenhum aluno cadastrado ainda. Use o formulário acima para começar.")
else:
    # Itera sobre a lista de alunos e exibe cada um
    for student in st.session_state.students:
        with st.expander(f"{student['name']} - {student['grade']}"):
            st.markdown(f"**Data de Nascimento:** {student['birth_date']}")
            st.markdown(f"**Escola:** {student['school']}")
            
            st.markdown("**Diagnósticos e Observações:**")
            st.info(student['diagnosis'] if student['diagnosis'] else "Nenhuma observação.")

            st.markdown("**Contato e Observações da Família:**")
            st.info(student['family_contact'] if student['family_contact'] else "Nenhum contato.")

            st.markdown(f"*Cadastro criado em: {student['created_at']}*")

            # Botões para futuras ações (ainda não funcionais)
            col1_action, col2_action, col3_action = st.columns(3)
            with col1_action:
                st.button("📝 Editar Prontuário", key=f"edit_{student['id']}")
            with col2_action:
                st.button("➕ Novo Plano (PEI)", key=f"pei_{student['id']}")
            with col3_action:
                st.button("❌ Excluir Aluno", key=f"del_{student['id']}")
