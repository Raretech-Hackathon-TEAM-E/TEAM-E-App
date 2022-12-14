from flask import Flask, request, redirect, render_template, session, flash
from models import dbConnect
from util.user import User
# 日付を扱う＋計算するためのモジュール（python標準）
from datetime import timedelta
import hashlib
import uuid
import re


app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
# セッションの寿命（30日間）
app.permanent_session_lifetime = timedelta(days=30)



# 【サインアップ】


@app.route('/signup')
def signup():
    return render_template('registration/signup.html')

@app.route('/signup', methods=['POST'])
def userSignup():
    name = request.form.get('name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

#メールアドレスの形式を定義する変数（38行目で利用） 
    pattern =  "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if name == '' or email == '' or password1 == '' or password2 == '':
        flash('空のフォームがあるようです')
    elif password1 != password2:
        flash('二つのパスワードの値が違っています')
    elif re.match(pattern, email) is None:
        flash('正しいメールアドレスの形式ではありません')
    else:
        uid = uuid.uuid4()
        password = hashlib.sha256(password1.encode('utf-8')).hexdigest()
        user = User(uid, name, email, password)
        DBusermail = dbConnect.getUserByMail(email)
        DBusername = dbConnect.getUserByName(name)

        if DBusermail or DBusername != None:
            flash('既に登録されています')

        else:
            dbConnect.createUser(user)
            UserId = str(uid)
            UserName = str(name)
            session['uid'] = UserId
            session['name'] = UserName
            return redirect('/')
    return redirect('/signup')


# 【ログイン機能】

@app.route('/login')
def login():
    return render_template('registration/login.html')


@app.route('/login', methods=['POST'])
def userLogin():
    email = request.form.get('email')
    password = request.form.get('password')

    if email == '' or password == '':
        flash('空のフォームがあるようです')
    else:
        user = dbConnect.getUserByMail(email)
        if user is None:
            flash('このユーザーは存在しません')
        else:
            hashPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if hashPassword != user["password"]:
                flash('パスワードが間違っています！')
            else:
                session['uid'] = user["uid"]
                session['name'] = user["user_name"]
                return redirect('/')
    return redirect('/login')



# 【メッセージ】

@app.route('/detail/<cid>')
def detail(cid):
    uid = session.get("uid")
    name = session.get("name")
    if uid is None:
        return redirect('/login')
    cid = cid
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
    
    return render_template('detail.html', messages = messages, channel=channel, uid=uid, name=name)

# 【メッセージ作成】

@app.route('/message', methods=['POST'])
def add_message():
    uid = session.get("uid")
    name = session.get("name")
    if uid is None:
        return redirect('/login')
    elif name in session:
        return name
    
    message = request.form.get('message')
    channel_id = request.form.get('channel_id')
    
    if message:
        dbConnect.createMessage(uid,channel_id,message)

    channel = dbConnect.getChannelById(channel_id)
    messages = dbConnect.getMessageAll(channel_id)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid, name=name)

# 【メッセージ削除】

@app.route('/delete_message', methods=['POST'])
def delete_message():
    uid = session.get("uid")
    name = session.get('name')
    if uid is None:
        return redirect('login')
    elif name in session:
        return name
    
    message_id = request.form.get('message_id')
    cid = request.form.get('channel_id')
    
    if message_id:
        dbConnect.deleteMessage(message_id)
    
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid, name=name)


#"/"へのアクセス
@app.route('/')
def index():
    uid = session.get('uid')
    name = session.get('name')
    if uid is None:
        return redirect('/login')
    elif name in session:
        return name
    else:
        channels = dbConnect.getChannelAll()
    return render_template('index.html', channels=channels, uid=uid, name=name)


@app.route('/', methods=['POST'])
def add_channel():
    uid = session.get('uid')
    name = session.get('name')
    if uid is None:
        return redirect('/login')
    elif name in session:
        return name
    channel_name = request.form.get('channel-title')
    channel = dbConnect.getChannelByName(channel_name)
    if channel == None:
        channel_description = request.form.get('channel-description')
        dbConnect.addChannel(uid, channel_name, channel_description)
        return redirect('/')
    else:
        return redirect('/duplicatederror')



#チャンネル削除
@app.route('/delete/<cid>')
def delete_channel(cid):
    uid = session.get("uid")
    name = session.get('name')
    if uid is None:
        return redirect('/login')
    elif name in session:
        return name
    cid = cid
    channel = dbConnect.getChannelById(cid)

    if channel["uid"] != uid:
        flash('チャンネルは作成者のみ削除可能です')
        return redirect ('/')
    else:
        dbConnect.deleteChannel(cid)
        channels = dbConnect.getChannelAll()
        return render_template('index.html', channels=channels, uid=uid, name=name)


#チャンネル編集


@app.route('/duplicatederror')
def duplicated():
    return render_template('error/error.html')

@app.route('/update_channel', methods=['POST'])
def update_channel():
    uid = session.get("uid")
    name = session.get("name")
    if uid is None:
        return redirect('/login')
    elif name in session:
        return name

    else:
        cid = request.form.get('cid')
        channel_name = request.form.get('channel-title')
        channel_description = request.form.get('channel-description')
        DBcname = dbConnect.getChannelByName(channel_name)

        if DBcname != None:
            return redirect('/duplicatederror')

        else:
            dbConnect.updateChannel(uid, channel_name, channel_description, cid)
            channel = dbConnect.getChannelByID(cid)
            messages = dbConnect.getMessageAll(cid)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid, name=name)


# リポストhtmlへのルーティング

@app.route('/repost_open', methods=['POST'])
def repost_open():
    uid = session.get("uid")
    if uid is None:
        return redirect('login')

    quote_mid = request.form.get('message_id')
    cid = request.form.get('channel_id')

    quote_message = dbConnect.getQuoteMessageByID(quote_mid)
    channel = dbConnect.getChannelById(cid)
 #   return 'quote_message.[0]'


    return render_template('modal/repost.html', uid=uid, quote_message=quote_message, channel=channel)


# リポストhtml画面遷移ごのindex.htmlへのルーティング

@app.route('/repost', methods=['POST'])
def repost_message():
    uid = session.get("uid")
    name = session.get('name')
    if uid is None:
        return redirect('login')
    elif name in session:
        return name
    remessage = request.form.get('re_massage')
    quote_mid = request.form.get('message_id')
    cid = request.form.get('channel_id')
    mark = request.form.get('repost_mark')

    if remessage:
        dbConnect.repostMessage(uid, cid, remessage, quote_mid, mark)
    
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid, name=name)
    


# ログアウト
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')



# 404エラー
@app.errorhandler(404)
def show_error404(error):
    return render_template('error/error404.html')


#500エラー
@app.errorhandler(500)
def show_error500(error):
    return render_template('error/error500.html')


if __name__ == '__main__':
    app.run(debug=True)

