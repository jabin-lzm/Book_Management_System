from random import Random
from book.models import EmailVerifyRecord
from django.core.mail import send_mail
from Book_Management_System.settings import EMAIL_FROM


def random_str(randomlength=8):
    str=''
    chars='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length=len(chars)-1
    random=Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str


def send_register_email(email):
    email_record=EmailVerifyRecord()
    code=random_str(16)
    email_record.code=code
    email_record.email=email
    email_record.save()
    email_title = ''
    email_body = '请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}'.format(code)

    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if send_status:
        pass