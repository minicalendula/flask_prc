from flask import Flask, g, request, Response, make_response, session
from flask import render_template
from datetime import datetime, date, timedelta

app = Flask(__name__)
app.debug = True

@app.route('/wc')
def wc():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("SET COOKIE")
    res.set_cookie(key,val)
    return make_response(res)

# html 요청이 처음 들어올 때, 작업이 실행됨, ex) DB connection
@app.before_request
def before_request():
    print("before_request!!!")
    g.str = "한글"

@app.route('/', redirect_to='/index.html')

@app.route('/index.html')
def ind():
    return render_template('index.html')

'''
# html 요청을 전달할 때, 작업이 실행됨, ex) DB end
@app.after_request
def after_request(g):
    print("after_request!!")


def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans

@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "우리나라 시간 형식 : "+ str(datestr)

@app.route("/gg")
def helloworld():
    return "Hello Flask World!" + getattr(g, 'str', '111')

@app.route("/", redirect_to='/gg')
def helloworld2():
    return "Hello Flask World!!!!!!!!!!!"

@app.route('/test/<tid>')
def test3(tid):
    return "tid is"+ tid
'''
