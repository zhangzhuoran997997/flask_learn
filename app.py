from glob import escape
from flask import Flask,escape,url_for,render_template
from data import name,movies 

app = Flask(__name__)

# view function 请求处理函数 => app.route()
# 作用为绑定上对应的URL，当在浏览器访问这个URL时就会触发这个函数
# 可以绑定多个url地址
@app.route('/home')
@app.route('/zzr/<name>')
def hello(name="user"):
    return '<h1>Hello %s!</h1>' % escape(name)
# url_for 函数可以得到域名地址，同时可以输入域名中需要的参数
@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('hello',name="zzr"))
    print(url_for('hello',name="zzr",number=111))
    return "Test Page"

# template 动态文件中
# {{...}} 用来标记变量
# {%...%} 用来标记语句
# {#...#} 用来写注释 
@app.route('/')
def index():
    return render_template("index.html",name=name,movies=movies)