import os
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

from dotenv import load_dotenv

load_dotenv()

CAMINHO_HTML = pathlib.Path(__file__).parent / 'file_to_email.html'

remetente = os.getenv('FROM_EMAIL','')
destinatario = remetente

# Configurações do SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL','')
smtp_password = os.getenv('EMAIL_PASSWORD','')

# Mensagem de texto
with open(CAMINHO_HTML, 'r', encoding='utf8') as file:
	texto_arquivo = file.read()
	template = Template(texto_arquivo)
	texto_email = template.substitute(nome='João')
	print(texto_email)


mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do em-ail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
	server.ehlo()
	server.starttls()
	server.login(smtp_username, smtp_password)
	server.send_message(mime_multipart)

