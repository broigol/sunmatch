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
db.create_tables()

insta = GerenciadorBanco(db.engine, db.session)

# Instancia o df de cidades e estados
df = pd.read_excel(config['df_city_states'])

# Plot do header
header_title = st.title('Cadastro de Instaladores 🌞')
st.subheader(body='', divider='gray')

st.text('Preencha os campos abaixo:')
# Campos do formulário
cnpj = st.text_input('CNPJ')
razao_social = st.text_input('Razão Social')
telefone = st.text_input('Telefone/Celular')
email = st.text_input('E-mail')

# Seleção de estado
estado = st.selectbox('Estado', df['Estado'].unique())

# Filtra cidades de acordo com o estado selecionado
cidades_filtradas = df[df['Estado'] == estado]['Cidade'].unique()

# Seleção de cidade
cidade = st.selectbox('Cidade', cidades_filtradas)

if st.button('Cadastrar'):    
    try:
        # Adicionando um registro
        insta.adicionar_registro(
            cnpj
            ,razao_social
            ,telefone
            ,email
            ,estado
            ,cidade 
        )
        st.write(f'Empresa {razao_social} cadastrada com sucesso 🌞😍🙌')
    except Exception as error:
        st.write(f'Erro de Cadastro ❌')
        st.write(error)


