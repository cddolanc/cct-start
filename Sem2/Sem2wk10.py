import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com',587)

smtp_object.ehlo()