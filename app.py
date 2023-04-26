import streamlit as st
import pandas as pd

st.write('Meu primeiro site')


caminho = st.file_uploader('Coloque um csv')

if caminho:
    try:
        df = pd.read_csv(caminho)

        st.write(df.head())
    except:
        st.write('O tipo de arquivo esta errado!')
else:
    st.write('COLOQUE O ARQUIVO!')