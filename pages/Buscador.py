import streamlit as st
import pandas as pd
import backend as bk

FILEPATH = "DataBase/inscricoes_e_notas_de_corte_Sisu_2022-1.xlsx"
df = pd.read_excel(FILEPATH, sheet_name="inscricao_2022_1",
                   usecols=["SG_IES", "NO_CAMPUS", "NO_MUNICIPIO_CAMPUS",
                            "NO_CURSO", "DS_GRAU", "DS_TURNO",
                            "DS_MOD_CONCORRENCIA", "QT_VAGAS_CONCORRENCIA",
                            "NU_NOTACORTE", "QT_INSCRICAO"])

st.set_page_config(layout="wide")
st.header("IntépreteSISU")

cursos = bk.get_cursos(df)
universidades = bk.get_universidades(df)

curso = st.selectbox(label="Selecione um curso.", options=cursos)
universidade = st.selectbox(label="Selecione uma faculdade.",
                            options=universidades)


st.subheader("Suas opções:")
resultados = bk.get_possibilidades(df, curso, universidade)

if resultados is not None:
    st.dataframe(data=resultados)
