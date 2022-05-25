import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.google.com', 25)
server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('mailtesting@neualnine.com', password)

message = MIMEMultipart()
message['From'] = 'NeuralNine'
message['To'] = 'testmails@spaml.de'
message['Subject'] = 'Just a test!'

with open('message.txt', 'r') as f:
    message_from_file = f.read()

message.attach(MIMEText(message_from_file, 'plain'))

filename = 'test.jpg'
attachment = open(filename, 'rb')

payload = MIMEBase('application', 'octet-stream')
payload.set_payload(attachment.read())

encoders.encode_base64(payload)
payload.add_header('Content-Disposition', f'attachment; filename={filename}')
message.attach(payload)

text = message.as_string()
server.sendmail('mailtesting@neuralnine.com', 'testmails@spaml.de', text)
