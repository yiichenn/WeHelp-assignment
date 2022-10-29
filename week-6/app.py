from flask import Flask,request,render_template,session,redirect,url_for
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="website" #使用這個資料庫，就不用寫 USE 了
)
mycursor = mydb.cursor()


#建立 Application 物件
app=Flask(__name__,static_folder="static", static_url_path="/" ) #__name__ 這邊是用來定位目前載入資料夾的位置，用來判別 template__folder 或 static_folder 資料夾位置
app.secret_key="any string but secret"  #設定 Session 的密鑰
#使用 POST 處理路徑 / 的對應函式
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup",methods=["POST"])
def signup():
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]

    sql="INSERT INTO member(name,username,password) VALUES(%s,%s,%s)"
    val=(name,username,password)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM member WHERE username =%s", (username,))
    username_result=mycursor.fetchone()

    if username_result != None:
        return redirect(url_for("error",message="帳號已經被註冊"))
    else:
        mycursor.execute(sql,val)
        mydb.commit()
        return redirect("/")
@app.route("/signin",methods=["POST"])
def signin():
    with mydb.cursor(dictionary=True) as cursor:
        account=request.form["account"]
        password=request.form["password"]
        sql="SELECT * FROM member WHERE username =%s AND password=%s;"
        select=(account,password)
        mycursor.execute(sql,select)
        result=mycursor.fetchone()

        if account =="" or password =="":
            return redirect(url_for("error",message="請輸入帳號、密碼"))
        elif result != None:
            name=result[1]
            session["name"]=name
            session["account"]=account
            session["password"]=password
            return redirect("/member")
        else:
            return redirect(url_for("error",message="帳號或密碼輸入錯誤"))

@app.route("/member")
def member():                                  
    if "account" and "password" in session:
        name=session["name"]
        return render_template('member.html',name=name)
    else:
        return render_template('index.html')

@app.route("/error")
def error():
    message=request.args.get("message","")
    return render_template("error.html",message=message)

@app.route("/signout")
def signout():
    # 移除 session 中的資訊
    del session["account"]
    del session["password"]
    return redirect("/")
    

#啟動網站伺服器，可透過 port 參數指定埠號

if __name__ == '__main__':
    app.debug = True
    app.run(port=3000,debug=True)