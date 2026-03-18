# This file defines the projects page, showcasing various projects or works completed by the individual.

import streamlit as st

def display_projects():
    st.title("💻 我的作品")
    st.write("这里是我学习过程中做的一些小项目，欢迎交流指正～")
    
    # 作品1：宠物信息管理工具
    with st.expander("作品1：宠物信息管理工具", expanded=False):
        st.write("### 项目介绍")
        st.write("- 技术栈：Python + Streamlit")
        st.write("- 功能：添加宠物信息、生日提醒、成年判断")
        st.write("- 说明：基于面向对象思想开发，适合宠物主人记录宠物信息")
        st.markdown("[查看源码 →](https://github.com/)", unsafe_allow_html=True)
        st.image("https://picsum.photos/600/400?random=1", caption="宠物信息管理工具界面", use_column_width=True)

    # 作品2：简易计算器
    with st.expander("作品2：简易计算器", expanded=False):
        st.write("### 项目介绍")
        st.write("- 技术栈：Python + Streamlit")
        st.write("- 功能：支持加减乘除四则运算")
        st.write("- 说明：基础Python语法练习，适合新手入门")
        st.markdown("[查看源码 →](https://github.com/)", unsafe_allow_html=True)
        st.image("https://picsum.photos/600/400?random=2", caption="简易计算器界面", use_column_width=True)

if __name__ == "__main__":
    display_projects()