import streamlit as st
# Importando os dados dos arquivos BNCC
import bncc_infantil
import bncc_fundamental
import bncc_medio

st.set_page_config(page_title="Diagnóstico BNCC", page_icon="🔬", layout="wide")

st.title("🔬 Módulo de Diagnóstico da BNCC")
st.warning("Esta é uma versão temporária para depuração. Vamos encontrar o problema.")

if 'students' not in st.session_state or not st.session_state.students:
    st.info("⚠️ Cadastre um aluno no 'Módulo do Aluno' para continuar.")
    st.stop()
else:
    student_list = [s['name'] for s in st.session_state.students]
    selected_student_name = st.selectbox("Selecione um Aluno (apenas para teste):", options=student_list)

st.header("Busca na BNCC")

etapa = st.selectbox("Etapa de Ensino", ["Educação Infantil", "Ensino Fundamental"])

st.markdown("---")
st.subheader("Informações de Diagnóstico:")

if etapa == "Educação Infantil":
    st.write("Modo: Educação Infantil")
    # Lógica de diagnóstico para Ed. Infantil
    campos = list(bncc_infantil.bncc_infantil.keys())
    st.write(f"**1. Campos de experiência encontrados:** `{campos}`")
    
    campo_selecionado = st.selectbox("Campo de Experiência", campos)
    st.write(f"**2. Você selecionou o campo:** `{campo_selecionado}`")
    
    objetivos = bncc_infantil.bncc_infantil.get(campo_selecionado, [])
    st.write(f"**3. O código encontrou {len(objetivos)} objetivos para este campo.**")
    
    st.markdown("---")
    habilidades_selecionadas = st.multiselect("Selecione os Objetivos de Aprendizagem e Desenvolvimento:", options=objetivos)

elif etapa == "Ensino Fundamental":
    st.write("Modo: Ensino Fundamental")
    # Lógica de diagnóstico para Ed. Fundamental
    areas = list(bncc_fundamental.bncc_fundamental.keys())
    st.write(f"**1. Áreas do conhecimento encontradas:** `{areas}`")
    area_selecionada = st.selectbox("Área do Conhecimento", areas)
    st.write(f"**2. Você selecionou a área:** `{area_selecionada}`")

    area_data = bncc_fundamental.bncc_fundamental.get(area_selecionada, {})
    componentes = list(area_data.keys())
    st.write(f"**3. Componentes curriculares encontrados para '{area_selecionada}':** `{componentes}`")
    componente_selecionado = st.selectbox("Componente Curricular", componentes)
    st.write(f"**4. Você selecionou o componente:** `{componente_selecionado}`")
    
    componente_data = area_data.get(componente_selecionado, {})
    anos = list(componente_data.keys())
    st.write(f"**5. Anos encontrados para '{componente_selecionado}':** `{anos}`")
    ano_selecionado = st.selectbox("Ano", anos)
    st.write(f"**6. Você selecionou o ano:** `{ano_selecionado}`")

    habilidades = componente_data.get(ano_selecionado, [])
    st.write(f"**7. O código encontrou {len(habilidades)} habilidades para '{ano_selecionado}'.**")
    
    st.markdown("---")
    habilidades_selecionadas = st.multiselect("Selecione as Habilidades:", options=habilidades)
