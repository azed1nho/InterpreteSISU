import streamlit as st

st.set_page_config(layout="wide")
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

text_welcome = """Olá. Este foi criado para ajudar a você encontrar a
sua faculdade no ano de 2023. A base de dados utilizada vem direto do SISU, incluindo
as notas de corte, logo, NÃO ME RESPONSABILIZO POR NENHUM TIPO DE ERRO. É RESPONSABILIDADE do
usuário conferir no próprio site da faculdade a veracidade dos dados aqui apresentados.
Embora o programa seja 'amador', sinta-se à vontade para utilizar o quanto quiser! 
(DESDE QUE ESTEJA DE ACORDO COM O QUE FOI DITO ACIMA)"""

text_help = """Utilizando a barra lateral você deve acessar a opção 'Buscador', 
e então selecionar o curso que você deseja. Caso esteja com dificuldades de 
encontrar o seu curso você também pode escrever o nome, e a caixa de seleção
filtrará as opções.

É importante lembrar que as notas estão, provavelmente, com cáculo de peso,
específico de cada faculdade. Então, reforço mais uma vez, confira o TERMO DE 
ADESAO da sua universidade e tire suas dúvidas."""


st.title("IntépreteSISU")

st.header("Bem-Vindo!")

st.header("Como usar o site")

st.markdown(f'<p class="big-font">{text_welcome}</p>', unsafe_allow_html=True)

st.info("A base de dados está aqui: https://sisu.mec.gov.br/#/relatorio#onepage")

st.header("Como usar o site")
st.markdown(f'<p class="big-font">{text_help}</p>', unsafe_allow_html=True)

st.info("O programa ainda está em desenvolvimento, então algumas coisas estão sendo"
        "ajustadas com o tempo. \nCaso encontre algum erro entre em contato pelo"
        " e-mail: pyprgpy@gmail.com")
