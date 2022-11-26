import streamlit as st
import random

st.set_page_config(
   page_title="Noctua Score",
   page_icon="🦉",
   layout="wide",
   initial_sidebar_state="expanded",
)


st.title("Noctua")
sidebar = st.sidebar.image('assets/img/logo.png')  

st.markdown("""
[![Documentation Status](https://img.shields.io/badge/documentation-📖-red?style=for-the-badge)](https://atlantico-academy.github.io/risk-prediction)


## Resumo

O avanço da inflação e da crise econômica no Brasil na atualidade traz uma grande dificuldade para os brasileiros pagarem suas contas, especialmente no que tange o pagamento de crédito. Logo, esta alta da inadimplência traz também uma redução da arrecadação dos credores, que encontram um grande dilema: Para quem emprestar dinheiro? Como garantir que essa pessoa vai conseguir pagar o crédito tomado? Uma aplicação capaz de tomar o perfil socioeconômico dos seus potenciais clientes, assim como um histórico de pagamento e decidir se vale a pena tomar o risco do empréstimo se tornaria uma grande ferramenta a ser utilizada em bancos. Por isso, tomaremos esta ideia e utilizaremos do banco de dados [default of credit card clients](https://archive-beta.ics.uci.edu/ml/datasets/default+of+credit+card+clients) para a extração de características dos clientes.

## Resumo Gráfico

""")

st.image("grafico.png")

equipe = [
    "- [Deiferson da Silva Moura](https://github.com/deiferson)",
    "- [Francisco Leocassio da Silva](https://github.com/leocassiosilva)",
    "- [Gabriel Lucas Silva Felix](https://github.com/gabriellfelix)",
    "- [Marcello Alexandre Rodrigues Filho](https://github.com/marcelloale)",
    "- [Maria Luísa Leandro de Lima](https://github.com/maluwastaken)"
]

random.shuffle(equipe)

st.markdown("## Equipe")
st.markdown('\n'.join(equipe))
