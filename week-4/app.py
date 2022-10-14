from flask import Flask #載入 Flask
from flask import request #載入 Request 物件
from flask import render_template #載入 render_templates 函式
from flask import session
from flask import redirect
from flask import url_for

#建立 Application 物件
app=Flask(__name__,static_folder="static", static_url_path="/" )
app.secret_key="any string but secret"  #設定 Session 的密鑰
#使用 POST 處理路徑 / 的對應函式
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin",methods=["POST"])
def signin():
    #接收 GET 方法的 Query String
    #maxNumber=request.args.get("max","")
    #maxNumber=int(maxNumber)
    #接收 POST 方法的 Query String(兩個寫法不一樣)
    user_account=request.form["account"]
    user_password=request.form["password"]
    if user_account and user_password == "test":
        session["user_account"]=user_account #session["欄位名稱"]=資料 把取得的資料存放到欄位裡面
        session["user_password"]=user_password
        return redirect("/member")
    elif user_account =="" or user_password=="":
        return redirect(url_for("error",message="請輸入帳號、密碼"))
    else:
        return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))

@app.route("/member")
def member():                                  
    if "user_account" and "user_password" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("message","")
    return render_template("error.html",message=message)

@app.route("/signout")
def signout():
    # 移除 session 中的資訊
    del session["user_account"]
    del session["user_password"]
    return redirect("/")
#啟動網站伺服器，可透過 port 參數指定埠號
app.run(port=3000)