import streamlit as st
import pandas as pd

st.set_page_config(page_title='Aventis Labs', page_icon='', layout='wide', initial_sidebar_state='expanded')




st.title('Aventis Labs')
st.write("Aventis is a forward thinking company dedicated to creating innovative products that prioritize the betterment of humanity. With a deep commitment to social impact of our technologies, we design solutions that not only meet the needs of today but also help build a brighter, more sustainable future. At Aventis, we put humanity first, ensuring that every product we develop serves to improve lives, enhance well-being, and foster positive change for generations to come. Driven by Innovation, Guided by Humanity")

st.header('Our Team')

col1, col2, col3 = st.columns(3)
df = pd.read_csv('data.csv')

per_col = int(len(df) // 3)

with col1:
    for index,row in df[:per_col].iterrows():
        st.header(row['first name'].title() + ' ' + row['last name'].title())
        st.write(row['role'])
        st.image("images/" + row['image'],width=200)

with col2:
    for index,row in df[per_col:per_col*2].iterrows():
        st.header(row['first name'].title() + ' ' + row['last name'].title())
        st.write(row['role'])
        st.image("images/" + row['image'],width=200)

with col3:
    for index,row in df[per_col*2:].iterrows():
        st.header(row['first name'].title() + ' ' + row['last name'].title())
        st.write(row['role'])
        st.image("images/" + row['image'],width=200)