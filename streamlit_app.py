import streamlit as st
import time
# 定义一个包含所有页面的字典
pages = {
    '首页': 'D:\\pythono\\ModernY\\modern_Y_freshment\\Main_page.py',
    '项目概况': 'D:\\pythono\\ModernY\\modern_Y_freshment\\Project_overview.py',
    '项目实验': {
        '碳点的制备和检测': 'D:\\pythono\\ModernY\\modern_Y_freshment\\Experiment_degsin\\CDs.py',
        '精油的抗菌实验': 'D:\\pythono\\ModernY\\modern_Y_freshment\\Experiment_degsin\\Essential_oil_Experiment.py',
        '复合膜的制备和表征': 'D:\\pythono\\ModernY\\modern_Y_freshment\\Experiment_degsin\\Composite_membrane.py',
        '复配实验': 'D:\\pythono\\ModernY\\modern_Y_freshment\\Experiment_degsin\\Compouding_experiment.py',
        '复合液与膜的复配': 'D:\\pythono\\ModernY\\modern_Y_freshment\\Experiment_degsin\\Composite_of_membranes.py',
        '无花果的保鲜检验': 'D:\\pythono\\ModernY\\modern_Y_freshment\\Experiment_degsin\\Fig_verification.py'
    },
    '实验记录': 'D:\\pythono\\ModernY\\modern_Y_freshment\\Experiment_records\\Experiment_records.py',
    '其他': 'D:\\pythono\\ModernY\\modern_Y_freshment\\Others\\Others.py'
}

# 导航栏设置
page_name = st.sidebar.radio('导航', list(pages.keys()))
page_file = None
# 根据用户选择加载相应页面
if page_name == '首页':
    page_file = pages[page_name]
elif page_name == '项目概况':
    page_file = pages[page_name]
elif page_name == '实验记录':
    page_file = pages[page_name]
elif page_name == '其他':
    page_file = pages[page_name]
elif page_name == '项目实验':
    page = pages[page_name]
    page_title = st.sidebar.radio('具体内容', list(page.keys()))
    page_file = page[page_title]

# 执行所选页面的Python脚本
if page_file:
    exec(open(page_file, encoding='utf-8').read())
else:
    st.write("未选择页面或页面名称不正确。")

