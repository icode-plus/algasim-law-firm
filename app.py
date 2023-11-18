from flask import Flask, render_template, redirect,  request, flash 
from email.message import EmailMessage
import ssl
import smtplib
import os
PORT = 5000

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY') or 'you-will-never-guess'


def reply(email_receiver):
    name = "عبدالعزيز الجاسم"
    email_sender = 'coursesforyo@gmail.com'
    email_password = 'hthaynywgefenetz'
     
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = name
    em.set_content( "شكرا لتواصلكم معنا ,ابقواعلى تواصل معنا وسوف نتواصل معكم في اقرب وقت ممكن ! شكرا لكم.")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp :
        smtp.login(email_sender , email_password)
        smtp.sendmail(email_sender , email_receiver , em.as_string())


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/get_job')
def get_job():
    return render_template('getjob.html')

@app.route('/contact')
def get_contact():
    return render_template('contact.html')

@app.route('/lowyers')
def processing():
    return render_template('abdelaziz.html')

@app.route('/about-us')
def who_us():
    return render_template('about-us.html')

@app.route('/faq')

def faq():
    return render_template('faq.html')
@app.route('/appointment')

def appointment():
    return render_template('appointment.html')
@app.route('/sendmail', methods=['POST'])
def send_email():
    name =request.form.get("name")
    email = request.form.get('email')
##########################################################################
    email_sender = 'coursesforyo@gmail.com'
    email_password = 'hthaynywgefenetz'
    email_receiver = "websmakersite@gmail.com"
    subject =  request.form.get('subject')
    body =  request.form.get('message')
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = "الى المكتب بعنوان  "+subject
    em.set_content( name +"\n"+" ارسل لك رسالة   :"+"\n" + body+"\t \n"+"ايميل الراسل : \n"+email)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp :
        smtp.login(email_sender , email_password)
        smtp.sendmail(email_sender , email_receiver , em.as_string())

    flash("تم استلام طلبك ' وسنقوم بالرد عليكم في اقرب وقت شكرا لكمز")
    reply(email)
    return redirect('/')




@app.route('/contact_abdulaziz', methods=['POST'])
def contact_abdulaziz():
    name =request.form.get("name")
    email = request.form.get('email')
##########################################################################
    email_sender = 'coursesforyo@gmail.com'
    email_password = 'hthaynywgefenetz'
    email_receiver = "websmakersite@gmail.com"
    subject =  request.form.get('subject')
    body =  request.form.get('message')
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = "طلب للتواصل مع عبدالعزيز"+"\n"+subject
    em.set_content( name +"\n"+"   ارسل لك رسالة :   :"+"\n" + body+"\t \n"+"sender email is : \n"+email)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp :
        smtp.login(email_sender , email_password)
        smtp.sendmail(email_sender , email_receiver , em.as_string())

    flash("تم استلام طلبكم وسيتم الرد عليكم في اقرب وقت")
    reply(email)
    return redirect('/')




@app.route('/estshara', methods=['POST'])
def estshara():
    name =request.form.get("name")
    email = request.form.get('email')
##########################################################################
    email_sender = 'coursesforyo@gmail.com'
    email_password = 'hthaynywgefenetz'
    email_receiver = "websmakersite@gmail.com"
    subject =  request.form.get('subject')
    body =  request.form.get('message')
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] =  ":طلب استشارة بعنوان"+ subject
    em.set_content( name +"\n"+" ارسل طلباستشارة    :"+"\n" + body+"\t \n"+"sender email is : \n"+email)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp :
        smtp.login(email_sender , email_password)
        smtp.sendmail(email_sender , email_receiver , em.as_string())

    flash("تم استلام طلبكموسيتم الرد عليكم في اقرب وقت")
    reply(email)
    return redirect('/')



@app.route('/applyjob', methods=['POST'])
def applyjob():
    name = request.form.get("name")
    email = request.form.get('email')
    qualification = request.form.get('qualification')
    experience = request.form.get('experience')
    gpa = request.form.get('gpa')
    resume = request.form.get('resume')
    e_type = request.form.get('e_type')

    email_sender = 'coursesforyo@gmail.com'
    email_password = 'hthaynywgefenetz'
    email_receiver = "websmakersite@gmail.com"
    cv_file = request.files['emp_cv']

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = "طلب الحصول علىوظيفة"

    # Attach the message body
    body = (
        name + "\n" + " طلب الحصول على وظيفة    :" + "\n"
        + " و بياناته كالتالي : " + "\n" + " الاسم : " + name + "\n"
        + "البريد الالكتروني : " + "\n" + email + "\n" + "المؤهلات :" + qualification + "\n" + "عدد سنوات الخبرة :" + experience + "\n" + "ألمعدل التراكمي:" + gpa + "\n"
        + "سيرة ذاتية : " + resume + "\n" + "والمتقدم يعمل : " + e_type + "\n"
    )
    msg.attach(MIMEText(body, 'plain'))

    # Attach the CV file
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(cv_file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % cv_file.filename)
    msg.attach(part)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, msg.as_string())

    flash("شكرا لتواصلكم معنا ' سنرد عليكم في اقرب وقت ممكن ")
    reply(email)
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('processing.html'), 404


#########################################################to run the website####################################################################
if __name__ == "__main__":
    app.run(debug=True, port=PORT, host='0.0.0.0')