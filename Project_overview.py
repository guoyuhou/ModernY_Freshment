import streamlit as st
st.title('实验概况')
st.divider()
st.header('项目概述')
st.caption('this is a caption')
st.subheader('1. 项目目的:')
st.text('本项目是基于碳点和牛至精油的复配材料所作成的生物膜材料，来探究膜对无花果的保鲜作用')
st.divider()
st.subheader('2. 项目框架:')
st.graphviz_chart('''
    digraph{
        碳点 -> 碳点和精油的复配
        复合膜的制备和表征 -> 复合物和膜的复配
        碳点和精油的复配 -> 复合物和膜的复配
        复合物和膜的复配 -> 无花果的保鲜验证
        精油 -> 碳点和精油的复配
    }
''')
st.divider()