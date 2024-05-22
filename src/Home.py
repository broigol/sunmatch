import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import streamlit as st
import yaml

#from streamlit_navigation_bar import st_navbar

config = yaml.safe_load(open(r'src\view\config.yaml', 'r'))

# Configurar a página
st.set_page_config(
    page_title=config['home']['page_title'],
    page_icon = config['page_icon'],
    layout="centered"

    #layout="wide"
)

# Carregar imagem
image_path = config['home']['header_image']
st.image(image_path, use_column_width=True)

# Centralizar o texto abaixo da imagem
st.markdown("<h1 style='text-align: center;'>Bem-vindo à Minha Aplicação</h1>", unsafe_allow_html=True)

# Adicionar espaço entre o texto e os botões
st.write("")

# Criação das colunas para centralizar os botões
col1, col2 = st.columns([1, 2])

with col1:
    st.button("Botão 1")

with col2:
    st.button("Botão 2")

'''
# Custom CSS para centralizar os botões
st.markdown("""
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        gap: 10px;
    }
    .stButton > button {
        width: 200px;
    }
    </style>
    """, unsafe_allow_html=True)

# Criação do container para centralizar os botões
st.markdown('<div class="button-container">', unsafe_allow_html=True)
'''

# Opcional: Ações dos botões
if st.button("Botão 1"):
    st.write("Você clicou no Botão 1")

if st.button("Botão 2"):
    st.write("Você clicou no Botão 2")
