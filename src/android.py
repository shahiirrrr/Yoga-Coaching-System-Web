import smtplib
from email.mime.text import MIMEText
from src.em1 import camclick
from flask import *

app=Flask(__name__)
from src.dbconnection import *



@app.route('/Register',methods=['post'])
def Register():
    fname = request.form['fname']
    lname = request.form['lname']
    gender = request.form['gender']
    dob = request.form['DOB']
    phone = request.form['phn']
    email = request.form['email']
    height = request.form['heigth']
    weight = request.form['weigth']
    health = request.form['health']
    uname = request.form['uname']
    passw = request.form['pass']
    qry = "INSERT INTO `login_table` VALUES(NULL,%s,%s,'user')"
    val = (uname, passw)
    id = iud(qry, val)
    qry1 = "INSERT INTO `user_table` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(id), fname, lname, gender, dob, phone, email,height,weight, health)
    iud(qry1, val1)
    return jsonify({'task': 'valid'})


@app.route('/login', methods=['post'])
def login():
    username = request.form['uname']
    password = request.form['pass']
    qry = 'SELECT * FROM `login_table` WHERE `USER_NAME`=%s AND `PASSWORD`=%s'
    val = (username, password)
    res = selectone(qry, val)
    print(res,"=============")
    if res is None:
        return jsonify({'task': 'invalid','lid':0})
    else:
        id = res['LOGIN_ID']
        return jsonify({'task': 'success', 'lid': id})

@app.route('/forget_password', methods=['get', 'post'])
def forget_password():
    print(request.form)
    try:
        print("1")
        print(request.form)
        email = request.form['email']
        print(email)
        qry = "SELECT `login_table`.`PASSWORD` FROM `user_table`  JOIN `login_table` ON `login_table`.`LOGIN_ID` = `user_table`.`LOGIN_ID` WHERE EMAIL=%s"
        s = selectone(qry, email)
        print(s, "=============")
        if s is None:
            return jsonify({'task': 'invalid email'})
        else:
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('shahirfarhan2003@gmail.com', 'ekwobnyardsxlsla')
                print("login=======")
            except Exception as e:
                print("Couldn't setup email!!" + str(e))
            msg = MIMEText("Your password is : " + str(s['PASSWORD']))
            print(msg)
            msg['Subject'] = 'your password'
            msg['To'] = email
            msg['From'] = 'shahirfarhan2003@gmail.com'

            print("ok====")

            try:
                gmail.send_message(msg)
            except Exception as e:
                return jsonify({"task": "invalid"})
            return jsonify({"task": "success"})
    except Exception as e:
        print(e)
        return jsonify({"task": "invalid"})


@app.route('/view_video',methods=['post'])
def view_video():
    id=request.form['lid']
    qry="SELECT * FROM `video_table`  JOIN `trainer_table` ON `trainer_table`.`LOGIN_ID`=`video_table`.`trainer_id` JOIN `request` ON `request`.`tid`=`trainer_table`.`LOGIN_ID` WHERE `request`.`uid`=%s AND `request`.`status`='Accepted'"
    print(qry)
    res=selectall2(qry,id)
    return jsonify(res)




@app.route('/send_complaints', methods=['post'])
def send_complaints():
    id=request.form['lid']
    tid=request.form['tid']
    complaint=request.form['complaint']
    qry="INSERT INTO `compaint_table` VALUES(NULL,%s,%s,%s,'pending',CURDATE())"
    val=(id,tid,complaint)
    iud(qry,val)
    return jsonify({'task':'valid'})

@app.route('/view_trainercomp', methods=['post'])
def view_trainercomp():
    qry = "SELECT * FROM `trainer_table` "
    res = selectall(qry)
    return jsonify(res)





@app.route('/view_complaint', methods=['post'])
def view_complaints():
    id=request.form['lid']
    qry="SELECT * FROM `compaint_table` JOIN `trainer_table`ON `trainer_table`.`LOGIN_ID`=`compaint_table`.`TID` WHERE USER_ID=%s"
    r=selectall2(qry,id)
    return jsonify(r)


@app.route('/complaint_reply', methods=['post'])
def complaint_reply():
    id = request.form['lid']
    qry="SELECT * FROM `compaint_table` WHERE `USER_ID`=%s"
    res = selectall2(qry, id)
    return jsonify(res)


@app.route('/ask_doubt', methods=['post'])
def ask_doubt():
    print(request.form)
    try:
        lid = request.form['lid']
        DOUBT = request.form['doubt']
        qry1="SELECT `tid` FROM `request`JOIN `user_table`ON `request`.`uid`=`user_table`.`LOGIN_ID`WHERE`request`.`status`='accepted' AND`request`.`uid`=%s "
        res = selectone(qry1, lid)
        qry = "INSERT INTO `doubt_table` VALUES(NULL,%s,%s,%s,'pending',CURDATE())"
        val = (lid, res['tid'], DOUBT)
        iud(qry, val)
        return jsonify({'task': 'valid'})
    except Exception as e:
        print("Error ",e)
        return jsonify({'task': 'in valid'})


@app.route('/doubt_reply' ,methods=['post'])
def doubt_reply():
    id = request.form['lid']
    qry = "SELECT * FROM `doubt_table` WHERE `USER_ID`=%s"
    res = selectall2(qry, id)
    print(res)
    return jsonify(res)


@app.route('/view_trainer' ,methods=['post'])
def view_trainer():
    qry = "SELECT * FROM `trainer_table` "
    res = selectall(qry)
    return jsonify(res)

@app.route('/send_request', methods=['post'])
def send_request():
    id = request.form['lid']
    tid = request.form['tid']
    # requestt = request.form['requestt']
    qry = "INSERT INTO `request` VALUES(NULL,%s,%s,CURDATE(),'pending')"
    val = (id, tid)
    iud(qry, val)
    return jsonify({'task': 'valid'})


@app.route('/startcam',methods=['get','post'])
def startcam():
    camclick()
    return redirect("/")



app.run(host='0.0.0.0',port='5000')