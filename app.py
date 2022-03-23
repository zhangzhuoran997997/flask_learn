from glob import escape
from flask import Flask,escape,url_for
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