import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controller.sunmatch_db import GerenciadorBanco
from model.sunmatch_db import StartDb

import streamlit as st
import pandas as pd
import yaml

#from streamlit_navigation_bar import st_navbar

config = yaml.safe_load(open(r'src\view\config.yaml', 'r'))

# Configurar a página
st.set_page_config(
    page_title=config['cadastro']['page_title'],
    page_icon = config['page_icon'],
    #layout="wide"
)

db = StartDb()

insta = GerenciadorBanco(db.engine, db.session)

# Criar DataFrames
df_cidades = pd.read_excel(config['df_city_states'])
x = type(insta.listar_registros)
df_instaladores = pd.read_sql_query(
    'Select * From instaladores',
    con = insta.engine
)

# Título da página
st.title('Filtro de Instaladores')

# Seleção de estado com pesquisa
estado = st.selectbox('Selecione o Estado', options=df_cidades['Estado'].unique(), help='Pesquise e selecione o estado')

# Filtra cidades de acordo com o estado selecionado
cidades_filtradas = df_cidades[df_cidades['Estado'] == estado]['Cidade'].unique()

# Seleção de cidade com pesquisa
cidade = st.selectbox('Selecione a Cidade', options=cidades_filtradas, help='Pesquise e selecione a cidade')

# Filtrar instaladores com base no estado e cidade selecionados
df_filtrado = df_instaladores[(df_instaladores['estado'] == estado) & (df_instaladores['cidade'] == cidade)]

# Mostrar os instaladores filtrados como blocos de anúncios
st.subheader('Instaladores Disponíveis')

# Estilo personalizado para os blocos de anúncios
st.markdown("""
    <style>
    .instalador-bloco {
        border: 1px solid #ddd;
        padding: 10px;
        margin: 10px;
        border-radius: 5px;
        text-align: left;
    }
    .instalador-titulo {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .instalador-contato {
        font-size: 16px;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Exibir os instaladores filtrados como blocos de anúncios em 3 colunas
cols = st.columns(3)
for index, row in df_filtrado.iterrows():
    col_index = index % 3
    with cols[col_index]:
        st.markdown(f"""
            <div class="instalador-bloco">
                <div class="instalador-titulo">{row['document']}</div>
                <div class="instalador-contato">Contato: {row['razao_social']}</div>
                <div class="instalador-localizacao">Localização: {row['telefone']}, {row['email']}</div>
                <div class="instalador-localizacao">Localização: {row['cidade']}, {row['estado']}</div>
            </div>
            """, unsafe_allow_html=True)
