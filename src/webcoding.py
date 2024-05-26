import os
from flask import *
from src.em1 import camclick
import functools
from werkzeug.utils import secure_filename
import smtplib
from email.mime.text import MIMEText
app=Flask(__name__)


def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return render_template('indexlogin.html')
        return func()

    return secure_function


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
from src.dbconnection import *
app.secret_key="sdrftgyhuio"

@app.route('/')
def log():
    return render_template("logintmp.html")

@app.route('/login',methods=['get','post'])
def login():
    username=request.form['textfield']
    password=request.form['textfield2']
    qry='SELECT * FROM `login_table` WHERE `USER_NAME`=%s AND `PASSWORD`=%s'
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("Invalid");window.location="/"</script>'''
    elif res ['TYPE']=='admin':
        session['lid']=res['LOGIN_ID']
        return '''<script>alert("welcome");window.location="/adminhome"</script>'''
    elif res ['TYPE']=='trainer':
        session['lid']=res['LOGIN_ID']

        return '''<script>alert("welcome");window.location="/trainerhome"</script>'''
    else:
        return '''<script>alert("Invalid");window.location="/"</script>'''






@app.route('/addtrainer',methods=['get','post'])
@login_required
def addtrainer():
    return render_template("admin/add trainer.html")

@app.route('/addtrainer1',methods=['get','post'])
def addtrainer1():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    gender=request.form['radiobutton']
    dob=request.form['textfield8']
    phone=request.form['textfield3']
    email=request.form['textfield4']
    qualification=request.form['textfield5']
    username=request.form['textfield6']
    password=request.form['textfield7']
    qry="INSERT INTO `login_table` VALUES(NULL,%s,%s,'trainer')"
    val=(username,password)
    id=iud(qry,val)
    qry1="INSERT INTO `trainer_table` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),fname,lname,gender,dob,phone,email,qualification)
    iud(qry1,val1)
    return '''<script>alert("Added");window.location="/trainermng"</script>'''


@app.route('/edittrainer',methods=['get','post'])
@login_required
def edittrainer():
    id=request.args.get('eid')
    session['TE_id']=id
    qry="SELECT * FROM `trainer_table` WHERE `LOGIN_ID`=%s"
    res=selectone(qry,id)
    return render_template("admin/edittrainer.html",val=res)


@app.route('/edittrainer1',methods=['get','post'])
@login_required
def edittrainer1():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    gender=request.form['radiobutton']
    dob=request.form['textfield8']
    phone=request.form['textfield3']
    email=request.form['textfield4']
    qualification=request.form['textfield5']
    qry1="UPDATE `trainer_table` SET `FIRST_NAME`=%s,`LAST_NAME`=%s,`GENDER`=%s,`DOB`=%s,`PHONE`=%s,`EMAIL`=%s,`QUALIFICATION`=%s WHERE `LOGIN_ID`=%s"

    val1=(fname,lname,gender,dob,phone,email,qualification,session['TE_id'])
    iud(qry1,val1)
    return '''<script>alert("Edited");window.location="/trainermng"</script>'''


@app.route('/deletetrainer',methods=['get','post'])
@login_required
def deletetrainer():
    id=request.args.get('eid')
    qry=" DELETE FROM `trainer_table` WHERE `LOGIN_ID`=%s"
    iud(qry,id)
    qry1=" DELETE FROM `login_table` WHERE `LOGIN_ID`=%s"
    iud(qry1,id)
    return '''<script>alert("DELETED");window.location="/trainermng"</script>'''




@app.route('/addwork',methods=['get','post'])
@login_required
def addwork():
    return render_template("admin/add work.html")

@app.route('/addwork1',methods=['get','post'])
@login_required
def addwork1():
    work = request.form['textfield']
    details = request.form['textfield2']
    qry="INSERT INTO `work_table` VALUES (NULL,%s,%s,curdate())"
    val=(work,details)
    iud(qry,val)
    return '''<script>alert("Added");window.location="/addnmngewrk"</script>'''

@app.route('/assigned_work_status',methods=['get','post'])
@login_required
def assigned_work_status():
    qry="   SELECT  `work_table` .*,`trainer_table`.`FIRST_NAME`,`trainer_table`.`LAST_NAME`,`assignwork_table`.`STATUS`,assignwork_table.ASSIGNEDWORK_ID FROM `work_table`JOIN `assignwork_table` ON `work_table`.`WORK_ID`=`assignwork_table`.`WORK_ID`JOIN `trainer_table` ON `trainer_table`.`LOGIN_ID`=`assignwork_table`.`TRAINER_ID`"
    res = selectall(qry)
    return render_template("admin/assigned_work_status.html",val=res)





@app.route('/addnmngewrk',methods=['get','post'])
@login_required
def addnmngewrk():
    qry="select * from work_table"
    res = selectall(qry)
    print(res)
    return render_template("admin/addmngewrk.html",val=res)



@app.route('/assignwork',methods=['get','post'])
@login_required
def assignwork():
    qry="select * from trainer_table"
    res=selectall(qry)
    print(res)

    qry1 = "select * from work_table"
    res1 = selectall(qry1)
    print(res1)

    return render_template("admin/ADMIN WORK.html",val=res,val1=res1)


@app.route('/assignwork1',methods=['get','post'])
@login_required
def assignwork1():
    tr=request.form['select']
    work=request.form['select2']
    qry="INSERT INTO `assignwork_table` VALUES(NULL,%s,%s,CURDATE(),'Assigned')"
    val=(tr,work)
    iud(qry,val)
    return '''<script>alert("Assigned");window.location="/assigned_work_status"</script>'''


@app.route('/delete_assigned_work',methods=['get','post'])
@login_required
def delete_assigned_work():
    id=request.args.get('id')
    print(id)
    qry=" DELETE FROM `assignwork_table` WHERE `ASSIGNEDWORK_ID`=%s"
    iud(qry,id)
    return '''<script>alert("DELETED");window.location="assigned_work_status"</script>'''




@app.route('/deletework',methods=['get','post'])
@login_required
def deletework():
    id=request.args.get('eid')
    qry=" DELETE FROM `work_table` WHERE `WORK_ID`=%s"
    iud(qry,id)

    return '''<script>alert("DELETED");window.location="addnmngewrk"</script>'''


@app.route('/adminhome',methods=['get','post'])
@login_required
def adminhome():
    return render_template("admin/admin2.html")


@app.route('/trainermng',methods=['get','post'])
@login_required
def trainermng():
    qry="SELECT * FROM `trainer_table`"
    res=selectall(qry)
    return render_template("admin/trainer mng.html",val=res)




@app.route('/blockunblock',methods=['get','post'])
@login_required
def blockunblock():
    qry = "SELECT * FROM `user_table` JOIN `login_table` ON `user_table`.`LOGIN_ID`=`login_table`.`LOGIN_ID`"
    res=selectall(qry)
    return render_template("admin/blockunblock.html",val=res)


@app.route('/block_user',methods=['get','post'])
@login_required
def block_user():
    id = request.args.get('id')
    qry = "UPDATE `login_table` SET `TYPE`='blocked' WHERE `LOGIN_ID`=%s"
    iud(qry,id)
    return '''<script>alert("Blocked");window.location="/blockunblock#abt"</script>'''

@app.route('/unblock_user',methods=['get','post'])
@login_required
def ublock_user():
    id = request.args.get('id')
    qry = "UPDATE `login_table` SET `TYPE`='user' WHERE `LOGIN_ID`=%s"
    iud(qry,id)
    return '''<script>alert("Unblocked");window.location="/blockunblock#abt"</script>'''


@app.route('/complaints',methods=['get','post'])
@login_required
def complaints():
    res = selectall("SELECT `compaint_table`.* ,`trainer_table`.*,`user_table`.`FIRST_NAME` AS ufname ,`user_table`.`LAST_NAME` AS ulname FROM `compaint_table` JOIN `user_table` ON `compaint_table`.`USER_ID`=`user_table`.`LOGIN_ID` JOIN `trainer_table` ON  `compaint_table`.`TID`=`trainer_table`.`LOGIN_ID`")
    return render_template("admin/complaints.html",val = res)



@app.route('/send_reply',methods=['get','post'])
@login_required
def reply():
    id = request.args.get('id')

    if request.method=="POST":
        reply = request.form['r']
        iud("UPDATE `compaint_table` SET `REPLY` = %s WHERE `COMPLAINT_ID`=%s",(reply,id))
        return '''<script>alert("Reply added");window.location="complaints#abt"</script>'''
    else:
        return render_template("admin/reply.html")








@app.route('/Addvideo',methods=['get','post'])
@login_required
def Addvideo():
    return render_template("trainer/Add video.html")

@app.route('/Addvideo1',methods=['get','post'])
@login_required
def Addvideo1():
    video=request.files['file']
    fname=secure_filename(video.filename)
    video.save(os.path.join('static/video',fname))
    det=request.form['textfield']
    qry="INSERT INTO `video_table` VALUES(NULL,%s,%s,%s,CURDATE())"
    val=(session['lid'],fname,det)
    iud(qry,val)

    return '''<script>alert(" added");window.location="/video"</script>'''

@app.route('/deletevideo',methods=['get','post'])
@login_required
def deletevideo():
    id=request.args.get('eid')
    qry=" DELETE FROM `video_table` WHERE `VIDEO_ID`=%s"
    iud(qry,id)

    return '''<script>alert("DELETED");window.location="/video"</script>'''




@app.route('/doubtreply',methods=['get','post'])
@login_required
def doubtreply():
    id=request.args.get('id')
    session['DR_id']=id
    return render_template("trainer/doubtreply.html")


@app.route('/doubtreply1',methods=['get','post'])
@login_required
def doubtreply1():
    reply=request.form['textfield']
    qry="UPDATE `doubt_table` SET `REPLY`=%s WHERE `DOUBT_ID`=%s"
    val=(reply,session['DR_id'])
    iud(qry,val)
    return '''<script>alert("sended");window.location="/doubtview#abt"</script>'''



@app.route('/doubtview',methods=['get','post'])
@login_required
def doubtview():
    qry="SELECT `doubt_table`.* ,`user_table`.`FIRST_NAME`,`LAST_NAME` FROM `user_table` JOIN`doubt_table` ON `doubt_table`.`USER_ID`=`user_table`.`LOGIN_ID` WHERE `TRAINER_ID`=%s AND `REPLY`='pending'"
    res=selectall2(qry,session['lid'])
    return render_template("trainer/doubtview.html",val=res)


@app.route('/trainerhome',methods=['get','post'])
@login_required
def trainerhome():
    return render_template("trainer/trainer.html")

@app.route('/User',methods=['get','post'])
@login_required
def User():
    qry="SELECT `user_table`.* FROM `user_table` JOIN `request` ON `user_table`.`LOGIN_ID`=`request`.`uid` JOIN `trainer_table` ON `request`.`tid`=`trainer_table`.`LOGIN_ID` WHERE `request`.`tid`=%s and `request`.`status`='accepted'"
    res=selectall2(qry,session['lid'])
    return render_template("trainer/User.html",val=res)

@app.route('/view_request',methods=['get','post'])
@login_required
def view_request():

    qry = "SELECT `request`.*,`user_table`.* FROM `user_table` JOIN `request` ON `request`.`uid`=`user_table`.`LOGIN_ID` WHERE `request`.`tid`=%s"
    res=selectall2(qry,session['lid'])
    return render_template("trainer/request.html",val=res)

@app.route('/acceptrequest')
def acceptrequest():
    id=request.args.get('id')
    print(id,"kkkkkkkkkkkkkkkkkk")
    q="UPDATE `request` SET `status`='accepted' WHERE `rid`=%s"
    iud(q,str(id))
    return '''<script>alert("accepted");window.location="/User"</script>'''


@app.route('/cancelrequest')
def cancelrequest():
    id=request.args.get('id')
    print(id,"kkkkkkkkkkkkkkkkkk")
    q="UPDATE `request` SET `status`='rejected' WHERE `rid`=%s"
    iud(q,str(id))
    return '''<script>alert("Rejected");window.location="/view_request"</script>'''


@app.route('/rejectrequest')
def rejectrequest():
    id=request.args.get('id')
    q="UPDATE `request` SET `status`='rejected' WHERE `rid`=%s"
    iud(q,str(id))
    return '''<script>alert("rejected");window.location="/User"</script>'''




@app.route('/TRAINERWORK',methods=['get','post'])
@login_required
def TRAINERWORK():
    qry="SELECT * FROM`work_table`  JOIN `assignwork_table` ON `work_table`.`WORK_ID`=`assignwork_table`.`WORK_ID` WHERE `assignwork_table`.`TRAINER_ID`=%s"
    res=selectall2(qry,session['lid'])
    print(res)
    return render_template("trainer/TRAINER WORK.html",val=res)


@app.route('/updatestatus',methods=['get','post'])
@login_required
def updatestatus():
    id=request.args.get("id")
    session['wid']=id
    return render_template("trainer/updatestatus.html")



@app.route('/updatestatus1',methods=['get','post'])
@login_required
def updatestatus1():
    status=request.form['textfield']
    id=session['wid']
    qry="UPDATE `assignwork_table` SET `STATUS`=%s WHERE `ASSIGNEDWORK_ID`=%s"
    val=(status,id)
    iud(qry,val)

    return redirect("/TRAINERWORK#abt")


@app.route('/video',methods=['get','post'])
@login_required
def video():
    qry="SELECT `video_table`.* FROM `video_table` JOIN `trainer_table` ON `trainer_table`.`LOGIN_ID`=`video_table`.`trainer_id` WHERE  `video_table`.`trainer_id`=%s"
    res=selectall2(qry,session['lid'])
    return render_template("trainer/video.html",val=res)




@app.route('/fp',methods=['get','post'])

def fp():

    return render_template("fp.html")



@app.route('/fpp',methods=['get','post'])
def fpp():
    username=request.form['textfield']
    password=request.form['textfield2']

    qry='SELECT  `PASSWORD` FROM `login_table` WHERE `USER_NAME`=%s AND `LOGIN_ID` IN(SELECT `LOGIN_ID` FROM `trainer_table` WHERE `EMAIL`=%s)'
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("Invalid username or email");window.location="/fp"</script>'''
    else:
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('shahirfarhan2003@gmail.com', 'ekwobnyardsxlsla')
            print("login=======")
        except Exception as e:
            print("Couldn't setup email!!" + str(e))
        msg = MIMEText("Your password is : " + str(res['PASSWORD']))
        print(msg)
        msg['Subject'] = 'your password'
        msg['To'] = password
        msg['From'] = 'shahirfarhan2003@gmail.com'

        print("ok====")

        try:
            gmail.send_message(msg)
        except Exception as e:
            print(e)
            return '''<script>alert("Network Error");window.location="/"</script>'''

        return '''<script>alert("Please check you registred mail");window.location="/"</script>'''




@app.route('/startcam',methods=['get','post'])
def startcam():
    camclick()
    return redirect("/")



app.run(debug=True)