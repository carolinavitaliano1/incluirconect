import streamlit as st
import pandas as pd
from datetime import datetime

# --- Configuração da Página ---
st.set_page_config(
    page_title="Módulo de Planejamento",
    page_icon="📅",
    layout="wide"
)

st.title("📅 Módulo de Planejamento — PEI e PAEE")
st.markdown("Planejamento educacional simplificado, estruturado e acessível.")

# --- Inicialização do Banco de Dados Temporário ---
if 'students' not in st.session_state or not st.session_state.students:
    st.warning("⚠️ Nenhum aluno cadastrado. Por favor, vá ao 'Módulo do Aluno' e cadastre pelo menos um aluno para criar um plano.")
    st.stop()

if 'plans' not in st.session_state:
    st.session_state.plans = []

# --- Seleção do Aluno ---
st.header("1. Selecione o Aluno")
student_list = [s['name'] for s in st.session_state.students]
selected_student_name = st.selectbox("Escolha um aluno para ver ou criar um plano:", options=student_list)

# Encontrar o ID do aluno selecionado
selected_student_id = None
for student in st.session_state.students:
    if student['name'] == selected_student_name:
        selected_student_id = student['id']
        break

# --- Formulário para Criar um Novo Plano ---
with st.expander("➕ Criar Novo Plano (PEI / PAEE)"):
    with st.form("new_plan_form", clear_on_submit=True):
        st.subheader("Detalhes do Plano")
        plan_title = st.text_input("Título do Plano", placeholder="Ex: PEI - 2º Semestre 2025")
        start_date = st.date_input("Data de Início")
        end_date = st.date_input("Data de Término")
        main_objective = st.text_area("Objetivo Geral do Plano", placeholder="Descreva o foco principal do plano para este período.")

        st.subheader("Metas do Plano")
        
        # Coleta das metas em um formato mais simples dentro do formulário
        metas_input = st.text_area("Digite as metas (uma por linha)", 
                                   placeholder="Ex:\n- Curto Prazo: Reconhecer os números de 1 a 10.\n- Médio Prazo: Realizar somas simples com apoio visual.\n- Longo Prazo: Desenvolver autonomia na resolução de problemas matemáticos do cotidiano.")

        submit_button = st.form_submit_button("Salvar Plano Completo")

        if submit_button:
            if plan_title and main_objective and metas_input:
                # Processar as metas digitadas
                goal_lines = metas_input.strip().split('\n')
                goals_list = []
                for line in goal_lines:
                    if line.strip():
                        # Remove o marcador "-" se houver
                        description = line.strip().lstrip('- ').strip()
                        goal_type = "Não definido"
                        if "Curto Prazo:" in description:
                            goal_type = "Curto Prazo"
                            description = description.replace("Curto Prazo:", "").strip()
                        elif "Médio Prazo:" in description:
                            goal_type = "Médio Prazo"
                            description = description.replace("Médio Prazo:", "").strip()
                        elif "Longo Prazo:" in description:
                            goal_type = "Longo Prazo"
                            description = description.replace("Longo Prazo:", "").strip()

                        goals_list.append({
                            "description": description,
                            "type": goal_type,
                            "status": "Não Iniciado",
                            "notes": ""
                        })

                new_plan = {
                    "id": len(st.session_state.plans) + 1,
                    "student_id": selected_student_id,
                    "student_name": selected_student_name,
                    "title": plan_title,
                    "start_date": start_date.strftime("%d/%m/%Y"),
                    "end_date": end_date.strftime("%d/%m/%Y"),
                    "objective": main_objective,
                    "goals": goals_list,
                    "created_at": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                }
                st.session_state.plans.append(new_plan)
                st.success(f"Plano '{plan_title}' para {selected_student_name} salvo com sucesso!")
            else:
                st.error("Por favor, preencha todos os campos obrigatórios.")


# --- Exibição e Monitoramento dos Planos Existentes ---
st.markdown("---")
st.header(f"2. Monitoramento dos Planos de {selected_student_name}")

student_plans = [p for p in st.session_state.plans if p['student_id'] == selected_student_id]

if not student_plans:
    st.info(f"Nenhum plano cadastrado para {selected_student_name}. Use o formulário acima para criar o primeiro.")
else:
    for plan in student_plans:
        with st.container(border=True):
            st.subheader(plan['title'])
            st.caption(f"Período: {plan['start_date']} a {plan['end_date']} | Criado em: {plan['created_at']}")
            st.markdown(f"**Objetivo Geral:** {plan['objective']}")

            if plan['goals']:
                # Calcular progresso
                completed_goals = sum(1 for goal in plan['goals'] if goal['status'] == 'Concluído')
                progress = completed_goals / len(plan['goals']) if plan['goals'] else 0
                
                st.progress(progress, text=f"Progresso: {completed_goals} de {len(plan['goals'])} metas concluídas ({progress:.0%})")

                # Exibir metas em um DataFrame para melhor visualização e edição
                goals_df = pd.DataFrame(plan['goals'])
                
                st.write("**Metas Detalhadas:**")

                # Criar um editor de dados para as metas
                edited_df = st.data_editor(
                    goals_df,
                    column_config={
                        "description": st.column_config.TextColumn("Descrição da Meta", width="large"),
                        "type": st.column_config.SelectboxColumn("Prazo", options=["Curto Prazo", "Médio Prazo", "Longo Prazo"]),
                        "status": st.column_config.SelectboxColumn("Status", options=["Não Iniciado", "Em Andamento", "Concluído"]),
                        "notes": st.column_config.TextColumn("Registros de Evolução", width="medium"),
                    },
                    hide_index=True,
                    num_rows="dynamic", # Permite adicionar/remover metas
                    key=f"editor_{plan['id']}"
                )

                # Botão para salvar as alterações feitas no data_editor
                if st.button("Salvar Alterações nas Metas", key=f"save_{plan['id']}"):
                    # Atualizar o plano no session_state com os dados do dataframe editado
                    plan['goals'] = edited_df.to_dict('records')
                    st.success("Alterações nas metas salvas com sucesso!")
                    st.rerun() # Recarrega a página para refletir as mudanças
            else:
                st.write("Nenhuma meta definida para este plano.")
