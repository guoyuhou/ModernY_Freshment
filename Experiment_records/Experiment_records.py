import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 定义存储实验记录的文件名
RECORDS_FILE = 'experiment_records.csv'

# 检查文件是否存在，如果不存在则创建它
if not os.path.exists(RECORDS_FILE):
    # 创建一个包含列标题的空DataFrame，并将其保存到文件
    pd.DataFrame(columns=['Date', 'Experiment Record']).to_csv(RECORDS_FILE, index=False)

# 读取实验记录
records = pd.read_csv(RECORDS_FILE)


def main():
    st.title('实验记录应用')
    records = pd.read_csv(RECORDS_FILE)
    menu = ["输入实验记录", "查看实验记录"]
    choice = st.sidebar.selectbox("菜单", menu)

    if choice == "输入实验记录":
        st.subheader("输入今天的实验记录")
        experiment_record = st.text_input("实验记录")

        if st.button("提交"):
            # 获取当前日期
            current_date = datetime.now().strftime('%Y-%m-%d')
            # 将新记录添加到DataFrame中
            new_record = pd.DataFrame({'Date': [current_date], 'Experiment Record': [experiment_record]})
            records = pd.concat([records, new_record], ignore_index=True)
            # 将更新后的DataFrame保存回文件
            records.to_csv(RECORDS_FILE, index=False)
            st.success("实验记录已保存！")

    elif choice == "查看实验记录":
        st.subheader("查看实验记录")
        # 显示实验记录表格
        st.write(records)


if __name__ == "__main__":
    main()