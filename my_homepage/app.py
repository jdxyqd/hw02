# 导入Flask框架和模板渲染函数
from flask import Flask, render_template

# 初始化Flask应用实例
app = Flask(__name__)

# 首页路由：访问根路径/时触发
@app.route('/')
def index():
    # 定义要传递给模板的个人信息变量
    user_info = {
        "name": "芦姝婷",
        "major": "人工智能专业",
        "grade": "2025级",
        "motto": "脚踏实地，仰望星空"
    }
    # 渲染首页模板并传递变量
    return render_template('index.html', info=user_info)

# 关于我路由：访问/about路径时触发
@app.route('/about')
def about():
    # 定义要传递给模板的个人经历变量
    experience = {
        "education": "2025年考入北京石油化工大学，就读人工智能专业，主修Python、机器学习、计算机视觉等课程",
        "hobbies": "编程、打羽毛球、学习人工智能前沿技术",
        "skills": "Python编程、Pygame游戏开发、Flask开发"
    }
    # 渲染关于我模板并传递变量
    return render_template('about.html', exp=experience)

# 联系我路由：访问/contact路径时触发
@app.route('/contact')
def contact():
    # 定义要传递给模板的联系方式变量
    contact_info = {
        "email": "zhangsan@example.com",
        "github": "https://github.com/zhangsan"
    }
    # 渲染联系我模板并传递变量
    return render_template('contact.html', contact=contact_info)

# 程序入口：启动Flask应用
if __name__ == '__main__':
    # 开启调试模式，端口设为5001（避免5000端口被占用）
    app.run(debug=True, port=5001)
