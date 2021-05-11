from flask import Flask, g, Response, make_response, session
from flask import render_template, Markup, request, redirect
from datetime import datetime, date, timedelta
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)
mysql = MySQL()
app.debug = True
app.config['MYSQL_DATABASE_USER'] = 'aigroup'
app.config['MYSQL_DATABASE_PASSWORD'] = 'aigroup'
app.config['MYSQL_DATABASE_DB'] = 'aiserver'
app.config['MYSQL_DATABASE_HOST'] = '10.0.11.94'
mysql.init_app(app)
conn=mysql.connect()


# html 요청이 처음 들어올 때, 작업이 실행됨, ex) DB connection
@app.before_request
def before_request():
    print("before_request!!!")

@app.route('/', redirect_to='/index.html')

@app.route('/index.html')
def redir():
    return render_template('index.html')

@app.route('/ins1', methods=['GET','POST'])
def ins1():
    if request.method == 'POST':
        Num = request.form['num']
        Name = request.form['name']
        Music = request.form['music']
        Code = request.form['code']
        print(Num+Name+Music+Code)
        sql = "insert into flask_ins_test values(%s,\"%s\",\"%s\",\"%s\", now())" % (Num,Name,Music,Code)
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception(e):
            print(e)
    return redirect('index.html')

@app.route('/ins2', methods=['GET','POST'])
def ins2():
    if request.method == 'POST':
        rcode = request.form['rc']
        rname = request.form['rn']
        cond = request.form['cd']
        val = request.form['val']
        print(rcode+rname+cond+val)
        sql = "insert into sel_code_test values(\"%s\",\"%s\",\"%s\",\"%s\", now())" % (rcode,rname,cond,val)
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception(e):
            print(e)
    return redirect('index.html')


if __name__ == '__main__':
    app.run()

'''````````````````````````````````````````````````````````
# html 요청을 전달할 때, 작업이 실행됨, ex) DB end
@app.after_request
def after_request(g):
    #tit = Markup("<strong>Title</strong>")
    #mu = Markup("<h1>h1 = <i>%s</i></h1>")
    #h = mu % "Italic"
    #print("h=",h)
    #lst = [("a", "메이플"),("b","리니지"), ("c", "던파")]
    #return render_template('index.html', title=tit, mu=h, lst=lst)
    print("after_request!!")

Num = request.form('num')
Name = request.form('name')
Music = request.form('music') 
Code = request.form('code')


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

    db_info = pymysql.connect(host='10.0.11.94',port=3306,db='aiserver',\
                    user='aigroup',passwd='aigroup', charset='utf8')
    cur = db_info.cursor()
        try:
        cur.execute(sql)
    except Exception(e):
        print(e)
    finally:
        db_info.commit()
        db_info.close()


'''
