import streamlit as st
import pandas as pd
import random
import numpy as np
import time
import pygwalker as pyg
from st_pages import add_page_title, get_nav_from_toml
from annotated_text import annotated_text
st.title('Modern_Y')
st.write('欢迎！'
'在这里，你可以更新你的工作并查看项目进度。这样你才能更好地工作！:sunglasses:')

def stream_data(text):
    for word in text.split(' '):
        yield word + ' '
        time.sleep(0.02)
text = '''welcome, i am happy that you could j  oin us!
    our team aimed to produce some papers and increased our scientific skills
    first i am happy i could learn something from our team, and i want you to translate this project to other people!
    ——Diary'''

if st.button('点击这里'):
    st.write_stream(stream_data(text))

md = st.text_area('在这里输入你的项目进展，更新项目内容',
                  "Happy    ! :balloon:")


st.markdown(md)

st.subheader('')

