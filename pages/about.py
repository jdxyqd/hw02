# This file defines the about page of the website. It provides information about the individual or organization behind the website.

import streamlit as st

def about():
    st.title("关于我")
    st.subheader("欢迎来到我的个人网站！")
    st.write("""
    大家好！我是一名热爱编程的学生，专注于使用Python和Web开发技术来创建有趣和实用的项目。
    在这个网站上，您可以找到我的个人信息、项目展示以及联系方式。
    """)
    st.write("### 我的背景")
    st.write("""
    我在计算机科学领域有着扎实的基础，热衷于学习新技术和解决实际问题。
    我希望通过这个平台与更多志同道合的人交流和分享经验。
    """)
    st.write("### 联系我")
    st.write("""
    如果您对我的工作感兴趣，或者有任何问题，请随时通过联系页面与我联系。
    """) 

if __name__ == "__main__":
    about()