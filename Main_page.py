import streamlit as st
import pandas as pd
import random
import numpy as np
import time
import pygwalker as pyg
from st_pages import add_page_title, get_nav_from_toml
from annotated_text import annotated_text


st.title('ModernY')

# 温度、风向、等
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.write('欢迎！'
'在这里，你可以更新你的工作并查看项目进度。这样你才能更好地工作！:sunglasses:')

def stream_data(text):
    for word in text.split(' '):
        yield word + ' '
        time.sleep(0.02)
text = '''作者：刘曜畅'''


if st.button('点击这里'):
    st.write_stream(stream_data(text))

st.divider()

