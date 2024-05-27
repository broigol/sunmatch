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

)

# Carregar imagem
image_path = config['home']['header_image']
st.image(image_path, use_column_width=True)

# Centralizar o texto abaixo da imagem
st.markdown("""
    
    <h3 style='text-align: left;'>Bem-vindo ao SunMatch! Conectando donos e instaladores de sistemas solares.</h3>
    </br>
    <p>
        Clique em "Cadastro" para se cadastrar como instalador e, se procura o instalador mais próximo, clique em "Anúncios".
    </p>
""", unsafe_allow_html=True)

# Adicionar espaço entre o texto e os botões
st.write("")

# Criação das colunas para centralizar os botões
col1, col2 = st.columns([1, 2])
    
# Estilo do botão
st.markdown("""
    <style>
    .btn-custom {
        display: inline-block;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        color: #000000;
        background-color: #fbb515;
        border: none;
        border-radius: 5px;
        text-align: center;
        text-decoration: none;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .btn-custom:hover {
        background-color: #1b69b3;
        color: #fbb515;
    }
</style>
""", unsafe_allow_html=True)

with col1:
    # Botão HTML
    st.markdown('<a href="/Cadastro" target="_self" class="btn-custom">Cadastro</a>', unsafe_allow_html=True)

with col2:
    # Botão HTML
    st.markdown('<a href="/Anúncios" target="_self" class="btn-custom">Anúncios</a>', unsafe_allow_html=True)
